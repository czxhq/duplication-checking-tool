import os
import sys

from PyQt5.QtCore import QMimeData, QUrl, Qt, QSortFilterProxyModel, QDir
from PyQt5.QtGui import QDrag, QStandardItem, QStandardItemModel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTextEdit, QTreeView, QMenu, QFileSystemModel, QWidget, QPushButton, QVBoxLayout, QDialog, \
    QApplication


# 可以接受拖动的文本显示框
class FileDropEdit(QTextEdit):
    def __init__(self, parent=None):
        super(FileDropEdit, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        self.setPlainText(content)
                except Exception as e:
                    print(f"读文件时错误: {e}")
            event.acceptProposedAction()


# 工作目录
class DraggableTreeView(QTreeView):
    def __init__(self, parent=None):
        super(DraggableTreeView, self).__init__(parent)
        self.setDragEnabled(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_context_menu)

        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(QDir.currentPath())

        self.proxy_model = PythonFileFilterProxyModel()
        self.proxy_model.setSourceModel(self.file_system_model)
        self.proxy_model.setFilterKeyColumn(0)

        self.setModel(self.proxy_model)
        self.setRootIndex(self.proxy_model.mapFromSource(self.file_system_model.index(QDir.currentPath())))

    def startDrag(self, supported_actions):
        try:
            index = self.currentIndex()
            if index.isValid():
                source_index = self.model().mapToSource(index)
                file_path = self.model().sourceModel().filePath(source_index)
                mime_data = QMimeData()
                url = QUrl.fromLocalFile(file_path)
                mime_data.setUrls([url])

                drag = QDrag(self)
                drag.setMimeData(mime_data)
                drag.exec_(Qt.MoveAction)
            else:
                print("错误指引")
        except Exception as e:
            print(f"Error in startDrag: {e}")

    def open_context_menu(self, position):
        indexes = self.selectedIndexes()
        if indexes:
            context_menu = QMenu()
            delete_action = context_menu.addAction("Delete")
            delete_action.triggered.connect(self.delete_file)
            context_menu.exec_(self.viewport().mapToGlobal(position))

    def delete_file(self):
        index = self.currentIndex()
        if index.isValid():
            source_index = self.model().mapToSource(index)
            file_path = self.model().sourceModel().filePath(source_index)
            if os.path.isfile(file_path):
                os.remove(file_path)
                self.model().sourceModel().remove(source_index)
                print(f"Deleted file: {file_path}")


# python 文件模式
class PythonFileFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super(PythonFileFilterProxyModel, self).__init__(parent)
        self.filter_string = ""

    def setFilterString(self, filter_string):
        self.filter_string = filter_string
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 0, source_parent)
        if self.sourceModel().isDir(index):
            return True
        file_path = self.sourceModel().filePath(index)
        return file_path.endswith('.py') and (self.filter_string in os.path.basename(file_path))

class DropTargetTreeView(QTreeView):
    def __init__(self, parent=None):
        super(DropTargetTreeView, self).__init__(parent)
        self.setAcceptDrops(True)

        # Create a standard item model for the target tree view
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["已选文件"])
        self.setModel(self.model)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_name = os.path.basename(url.toLocalFile())
                item = QStandardItem(file_name)
                item.setData(url.toLocalFile(), Qt.UserRole)
                self.model.appendRow(item)
            event.acceptProposedAction()

    def get_selected_files(self):
        selected_files = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row)
            file_path = item.data(Qt.UserRole)
            selected_files.append(file_path)
        return selected_files

# 网页展示
class HtmlWidget(QDialog):
    def __init__(self, html_files, parent=None):
        super().__init__(parent)

        self.setWindowTitle("查重结果")

        # 存储网页文件
        self.html_files = html_files
        self.current_index = 0

        # 网页引擎组件
        self.browser = QWebEngineView()

        # 加载第一个网页文件
        self.load_html_file(self.html_files[self.current_index])

        # 首页
        self.home_button = QPushButton("首页")

        # 实现返回首页的按钮功能
        self.home_button.clicked.connect(self.toHome)

        # 设置布局
        container = QVBoxLayout()
        container.addWidget(self.browser)
        container.addWidget(self.home_button)

        self.setLayout(container)

    def load_html_file(self, file_path):
        file_url = QUrl.fromLocalFile(file_path)
        self.browser.setUrl(file_url)

    def toHome(self):
        self.load_html_file(self.html_files[0])

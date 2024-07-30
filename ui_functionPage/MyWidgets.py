import os
import sys

from PyQt5.QtCore import QMimeData, QUrl, Qt, QSortFilterProxyModel, QDir
from PyQt5.QtGui import QDrag, QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTextEdit, QTreeView, QMenu, QFileSystemModel, QWidget, QPushButton, QVBoxLayout, QDialog, \
    QApplication, QAbstractItemView, QComboBox, QHBoxLayout, QLabel

from ui_functionPage.MyFileFunction import getHighRedundancyFiles


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
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置为多选模式

        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(QDir.currentPath())

        self.proxy_model = FileFilterProxyModel('.py')
        self.proxy_model.setSourceModel(self.file_system_model)
        self.proxy_model.setFilterKeyColumn(0)

        self.setModel(self.proxy_model)
        self.setRootIndex(self.proxy_model.mapFromSource(self.file_system_model.index(QDir.currentPath())))

    def setFileType(self, file_type):
        self.proxy_model = FileFilterProxyModel(file_type)
        self.proxy_model.setSourceModel(self.file_system_model)
        self.proxy_model.setFilterKeyColumn(0)

        self.setModel(self.proxy_model)
        self.setRootIndex(self.proxy_model.mapFromSource(self.file_system_model.index(QDir.currentPath())))

    def startDrag(self, supported_actions):
        try:
            indexes = self.selectedIndexes()
            if indexes:
                mime_data = QMimeData()
                urls = []

                for index in indexes:
                    if index.column() == 0:  # 只处理文件名列
                        source_index = self.model().mapToSource(index)
                        file_path = self.model().sourceModel().filePath(source_index)
                        urls.append(QUrl.fromLocalFile(file_path))

                if urls:
                    mime_data.setUrls(urls)
                    drag = QDrag(self)
                    drag.setMimeData(mime_data)
                    drag.exec_(Qt.MoveAction)
            else:
                print("No valid indexes selected")
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
        indexes = self.selectedIndexes()
        for index in indexes:
            if index.isValid() and index.column() == 0:
                source_index = self.model().mapToSource(index)
                file_path = self.model().sourceModel().filePath(source_index)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    self.model().sourceModel().remove(source_index)
                    print(f"Deleted file: {file_path}")

# 文件模式
class FileFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, file_type, parent=None):
        super(FileFilterProxyModel, self).__init__(parent)
        self.file_type = file_type
        self.filter_string = ""

    def setFilterString(self, filter_string):
        self.filter_string = filter_string
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 0, source_parent)
        if self.sourceModel().isDir(index):
            return True
        file_path = self.sourceModel().filePath(index)
        return file_path.endswith(self.file_type) and (self.filter_string in os.path.basename(file_path))

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

        self.reason_json_path = None
        self.code_path = None
        self.work_dir = None

        self.setWindowTitle("查重结果")
        # 去掉标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 存储网页文件
        self.html_files = html_files
        self.current_index = 0

        # 网页引擎组件
        self.browser = QWebEngineView()

        # 加载第一个网页文件
        self.load_html_file(self.html_files[self.current_index])

        # 顶栏
        self.top_bar = QWidget()
        self.top_bar_layout = QHBoxLayout()
        self.top_bar.setLayout(self.top_bar_layout)

        # 顶栏标题
        self.window_topic = QLabel("查重结果")

        # 按钮
        self.home_button = QPushButton()
        self.full_screen_button = QPushButton()
        self.close_button = QPushButton()
        self.out_copy_codes = QPushButton()
        self.out_copy_codes.setToolTip("导出抄袭代码: 重复率大于 30% 认定为抄袭")

        # 设置按钮图标
        self.home_button.setIcon(QIcon(".\\ui_functionPage\\icons\\home.png"))
        self.full_screen_button.setIcon(QIcon(".\\ui_functionPage\\icons\\full_screen.png"))
        self.close_button.setIcon(QIcon(".\\ui_functionPage\\icons\\close.png"))
        self.out_copy_codes.setIcon(QIcon(".\\ui_functionPage\\icons\\download.png"))

        # 按钮功能
        self.full_screen_button.clicked.connect(self.toggleFullScreen)
        self.close_button.clicked.connect(self.close)
        self.home_button.clicked.connect(self.toHome)
        self.out_copy_codes.clicked.connect(self.outportCopyCodes)

        # 设置按钮样式
        self.apply_styles()

        # 添加按钮到顶栏
        self.top_bar_layout.addWidget(self.window_topic)
        self.top_bar_layout.addStretch()
        self.top_bar_layout.addWidget(self.full_screen_button)
        self.top_bar_layout.addWidget(self.close_button)

        # 底栏
        self.bottom_bar_layout = QHBoxLayout()
        self.bottom_bar_layout.addWidget(self.home_button)


        # 设置布局
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.top_bar)
        self.main_layout.addWidget(self.browser)
        self.main_layout.addLayout(self.bottom_bar_layout)
        self.main_layout.setStretchFactor(self.top_bar, 1)
        self.main_layout.setStretchFactor(self.browser, 1000)
        self.main_layout.setStretchFactor(self.bottom_bar_layout, 10)
        self.setLayout(self.main_layout)

    def setPath(self, reason_path, code_path, work_dir):
        self.reason_json_path = reason_path
        self.code_path = code_path
        self.work_dir = work_dir

    def load_html_file(self, file_path):
        file_url = QUrl.fromLocalFile(file_path)
        self.browser.setUrl(file_url)

    def toHome(self):
        self.load_html_file(self.html_files[0])

    def toggleFullScreen(self):
        if self.windowState() & Qt.WindowFullScreen:
            self.setWindowState(self.windowState() & ~Qt.WindowFullScreen)
        else:
            self.setWindowState(self.windowState() | Qt.WindowFullScreen)

    def outportCopyCodes(self):
        getHighRedundancyFiles(self.reason_json_path, self.code_path, self.work_dir)

    def apply_styles(self):
        # 设置按钮样式
        button_style = """
        QPushButton {
            background-color: transparent;
            border: none;
            padding: 5px;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color: #f0f0f0;
        }
        QPushButton:pressed {
            background-color: #e0e0e0;
        }
        """
        self.home_button.setStyleSheet(button_style)
        self.full_screen_button.setStyleSheet(button_style)
        self.close_button.setStyleSheet(button_style)
        self.out_copy_codes.setStyleSheet(button_style)

    def openLocally(self):
        self.bottom_bar_layout.addWidget(self.out_copy_codes)

class SelectTypeComboBox(QComboBox):
    def __init__(self):
        super().__init__()

        self.addItem("Python Files (*.py)", ".py")
        self.addItem("C Files (*.c)", ".c")
        self.addItem("C++ Files (*.cpp, *.cc)", ".cpp")
        self.addItem("Java Files (*.java)", ".java")
        self.addItem("Verilog Files (*.v, *.sv)", ".v")
        self.addItem("MIPS Files (*.asm, *.s)", ".asm")
        self.addItem("JavaScript Files (*.js)", ".js")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = HtmlWidget(['F:/PythonProgramming/FunctionPage\\result\\index.html'])
    w.exec_()

    app.exec_()

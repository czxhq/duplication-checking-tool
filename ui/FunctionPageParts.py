import os
import shutil
import sys
import tempfile

from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QPushButton, QApplication, QLineEdit, \
    QFileDialog

from ui.MyFileFunction import copy_folder, copy_file, extract_zip
from ui.MyWidgets import FileDropEdit, DraggableTreeView, DropTargetTreeView, HtmlWidget
from ui.React import upload_zip_to_backend, download_zip_from_backend, interact


class CodeArea(QWidget):
    def __init__(self):
        super().__init__()

        # 两个代码显示区域
        self.code_showing_container = QSplitter(Qt.Horizontal)

        self.code_showing_A = FileDropEdit()
        self.code_showing_A.setPlaceholderText("代码区域 A")
        self.code_showing_A.setFont(QFont("Courier", 10))
        self.code_showing_B = FileDropEdit()
        self.code_showing_B.setPlaceholderText("代码区域 B")
        self.code_showing_B.setFont(QFont("Courier", 10))

        self.code_showing_container.addWidget(self.code_showing_A)
        self.code_showing_container.addWidget(self.code_showing_B)

        # 导入与清除按钮
        self.import_and_clear_button_container = QHBoxLayout()

        self.import_file_A = QPushButton("导入文件 A")
        self.import_file_B = QPushButton("导入文件 B")
        self.clear_all_button = QPushButton("清空")

        self.import_and_clear_button_container.addWidget(self.import_file_A)
        self.import_and_clear_button_container.addWidget(self.import_file_B)
        self.import_and_clear_button_container.addStretch(9)
        self.import_and_clear_button_container.addWidget(self.clear_all_button)
        self.import_and_clear_button_container.setStretchFactor(self.import_file_A, 1)
        self.import_and_clear_button_container.setStretchFactor(self.import_file_B, 1)
        self.import_and_clear_button_container.setStretchFactor(self.clear_all_button, 3)

        # 查重按钮
        self.check_button = QPushButton("查重")

        # 开始布局
        self.container = QVBoxLayout()
        self.container.addLayout(self.import_and_clear_button_container)
        self.container.addWidget(self.code_showing_container)
        self.container.addWidget(self.check_button)

        self.setLayout(self.container)


class WorkDirectoryArea(QWidget):
    def __init__(self):
        super().__init__()

        # 搜索栏
        self.search_layout = SearchWidget()

        # 导入文件夹按钮
        self.import_directory_button = QPushButton("导入文件夹作为工作区")

        # 工作区
        self.working_area = DraggableTreeView()

        # 开始布局
        self.container = QVBoxLayout()
        self.container.addLayout(self.search_layout)
        self.container.addWidget(self.import_directory_button)
        self.container.addWidget(self.working_area)

        self.setLayout(self.container)


class SearchWidget(QHBoxLayout):
    def __init__(self):
        super().__init__()

        # 输入框
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setPlaceholderText("查询文件")

        # 搜索按钮
        self.search_button = QPushButton("搜索")

        # 开始布局
        self.addWidget(self.search_line_edit)
        self.addWidget(self.search_button)

class SetTargetArea(QWidget):
    def __init__(self):
        super().__init__()

        # 导入与清空按钮
        self.clear_button = QPushButton("清空")

        import_and_clear_container = QHBoxLayout()
        import_and_clear_container.addStretch()
        import_and_clear_container.addWidget(self.clear_button)

        # 已选文件显示区
        self.chosen_files_area = DropTargetTreeView()

        # 查重按钮
        self.check_button = QPushButton("查重")

        # 设计布局
        target_area_container = QVBoxLayout()

        target_area_container.addLayout(import_and_clear_container)
        target_area_container.addWidget(self.chosen_files_area)
        target_area_container.addWidget(self.check_button)

        self.setLayout(target_area_container)


class FunctionPage(QWidget):
    def __init__(self):
        super().__init__()
        self.work_space_dir = QDir.currentPath()

        self.function_parts = QSplitter(Qt.Horizontal)

        self.work_directory_area = WorkDirectoryArea()
        self.target_files = SetTargetArea()

        self.function_parts.addWidget(self.work_directory_area)
        self.function_parts.addWidget(self.target_files)

        self.container = QVBoxLayout()
        self.container.addWidget(self.function_parts)

        self.setLayout(self.container)

        # 按钮逻辑
        # 设置工作区文件夹
        self.work_directory_area.import_directory_button.clicked.connect(self.setWorkingDirectory)
        # 搜索
        self.work_directory_area.search_layout.search_button.clicked.connect(self.searchFile)
        # 查重
        self.target_files.check_button.clicked.connect(self.check)
        # 清空
        self.target_files.clear_button.clicked.connect(self.clear)

    def setWorkingDirectory(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder', QDir.currentPath())
        if folder_path:
            self.work_directory_area.working_area.file_system_model.setRootPath(folder_path)
            self.work_directory_area.working_area.setRootIndex(
                self.work_directory_area.working_area.proxy_model.mapFromSource(
                    self.work_directory_area.working_area.file_system_model.index(folder_path)))
            self.work_space_dir = folder_path

    def searchFile(self):
        filter_string = self.work_directory_area.search_layout.search_line_edit.text()
        self.work_directory_area.working_area.proxy_model.setFilterString(filter_string)

    def clear(self):
        self.target_files.chosen_files_area.model.clear()
        self.target_files.chosen_files_area.model.setHorizontalHeaderLabels(["已选文件"])

    def check(self):
        selected_files = self.target_files.chosen_files_area.get_selected_files()
        if not selected_files:
            print("没有选择文件.")
            return

        workspace_dir = self.work_space_dir
        zip_path = os.path.join(workspace_dir, "selected_files.zip")
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_folder = os.path.join(temp_dir, "files_to_compress")
            os.mkdir(temp_folder)

            # Copy selected files to the temporary directory
            for file_path in selected_files:
                if os.path.isdir(file_path):
                    copy_folder(file_path, temp_folder)
                elif os.path.isfile(file_path):
                    copy_file(file_path, temp_folder)

            # Create a zip file from the temporary directory
            shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_folder)

        print(f"文件压缩至 {zip_path}")

        interact('http://8.141.14.176:8000/upload/', zip_path, workspace_dir, "Compare.zip")

        result_path = os.path.join(workspace_dir, "result")
        extract_zip(os.path.join(workspace_dir, "Compare.zip"), result_path)
        zip_path = os.path.join(result_path, "moss_test", "moss_result.zip")
        result_path = os.path.join(result_path, "new_result")
        extract_zip(zip_path, result_path)

        result_page = HtmlWidget([os.path.join(result_path, "index.html")], self)
        result_page.exec_()

    def fileToResult(self, zip_file_path):
        result_path = os.path.join(self.work_space_dir, "result")
        extract_zip(zip_file_path, result_path)
        zip_path = os.path.join(result_path, "moss_test", "moss_result.zip")
        result_path = os.path.join(result_path, "new_result")
        extract_zip(zip_path, result_path)

        result_page = HtmlWidget([os.path.join(result_path, "index.html")], self)
        result_page.exec_()
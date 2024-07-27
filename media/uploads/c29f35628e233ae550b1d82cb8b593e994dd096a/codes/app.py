import requests
from PyQt5.QtCore import QDir, QUrl
from PyQt5.QtWidgets import QFileDialog


def download_zip_from_backend(backend_url, save_dir=None):
    # 发送请求到后端
    response = requests.get(backend_url)

    # 确保请求成功
    if response.status_code == 200:
        # 打开保存对话框选择文件夹
            zip_filename = "downloaded_files.zip"
            save_path = 'D://' + zip_filename
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"文件保存至: {save_path}")
    else:
        print("请求后端失败")
backend_url = "http://60.205.191.48:8000/test"
download_zip_from_backend(backend_url)
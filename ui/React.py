import os

import requests

def upload_zip_to_backend(zip_file_path):
    url = 'http://' + '8.141.14.176' + ':8000/upload/'

    with open(zip_file_path, 'rb') as file:
        # 发送POST请求
        response = requests.post(url, files={'zip_file': file})

def download_zip_from_backend(save_path, zip_file_name):
    backend_url = "http://localhost:8000/test"
    response = requests.get(backend_url)

    if response.status_code == 200:
        new_save_path = os.path.join(save_path, zip_file_name)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"文件保存至: {save_path}")
    else:
        print("请求后端失败")

def interact(url, zip_path, work_dir, zip_file_name):
    with open(zip_path, 'rb') as file:
        # 发送POST请求
        response = requests.post(url, files={'zip_file': file})
        if response.status_code == 200:
            new_save_path = os.path.join(work_dir, zip_file_name)
            with open(work_dir, 'wb') as file:
                file.write(response.content)
            print(f"文件保存至: {work_dir}")
        else:
            print("请求后端失败")

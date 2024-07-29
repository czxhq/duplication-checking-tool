import os

import requests


def interact(url, zip_path, work_dir, zip_file_name):
    with open(zip_path, 'rb') as file:
        # 发送POST请求
        response = requests.post(url, files={'zip_file': file})
        if response.status_code == 200:
            new_save_path = os.path.join(work_dir, zip_file_name)
            with open(new_save_path, 'wb') as file:
                file.write(response.content)
            print(f"文件保存至: {new_save_path}")
        else:
            print("请求后端失败")

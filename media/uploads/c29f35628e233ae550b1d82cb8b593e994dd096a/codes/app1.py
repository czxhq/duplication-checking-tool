import requests

# 本地zip文件的路径
zip_file_path = 'D://downloaded_files.zip'
# 后端服务的URL
url = 'http://60.205.191.48:8000/test1'

# 打开文件
with open(zip_file_path, 'rb') as file:
    # 发送POST请求
    response = requests.post(url, files={'zip_file': file})

# 输出响应内容
print(response.json())
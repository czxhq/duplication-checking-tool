# Config Guide
To use this, change the corresponding field in **global_config.py** to your own, such as *'localhost'*

When using *'localhost'*, add the following code to the beginning of the file
```
from global_config import localhost
```
use the port **8000**
# login
```python
url = 'http://'+'localhost'+':8000/login/'
json = {
  'username': 'czx',
  'password': 'qaz123qaz'
}
resp = {
  'result': # success, logined, wrong 
}
```
# logout
```python
url = 'http://'+'localhost'+':8000/logout/'
json = {
  'username': 'czx'
}
resp = {
  'result': # success
}
```
# register
```python
url = 'http://'+'localhost'+':8000/register/'
json = {
  'username': 'czx',
  'password': 'qaz123qaz',
  'password_confirm': 'qaz123qaz'
}
resp = {
  'result': # success, exist, mismatch, empty-u(username), empty-p(password), empty-c(password_confirm) 
}
```
# change_password
```python
url = 'http://'+'localhost'+':8000/change_password/'
json = {
  'username': 'czx',
  'password': 'qaz123qaz',
  'new_pw': 'qaz1234qaz'
}
```

# upload(上传查重文件)


```python
# 既要post, 又要下载
url = 'http://'+'localhost'+':8000/upload/'
# zip文件夹要装入一个文件夹(装查重的文件)和一个名为PACKAGE.json的文件
# resp的内容是装有html的zip文件
```

```json
{
    'username': 'czx',
    'date': '', // 这个是一个显示时间的字符串, 精确到秒
    'foldername': 'codes', //装查重文件的文件夹的名字
}
```



# getRecords(获取某用户的所有记录)

```python
# 使用get方法
url = 'http://'+'localhost'+':8000/getRecords/'
json = {
  'username': 'czx',
}
resp = {
  'result': [{'id': 1, 'date':''}] # 返回的是一个列表, 每一项是一个字典, 包含查重id和时间, 没有记录就是空列表
}
```





# load(获取完整的记录信息下载zip)

```python
# 使用get方法
url = 'http://'+'localhost'+':8000/load/'
json = {
  'id': 1, # 该id必须是存在的id
}
# resp的内容是装有html的zip文件
}
resp = {
  'result': # success, mismatch, empty
}
```

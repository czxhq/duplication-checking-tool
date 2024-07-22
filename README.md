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

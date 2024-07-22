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
```
# logout
```python
url = 'http://'+'localhost'+':8000/logout/'
```
# register
```python
url = 'http://'+'localhost'+':8000/register/'
```

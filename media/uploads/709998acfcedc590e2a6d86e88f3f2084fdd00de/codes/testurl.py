import requests
params = {
    'username': 'czx',
    'password': 'qaz123qaz'
}

params1 = {
    'username': 'admin',
    'password': 'admin123admin',
}

params2 = {
    'username': 'newuser',
    'password': 'newpassword'
}

param3 = {
    'username': 'newuser',
    'password': 'newpassword',
    'new_pw': ''
}

param4 = {
    'username': 'newuser',
    'password': 'newpassword1',
    'new_pw': 'newpassword'
}

param5 = {
    'username': 'czx'
}
def login(param):
    resp = requests.get('http://8.141.14.176:8000/login/', params=param)
    print(resp.json())
def logout(param):
    resp = requests.get('http://8.141.14.176:8000/logout/', params=param)
    print(resp.json())
def register(param):
    resp = requests.get('http://8.141.14.176:8000/register/', params=param)
    print(resp.json())
def change_password(param):
    resp = requests.get('http://8.141.14.176:8000/change_password/', params=param)
    print(resp.json())
def get_records(param):
    resp = requests.get('http://8.141.14.176:8000/getRecords/', params=param)
    print(resp.json())
get_records(param5)


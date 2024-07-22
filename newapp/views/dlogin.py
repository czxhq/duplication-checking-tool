from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from newapp.models.duser import DUser 

def dlogin(request):
    data = request.GET
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({
            'result': 'wrong'
        })
    duser = DUser.objects.get(user=user)
    if duser.is_login:
        return JsonResponse({
            'result': 'logined'
        })
    login(request, user)
    duser.is_login = True
    duser.save()
    return JsonResponse({
        'result': 'success'
    })


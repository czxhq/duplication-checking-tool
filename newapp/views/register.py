from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from newapp.models.duser import DUser

def register(request):
    data = request.GET
    username = data.get('username', "").strip()
    password = data.get('password', "").strip()
    password_confirm = data.get('password_confirm', "").strip()
    if not username:
        return JsonResponse({
            'result': 'empty-u'
        })
    if not password:
        return JsonResponse({
            'result': 'empty-p'
        })
    if not password_confirm:
        return JsonResponse({
            'result': 'empty-c'
        })
    if password != password_confirm:
        return JsonResponse({
            'result': 'mismatch'
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': 'exist'
        })
    user = User(username=username)
    user.set_password(password)
    user.save()
    DUser.objects.create(user=user)
    return JsonResponse({
        'result': 'success'
    })


from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from newapp.models.duser import DUser

def dlogout(request):
    data = request.GET
    username = data.get('username')
    user = User.objects.get(username=username)
    duser = DUser.objects.get(user=user)
    if not user.is_authenticated:
        return JsonResponse({
            'result': 'success',
        })
    logout(request)
    duser.is_login = False
    duser.save()
    return JsonResponse({
        'result': 'success',
    })

from django.contrib.auth import authenticate
from django.http import JsonResponse

def change_password(request):
    data = request.GET
    username = data.get('username')
    password = data.get('password')
    new_pw = data.get('new_pw')
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({
            'result': 'mismatch'
        })
    if not new_pw:
        return JsonResponse({
            'result': 'empty'
        })
    user.set_password(new_pw)
    user.save()
    return JsonResponse({
        'result': 'success'
    })

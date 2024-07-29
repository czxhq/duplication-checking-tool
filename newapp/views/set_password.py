from django.contrib.auth.models import User
from django.http import JsonResponse

def set_password(request):
    data = request.GET
    username = data.get("username")
    password = data.get("password", "").strip()
    password_confirm = data.get("password_confirm", "").strip()
    user = User.objects.get(username=username)
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
    user.set_password(password)
    user.save()
    return JsonResponse({
        'result': 'success'
    })

from newapp.models.duser import DUser
from django.contrib.auth.models import User
from django.http import JsonResponse

def getSecurity(request):
    data = request.GET
    username = data.get("username")
    user = User.objects.get(username=username)
    duser = DUser.objects.get(user=user)
    if not duser.is_sec:
        return JsonResponse({
            'result': 'no'
        })
    que1 = duser.que1
    que2 = duser.que2
    return JsonResponse({
        'result': 'yes',
        'que1': que1,
        'que2': que2
    })

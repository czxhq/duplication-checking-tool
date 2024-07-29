from django.http import JsonResponse
from django.contrib.auth.models import User
from newapp.models.duser import DUser

def isLong(str):
    return len(str) > 255

def setSecurity(request):
    data = request.GET
    username = data.get("username")
    que1 = data.get("que1")
    ans1 = data.get("ans1")
    que2 = data.get("que2")
    ans2 = data.get("ans2")
    if not que1 or not ans1 or not que2 or not ans2:
        return JsonResponse({
            'result': 'empty'
        })
    if isLong(que1) or isLong(ans1) or isLong(que2) or isLong(ans2):
        return JsonResponse({
            'result': 'too-long'
        })
    user = User.objects.get(username=username)
    duser = DUser.objects.get(user=user)
    duser.que1 = que1
    duser.ans1 = ans1
    duser.que2 = que2
    duser.ans2 = ans2
    duser.is_sec = True
    duser.save()
    return JsonResponse({
        'result': 'success'
    })

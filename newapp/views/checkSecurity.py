from django.http import JsonResponse
from newapp.models.duser import DUser
from django.contrib.auth.models import User

def checkSecurity(request):
    data = request.GET
    username = data.get("username")
    ans1 = data.get("ans1")
    ans2 = data.get("ans2")
    user = User.objects.get(username=username)
    duser = DUser.objects.get(user=user)
    if ans1 == duser.ans1 and ans2 == duser.ans2:
        return JsonResponse({
            'result': 'success'
        })
    return JsonResponse({
        'result': 'failed'
    })

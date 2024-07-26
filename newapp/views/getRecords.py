from django.http import JsonResponse
from newapp.models.record import Record

def getRecords(request):
    data = request.GET
    username = data.get('username')
    li = []
    records = Record.objects.filter(username=username)
    for record in records:
        dict = {}
        dict['id'] = record.id
        dict['date'] = record.date
        li.append(dict)
    return JsonResponse({
        'result': li
    })

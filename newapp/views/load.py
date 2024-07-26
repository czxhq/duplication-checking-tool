from django.http import FileResponse
from newapp.models.record import Record

def load(request):
    data = request.GET
    rid = data.get('id')
    record = Record.objects.get(id=rid)
    zip_path = record.res_path
    response = FileResponse(open(zip_path, 'rb'), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="downloaded_files.zip"'
    return response

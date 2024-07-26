from django.http import FileResponse
from zipfile import ZipFile
from django.core.files import File
import os
import json

def upload(request):
    filename = 'PACKAGE.json'
    if request.method == 'POST':
        zip_file = request.FILES['zip_file']
        dfile = File(zip_file)
        instance = Record.objects.create(pre=dfile)
        zip_path = instance.pre.path
        folder = os.path.dirname(zip_path)
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(folder)
        json_path = os.path.join(folder, filename)
        with open(json_path, 'r') as file:
            data = json.load(file)
            instance.username = data.username
            instance.date = data.date
            folder_path = os.path.join(folder, data.foldername)
            respath = os.path.join(folder_path, 'result.zip')
            instance.res_path = respath
            instance.save()
            # call function(folder_path)
            response = FileResponse(open(res_path, 'rb'), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="downloaded_files.zip"'
            return response




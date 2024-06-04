from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializer import FileSerializer

gauth = GoogleAuth()

client_json_path = 'api/client_secrets.json'
gauth.DEFAULT_SETTINGS['client_config_file'] = client_json_path


@api_view(['POST'])
def filecreate(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data.get('data')
        name = serializer.validated_data.get('name')
        drive = GoogleDrive(gauth)
        # id папки NOVAtest на Google Drive
        id = '1nX-d27PxbC3Zefbtqs8vavWI-k4lAZSu'
        # Создается экземпляр GoogleDriveFile с названием name
        textfile = drive.CreateFile({'title': name, 'parents':  [{'id': id}]})
        # Создается содержание файла данными data
        textfile.SetContentString(data)
        # Файл загружается на Google Drive
        # в папку с id=1nX-d27PxbC3Zefbtqs8vavWI-k4lAZSu
        textfile.Upload()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

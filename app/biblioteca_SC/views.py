from django.shortcuts import render
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
# Create your views here.

def upload_pdf(request):
    return render(request, 'upload_pdf.html')

def pdf_uploaded(request):

    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = '/home/analista/S-C/Biblioteca-UNERG-SC/app/biblioteca_SC/client_secret_1086440147501-gnjvr0he4m6r9eidlmuat4sjkjje3isn.apps.googleusercontent.com.json'
    creds = None
    creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    pdf_file = request.FILES.get('pdf_file')
    file_upload = MediaFileUpload(pdf_file.temporary_file_path(), mimetype='application/pdf')

    drive_service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': pdf_file.name, 'parents': ['1kSrmg44-0UBubcPzEfpnQHgFequVGKOj']}
    file = drive_service.files().create(body=file_metadata, media_body=file_upload, fields='id').execute()

    # Lógica para guardar el archivo PDF en Google Drive
    return render(request, 'pdf_uploaded.html')

# def hola(request):
#     title = 'SERVICIO COMUNITARIO'
#     return render(request,'index.html', {
#         'title' : title
#     })
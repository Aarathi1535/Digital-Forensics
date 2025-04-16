from django.shortcuts import render
from .models import UploadedDocument
from .detection2 import classify_document
import os

def upload_document(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        doc = UploadedDocument(document=uploaded_file)
        doc.save()

        file_path = doc.document.path
        result = classify_document(file_path)

        return render(request, 'result.html', {'result': result, 'file_path': doc.document.url})

    return render(request, 'upload.html')

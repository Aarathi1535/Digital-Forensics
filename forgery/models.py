from django.db import models

class UploadedDocument(models.Model):
    document = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

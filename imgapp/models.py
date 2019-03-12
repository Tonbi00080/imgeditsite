from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    cvt_type = models.CharField(max_length=255)
    img= models.FileField(upload_to='img/')
    edittedImg= models.FileField(upload_to='edittedImg/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.utils import timezone

def get_image_path(instance, filename):
    return "img/%s.jpg" % instance.name

# Create your models here.
class Image(models.Model):
    name = models.CharField(primary_key=True, max_length=255, verbose_name='画像名')
    cvt_type = models.CharField(max_length=255, verbose_name='編集タイプ')
    img= models.FileField(upload_to=get_image_path, verbose_name='加工したい画像')
    edittedImg= models.FileField(upload_to='edittedImg/', verbose_name='加工した画像')
    uploaded_at = models.DateTimeField(default=timezone.now)

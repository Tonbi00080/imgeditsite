from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def index(request):
    return render(request,'imgapp/index.html')

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # ファイルの保存
            form.save()
            # descriptionに入力した値と同じデータの画像を取得する
            item = Image.objects.get(description=form.cleaned_data['description'])
            return render(request,'imgapp/preview.html',{
            'form': form,
            'item': item
            })
    else:
        form = ImageForm()
    return render(request, 'imgapp/upload.html',{'form': form})

def preview(request):
    return render(request,'imgapp/preview.html')

def complete(request):
    return render(request,'imgapp/complete.html')

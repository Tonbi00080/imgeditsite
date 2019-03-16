from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from .editImage import editImage, setLabelCvtType, setOutputPath

# Create your views here.
def index(request):
    return render(request,'imgapp/index.html')

def upload(request):
    if "cvt_param" in request.GET:
        # query_paramが指定されている場合の処理
        cvt_param = request.GET.get("cvt_param")

        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                # ファイルの保存
                form.save()
                # descriptionに入力した値と同じデータの画像を取得する
                item = Image.objects.get(name=form.cleaned_data['name'])
                item.cvt_type = setLabelCvtType(cvt_param)
                editImage(item.img.url, item.name, cvt_param)
                item.edittedImg = setOutputPath(item.name, cvt_param)
                item.save()
                param ={
                    'cvt_param': cvt_param
                }
                return render(request,'imgapp/preview.html',{
                'form': form,
                'item': item,
                'param': param
                })
        else:
            form = ImageForm()
            cvt_param = request.GET.get("cvt_param")
            cvt_type = setLabelCvtType(cvt_param)
            param ={
                'cvt_type': cvt_type
            }
        return render(request, 'imgapp/upload.html',{
        'form': form,
        'param': param
        })
    else:
        return render(request, 'imgapp/error.html')


def preview(request):
    return render(request,'imgapp/preview.html')

def complete(request):
    return render(request,'imgapp/complete.html')

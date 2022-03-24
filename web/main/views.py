from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')


def editor(request):
    return render(request, 'main/editor.html')


def capture(request):
    if request.method == "POST":
        exec(open("C:/Users/wasti/PycharmProjects/web/web/main/capture.py").read())
    return render(request, 'main/editor.html')


import PIL.Image
import shutil
from PIL import ImageFilter
import pilgram


def filters1(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        pilgram._1977(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters2(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        pilgram.css.saturate(img, 2).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters3(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = img.filter(ImageFilter.SHARPEN).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters4(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = img.filter(ImageFilter.BLUR).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters5(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.toaster(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters6(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.inkwell(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters7(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.kelvin(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters8(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.brooklyn(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters9(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.clarendon(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters10(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.earlybird(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
    return render(request, "main/editor.html")

def filters11(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedOrig.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        shutil.copyfile(original, target)
        img_orig = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedOrig.png")
    return render(request, "main/editor.html")

def filters12(request):
    if request.method == "POST":
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        shutil.copyfile(original, target)
        img_bckp = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png")
    return render(request, "main/editor.html")


import mimetypes
from django.http import HttpResponse

def download(request):
    fl_path = r'C:\Users\wasti\PycharmProjects\web\web\main\static\resources\PhotoRed.png'
    filename = 'PhotoRed'
    with open(fl_path, 'r', encoding="utf-8") as f:
        text = f.read().decode(errors='replace')
    fl = open(fl_path, 'r', encoding="utf-8")
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response()



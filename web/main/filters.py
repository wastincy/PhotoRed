import PIL.Image
import shutil
from PIL import ImageFilter
import pilgram
img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
img.show()

original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedOrig.png'
shutil.copyfile(original, target)

def fltr_commnd():
    print()
    print("press 1 to apply 1977 filter") #эффект старой камеры
    print("press 2 to apply saturate filter") #насыщенность повысить
    print("press 3 to apply sharpen filter") # повысить четкость
    print("press 4 to apply blur filter") #заблюрить(размыть) изображение
    print("press 5 to apply toaster filter") #насыщенный первый фильтр
    print("press 6 to apply inkwell filter") #ч/б
    print("press 7 to apply kelvin filter") #ярко-контрастный
    print("press 8 to apply brooklyn filter") #более светлый
    print("press 9 to apply clarendon filter") #очень насыщенный светлый
    print("press 10 to apply earlybird filter") #насыщенный тусклый,контрастный
    print("press 11 to show the first taken image")
    print("press 12 to show previous image")
    print("press 13 to return to first taken image")
    print("press 14 to use previous image")
    print("print -1 to exit")

print(fltr_commnd())
num=input()
while (num != "-1"):


    if (num == "1"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        pilgram._1977(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()


    if (num == "2"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        pilgram.css.saturate(img, 2).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()


    if (num == "3"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\Alex\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = img.filter(ImageFilter.SHARPEN).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()

    if (num == "4"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\Alex\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = img.filter(ImageFilter.BLUR).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()

    if (num == "5"):
        original = r'C:\Users\Alex\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.toaster(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()


    if (num == "6"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\Alex\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.inkwell(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()

    if (num == "7"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.kelvin(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()

    if (num == "8"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.brooklyn(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()

    if (num == "9"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.clarendon(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()



    if (num == "10"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        img=PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img = pilgram.earlybird(img).save(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        fltr_commnd()
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        num = input()


    if (num == "11"):
        img_orig = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedOrig.png")
        img_orig.show()
        fltr_commnd()
        num = input()


    if (num == "12"):
        img_bckp = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png")
        img_bckp.show()
        fltr_commnd()
        num = input()


    if (num == "13"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedOrig.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        fltr_commnd()
        num = input()


    if (num == "14"):
        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        shutil.copyfile(original, target)
        img = PIL.Image.open(r"C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png")
        img.show()
        fltr_commnd()
        num = input()







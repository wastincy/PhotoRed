import os
import PIL.Image
def commnd():
    print()
    print("press 1 to take photo")
    print("press 2 to open filter menu")
    print("press 0 to exit")
def fltr_commnd():
    print()
    print("press filter_1 to ")
    print("press filter_2 ")
    print("press filter_3")
print("hello")
print("what do you need to do?")
print(commnd())
match = input()
while (match!=0):
    if match == "1":
        exec(open("C:/Users/wasti/PycharmProjects/web/web/main/capture.py").read())
        img = PIL.Image.open("C:/Users/wasti/PycharmProjects/web/web/static/Resources/PhotoRed.png")
        img.show()
        print(commnd())

    if match == "2":
        print("choose filters from list below")
        print(fltr_commnd())
        exec(open("C:/Users/wasti/PycharmProjects/web/web/main/filters.py").read())
        print(fltr_commnd())
        print(commnd())

    if match == "0":
        dir_name = "C:/Users/wasti/PycharmProjects/web/web/static/Resources/"
        pictr = os.listdir(dir_name)
        for item in pictr:
            if item.endswith(".png"):
                os.remove(os.path.join(dir_name, item))
        break
    match = input()






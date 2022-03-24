import cv2
import shutil
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 1600)
cam.set(4, 900)
cam.set(10, 100)



while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow("Smile,please =)", frame)


    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "C:\\Users\\wasti\\PycharmProjects\\web\\web\\main\\static\\resources\\PhotoRed.png"
        cv2.imwrite(img_name, frame)
        print("photo has been written!")
        print("Closing camera...")

        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedOrig.png'
        shutil.copyfile(original, target)

        original = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRed.png'
        target = r'C:\Users\wasti\PycharmProjects\web\web\main\static\Resources\PhotoRedBackup.png'
        shutil.copyfile(original, target)
        break
cam.release()
cv2.destroyAllWindows()

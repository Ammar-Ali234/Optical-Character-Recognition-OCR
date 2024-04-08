import cv2
from matplotlib import pyplot as pt
import easyocr

img=cv2.imread("C:\\Users\\HP\Downloads\\tt1.png")

read=easyocr.Reader(['en'],gpu=False)

text=read.readtext(img)
print(text)


for t in text:
    print(t)

    bbox, text, source=t

    cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),5)
    cv2.putText(img,text,bbox[0],cv2.FONT_HERSHEY_COMPLEX,0.65,(255,0,0),2)

pt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
pt.show()
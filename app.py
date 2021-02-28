import cv2

faceCascade=cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)
cap.set(3,640)#Weight
cap.set(4,480)#Height
cap.set(10,100)#Brightness
z=0

while True:

    success, img = cap.read()
    faces=faceCascade.detectMultiScale(img,1.1,4)
    if z==0:
        if cv2.waitKey(1) & 0xFF == ord('p'):
            z=1
            print("Stop")
        for (x,y,w,h) in faces:
            a=w*h
            if a>5000:
                #cv2.circle(img,((x+int(w/2)),(y+int(h/2))),int((h/2)+30),(0,255,0),3)
                #cv2.rectangle(img,(x-30,y-30),(x+w+30,y+h+30),(255,0,0),3)
                try:
                    cropped=cv2.GaussianBlur(img[y-30:y+h+30,x-30:x+w+30],(99,99),0)
                except:
                    pass
            try:
                img[y-30:y+h+30,x-30:x+w+30]=cropped
                #cv2.imshow("Crop",cropped)
            except:
                pass

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quit")
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        z=0
        print("Start")

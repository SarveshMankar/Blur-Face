import cv2

faceCascade=cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)
cap.set(3,640)#Weight
cap.set(4,480)#Height
cap.set(10,100)#Brightness
z=0

print("Press 'p' to Stop Blurring Face Part.\n")
print("Press 's' to Start Blurring Face Part.\n")
print("Press 'q' to Quitting.\n")

while True:

    success, img = cap.read()
    #Detecting the Face
    faces=faceCascade.detectMultiScale(img,1.1,4)
    if z==0:
        #For Stopping to Blur the face Part
        if cv2.waitKey(1) & 0xFF == ord('p'):
            z=1
            print("Stopped")
        for (x,y,w,h) in faces:
            a=w*h
            if a>5000:
                try:
                    cropped=cv2.GaussianBlur(img[y-30:y+h+30,x-30:x+w+30],(99,99),0)
                except:
                    pass
            try:
                img[y-30:y+h+30,x-30:x+w+30]=cropped
                #cv2.imshow("Crop",cropped)
            except:
                pass
    #Showing the Live Cam
    cv2.imshow("Video",img)
    
    #For Quitting
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exited")
        break
    #For Starting to Blur the face Part
    if cv2.waitKey(1) & 0xFF == ord('s'):
        z=0
        print("Started")

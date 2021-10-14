
# importation des librairies
import cv2
import os
import numpy as np
import time
# initialisation des chemins du programme
Mpath="C:/Users/aelie/Documents/02ArtsetMetiers/04Lille/07-Pjt"
os.chdir(Mpath)

def Dep(Img1,Img2,listeEch):
    Deplacement=[]
    for i in range(len(listeEch)):
        x,y,h,w=listeEch[i]
        Echan=Img1[y:y+h, x:x+w]
        result = cv2.matchTemplate(Echan, Img2, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        Deplacement+=[[max_loc[0]-x,max_loc[1]-y]]
    return(Deplacement)


# ouverture de la video
cap = cv2.VideoCapture(Mpath+'/images/tissu.mp4')

cdt=0
frame=0
Echantillonage=[[100,100,200,200]]

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")
# Read until video is completed
while (cap.isOpened()):
# Capture frame-by-frame
    prevframe=frame
    ret, frame = cap.read()
    if ret == True:
        if cdt!=0:
            deplacement=Dep(prevframe,frame,Echantillonage)
            for j in range(len(Echantillonage)):
                cv2.rectangle(frame, (Echantillonage[j][0],Echantillonage[j][1]), (Echantillonage[j][0]+Echantillonage[j][2],Echantillonage[j][1]+Echantillonage[j][2]), (0, 255, 255), 2)
                cv2.rectangle(frame, (Echantillonage[j][0]+deplacement[j][0], Echantillonage[j][1]+deplacement[j][1]),
                      (Echantillonage[j][0] + Echantillonage[j][2]+deplacement[j][0], Echantillonage[j][1] + Echantillonage[j][2]+deplacement[j][1]),
                      (0, 0, 255), 2)

        # Display the resulting frame
        cdt=1
        cv2.imshow('Frame', frame)
    # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break
# When everything done, release the video capture object
cap.release()
cv2.destroyAllWindows()




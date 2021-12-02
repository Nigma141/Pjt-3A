# importation des librairies
import os
import cv2
import etallonageCam
import time
import numpy as np
import matplotlib.pyplot as plt

# initialisation des chemins du programme


def Dep(Img1, Img2, listeEch):
    Deplacement = []
    for i in range(len(listeEch)):
        x, y, h, w = listeEch[i]
        Echan = Img1[y:y + h, x:x + w]
        result = cv2.matchTemplate(Echan, Img2, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        Deplacement += [[max_loc[0] - x, max_loc[1] - y]]
    return (Deplacement)





def main(Mpath):
    # ouverture de la video
    cap = cv2.VideoCapture(Mpath + '/images/tissu.avi')
    cdt = 0
    frame = 0
    #Echantillonage = [[500, 500, 200, 200],[100, 500, 200, 200]]
    Echantillonage = [[100, 150, 200, 200]]
    DX=[]

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
    # Read until video is completed
    while (cap.isOpened()):
    # Capture frame-by-frame
        prevframe = frame
        ret, frame = cap.read()
        temps=[]
        if ret == True:
            frame = cv2.resize(frame, (480, 720))
            if cdt != 0:
                deplacement = Dep(prevframe, frame, Echantillonage)
                for j in range(len(Echantillonage)):
                    cv2.rectangle(frame, (Echantillonage[j][0], Echantillonage[j][1]), (
                    Echantillonage[j][0] + Echantillonage[j][2], Echantillonage[j][1] + Echantillonage[j][2]),
                              (0, 255, 255), 2)
                    cv2.rectangle(frame,
                            (Echantillonage[j][0] + deplacement[j][0], Echantillonage[j][1] + deplacement[j][1]),
                            (Echantillonage[j][0] + Echantillonage[j][2] + deplacement[j][0],
                            Echantillonage[j][1] + Echantillonage[j][2] + deplacement[j][1]),
                            (0, 0, 255), 2)
                DX+=[deplacement]
            # Display the resulting frame
            cdt = 1
            cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                # Break the loop
        else:
            break
        # When everything done, release the video capture object
    cap.release()
    cv2.destroyAllWindows()
    return (DX)

def Affichage(DX):
    listeX=[]
    listeY = []
    for i in range(len(DX[0])):
        dx=[DX[j][i][0] for j in range(len(DX))]
        dy = [DX[j][i][1] for j in range(len(DX))]
        X=np.cumsum(dx)
        Y=np.cumsum(dy)
        plt.plot(X,Y)
        listeX+=[[X]]
        listeY+= [[Y]]
    plt.show()
    print(listeX,listeY)
    return()




if __name__ == "__main__":
    print("Debut")
    Mpath=os.getcwd()
    #etallonageCam.etalonnage(Mpath+'\images\carte.jpg',Mpath+'\images\etalonnage.jpg')
    DX=main(Mpath)
    Affichage(DX)
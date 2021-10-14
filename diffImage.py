# importation des librairies
import cv2
import os
import numpy as np
import time
# initialisation des chemins du programme
Mpath="C:/Users/aelie/Documents/02ArtsetMetiers/04Lille/07-Pjt"
os.chdir(Mpath)


# ouverture des images
img1 = cv2.imread(Mpath+"/images/img1.jpg",0)
img2 = cv2.imread(Mpath+"/images/img2.jpg",0)
img3 = cv2.imread(Mpath+"/images/img3.jpg",0)
img4 = np.copy(img1)
img5 = np.copy(img2)



# traitement fait sur les images
result = cv2.matchTemplate(img3, img1, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
w = img3.shape[1]
h = img3.shape[0]
cv2.rectangle(img4, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)

result2 = cv2.matchTemplate(img3, img2, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result2)
w = img3.shape[1]
h = img3.shape[0]
cv2.rectangle(img5, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)


#affichage
tailleImage=(480,360)
Rendu1 = cv2.resize(img1, tailleImage)
Rendu2 = cv2.resize(img3, tailleImage)
affichage1 = np.hstack((Rendu1, Rendu2))

Rendu3=cv2.resize(result, tailleImage)
Rendu4=cv2.resize(img4, tailleImage)
Rendu5=cv2.resize(img5, tailleImage)
affichage2=np.hstack((Rendu4, Rendu5))
affichage=np.vstack((affichage1,affichage2))
cv2.imshow('affichage', affichage)
cv2.imshow('traitement', Rendu3)
cv2.waitKey(0)
cv2.destroyWindow()

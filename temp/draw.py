import cv2
import numpy as np
from utils import *
from config import *
import os
landmarks = np.load('../dat/standard_landmark_68pts.npy')
landmarks[:,0] += 0.0
landmarks[:,1] += 0.25
landmarks *= 128*0.5
landmarks[:,0] += 64
landmarks[:,1] += 64
lm = []
lm.append(landmarks[36]*0.5 + 0.5*landmarks[39])
lm.append(landmarks[42]*0.5 + 0.5*landmarks[45])
lm.append(landmarks[33])
lm.append(landmarks[48])
lm.append(landmarks[54])

print(lm)


imgs = os.listdir('imgs')
for imgpath in imgs:
    img = cv2.imread(os.path.join('imgs',imgpath))
    draw_landmarks(img,[landmarks],'RED')
    draw_landmarks(img,[lm],'GREEN')
    cv2.imwrite(os.path.join('crop',imgpath),img)

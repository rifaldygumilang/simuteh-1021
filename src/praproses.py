import cv2
import numpy as np
def praproses(img_bgr, p=None):
    p = {'lebar': 640, **(p or {})}
    h, w = img_bgr.shape[:2]
    img = cv2.resize(img_bgr, (p['lebar'], int(round(h * p['lebar'] / w))), interpolation=cv2.INTER_AREA)
    return img


import cv2
import numpy as np

def tepi_acuan(mask):
    m = (mask > 0).astype(np.uint8)
    return ((m - cv2.erode(m, np.ones((3, 3), np.uint8))) > 0).astype(np.uint8) * 255

def skor_tepi(prediksi, acuan, toleransi=2):
    p = prediksi > 0
    a = acuan > 0
    if p.sum() == 0 or a.sum() == 0: return 0.0, 0.0, 0.0
    jarak_ke_a = cv2.distanceTransform((~a).astype(np.uint8), cv2.DIST_L2, 3)
    jarak_ke_p = cv2.distanceTransform((~p).astype(np.uint8), cv2.DIST_L2, 3)
    presisi = float((jarak_ke_a[p] <= toleransi).mean())
    recall = float((jarak_ke_p[a] <= toleransi).mean())
    f1 = 0.0 if presisi + recall == 0 else 2 * presisi * recall / (presisi + recall)
    return round(presisi, 3), round(recall, 3), round(f1, 3)

def iou(a, b):
    a, b = a > 0, b > 0
    gabungan = (a | b).sum()
    return 1.0 if gabungan == 0 else float((a & b).sum() / gabungan)

def mask_daun_awal(img_bgr):
    s = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)[:, :, 1]
    _, m = cv2.threshold(s, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return m

def bercak_awal(img_praproses, m_daun, kanal=2, k=4.0):
    c = img_praproses[:, :, kanal]
    median = np.median(c[m_daun > 0])
    mad = np.median(np.abs(c[m_daun > 0] - median))
    ambang = median - k * mad
    _, biner = cv2.threshold(c, ambang, 255, cv2.THRESH_BINARY_INV)
    return cv2.bitwise_and(biner, m_daun)

def canny_persentil(gray, q=95):
    if len(gray.shape) == 3: gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    hi = np.percentile(gray, q)
    lo = hi * 0.5
    blurred = cv2.GaussianBlur(gray, (5, 5), 1.5)
    return cv2.Canny(blurred, lo, hi)

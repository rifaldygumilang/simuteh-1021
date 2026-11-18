"""bercak.py: analisis bercak SIMUTEH (dipakai ulang mulai P7)."""
import json
import cv2
import numpy as np
from utils_tepi import mask_daun_awal, bercak_awal

PARAM_BERCAK = {
    "kanal": 2, "k": 4.0, "se_bentuk": "elips", "se_open": 5, "se_close": 5,
    "luas_min": 20, "bulat_min": 0.5, "rasio_maks": 1.8,
    "batas_ringan": 0.1, "batas_berat": 2.0, "mm_per_px": 0.4375,
}
_BENTUK = {"elips": cv2.MORPH_ELLIPSE, "persegi": cv2.MORPH_RECT, "silang": cv2.MORPH_CROSS}

def _se(p, uk):
    return cv2.getStructuringElement(_BENTUK[p["se_bentuk"]], (uk, uk))

def bersihkan(biner, p):
    if p["se_open"] > 0:
        biner = cv2.morphologyEx(biner, cv2.MORPH_OPEN, _se(p, p["se_open"]))
    if p["se_close"] > 0:
        biner = cv2.morphologyEx(biner, cv2.MORPH_CLOSE, _se(p, p["se_close"]))
    return biner

def ukur_dan_saring(biner, p):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(biner, connectivity=8)
    keluar = np.zeros_like(biner)
    daftar = []
    for i in range(1, num_labels):
        luas = stats[i, cv2.CC_STAT_AREA]
        if luas == 0: continue
        mask_komponen = (labels == i).astype(np.uint8) * 255
        contours, _ = cv2.findContours(mask_komponen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            cnt = contours[0]
            keliling = cv2.arcLength(cnt, True)
            kebulatan = (4 * np.pi * luas) / (keliling ** 2) if keliling > 0 else 0
            rect = cv2.minAreaRect(cnt)
            (w, h) = rect[1]
            rasio_aspek = max(w, h) / min(w, h) if (w > 0 and h > 0) else 99.9
            if (luas >= p["luas_min"]) and (kebulatan >= p["bulat_min"]) and (rasio_aspek <= p["rasio_maks"]):
                keluar[labels == i] = 255
                daftar.append({"luas": luas, "keliling": round(keliling, 2), "kebulatan": round(kebulatan, 3), "rasio_aspek": round(rasio_aspek, 3)})
    return keluar, daftar

def analisis_daun(img_praproses, p=None):
    p = {**PARAM_BERCAK, **(p or {})}
    m_daun = mask_daun_awal(img_praproses)
    biner = bercak_awal(img_praproses, m_daun, kanal=p["kanal"], k=p["k"])
    m_bercak, daftar = ukur_dan_saring(bersihkan(biner, p), p)
    luas_daun = np.sum(m_daun > 0)
    luas_bercak = np.sum(m_bercak > 0)
    persen = (luas_bercak / luas_daun) * 100.0 if luas_daun > 0 else 0.0
    if persen < p["batas_ringan"]: kelas = "Sehat"
    elif persen < p["batas_berat"]: kelas = "Ringan"
    else: kelas = "Berat"
    return {"mask_daun": m_daun, "mask_bercak": m_bercak, "jumlah_bercak": len(daftar), "persen_bercak": round(float(persen), 3), "kelas": kelas, "bercak": daftar}

def simpan_param(p, path="../hasil/param_bercak.json"):
    with open(path, "w") as f:
        json.dump({**PARAM_BERCAK, **p}, f, indent=2)

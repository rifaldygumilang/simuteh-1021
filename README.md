# Proyek Analisis Bercak SIMUTEH (P5-P6)
Repositori ini berisi modul untuk menganalisis bercak pada daun teh menggunakan operasi morfologi dan komponen terhubung.
## Ringkasan Hasil P5-P6
- **P5 (Praproses & Morfologi):** Implementasi thresholding, operasi Opening (menghilangkan noise) dan Closing (menutup lubang) menggunakan Structuring Element elips.
- **P6 (Integrasi & Evaluasi):** Modul bercak.py berhasil dibuat. Evaluasi pada dataset simulasi menunjukkan performa yang baik. Analisis kesalahan mengidentifikasi false positive akibat bayangan dan false negative akibat kontras rendah.
## Cara Memakai analisis_daun
Fungsi utama untuk menganalisis citra daun adalah analisis_daun yang terdapat di dalam file src/bercak.py.
Contoh Penggunaan:
```python
import cv2
import sys
sys.path.append('./src')
import bercak

img = cv2.imread('path/ke/gambar_teh.png')
hasil = bercak.analisis_daun(img)

print(f"Kelas Mutu: {hasil['kelas']}")
print(f"Persen Bercak: {hasil['persen_bercak']} %")
```

## Tag Rilis
Versi ini ditandai dengan tag: v0.3-morfologi.

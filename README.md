# Proyek Analisis Bercak Daun Teh (SIMUTEH-1021)

Repositori ini berisi rangkaian modul praktikum pengolahan citra digital untuk analisis dan deteksi bercak pada daun teh menggunakan pustaka OpenCV dan Python.

## 📌 Ringkasan Tahapan Modul (P1 - P6)

* **Modul P1 (Lingkungan & Dasar Citra):** Inisialisasi lingkungan kerja Python, konfigurasi pustaka OpenCV dan NumPy, serta pemuatan citra dasar.
* **Modul P2 (Analisis Ruang Warna):** Analisis karakteristik warna citra daun dan pemisahan kanal warna (RGB/BGR) untuk menonjolkan area tertentu.
* **Modul P3 (Histogram Intensitas):** Analisis distribusi intensitas piksel dan peregangan kontras untuk optimalisasi pencahayaan citra.
* **Modul P4 (Penapisan / Filtering):** Penerapan filter penghalus (*Gaussian Blur*) guna mereduksi *noise* pada citra daun.
* **Modul P5 (Praproses & Deteksi Tepi):** Tahap segmentasi awal menggunakan teknik penapisan biner serta *Canny Edge Detection* untuk mendeteksi batas tepi daun dan area bercak.
* **Modul P6 (Operasi Morfologi & Analisis Bercak):** Penerapan operasi morfologi (*Opening* untuk menghilangkan *noise* dan *Closing* untuk menutup lubang menggunakan *Structuring Element*) serta perhitungan analisis bercak daun secara komputasional.

## 📁 Struktur Direktori Proyek
* `notebook/`: Berisi file Jupyter Notebook lengkap dari modul P1 hingga P6.
* `src/`: Berisi skrip fungsi Python pendukung (*preprocessing*, deteksi tepi, dan analisis bercak).
* `data/`: Kumpulan data citra uji coba.
* `hasil/`: Output parameter dan hasil pengolahan citra.

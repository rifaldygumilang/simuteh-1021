import cv2
import matplotlib.pyplot as plt
def baca(path): return cv2.imread(path)
def tampil(images, titles, ukuran=(15, 5)):
    fig, axes = plt.subplots(1, len(images), figsize=ukuran)
    if len(images) == 1: axes = [axes]
    for ax, img, title in zip(axes, images, titles):
        if len(img.shape) == 3: ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        else: ax.imshow(img, cmap='gray')
        ax.set_title(title); ax.axis('off')
    plt.tight_layout(); plt.show()

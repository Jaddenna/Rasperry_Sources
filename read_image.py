import matplotlib.image as mimg
import matplotlib.pyplot as plt
import numpy as np

class Read_Image:
    def __init__(self, cols=64, rows=64):
        self.cols = cols
        self.rows = rows

    def compress(self):
        image_path = input("Dateipfad: ")

        dpi = 80

        img = plt.imread(image_path)
        height, width, nbands = img.shape

        figsize = 64 / float(dpi), 64 / float(dpi)

        fig = plt.figure(figsize=figsize)

        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        ax.imshow(img, interpolation='nearest')
        ax.set(xlim=[0, width], ylim=[height, 0], aspect=1)

        fig.savefig(image_path.replace(".png", "_comprimiert.png"), dpi=dpi, transparent=True)

    def get_rgb_matrix(self):
        image_path = input("Dateipfad komprimiert: ")
        try:
            img = plt.imread(image_path)
        except ValueError:
            return
        
        for r in range(len(img)):
            for c in range(len(img[r])):
                img[r][c][0] = self.to_rgb(img[r][c][0])
                img[r][c][1] = self.to_rgb(img[r][c][1])
                img[r][c][2] = self.to_rgb(img[r][c][2])

        return img


    def to_rgb(self, color):
        return  int(color * 255)

if __name__ == '__main__':
    ri = Read_Image()
    ri.compress()
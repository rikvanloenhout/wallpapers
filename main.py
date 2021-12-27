import os
import time
import matplotlib.pyplot as plt

from src import julia
from src import mandelbrot
from src import ulam

def generate(module, name, width, height, cmap):
    dpi = 100
    plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)

    plt.imshow(module.generate(height, width), cmap=cmap, interpolation='nearest')
    plt.axis('off')
    plt.margins(0,0)

    plt.savefig(os.path.join("./images", name + ".png"), bbox_inches='tight', pad_inches = 0)

if __name__ == "__main__":

    width  = 1920
    height = 1080
    cmap = "magma" # viridis, plasma, inferno, gist_rainbow

    width = 3840
    height = 2160

    modules = {
        # "julia":        julia,
        # "mandelbrot":   mandelbrot,
        "ulam":         ulam
    }

    for name in modules:
        generate(modules[name], name, width, height, cmap)

import os
import time
import sys
import argparse
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

    parser=argparse.ArgumentParser()
    parser.add_argument('-r', '--resolution', help='resolution, e.g. 1920x1080')
    parser.add_argument('-c', '--colormap', help='pillow color map name')

    args=parser.parse_args()

    width  = 1920
    height = 1080
    cmap = "magma" # viridis, plasma, inferno, gist_rainbow

    if args.resolution:
        parts = args.resolution.split("x")
        width  = parts[0]
        height = parts[1]

    if args.colormap:
        cmap = args.colormap

    modules = {
        "julia":        julia,
        "mandelbrot":   mandelbrot,
        "ulam":         ulam
    }

    for name in modules:
        generate(modules[name], name, width, height, cmap)

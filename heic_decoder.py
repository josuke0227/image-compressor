import os
import pyheif
from PIL import Image


def main(data, file_name):
    i = pyheif.read_heif(data)
    pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
    new_file = os.path.splitext(file_name)[0] + ".jpg"
    pi.save(new_file, "JPEG")
    return new_file

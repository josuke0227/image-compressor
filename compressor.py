from PIL import Image


def main(file_name, save_dir, quality):
    img = Image.open(file_name)
    img.save(save_dir+"/compressed/"+"Compressed_" +
             file_name, optimize=True, quality=quality)

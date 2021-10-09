import os
import whatimage
import heic_decoder
import compressor


def main(directory, quality):
    print("Compressing files...")

    if directory:
        os.chdir(directory)
        os.mkdir("compressed")

    files = os.listdir()

    for file in files:
        try:
            with open(file, "rb") as f:
                data = f.read()
                fmt = whatimage.identify_image(data)
                if fmt != None:
                    if fmt == "heic":
                        decoded_file_name = heic_decoder.main(data, file)
                        compressor.main(decoded_file_name, directory,
                                        quality=quality)
                        os.remove(decoded_file_name)
                    else:
                        compressor.main(file, directory,  quality=quality)

        except IsADirectoryError:
            continue
    print("Done!")


directory = input("Enter the path: ")
power = input("Choose the compression power from 'H / M / L': ")
quality_preset = {"H": 30, "M": 65, "L": 90}
quality = quality_preset[power]
main(directory, quality)

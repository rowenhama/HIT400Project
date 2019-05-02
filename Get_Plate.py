from subprocess import check_output as qx
import cv2
import math
from tkinter import filedialog as fd
import tkinter as tk
import easygui
import os
import sklearn


def read_img(filename):
    # filename = easygui.fileopenbox()
    # print(filename)
    # cmd = r"C:\Users\James\PycharmProjects\test_alpr\openalpr\alpr.exe -n 1 -j C:\Users\James\PycharmProjects\test_alpr\LicPlateImages\2.png"

    cmd = r"C:\Users\James\PycharmProjects\test_alpr\openalpr\alpr.exe -n 1 -j " + filename
    output = qx(cmd)

    out_str = output.decode("utf-8")
    plate_txt = out_str.find("plate")

    if plate_txt != -1:
        print(out_str)
        plate_txt = plate_txt + 8
        plate_txt_end = out_str.find('","', plate_txt)

        print("============================================\n           Printing plate #\n")
        x = plate_txt
        plate_num = ""
        while x < plate_txt_end:
            plate_num = plate_num + out_str[x]
            x = x + 1

        print(plate_num)
        return plate_num


def count_files():
    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    foldername = fd.askdirectory()
    path, dirs, files = next(os.walk(foldername))
    file_count = len(files)
    print(file_count)
    #
    # list_of_file = os.listdir(foldername)
    # number_files = len(list_of_file)
    # print(number_files)
    root.destroy()


def iter_files():
    plates = list()
    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    foldername = fd.askdirectory()
    directory = os.fsencode(foldername)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # print(os.path.join(directory, filename))
            filepath = os.path.join(directory.decode("utf-8"), filename)
            plates.append(read_img(filepath))
            continue
        else:
            print("No more image files available!\nPlates found:\n\t\t", plates)
    root.destroy()


def main():
    # read_img()
    # extract_frame()
    # count_files()
    iter_files()


if __name__ == '__main__':
    main()

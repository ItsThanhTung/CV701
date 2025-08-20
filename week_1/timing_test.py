import time
import numpy as np
import torch
import argparse
import cv2
import os
import pickle
import json
import subprocess
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--load_folder", type=str, nargs="+", required=True)
    parser.add_argument("--output_file", type=str, required=True)
    return parser.parse_args()

def load_image(image_path):
    image = Image.open(image_path)
    return image

def load_image_pickle(image_path):
    with open(image_path, "rb") as f:
        image = pickle.load(f)
    return image


def timing_test(image_folder):
    total_time = 0
    for image_file in os.listdir(image_folder):
        if image_file.endswith(".png"):
            start_time = time.time()
            image = load_image(os.path.join(image_folder, image_file))
            end_time = time.time()
        elif image_file.endswith(".jpg"):
            start_time = time.time()
            image = load_image(os.path.join(image_folder, image_file))
            end_time = time.time()
        elif image_file.endswith(".pickle"):
            start_time = time.time()
            image = load_image_pickle(os.path.join(image_folder, image_file))
            end_time = time.time()
        total_time += end_time - start_time

    return total_time, total_time / len(os.listdir(image_folder))


if __name__ == "__main__":
    args = parse_args()
    with open(os.path.join(args.output_file), "w") as f:
        for image_folder in args.load_folder:
            print(f"Timing test for {image_folder}")
            total_time, average_time = timing_test(image_folder)
            json.dump({"image_folder": image_folder, 
                       "total_time": total_time, 
                       "average_time": average_time}, 
                      f, indent=4)
            f.write("\n")
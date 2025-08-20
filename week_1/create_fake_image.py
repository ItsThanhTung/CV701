import numpy as np
import argparse
import cv2
import torch
import pickle
import os
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_fake_images", type=int, required=True)
    parser.add_argument("--save_format", type=str, choices=["png", "jpg", "pickle"], required=True)
    parser.add_argument("--save_folder", type=str, required=True)
    parser.add_argument("--library", type=str, default="torch", choices=["torch", "numpy"], required=True)
    return parser.parse_args()
    
def create_fake_image(num_fake_images, save_format, library, save_folder):
    for i in range(num_fake_images):
        if library == "torch":
            fake_image = torch.randint(0, 255, (256, 256, 3), dtype=torch.uint8)
            fake_image = fake_image.numpy()
        elif library == "numpy":
            fake_image = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

        if save_format == "png" or save_format == "jpg":
            cv2.imwrite(os.path.join(save_folder, f"fake_image_{i}.{save_format}"), fake_image)
        elif save_format == "pickle":
            with open(os.path.join(save_folder, f"fake_image_{i}.pickle"), "wb") as f:
                pickle.dump(fake_image, f)
    

if __name__ == "__main__":
    args = parse_args()
    os.makedirs(args.save_folder, exist_ok=True)
    print(f"Creating {args.num_fake_images} fake images in {args.save_folder} with {args.library} library and {args.save_format} format")
    create_fake_image(args.num_fake_images, args.save_format, args.library, args.save_folder)
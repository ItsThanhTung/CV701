import numpy as np
import argparse
import cv2
import torch
import pickle
import os
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_fake_images", type=int, required=True)
    parser.add_argument("--save_folder", type=str, required=True)
    parser.add_argument("--library", type=str, default="torch", choices=["torch", "numpy"], required=True)
    return parser.parse_args()
    
def generate_image(library):
    if library == "torch":
        fake_image = torch.randint(0, 255, (256, 256, 3), dtype=torch.uint8)
        return fake_image.numpy()
    elif library == "numpy":
        return np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

def create_fake_image(num_fake_images, library, save_folder):    
    all_images = []
    # Generate all images once
    for i in range(num_fake_images):
        fake_image = generate_image(library)
        all_images.append(fake_image)
    
    # Save in all formats
    # Save individual PNG files
    png_folder = os.path.join(save_folder, "png")
    os.makedirs(png_folder, exist_ok=True)
    for i, image in enumerate(all_images):
        cv2.imwrite(os.path.join(png_folder, f"fake_image_{i}.png"), image)
    
    # Save individual pickle files
    pickle_folder = os.path.join(save_folder, "pickle")
    os.makedirs(pickle_folder, exist_ok=True)
    for i, image in enumerate(all_images):
        with open(os.path.join(pickle_folder, f"fake_image_{i}.pickle"), "wb") as f:
            pickle.dump(image, f)
    
    # Save all images in a single pickle file
    single_pickle_folder = os.path.join(save_folder, "single_file_pickle")
    os.makedirs(single_pickle_folder, exist_ok=True)
    single_pickle_path = os.path.join(single_pickle_folder, "all_fake_images.pickle")
    with open(single_pickle_path, "wb") as f:
        pickle.dump(all_images, f)


if __name__ == "__main__":
    args = parse_args()
    os.makedirs(args.save_folder, exist_ok=True)
    print(f"Creating {args.num_fake_images} fake images in {args.save_folder} with {args.library} library")
    print("Saving in all formats: PNG, individual pickle files, and single pickle file")
    create_fake_image(args.num_fake_images, args.library, args.save_folder)
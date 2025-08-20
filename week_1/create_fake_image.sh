#!/bin/bash

num_fake_images=10000

python create_fake_image.py --num_fake_images $num_fake_images \
                            --save_folder fake_images_numpy --library numpy
num_fake_images=10000

# numpy
python create_fake_image.py --num_fake_images $num_fake_images --save_format png \
                            --save_folder fake_images_png_np --library numpy
python create_fake_image.py --num_fake_images $num_fake_images --save_format jpg \
                            --save_folder fake_images_jpg_np --library numpy
python create_fake_image.py --num_fake_images $num_fake_images --save_format pickle \
                            --save_folder fake_images_pickle_np --library numpy

# torch  
python create_fake_image.py --num_fake_images $num_fake_images --save_format png \
                            --save_folder fake_images_png_torch --library torch
python create_fake_image.py --num_fake_images $num_fake_images --save_format jpg \
                            --save_folder fake_images_jpg_torch --library torch
python create_fake_image.py --num_fake_images $num_fake_images --save_format pickle \
                            --save_folder fake_images_pickle_torch --library torch
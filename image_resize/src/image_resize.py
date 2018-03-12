"""
pip install Pillow
pip install joblib
"""

from PIL import Image, ImageFilter
from joblib import Parallel, delayed
import glob
import os

IMG_BASE_DIR = '../image/base/*.jpg'
IMG_OUT_DIR = '../image/out/'

class Image_Resize:

    @staticmethod
    def get_base_images():
        return glob.glob(IMG_BASE_DIR)

    @staticmethod
    def image_resize(image_file_path):
        img = Image.open(image_file_path)
        resize_image = img.resize((512, 512), Image.LANCZOS)
        gray_img = resize_image.convert('L')
        gray_img.save(IMG_OUT_DIR + os.path.basename(image_file_path))


images = Image_Resize.get_base_images()

ret = Parallel(n_jobs=-1)(
	[
		delayed(Image_Resize.image_resize)(image)
		for image in images
	]
)

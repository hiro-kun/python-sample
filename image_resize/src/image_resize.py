"""
pip install Pillow
"""

"""
from pprint import pprint
pprint(file)
"""


from PIL import Image, ImageFilter
import glob
import os

class Image_Resize:

    @staticmethod
    def get_base_images():
        return glob.glob('../image/base/*.jpg')

    @staticmethod
    def image_resize(image_file_path):
        img = Image.open(image_file_path)
        img_resize_lanczos = img.resize((512, 512), Image.LANCZOS)
        gray_img = img_resize_lanczos.convert('L')
        gray_img.save('../image/out/' + os.path.basename(image_file_path))



images = Image_Resize.get_base_images()
for image in images:
    Image_Resize.image_resize(image)
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

files = glob.glob('../image/base/*.jpg')

for file in files:
    img = Image.open(file)
    img_resize_lanczos = img.resize((512, 512), Image.LANCZOS)
    gray_img = img_resize_lanczos.convert('L')
    gray_img.save('../image/out/' + os.path.basename(file))

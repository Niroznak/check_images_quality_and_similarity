import cv2
import imagehash
from PIL import Image


def variance_of_laplacian(image):
    # compute focus (variance of the Laplacian)
    return cv2.Laplacian(image, cv2.CV_64F).var()


def hash_average(image):
    im_hash = imagehash.average_hash(image)  # ,hash_size
    return im_hash


def get_image_params(file):
    im = cv2.imread(file)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    bright = gray.mean()
    blur = variance_of_laplacian(gray)
    try:
        im = Image.open(file).convert("L")
        hash = str(hash_average(im))
    except Exception as e:
        # raise e
        hash = 'failed hashing'
        pass
    return [file, blur, bright, hash]

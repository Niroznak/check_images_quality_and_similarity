import os


def get_image_list(data):
    if type(data) != list:
        images = []
        with open("images_list.txt", "r") as f:
            for line in f:
                images.append(line.strip())
        return images

    # create images list
    image_types = ["jpg", "gif", "png", "tga"]
    images = []
    for d in data:
        for root, Dir, file in os.walk(d):
            files = [c for c in file if c[-3:] in image_types]
            files = [root + '\\' + c for c in files]
            images += files
    # Optional, save images list to file
    with open("images_list.txt", "w") as f:
        for i in images:
            f.write(i + "\n")
    return images

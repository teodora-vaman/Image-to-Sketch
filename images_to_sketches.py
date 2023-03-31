import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from os import listdir
import argparse

def image_to_sketch(image):
    plt.figure(figsize=(20,20))
    plt.imshow(image, cmap='gray')

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    smooth_image = cv2.GaussianBlur(grayscale_image, (21,21), 0)
    sketch_image = cv2.divide(grayscale_image, smooth_image, scale=256.0)

    return sketch_image

def main(config):
    if not os.path.exists(config.image_folder):
        print("Folder does not exist")
        exit()
    
    if not os.path.exists(config.destination_folder):
        os.makedirs(config.destination_folder)

    for image_path in os.listdir(config.image_folder):
        if (image_path.endswith(".jpg")):
            image = cv2.imread(config.image_folder + "\\" + image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            sketch_image = image_to_sketch(image)
            cv2.imwrite(config.destination_folder + '\\' + image_path, sketch_image) 


if __name__ == "__main__":
    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--image_folder', type=str, default="images", help='folder that contains the images you want to transform into sketches')
        parser.add_argument('--destination_folder', type=str, default="destination", help='folder where sketches are saved')


        config = parser.parse_args()
        print(config)
        main(config)

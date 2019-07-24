import cv2
import numpy as np


def draw(image_matrix):
    # Constants
    factor = 35

    # Compute circle size
    width = len(image_matrix[0])
    height = len(image_matrix)
    radius = min(width // factor, height // factor)
    diameter = 2 * radius

    # Create a blank image
    image = np.zeros((height, width, 3), np.uint8) 
    image.fill(255)

    # maxX, maxY keep track of edges, to avoid white space
    maxX = maxY = 0

    # Draw circles
    i = 0
    while i < height:
        if i + diameter > height:
            break
        j = 0
        while j < width:
            if j + diameter > width:
                break
            centre = (j + radius, i + radius)
            block = image_matrix[i: i + radius, j: j + radius]
            colour = block.mean(axis=0).mean(axis=0)
            cv2.circle(image, centre, radius - 2, colour, -1)
            maxX = max(maxX, j + diameter)
            maxY = max(maxY, i + diameter)
            j += diameter + 1
        i += diameter + 1

    # Save image to file
    cv2.imwrite("path", image[:maxY, :maxX])


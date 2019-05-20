from random import randint
from sklearn.cluster import KMeans
import cv2
import numpy as np


# Fill out square of size in booleans (matrix of booleans)
# from position (i, j), travelling down and right
def fill(booleans, i, j, size):
    for x in range(i, i + size):
        for y in range(j, j + size):
            booleans[x][y] = 1


# Finds k most "dominant colours" using k-means clustering
def select(k, image_matrix):
    pixels = image_matrix.reshape((image_matrix.shape[0] * image_matrix.shape[1], 3))
    clt = KMeans(n_clusters = k)
    clt.fit(pixels)
    return clt.cluster_centers_


# Requires the square of the distance b/w two vectors
def dstSq(u, v):
    s = 0
    for i in range(len(u)):
        s += (u[i] - v[i])**2
    return s


# Decomposes a rectangle into a set squares randomly
def decompose(image_matrix, kMean=0):
    width = len(image_matrix[0])
    height = len(image_matrix)
    # TODO Find smart way to select min/max
    min_r = min(width, height) // 45
    max_r = min(width, height) // 20
    
    if kMean:
        colours = select(kMean, image_matrix)

    # Boolean matrix
    booleans = [[0] * width for i in range(height)]
    # Blank image (white)
    image = np.zeros((height, width, 3), np.uint8) 
    for i in range(len(image)):
        for j in range(len(image[0])):
            image[i][j] = [255, 255, 255]

    # Actual decomposition part
    for i in range(height):
        for j in range(width):
            # Check if position has been used
            if booleans[i][j] != 0:
                continue
            # Edge of matrix
            if i == height - 1 or j == width - 1:
                booleans[i][j] = 1
                continue
            # Generate random size
            size = randint(min_r, max_r + randint(1, 10))
            # See if size conflicts with existing squares or boundaries
            idx = j
            actual_width = 1
            while actual_width <= size and idx < width and booleans[i][idx] == 0:
                idx += 1
                actual_width += 1
            size = min(size, actual_width)
            if i + size >= height:
                size = height - i
            if j + size >= width:
                size = width - j
            # If the square is too small, we don't draw it
            if size < min_r:
                continue
            # Fill up rectangle
            c = (j + size // 2, i + size // 2)
            block = image_matrix[i: i + size, j: j + size]
            # Find colour in our list of colours closest to avg colour
            avg_colour = block.mean(axis=0).mean(axis=0)
            colour = avg_colour

            if kMean:
                colour = colours[0]
                dist = dstSq(avg_colour, colour)
                for k in range(1, len(colours)):
                    new = dstSq(avg_colour, colours[k])
                    if new < dist:
                        dist = new
                        colour = colours[k]
            fill(booleans, i, j, size)
            cv2.circle(image, c, size // 2 - 1, colour, -1)
    
    #cv2.imwrite("WRITEFILE/PATH/GOES/HERE.jpg", image)


if __name__ == '__main__':
    image_matrix = cv2.imread(FILE) # replace with input jpg file
    decompose(image_matrix, 0)

# non curvature ref program

# Import necessary libraries
import cv2 as cv
import matplotlib

# Adding first test image to convert default RGB to a 'computer readable' BGR
img = cv.imread("image.jpg")
img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

# Adding the list of images to imgFiles via the append method. 
imgDir = "Test_Images/"
imgFiles = os.listdir(imgDir)
imgList = []
for i in range(len(imgFiles)):
    imgList.append(mpimg.imgread(imgDir + imgFiles[i])) # mpimg is part of matplotlib

def displayImage(images, cmap = None):
    plt.figure(figsize=(40, 40))
    for i, image in enumerate(images):
        plt.subplot(3, 2, i + 1)
        plt.imshow(image, cmap)
        plt.autoscale(tight = True)
    plt.show()

displayImage(imageList)






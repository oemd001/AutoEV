import cv2 
from matplotlib import pyplot as plt 


img = cv2.imread("download.jpeg") 
  
# Convert images from RGB to required grayscale. 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
  
  
# minsize to help ensure that we're seeing an actual stop sign, not a red dot. 
stop_data = cv2.CascadeClassifier('stop_data.xml') # <-- Include .xml file. 
found = stop_data.detectMultiScale(img_gray,
                                   minSize =(30, 30)) 
# Don't do anything if there's no sign

amount_found = len(found) 
if amount_found != 0: 
    # Possibility for more than one stop sign?
    for (x, y, width, height) in found: 
        # Green 'box' when stop sign is detected. 
        cv2.rectangle(img_rgb, (x, y),  
                      (x + height, y + width),  
                      (0, 255, 0), 5) 
          
# Returns the image incl. the plot area.  
plt.subplot(1, 1, 1) 
plt.imshow(img_rgb) 
plt.show() 
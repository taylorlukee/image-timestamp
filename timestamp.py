# Import OpenCV2 for image processing
import cv2
import datetime
import time
import glob
import os

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Take user input: in this case we enter location

cv = input("Please enter a location:")
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y_%H-%M-%S')
text = f"{cv}-{st}"


# Read in the image file using opencv
im = cv2.imread('./zoo.jpg')

# Get the width and height of the image: im.shape has three items so [0:2] returns the first two
h, w = im.shape[0:2]

# Put text describe who is in the picture
# (10, h - 10) - means the bottom left of the text should start at x = 10, y = height of the image - 10
# ... in image software a lot of the time the y axis increases downward which is unusual from school
# this is why we first get the height 'h' of the image, (which corresponds to the bottom of the picture)
# then we subtract 10 as a bit of padding to make it look neater
cv2.putText(im, text, (10, h - 10), font, 1, (255,255,255), 2)

# Write the altered image tofile
cv2.imwrite(f"zoo{st}.jpeg", im)


files = glob.glob("*.jpg")
files.sort(key=os.path.getmtime)
print("\n".join(files))

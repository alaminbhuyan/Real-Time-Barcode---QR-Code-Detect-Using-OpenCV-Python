import cv2
import numpy as np

# Read Original image
img = cv2.imread(filename="Images/startech.png")
img2 = cv2.imread(filename="Images/linkedin.png")
img3 = cv2.imread(filename="Images/kaggle.png")
img4 = cv2.imread(filename="Images/github.png")

# Resize the  image for comfortable
imgResize = cv2.resize(src=img, dsize=(250, 250))
imgResize2 = cv2.resize(src=img2, dsize=(250, 250))
imgResize3 = cv2.resize(src=img3, dsize=(250, 250))
imgResize4 = cv2.resize(src=img4, dsize=(250, 250))

# Joining with Horizontally
imgHorizontal = np.hstack((imgResize, imgResize2, imgResize3, imgResize4))


cv2.imshow("Join Horizontal Image", imgHorizontal)
cv2.imwrite(filename="Images\\Output Img\\all_img.png", img=imgHorizontal)
cv2.waitKey()
cv2.destroyAllWindows()

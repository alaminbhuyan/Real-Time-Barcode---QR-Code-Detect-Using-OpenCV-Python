import numpy as np
import cv2
from pyzbar.pyzbar import decode

# image = cv2.imread("Images\\all_img.png")
image = cv2.imread("Images\\barcode.jpg")

for barcode_info in decode(image=image):
    img_data = barcode_info.data.decode('utf-8')
    print(img_data)
    points = np.array([barcode_info.polygon], dtype=np.int32).reshape((-1, 1, 2))
    cv2.polylines(img=image, pts=[points], isClosed=True, color=(255, 0, 255), thickness=2)
    points2 = barcode_info.rect
    # print(points2)
    # print(points2[0])
    # print(points2[1])
    cv2.putText(img=image, text=img_data, org=(points2[0]-10, points2[1]-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.4, color=(255, 0, 255), thickness=2)
cv2.imshow("image", image)
# cv2.imwrite(filename="Images\\Output Img\\all_image.png", img=image)
cv2.waitKey()

# It will give you this information as a list
# [Decoded(data=b'https://www.startech.com.bd/', type='QRCODE',
# rect=Rect(left=41, top=41, width=368, height=368),
# polygon=[Point(x=41, y=41), Point(x=41, y=408),
# Point(x=409, y=409), Point(x=408, y=41)], quality=1, orientation='UP')]

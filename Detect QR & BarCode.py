import numpy as np
import cv2
from pyzbar.pyzbar import decode

v_capture = cv2.VideoCapture(0)
# set width
v_capture.set(propId=3, value=680)
# set height
v_capture.set(propId=4, value=480)

# Read the text file
# with open(file='id_information.txt', mode='r') as file:
#     id_list = file.read().splitlines()

while True:
    success, frame = v_capture.read()
    if success:
        for code_info in decode(image=frame):
            # print(code_info.data)
            my_data = code_info.data.decode('utf-8')
            # print(my_data)
            # if my_data in id_list:
            #     my_text = "Authorized"
            #     my_color = (255, 0, 255)
            # else:
            #     my_text = "Not Authorized"
            #     my_color = (0, 0, 255)

            points = np.array([code_info.polygon], dtype=np.int32)
            points = points.reshape((-1, 1, 2))
            cv2.polylines(img=frame, pts=[points], isClosed=True, color=(255, 0, 255), thickness=2)
            points2 = code_info.rect
            cv2.putText(img=frame, text=my_data, org=(points2[0], points2[1]), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.5, color=(255, 0, 255), thickness=2)
        cv2.imshow("Image", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        exit()
v_capture.release()
cv2.destroyAllWindows()

# 실시간 영상 보는법

import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print("카메라가 잡혔어요!")
else:
    print("카메라가 안 잡혔어요!")

while True:   
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(10) == 27:
        break


cap.release()
cv2.destroyAllWindows() 
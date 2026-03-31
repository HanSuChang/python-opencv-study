# practice-hard.py
# 직접 마우스 클릭으로 좌표를 지정하면, 알아서 원근법을 적용하는 방식 
import cv2 
import numpy as np

points1 = np.zeros((4,2), dtype=np.float32)
count = 0

img = cv2.imread("images/book2.jpg")
rows, cols, ch = img.shape
points2 = np.float32([
    [0,0],
    [cols,0],
    [0,rows], 
    [cols, rows]]) 

def mouseHandler(event, x, y, flags, param):
    global points
    global count
    if event==cv2.EVENT_LBUTTONDOWN:
        points1[count] = [x, y]
        count += 1
        cv2.circle(img, (x,y), 5, (0, 0, 255), -1) #반지름 5크기 빨간 점
        cv2.imshow("img", img)
        if count == 4 :
            M = cv2.getPerspectiveTransform(points1, points2)
            dst = cv2.warpPerspective(img, M, (cols,rows))
            cv2.imshow("dst", dst)


cv2.imshow("img", img)
cv2.setMouseCallback("img", mouseHandler)
cv2.waitKey(0)
cv2.destroyAllWindows()
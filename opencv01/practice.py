import cv2
import numpy as np
import sys

oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' %(x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 0), 4, cv2.LINE_AA)
            cv2.imshow('image', img) 
            oldx, oldy = x, y

img = np.ones((512, 512, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)

while True:
    cv2.imshow('image', img) 
    key = cv2.waitKey(1) & 0xFF 
    
    if key == 27 or key == ord('q'): # 27은 ESC 키의 아스키 코드
        break

    # 위에 if는 창을 끄는거고 elif문은 그림판 지우기 버튼
    elif key == ord('c'):
        img[:] = 255
        cv2.imshow('image', img)
        print("그렸던거 초기화")

cv2.destroyAllWindows()
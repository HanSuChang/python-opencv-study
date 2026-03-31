# OpenCV 03 문서 스캐너 실습

import cv2
import numpy as np

src_pts = []

img = cv2.imread('images/book.jpg')


scale = 800 / img.shape[1]
img = cv2.resize(img, None, fx=scale, fy=scale)
img_draw = img.copy()

def on_mouse(event, x, y, flags, param):
    global src_pts, img_draw
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(src_pts) < 4:
            src_pts.append([x, y])
            cv2.circle(img_draw, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('Scanner', img_draw)

            if len(src_pts) == 4:
                # 클릭한 좌표 (좌상, 우상, 좌하, 우하 순서)
                lt, rt, lb, rb = np.float32(src_pts)

             
                # 결과창 크기 조절
                result_width, result_height = 600, 800
                
                pts1 = np.float32([lt, rt, lb, rb])
                pts2 = np.float32([
                    [0, 0], 
                    [result_width, 0], 
                    [0, result_height], 
                    [result_width, result_height]
                ])

                # 원근 변환(스캔) 실행
                M = cv2.getPerspectiveTransform(pts1, pts2)
                dst = cv2.warpPerspective(img, M, (result_width, result_height))
                cv2.imshow('Result', dst)
                

# 창 설정
cv2.namedWindow('Scanner')
cv2.setMouseCallback('Scanner', on_mouse)

cv2.imshow('Scanner', img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()
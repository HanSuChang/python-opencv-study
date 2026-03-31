import cv2
import numpy as np
import math

# 1. 이미지 읽기
image = cv2.imread('images/rail.jpg')
if image is None:
    exit()

height, width = image.shape[:2]

# 2. 전처리
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9, 9), 0)
edges = cv2.Canny(blur, 60, 180)

# 2-4. ROI 설정 
mask = np.zeros_like(edges)
polygon = np.array([[(0, height), (width // 2, height // 2), (width, height)]], np.int32)
cv2.fillPoly(mask, polygon, 255)
roi_edges = cv2.bitwise_and(edges, mask)

# 3. 직선 검출
lines = cv2.HoughLinesP(roi_edges, rho=1, theta=np.pi/180, threshold=30, minLineLength=60, maxLineGap=150)

# 4. 선 필터링 
left_lines = []
right_lines = []

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if x2 - x1 == 0: continue
        slope = (y2 - y1) / (x2 - x1)
        if 0.5 < abs(slope) < 10.0:
            if slope < 0:
                left_lines.append(line[0])
            else:
                right_lines.append(line[0])

result_img = image.copy()

# 5. 중앙 좌표 계산 및 시각화
if left_lines and right_lines:
    # 왼쪽과 오른쪽 선들의 평균 좌표 구하기
    left_avg = np.mean(left_lines, axis=0).astype(int)
    right_avg = np.mean(right_lines, axis=0).astype(int)

    # 중앙 좌표 계산 (산술 평균)
    # 하단 중앙 (정면)
    bottom_center_x = (left_avg[0] + right_avg[2]) // 2
    bottom_center_y = (left_avg[1] + right_avg[3]) // 2
    
    # 상단 중앙 
    top_center_x = (left_avg[2] + right_avg[0]) // 2
    top_center_y = (left_avg[3] + right_avg[1]) // 2

    # [시각화 1] 중앙선 
    cv2.line(result_img, (top_center_x, top_center_y), (bottom_center_x, bottom_center_y), (0, 255, 255), 3)
    
    # [시각화 2] 중앙 좌표점 
    cv2.circle(result_img, (bottom_center_x, bottom_center_y), 10, (0, 255, 0), -1)

    # 좌표 출력
    print(f"중앙 좌표 (X, Y): ({bottom_center_x}, {bottom_center_y})")

# 기존 레일 선 그리기
for line in left_lines:
    x1, y1, x2, y2 = line
    cv2.line(result_img, (x1, y1), (x2, y2), (0, 0, 255), 2)
for line in right_lines:
    x1, y1, x2, y2 = line
    cv2.line(result_img, (x1, y1), (x2, y2), (0, 0, 255), 2)




cv2.imshow('Original', image)
cv2.imshow('ROI Masked Edges', roi_edges) 
cv2.imshow('Rail Center Detection', result_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
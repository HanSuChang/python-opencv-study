# 기본 도형 그리기
import cv2
import numpy as np

# 흰색 배경 생성 (512x512) 이거 넘파이임 512, 512, 3 <- 사이즈, 255로 채운다(흰색)
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)

# 그리기, 맨 뒷 숫자
cv2.line(canvas, (50, 50), (650, 50), (255, 0, 0), 90)          # 파란 선  255), 뒤에 있는 숫자는 선의 굵기
cv2.rectangle(canvas, (50, 200), (900, 400), (0, 255, 0), -1) # 초록 꽉 찬 사각형
cv2.circle(canvas, (350, 300), 100, (0, 0, 265), 16)           # 빨간 원 ex- (0, 0, 255), 9) 255), 뒤에 있는 숫자는 원의 굵기


cv2.imshow('Canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
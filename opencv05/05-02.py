## 히스토그램 분석 및 평활화.

### 히스토그램 (Histogram)

#영상 내 픽셀 값들의 분포를 그래프로 표현한 것입니다. `cv2.calcHist()` 함수를 사용합니다.

### 평활화 (Equalization)

#히스토그램이 특정 영역에 뭉쳐 있는(너무 어둡거나 밝은) 영상의 분포를 골고루 펴주어 **명암비(Contrast)를 높이는 기법**입니다.


import cv2

src = cv2.imread("images/lena.jpg", cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(src) # 그레이스케일 영상 전용



cv2.imshow('Source', src)
cv2.imshow('Equalized', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
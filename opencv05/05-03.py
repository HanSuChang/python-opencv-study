## 모폴로지 연산 (Morphology)

#영상의 형태학적 변환을 통해 노이즈를 제거하거나 구멍을 메웁니다. 주로 이진화된 이미지(Binary Image)에 사용합니다.


### 침식 (Erosion)과 팽창 (Dilation)

#- 침식 (`erode`): 객체를 깎아냄. (작은 노이즈 제거, 객체 분리)
#- 팽창 (`dilate`): 객체를 살찌움. (구멍 메우기, 객체 연결)

### 열림 (Opening)과 닫힘 (Closing)

#- 열림 (Opening): 침식 -> 팽창. (밝은 노이즈 제거, 돌기 제거)
#- 닫힘 (Closing): 팽창 -> 침식. (객체 내부의 검은 구멍 메우기)

#python
#kernel = np.ones((3, 3), np.uint8)
## 열림 연산으로 자잘한 노이즈 제거
#result = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)



import cv2
import numpy as np


img = cv2.imread("images/morphology.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3, 3), np.uint8)


result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


# 침식
erosion = cv2.erode(img, kernel, iterations=1)

# 침식
dilation = cv2.dilate(img, kernel, iterations=1)


cv2.imshow("Original", img)
cv2.imshow("Erosion", erosion)   
cv2.imshow("Dilation", dilation) 
cv2.imshow("Result", result)  

cv2.waitKey(0)
cv2.destroyAllWindows()
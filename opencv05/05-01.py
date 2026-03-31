## 컬러 공간 (Color Spaces)과 색상 추출...

# 우리가 흔히 쓰는 RGB 방식은 빛의 삼원색을 섞는 방식이지만, 영상 처리에서는 조명의 영향을 덜 받거나 특정 색상을 찾기 쉬운 다른 모델들이 더 유용할 때가 많습니다.

### HSV (Hue, Saturation, Value)

#- Hue (색상): 색의 종류 (0~179 in OpenCV). 빨강(0), 초록(60), 파랑(120).
#- Saturation (채도): 색의 진한 정도. (흰색 섞임 정도)
#- Value (명도): 밝기.
#- 장점: 조명(밝기)이 변해도 색상(H) 정보는 유지되므로 색상 기반 검출에 유리합니다.

### YCrCb

#- Y (Luma): 밝기(Luminance) 정보.
#- Cr, Cb (Chroma): 색차 정보.
#- 장점: 피부색 검출에 탁월하며, 방송 시스템 표준입니다.

### 특정 색상 추출 (`cv2.inRange`)

#- `cv2.inRange(src, lowerb, upperb)`: 범위 내의 픽셀은 255(흰색), 나머지는 0(검은색)인 마스크를 반환합니다.




import cv2
import numpy as np

src = cv2.imread('images/lena.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 빨간색 추출 예시 (H: 0~10 or 170~180)
# 빨간색은 Hue 값이 0 근처와 180 근처 양쪽에 걸쳐 있습니다.
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow('Red Mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
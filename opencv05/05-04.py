## 윤곽선 (Contours) 검출

#동일한 색상이나 밝기를 가진 영역의 경계선(컨투어)을 찾아 리스트로 반환합니다.

#- `cv2.findContours(image, mode, method)`
#   - 입력: 주로 이진화된 이미지(검은 바탕에 흰 객체)를 사용해야 합니다.
#   - 반환: `contours` (윤곽선 좌표들의 리스트), `hierarchy` (계층 구조)
#   - Mode: `cv2.RETR_EXTERNAL` (가장 바깥쪽만), `cv2.RETR_TREE` (모든 계층)
#- `cv2.drawContours(image, contours, contourIdx, color, thickness)`**

import cv2

src = cv2.imread("images/shape.png") # 또는 ("images/lena.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, thresh =  cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierachy = \
cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

result = cv2.drawContours(src, contours, -1, (0, 0, 255), 1)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
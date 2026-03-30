# ## 비트 연산

#각 픽셀의 비트 단위 논리 연산을 수행합니다. 마스크(Mask)를 이용하여 특정 영역을 추출할 때 핵심적으로 사용됩니다.

#### 주요 비트 연산 함수

#- `cv2.bitwise_and(src1, src2, mask)`: 둘 다 1일 때만 1 (교집합, 마스킹)
#- `cv2.bitwise_or(src1, src2, mask)`: 하나라도 1이면 1 (합집합)
#- `cv2.bitwise_not(src)`: 반전 (0->1, 1->0)
#- `cv2.bitwise_xor(src1, src2, mask)`: 서로 다를 때 1

# 마스크(Mask) 연산의 원리

#- 흰색(255, 1): 통과 (Pass)
#- 검은색(0, 0): 차단 (Block)
#- `bitwise_and` 연산을 이미지와 마스크에 적용하면, 마스크의 흰색 부분에 해당하는 이미지 픽셀만 남습니다.


import cv2

src1 = cv2.imread("images/lena.jpg", cv2.IMREAD_GRAYSCALE)

# 임계점
rst, src2 = cv2.threshold(src1, 160, 255, cv2.THRESH_BINARY)
dst1 = cv2.bitwise_or(src1, src2)
dst2 = cv2.bitwise_not(src1)

dst = cv2.bitwise_and(src1, src2)



cv2.imshow("src1", src1)
cv2.imshow("src2", src2)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


## ROI (Region of Interest)와 채널 분리

### ROI 설정 (관심 영역)

#이미지 전체가 아닌 특정 부분만 처리하고 싶을 때 사용합니다. NumPy의 슬라이싱(Slicing) 기능을 사용합니다.

#python
#src = cv2.imread('lena.jpg')

# [y_start:y_end, x_start:x_end]
#face = src[200:400, 200:400] 

#cv2.imshow('Face ROI', face)
#캐니 에지 검출(Canny Edge Detection)   중요

## 캐니 에지 검출 (Canny Edge Detection)

#가장 널리 쓰이는 강력한 에지 검출 알고리즘입니다. 여러 단계(노이즈 제거 -> 그라디언트 -> 비최대 억제 -> 이중 임계값)를 거쳐 얇고 선명한 에지를 찾아냅니다.

# 1. 노이즈 제거 : 가우시안 필터를 이용해 노이즈 제거하기
# 2. 그라이언트 : 수평 및 수직 방향 모두에서 소벨 필터 커널로 필터링하기 
# 3. 비최대 억제 : 임계값 적용하기 
# 4. 이중 임계값 : 모든 엣지 중에서 임계값 벗어나는 것들 제외 

#- `cv2.Canny(image, threshold1, threshold2)`
#    - `threshold1`: 하단 임계값 (이 값 이하는 에지에서 제외)
#    - `threshold2`: 상단 임계값 (이 값 이상은 무조건 에지로 간주)
#    - 두 값 사이의 픽셀은 상단 임계값과 연결되어 있을 때만 에지로 인정합니다.



import cv2

img = cv2.imread("images/lena.jpg", cv2.IMREAD_GRAYSCALE)


dst1 = cv2.Canny(img, 50, 100)
dst2 = cv2.Canny(img, 50, 200)

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
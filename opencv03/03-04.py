# 크기 변환
### 크기 변환 (Resize)

#함수: `cv2.resize(src, dsize, fx, fy, interpolation)`
#보간법(Interpolation):
#   - `cv2.INTER_LINEAR`: 기본값, 속도 빠름. 주변 픽셀을 가중 평균내기.
#    - `cv2.INTER_CUBIC`: 화질 좋음, 속도 느림. (확대 시 추천). 주변 픽셀을 3차 함수로 계산해서 보간하기
#    - `cv2.INTER_AREA`: 영역 보간, 축소 시 물결 무늬(Moire) 방지에 좋음. 가까운 픽셀과 최대한 비슷하게 (가까운 픽셀을 복사하기)
import cv2


img = cv2.imread('images/lena.jpg')
dst1 = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_LINEAR)
dst2 = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_CUBIC)
dst3 = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_AREA)

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
## 허프 변환 (Hough Transform).

# 에지 픽셀들을 분석하여 직선이나 원 같은 수학적 도형을 찾아내는 기법입니다.

## 직선 검출 (Hough Line Transform)

# 도로의 차선 등을 찾을 때 사용합니다.

# `cv2.HoughLinesP(image, rho, theta, threshold, minLineLength, maxLineGap)`
#   - 확률적 허프 변환(Probabilistic)을 사용하여 속도가 빠르고 시작점/끝점을 바로 반환해줍니다.
#   - `rho`: 거리 해상도 (보통 1) - 얼마나 촘촘하게 선을 찾을지
#   - `theta`: 각도 해상도 (보통 `np.pi/180` = 1도) 각도를 얼마나 세말하게 볼지 
#   - `threshold`: 직선으로 판단할 최소 투표 수 - 얼마나 디테일한 선까지 판단할 것인지
#   - `minLineLength`: 선으로 인정할 최소 길이 - 얼마나 길어야 검출해줄 것인지
#   - `maxLineGap`: 선이 끊겨 있어도 하나의 선으로 간주할 최대 간격 - 이 값이 크면 끊어져 있어도 선으로 검출


# 허프 변환으로 직선 검출하는 예제 
import cv2
import numpy as np 

img = cv2.imread("images/lena.jpg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 50, 100)

# Canny 에지 이미지에서 직선 검출
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 
                        minLineLength=100, maxLineGap=10)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) # 컬러로 변환해 그리기
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
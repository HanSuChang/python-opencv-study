import cv2
import numpy as np


src = cv2.imread("images/coins.jpg")
if src is None: exit()

#전처리 - 블러
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)

#이진화 (배경은 검게, 동전은 하얗게)
# 배경이 밝으므로 THRESH_BINARY_INV를 사용
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#모폴로지 연산 
# 커널을 (3,3)으로 줄여서 동전 사이의 틈을 보존
kernel = np.ones((3, 3), np.uint8)

####################################################################################### 핵심
#  먼저 열림으로 혹시 붙어 있을지 모르는 미세한 선들을 끊어줌
morphed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=0)

#  그 다음 닫힘을 아주 살짝만 해서 안쪽 구멍만 최소한으로 메움
# iterations를 1~2 정도로 낮추기
morphed = cv2.morphologyEx(morphed, cv2.MORPH_CLOSE, kernel, iterations=2)
####################################################################################### 핵심


# 5. 윤곽선 검출
contours, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


result = src.copy()

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        cv2.drawContours(result, [cnt], -1, (0, 255, 0), 2)



coin_count = len(contours)
text = f"Found {coin_count} coins"
org = (20, 50)
cv2.putText(result, text, org, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3, cv2.LINE_AA)

#흑백
cv2.imshow("Binarization (Threshold)", thresh) 

cv2.imshow("Result (Individual Coins)", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
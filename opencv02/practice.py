# OpenCV 02 크로마키 만들기 실습

import cv2
import numpy as np
import sys


img_person = cv2.imread('images/22.jpg')
img_lena = cv2.imread('images/lena.jpg')


if img_person is None or img_lena is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

# 크기 사진 맞추는데 레나 사진 크기에 인물 사진 맞춤
height, width = img_lena.shape[:2]
img_person = cv2.resize(img_person, (width, height))

# 색상 공간 변환 (BGR -> HSV)
hsv = cv2.cvtColor(img_person, cv2.COLOR_BGR2HSV)

# 마스크 반전
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

# 5. 마스크 반전 
mask_inv = cv2.bitwise_not(mask)

# 22사진에 사람만 떼어내고 배경은 검정으로
person_extracted = cv2.bitwise_and(img_person, img_person, mask=mask_inv)

# 레나 사진에서 사람이 들어갈 자리를 검게 파냄
img_lena_masked = cv2.bitwise_and(img_lena, img_lena, mask=mask)

# 최종
final_result = cv2.addWeighted(person_extracted, 1.0, img_lena_masked, 1.0, 0)


cv2.imshow('1_Extracted Person', person_extracted)
cv2.imshow('2_Lena with Hole', img_lena_masked)
cv2.imshow('3_Final Result', final_result)

cv2.waitKey()
cv2.destroyAllWindows()
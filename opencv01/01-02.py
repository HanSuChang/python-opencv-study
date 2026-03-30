import cv2
import sys

# 이미지 불러오기 (넘파이 배열)
img = cv2.imread("images/lena.jpg")

if img is None :
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

cv2.imshow('Lena Window', img) # 윈도우 창 제목, 이미지 객체
 
#키 입력 기다리기... 키 입력 없으면 현 상태로 유지됨
cv2.waitKey(0)
cv2.destroyAllWindows() # 모든 오픈 씨비 창 끄기
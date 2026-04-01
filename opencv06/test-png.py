# OPEN CV 사진에서 드래그로 좌표값 쉽게 얻기

import cv2

# 1. 이미지 읽기 
img = cv2.imread('images/tigermask.png') 

if img is None:
    print("파일을 찾을 수 없습니다!")
    exit()

# 2. 마우스로 드래그해서 ROI 선택
# Enter: 확정 / c: 취소 후 다시 선택
print("--- 드래그 후 Enter를 누르세요 ---")
x, y, w, h = cv2.selectROI('Select ROI', img, fromCenter=False)

# 3. 좌표 출력 (이 숫자를 메모하세요)
print(f"\n[찾은 좌표값]")
print(f"x: {x}, y: {y}, 너비(w): {w}, 높이(h): {h}")

cv2.destroyAllWindows()


# [1] ################################################################
#     위의 코드로 좌표를 얻었으면 밑에 코드로 적용하기
################################################################




# EX (예로 들면!!!!!!!!!!!!!!)
# 위에서 얻은 숫자가 만약 x=100, y=200, w=50, h=30 이라면?

# 방법 A: 고정 숫자로 자르기 (가장 쉬운 방법)
# 공식: 이미지[y : y+h, x : x+w]

# 주석 풀기 (A) 
# roi = img[y : y+h, x : x+w]



# 방법 B: 비율로 변환해서 자르기 (터틀봇 추천 방법)
# 카메라 해상도가 바뀌어도 똑같은 위치를 잡을 수 있습니다.

# 주석 풀기 (B) - 밑에 3개 주석 풀기
#height, width = img.shape[:2]

#y_ratio = y / height    # 시작 높이 비율 (예: 0.7)
#h_ratio = h / height    # 잘라낼 높이 비율 (예: 0.2)


# 실제 적용 시 (C) - 밑에 코드 2개 주석 풀기
# 실제 적용 시

#start_y = int(height * y_ratio)
#end_y = int(height * (y_ratio + h_ratio))

# 가로(x)도 같은 방식으로 계산 가능합니다.


# 이것도 주석 풀기
# final_roi = img[start_y:end_y, :] # 가로는 전체를 다 본다면 이렇게!
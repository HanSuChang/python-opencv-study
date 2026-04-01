import cv2
import numpy as np

sticker = cv2.imread('images/tigermask.png', cv2.IMREAD_UNCHANGED)

if sticker is None:
    print("에러남 다시 확인해보자")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)


    # 얼굴 기준 스티커 꽉 채우게하기 (사이즈 조절) 
    for (x, y, w, h) in faces:
        adj_y, adj_h = int(y - 0.2 * h), int(h * 1.6)
        adj_x, adj_w = int(x - 0.25 * w), int(w * 1.5)

        # w (Width): 사각형의 가로 너비, h (Height): 사각형의 세로 높이
        # (x, y): 사각형의 왼쪽 상단 꼭짓점 좌표
        # x: 가로축 (왼쪽에서 오른쪽으로 갈수록 증가)
        # y: 세로축 (위에서 아래로 갈수록 증가 - 이게 수학이랑 반대)
        # y값을 빼주면(-) 화면 위로 올라가고, 더해주면(+) 아래로 내려감



        # 화면 경계 예외 처리 (이게 없으면 화면 끝에서 튕김)
        adj_y = max(0, adj_y)
        adj_x = max(0, adj_x)
        end_y = min(frame.shape[0], adj_y + adj_h)
        end_x = min(frame.shape[1], adj_x + adj_w)

        real_h = end_y - adj_y
        real_w = end_x - adj_x

        if real_h <= 0 or real_w <= 0: continue

        # 스티커 리사이즈 (real_w, real_h 수치를 사용하세요)
        face_sticker = cv2.resize(sticker, (real_w, real_h))
        roi = frame[adj_y:end_y, adj_x:end_x]

        # --- PNG 투명도(Alpha 채널) 합성 로직 ---
        # 채널 분리: Blue, Green, Red, Alpha
        b, g, r, a = cv2.split(face_sticker)
        
        # 알파 채널을 마스크로 사용
        mask = a
        mask_inv = cv2.bitwise_not(mask)

        # 호랑이 얼굴 부분만 따오기 (RGB 색상 결합)
        tiger_fg = cv2.merge((b, g, r))
        tiger_fg = cv2.bitwise_and(tiger_fg, tiger_fg, mask=mask)

        # 원본 배경(내 얼굴)에서 호랑이가 들어갈 자리 비우기
        bg_roied = cv2.bitwise_and(roi, roi, mask=mask_inv)

        # 두 영역 합체 후 원본에 삽입
        dst = cv2.add(bg_roied, tiger_fg)
        frame[adj_y:end_y, adj_x:end_x] = dst

    cv2.imshow('타이거 필터', frame)
    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()
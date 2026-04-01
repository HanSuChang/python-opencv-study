#여러명 검출 연습....

# 얼굴(이미지) 검출 실습


import cv2
img = cv2.imread("images/run.jpg") 

# 이미지 크기 조절기능
img = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 분류기 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 검출 (입력 이미지는 그레이스케일 권장)
# scaleFactor: 이미지 피라미드 스케일 (보통 1.1)
# minNeighbors: 검출된 영역이 얼마나 중복되어야 얼굴로 인정할지 (보통 3~5)
#파라미터
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
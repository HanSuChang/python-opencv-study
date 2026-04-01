# Haar cascade 연습

# lena로 검출



## Haar Cascade 얼굴 검출

#머신러닝 기반의 객체 검출 기술로, 속도가 매우 빨라 실시간 얼굴 인식에 많이 쓰였습니다. OpenCV는 미리 학습된 XML 파일들을 제공합니다.

### 작동 원리

# Haar Feature: 영상의 밝기 차이를 이용한 사각형 형태의 특징 필터.
# Cascade: 수많은 특징 중 얼굴일 확률이 높은 것부터 단계적으로 검사하여 속도를 높임.

### 얼굴 검출 코드

#`haarcascade_frontalface_default.xml` 파일이 필요합니다. (오픈 소스)



import cv2
img = cv2.imread("images/lena.jpg") 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 분류기 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 검출 (입력 이미지는 그레이스케일 권장)
# scaleFactor: 이미지 피라미드 스케일 (보통 1.1)
# minNeighbors: 검출된 영역이 얼마나 중복되어야 얼굴로 인정할지 (보통 3~5)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
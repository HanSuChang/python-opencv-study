## 템플릿 매칭 (Template Matching)

#원본 이미지에서 특정 부분 이미지(템플릿)와 일치하는 영역을 찾는 가장 단순한 방법입니다.

#- `cv2.matchTemplate(image, templ, method)`
#    - 템플릿 이미지를 원본 이미지 위에서 슬라이딩하며 유사도를 계산합니다.
#    - 결과는 2차원 실수 행렬로 나오며, `cv2.minMaxLoc()`으로 최댓값(또는 최솟값) 위치를 찾아야 합니다.
#- 주의: 크기나 회전이 변하면 잘 찾지 못합니다.

import cv2
img = cv2.imread('images/lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 찾고 싶은 부분 (눈) 잘라내기 (템플릿 준비)
template = gray[180:290, 200:360] 

# 매칭 수행 (픽셀 간의 상관관계로 유사도를 체크하는 메소드 사용)
# 반환값은 유사도 맵 (상관관계를 포함한 행렬 )
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# max_loc이 매칭된 위치의 좌상단 좌표
top_left = max_loc
print(top_left)

cv2.circle(gray, top_left, 5, (0,0,0), -1)

# 이후 자유롭게 후처리 가능!
cv2.imshow("gray", gray)
cv2.imshow("template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()
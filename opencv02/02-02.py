#가중치 합: 영상 합성

#두 영상의 투명도를 조절하여 겹치는 효과(Alpha Blending)를 냅니다.

#- 수식: `dst = src1 * alpha + src2 * beta + gamma`
#- 함수: `cv2.addWeighted(src1, alpha, src2, beta, gamma)`


import cv2

src1 = cv2.imread("images/lena.jpg")
src2 = cv2.imread("images/lena.jpg")

dst = cv2.addWeighted(src1, 0.3, src2, 0.6, 0)    # 수식: dst = src1 * alpha + src2 * beta + gamma  ->  함수: cv2.addWeighted(src1, alpha, src2, beta, gamma)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
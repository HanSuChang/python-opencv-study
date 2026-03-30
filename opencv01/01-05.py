import cv2
import sys

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:     # R= 오른쪽 클릭, L= 왼쪽 클릭
        if flags & cv2.EVENT_FLAG_CTRLKEY:
            print("오른쪽 버튼 클릭 (with Ctrl):", x, y) # <-- 이 부분 들여쓰기만 수정했습니다.
            
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("오른쪽 버튼 더블클릭:", x, y)
    # 중복되었던 마지막 elif 문 한 줄만 제거했습니다.

img = cv2.imread("images/lena.jpg")

if img is None:
    print("이미지를 찾을 수 없습니다. 파일명과 확장자를 확인하세요.")
    sys.exit()

window_name = 'Lena Window'

cv2.imshow(window_name, img) 
cv2.setMouseCallback(window_name, mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np


# 이미지 코드
image = cv2.imread('../image/like_lenna.png')
new_height = 500
new_width = 500
image = cv2.resize(image, (new_height, new_width))



# 이미지 위에 그림 코드
cv2.circle(image, (300, 190), 40, (0, 0, 0), 3, cv2.LINE_AA)
cv2.ellipse(image, (390, 190), (30, 24), 90, 0, 360, (0, 0, 0), 4) 
# ellipse안의 parameter의 각 명칭 (대상이미지, 타원의 중심좌표, x,y축 반지름, 각도, startAngle, endAngle, RGB값, 선두께)



# 윈도우 창 담당 코드
cv2.imshow('image with circle', image) # imshow는 (파일의 이름, 이미지) 두개의 인자를 요구함
# 창을 열고 유지하는 코드
cv2.waitKey(0)
# 창을 끄는 기능을 하는 코드
cv2.destroyAllWindow()
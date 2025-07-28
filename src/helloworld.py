import cv2

image = cv2.imread('../image/like_lenna.png')
# resize 작업 시 원본을 불러놓고 작업할 것
image_small = cv2.resize(image,(100,100))

# imshow는 이미지를 보여주는 명령어
# cv2.imshow('image Window', image)
cv2.imshow('image Window', image_small)
print(image_small.shape)


# waitKey는 열린 창을 유지시키는 것
cv2.waitKey(0)

cv2.destroyAllWindows()

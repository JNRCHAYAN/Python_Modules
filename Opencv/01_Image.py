import cv2

img = cv2.imread('assets\pic.jpg',1)

# Image Mode 
#-1,cv2.IMREAD_COLOR
# 0, cv2.IMREAD_GRAYSCALE
# 1, cv2.IMREAD_UNCHANGED

img = cv2.resize(img,(500,500))

img = cv2.rotate(img, cv2.ROTATE_180)

cv2.imwrite('new_img.jpg',img)

cv2.imshow('pic',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

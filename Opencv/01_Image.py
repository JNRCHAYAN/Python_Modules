import cv2

img = cv2.imread('assets\pic.jpg',1)

# Image Mode 
#-1,cv2.IMREAD_COLOR
# 0, cv2.IMREAD_GRAYSCALE
# 1, cv2.IMREAD_UNCHANGED

cv2.imshow('pic',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

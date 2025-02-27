import cv2

img = cv2.imread('./candies.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#bgr = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
'''
HSV에서의 녹색계열
50 <= H <= 80
150 <= S <= 255
0 <= V <= 255
'''
'''
BGR에서 녹색계열
0 <= B <= 100
128 <= G <= 255
0 <= R <= 100
'''
dst = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))
#dst = cv2.inRange(bgr, (0, 128, 0), (100, 255, 100))
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
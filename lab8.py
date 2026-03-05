import cv2
import numpy as np

#task1
img = cv2.imread('variant-10.jpg')
gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret1, thresh1 = cv2.threshold(gray1, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh1', thresh1)


#task2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    cX, cY = w//2, h//2

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) > 500:
            m = cv2.moments(c)
        #m["m00"]
        #m["m10"] =x
        #m["m01"] =y
            if m["m00"] != 0:
                mx= int(m["m10"]/m["m00"])
                my= int(m["m01"]/m["m00"])

                if (cX - 75 <= mx <= cX + 75 and cY - 75 <= my <= cY + 75):
                    thresh = cv2.flip(thresh, 1)

            cv2.circle(frame, (mx, my), 5, (0, 0, 255), 3)
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.rectangle(frame, (cX - 75, cY - 75), (cX + 75, cY + 75), (255, 0, 0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('thresh', thresh)

cap.release()

cv2.destroyAllWindows()

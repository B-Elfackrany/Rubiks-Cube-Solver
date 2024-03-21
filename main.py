import cv2
import numpy as np

l_w = np.array([232, 0, 153])
u_w = np.array([255, 255, 255])

def program():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        # draw 3*3 matrix on the frame
        cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 0), 3)
        cv2.line(img, (100, 166), (300, 166), (0, 0, 0), 3)
        cv2.line(img, (100, 233), (300, 233), (0, 0, 0), 3)
        cv2.line(img, (166, 100), (166, 300), (0, 0, 0), 3)
        cv2.line(img, (233, 100), (233, 300), (0, 0, 0), 3)

        # crop the 3*3 matrix and display it
        crop_img = img[100:300, 100:300]
        cv2.imshow('crop', crop_img)

        mask = cv2.inRange(crop_img, l_w, u_w)
        res = cv2.bitwise_and(crop_img, crop_img, mask=mask)
        whitecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

        for cnt in whitecnts:
            blue_area = max(cnt, key=cv2.contourArea)
            (xg, yg, wg, hg) = cv2.boundingRect(blue_area)
            cv2.rectangle(img, (xg, yg), (xg + wg, yg + hg), (0, 255, 0), 2)
            cv2.putText(img, 'White', (xg, yg), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        for i in range(0, 3):
            for j in range(0, 3):
                # crop the 3*3 matrix
                crop_img = img[100 + i * 66:166 + i * 66, 100 + j * 66:166 + j * 66]
                # display the cropped matrix
                cv2.imshow('crop' + str(i) + str(j), crop_img)

        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    program()

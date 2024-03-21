import cv2

def program():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
 #my name is bigo 7amo
        #my name is blobo2
        # draw 3*3 matrix on the frame
        cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 0), 3)
        cv2.line(img, (100, 166), (300, 166), (0, 0, 0), 3)
        cv2.line(img, (100, 233), (300, 233), (0, 0, 0), 3)
        cv2.line(img, (166, 100), (166, 300), (0, 0, 0), 3)
        cv2.line(img, (233, 100), (233, 300), (0, 0, 0), 3)
        # crop the 3*3 matrix and display it
        crop_img = img[100:300, 100:300]
        cv2.imshow('crop', crop_img)

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

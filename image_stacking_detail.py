# import the opencv library
import cv2
import numpy as np


def get_color(r, g, b):
    # print('red:   ' + str(r))
    # print('green: ' + str(g))
    # print('blue:  ' + str(b))

    scale = max(r, g, b)

    r_n = float(r / scale)
    g_n = float(g / scale)
    b_n = float(b / scale)


    if abs(r_n-b_n) < .1 and g_n != 1:
        print('white')
    elif b_n == 1:
        print('blue')
    else:
        if g_n == 1:
            if abs(r_n-b_n) > abs(r_n-g_n):
                print('green')
            else:
                print('yellow')
        else:
            score_r = abs(r_n-g_n)
            score_b = abs(b_n-g_n)

            if .5 < score_r / score_b and score_r / score_b > 1.5:
                print('orange')
            elif score_r > score_b:
                print('red')
            else:
                print('yellow')


    print('--------')
    # for color in color_combos:
    # print(np.linalg.norm(given_color_norm - color))


# def color(r, g, b):

# define a video capture object
vid = cv2.VideoCapture(0)

ret, frame = vid.read()

f_height = frame.shape[0]
f_width = frame.shape[1]

cent_w = int(f_width/2)
cent_h = int(f_height/2)

f_min = min(f_height, f_width)

size = int(f_min/36)

shift = int(f_min/6)  

color_b = 0
color_g = 0
color_r = 0

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    for i in range(-1,2):
        for j in range(-1,2):
            frame = cv2.rectangle(frame, (cent_w - size + shift * i, cent_h - size + shift * j),
                                         (cent_w + size + shift * i, cent_h + size + shift * j),
                                         (255,255,255), 3)
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    let = cv2.waitKey(1)

    if let == ord('s'):
        print('screenshot')
        for i in range(-1,2):
            for j in range(-1,2):

                color_b = np.mean(frame[(cent_h - size + shift * j):(cent_h + size + shift * j),
                                    (cent_w - size + shift * i):(cent_w + size + shift * i), 0])

                color_g = np.mean(frame[(cent_h - size + shift * j):(cent_h + size + shift * j),
                                    (cent_w - size + shift * i):(cent_w + size + shift * i), 1])

                color_r = np.mean(frame[(cent_h - size + shift * j):(cent_h + size + shift * j),
                                    (cent_w - size + shift * i):(cent_w + size + shift * i), 2])

                get_color(color_r, color_g, color_b)

    if let == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
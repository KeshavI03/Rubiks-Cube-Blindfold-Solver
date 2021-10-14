# import the opencv library
import cv2
import numpy as np
import blindfold_solver2


def get_color(colors):

    blue = colors[0, 1, 1]

    red = colors[1, 1, 1]

    yellow = colors[2, 1, 1]

    orange = colors[3, 1, 1]

    white = colors[4, 1, 1]

    green = colors[5, 1, 1]

    f_c = []

    color_options = 'bryowg'

    col_string = ''

    for l in range(0, 6):
        for j in range(0,3):
            col_string = ''
            for i in range(0,3):

                guessed_color = 0
                color_dist = 10000

                for k in range(0, 6):
                    dist = pow(colors[k, 1, 1, 0]-colors[l, i, j, 0] , 2) + pow(colors[k, 1, 1, 1]-colors[l, i, j, 1] , 2) + pow(colors[k, 1, 1, 2]-colors[l, i, j, 2] , 2)

                    if dist < color_dist:
                        color_dist = dist
                        guessed_color = k

                col_string += color_options[guessed_color]

                # print(colors[0, i, j])
            f_c.append(col_string)

    # print(f_c)

    blindfold_solver2.solve(f_c[0:3], f_c[3:6], f_c[6:9], f_c[9:12], f_c[12:15], f_c[15:18])


# def color(r, g, b):

# define a video capture object
vid = cv2.VideoCapture(0)

ret, frame = vid.read()

f_height = frame.shape[0]
f_width = frame.shape[1]

cent_w = int(f_width/2)
cent_h = int(f_height/2)

f_min = min(f_height, f_width)

size = int(f_min/30)

shift = int(f_min/6)  

color_b = 0
color_g = 0
color_r = 0

face_num = 0

colors = np.zeros((6, 3, 3, 3) ,dtype=int)

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

                # colors.append(None)
                # colors[i, j, face_num] = [color_r, color_g, color_b]
                colors[face_num, i+1, j+1] = [color_r, color_g, color_b]
                # get_color(colors)

        face_num += 1

    if let == ord('q'):
        get_color(colors)
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
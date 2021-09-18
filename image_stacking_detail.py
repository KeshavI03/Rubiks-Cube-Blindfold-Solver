# import the opencv library
import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)

ret, frame = vid.read()

f_width = frame.shape[0]
f_height = frame.shape[1]

cent_w = int(f_width/2)
cent_h = int(f_height/2)

f_min = min(f_height, f_width)

size = int(f_min/36)

shift = int(f_min/6)
  
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

    if let == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
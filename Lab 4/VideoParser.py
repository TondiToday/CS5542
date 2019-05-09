
import cv2
import math

vidcap = cv2.VideoCapture('videoplayback.mp4')
framerate = math.ceil(vidcap.get(cv2.CAP_PROP_FPS))

success, image = vidcap.read()
framecount = 0
count = 0
while success:
  success, image = vidcap.read()
  framecount += 1 
  count += 1
  if count == (framerate * 10):
    count = 0
    cv2.imwrite("frame%d.jpg" % framecount, image)     # save frame as JPEG file
    print('Read a new frame: ', success)

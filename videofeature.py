import csv
import numpy
import collections
import operator
import cv2
from os import listdir
from os.path import isfile, join


###########################
def GetVideoProperties(video_directory):
  list_of_mp4_files = GetListOfFiles(video_directory, ".mp4")
  video_info_map = {}
  for filepath in list_of_mp4_files:
    video_info = GetVideoPropertiesSingleFile(filepath)
    video_id = GetVideoIDFromFilepath(filepath)
    video_info_map[video_id] = video_info
  return video_info_map

###########################
def PlayVideo(video_file_path, start_time, end_time):
  """Play a short video clip from the given video file."""
  print "INSIDE PLAY VIDEO"
  video = cv2.VideoCapture(video_file_path)
  print video
  nFrames = (int)(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
  print nFrames
  framerate = video.get(cv2.cv.CV_CAP_PROP_FPS)
  
  start_frame = int(start_time * float(framerate))
  end_frame = int(end_time * float(framerate))

  if end_frame > nFrames:
    end_frame = nFrames - 1
  print start_frame, end_frame

  frame_list = []
  print framerate
  for i in range(start_frame, end_frame):
    video.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, i)
    ret, frame = video.read()
    print i, ret
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow(video_file_path, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  video.release()
  cv2.destroyAllWindows()

  ###########################
def main():
  PlayVideo("C:/Users/Moon/Desktop/WETLAB Research/videos/CELL06-rgb.anvil.mov", 1, 200)

if __name__ == "__main__":
  main()

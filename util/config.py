import cv2 as cv

#User settings
save_filename = "footage.avi"
frames_per_second = 30
resolution = "720p"

#Some globals
#Default resolutions
DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

#Video encoding might require additional installs
VIDEO_TYPE = {
    'avi': cv.VideoWriter_fourcc(*'XVID'),
}
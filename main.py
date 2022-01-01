import cv2 as cv
import numpy as np
import datetime, sys, os

sys.path.append("./util/")

import util.config as config

def change_resolution(cap, width, height):
    cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)

def get_dimensions(cap, resolution="1080p"):
    width, height = config.DIMENSIONS[resolution]
    return width, height

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in config.VIDEO_TYPE:
      return config.VIDEO_TYPE[ext]
    else:
        return config.VIDEO_TYPE['avi']

if __name__ == "__main__":
    try:
        print("Starting...")
        cv.namedWindow("PostWatch")
        vc = cv.VideoCapture(0)
        out = cv.VideoWriter(f"[{datetime.datetime.now()}]-{config.save_filename}", get_video_type(config.save_filename), config.frames_per_second, get_dimensions(vc, config.resolution))
        
        ret, frame = vc.read()

        while True:
            if frame is not None:
                out.write(frame)
                cv.imshow("Press q to quit", frame)
            ret, frame = vc.read()

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        
        print("Closing...")
        vc.release()
        out.release()
        cv.destroyAllWindows()
        print("Done.")
    except Exception as e:
        print(e)
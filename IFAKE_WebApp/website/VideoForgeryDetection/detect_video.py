import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import cv2
import numpy as np
from keras.models import load_model

#vid_name = input("\nEnter the name of video: ")
#vid_src = "G:/Video_Forgery_Detection_Using_Machine_Learning/Input_Videos/" + vid_name + ".mp4"

def detect_video_forgery(vid_src):
    vid = []
    forged_frames = []

    sumFrames = 0
    cap = cv2.VideoCapture(vid_src)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        b = cv2.resize(frame, (320, 240), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        vid.append(b)
        sumFrames += 1

    print("\nNo. Of Frames in the Video: ", sumFrames)
    print("\nFrame Rate (FPS): ", fps)

    Xtest = np.array(vid)

    print("\nPredicting !! ")
    model = load_model('C://Users//User//django_projects//models//video//forgery_model_me.hdf5')
    output = model.predict(Xtest)

    output = output.reshape((-1))
    results = []

    # Calculate frame duration
    frame_duration = 1 / fps

    for idx, pred in enumerate(output):
        if pred > 0.5:
            results.append(1)
            forged_frames.append((idx + 1) * frame_duration)  # Timestamp of forged frame
        else:
            results.append(0)

    no_of_forged = sum(results)

    print('No of forged frames:', no_of_forged)

    if no_of_forged <= 5:
        print("\nThe video is not forged")
        return {'result': 'Authentic', 'f_frames': 0, 'forged_frames': []}
    else:
        print("\nThe video is forged")
        print("\nNumber of Forged Frames in the video: ", no_of_forged)
        print("\nForged Frames Timestamps (in seconds): ", forged_frames)
        return {'result': 'Forged', 'f_frames': no_of_forged, 'forged_frames': forged_frames}

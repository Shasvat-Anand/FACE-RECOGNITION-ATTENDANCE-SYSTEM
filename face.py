import face_recognition 
import cv2
import csv
import time
import numpy as np
from datetime import datetime 
from face2 import *

video_capture= cv2.VideoCapture(0)

student=known_face_name.copy()
face_location=[]
face_encoding=[]
face_names=[]
s=True

now=datetime.now()
current_date= now.strftime("%Y-%m-%d")

f=open(current_date+ '.csv', 'w+', newline='')
lnwriter=csv.writer(f)



while s:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations (rgb_small_frame)
        face_encodings = face_recognition.face_encodings (rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces (known_face_encoding, face_encoding) 
            name=""
            face_distance = face_recognition.face_distance (known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_name[best_match_index]

            face_names.append(name)
            if name in student:
                student.remove(name)
                print(student)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name,current_time,"Persent"])
                print("Next person")
                time.sleep(2)

        cv2.imshow("attendence system",frame)
        if cv2.waitKey(1) & 0xFF == ord('k'):
           break 

time.sleep(1)
for i in student:
    lnwriter.writerow([i,current_time,"Absent"])
cv2.destroyAllWindows()
f.close()
exit()
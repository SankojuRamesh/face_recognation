from imutils import paths
import face_recognition
import os

from shutil import   copy
from PIL import Image, ImageDraw
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
obama = face_recognition.load_image_file(filename)
folder = 'obama'
obamaface_encoding = face_recognition.face_encodings(obama)[0]
path = 'images/'
images = []
for file in os.listdir(path):
    if file.endswith(".jpg"):
            images.append(os.path.join(path, file))

isExist = os.path.exists(folder)
if not isExist:
   
   os.makedirs(folder)

for file_name in images:
    newPic = face_recognition.load_image_file(file_name)
    for face_encoding in face_recognition.face_encodings(newPic):
        
        results = face_recognition.compare_faces([obamaface_encoding], face_encoding, 0.5)
        if results[0] == True:
            
            copy(file_name, "./obama/" + file_name.split("/")[1])



# unknown_picture = face_recognition.load_image_file("2.jpg")
# unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# results = face_recognition.compare_faces([obamaface_encoding], unknown_face_encoding)
 

# if results[0] == True:
#     print("It's a picture of obama!")
# else:
#     print("It's not a picture of obama!")
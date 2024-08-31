import face_recognition

tesla_image= face_recognition.load_image_file("A:Pics\project pic\\tesla.jpg ")
tesla_encoding= face_recognition.face_encodings(tesla_image)[0]
#adi_image= face_recognition.load_image_file("A:\project pic\\roll_no (2).jpg")
#adi_encoding= face_recognition.face_encodings(adi_image)[0]
modi_image= face_recognition.load_image_file("A:Pics\project pic\\modiji.jpg")
modi_encoding= face_recognition.face_encodings(modi_image)[0]
yogi_image= face_recognition.load_image_file("A:Pics\project pic\\yogiji.webp")
yogi_encoding= face_recognition.face_encodings(yogi_image)[0]
#kiran_image= face_recognition.load_image_file("A:\project pic\\roll_no (3).jpg")
#kiran_encoding= face_recognition.face_encodings(kiran_image)[0]
tata_image= face_recognition.load_image_file("A:Pics\project pic\\ratan tata.webp")
tata_encoding= face_recognition.face_encodings(tata_image)[0]
anand_image= face_recognition.load_image_file("A:Pics\project pic\\anand.jpg")
anand_encoding= face_recognition.face_encodings(anand_image)[0]



known_face_encoding = [
modi_encoding,
tata_encoding,
yogi_encoding,
tesla_encoding,
# adi_encoding,
# kiran_encoding,
anand_encoding
]


known_face_name=[
"modi",
"tata",
"yogi",
"Tesla",
# "adi",
# "kiran",
 "anand"
]
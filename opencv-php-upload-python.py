import cv2
import os

path = "upload"
dir_list = os.listdir(path)

cascade = open("./opencv-data.txt", "r")

cascade = cascade.read()

cascade_dir = "data/haarcascades/"+cascade

print("Casacde: "+cascade_dir)

detected = []
not_detected = []

for x in range (len(dir_list)):
    img = cv2.imread("upload/"+dir_list[x])
    stop_data = cv2.CascadeClassifier(cascade_dir)
    found = stop_data.detectMultiScale(img,
								minSize =(20, 20))
    amount_found = len(found)
    if amount_found != 0:
        detected.append(dir_list[x])
    else:
        not_detected.append(dir_list[x])

f = open("picture.php", "w")
f.write("<?php include 'opencv-php-upload.php' ?>")
f.write("Cascade Being Used: "+cascade_dir+"<br>")
f.write("<h2>Detected</h2>")
f.close()

print("Cascade Being Used: "+cascade_dir)
print(" ")
print ("Pictures With Object")

for x in range (len(detected)):
    print (detected[x])
    f = open("picture.php", "a")
    f.write("<img style='height:100; width:100 object-fit:contain;' src='"+(path)+"/"+(detected[x])+"'>")
    f.close()

print(" ")

f = open("picture.php", "a")
f.write("<h2>Not Detected</h2>")
f.close()

print ("Pictures Without Object")

for x in range (len(not_detected)):
    print (not_detected[x])
    f = open("picture.php", "a")
    f.write("<img style='height:100; width:100 object-fit:contain;' src='"+(path)+"/"+(not_detected[x])+"'>")
    f.close()




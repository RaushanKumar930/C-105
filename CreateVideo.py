import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,size)

for i in range(count - 1, 0, -1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("Done")

#sunrise = https://s3-whjr-curriculum-uploads.whjr.online/4d3bd681-7b8d-4b2b-96e4-091f2e75a9f9.gif
#sunset = https://s3-whjr-curriculum-uploads.whjr.online/733f647f-dd63-46e9-b757-150c4bfcf976.mp4
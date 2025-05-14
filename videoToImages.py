import cv2
import os

def videoToImages(videoPath, imageOutputPath):
    time = 8 #page flip interval time
    start = 5.1 #first beep on 5 sec + 10/30 frames OR 5.33sec, then loop 8 sec

    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS) #should be 30
    #print("fps is", fps)

    totalVidFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    interval = int(time*fps) # num of frames every 8 sec beep

    i = int(fps*start)
    pageNum = 1      




    while i <= totalVidFrames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
       
        height, width, _ = frame.shape
        
        #center points
        point1 = 48*width//100 # [ :  |:  : ]
        point2 = 52*width//100 # [ :  :|  : ]
        
        #edge points
        pointA = 8*width//100  # [ |  ::  : ]
        pointB = 92*width//100 # [ :  ::  | ]

        leftHalf = frame[:, pointA:point2]  # [ |  :|  : ]
        rightHalf = frame[:, point1:pointB] # [ :  |:  | ]
        leftPath = os.path.join(imageOutputPath, f"page{pageNum}.jpg")
        rightPath = os.path.join(imageOutputPath, f"page{pageNum+1}.jpg")



        #write
        cv2.imwrite(leftPath, leftHalf)
        cv2.imwrite(rightPath, rightHalf)

        print("page#:", pageNum)
        print("page#:", pageNum+1)
        pageNum+=2 # 2 pages per pic

        i += interval


    cap.release()
    print("YAY! Success!!!!")

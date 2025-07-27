import cv2


# Reading an image 

img =  cv2.imread("./images/tigern.jpeg")

# print(type(img))   # images are just numpy arrays

# print(img.shape)


# Writing an image

# cv2.imwrite("./images/test.png",img)


# Visualize image

# cv2.imshow("frame",img)

# cv2.waitKey(6000)   # this keep the window open until we press a key , Parameter is a milliseconds time delay , it will wait for seconds and auto close the window


#  visualize  videos 

# video =  cv2.VideoCapture("./videos/test.mp4")  # video path , else webcam value



# def visualize_video():
#     while True:
#          ret, frame = video.read()
#          if ret:
#            cv2.imshow('frame',frame)
#            cv2.waitKey(40)


# video.release()

# cv2.destroyAllWindows()

#  visualizing webcam


# webcam =  cv2.VideoCapture(0)


# def visualize_webcam():
#     ret,frame =  webcam.read()
#     if ret:
#         cv2.imshow('frame',frame)
#         cv2.waitKey(30)


# visualize_webcam()

# webcam.release()

# cv2.destroyAllWindows()
    


# Image resizing 



# resized_img = cv2.resize(img,(640,480))

# cv2.imshow("img",resized_img)

# cv2.waitKey(0)

# print(resized_img.shape)
import cv2


# Reading an image 

img =  cv2.imread("./images/noisy.png")

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


# Cropping the images



# print(img.shape)

# cropped_img =  img[80:120,90:110]

# cv2.imshow("cropped_img",cropped_img)

# cv2.waitKey(0)


# cv2.imshow("bird",img)

# cv2.waitKey(0)


#  Color visualization 

# By Default opencv reads each image as BGR (Blue , Green , Red)

# converting image to rgb

# img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# cv2.imshow("rgb_img",img_rgb)

# cv2.waitKey(0)


# Blurring Images


k_size = 7
# blurred_img = cv2.blur(img,(k_size,k_size))

# cv2.imshow("blurred",blurred_img)

# cv2.waitKey(0)

# conveting a noisy image to blur , to remove some of the noise 

# using median blur
blurred_noisy_img = cv2.medianBlur(img,k_size)

cv2.imshow("original_noisy",img)

cv2.imshow("blurred_oisy",blurred_noisy_img)

cv2.waitKey(0)
import cv2

# read the image from a path
img_read = cv2.imread("./images/tigern.jpeg")

print(img_read.shape)
print(img_read)


# show image in a window
# cv2.imshow('tiger',img_read)

# # Wait for a key press and close
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# resize the image

# resized_img =  cv2.resize(img_read,(100,100))

# cv2.imshow('resized tiger',resized_img)


# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""Convert image to gray scale (black and white)"""

# gray_img =  cv2.cvtColor(img_read,cv2.COLOR_BGR2GRAY)

# cv2.imshow('gray tiger',gray_img)


# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""Edge detection"""

edges = cv2.Canny(img_read, 200, 200)


cv2.imshow("edged tiger", edges)


cv2.waitKey(0)
cv2.destroyAllWindows()

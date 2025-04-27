import cv2
import os

# read the image from a path
img_read = cv2.imread("./images/testhuman.jpeg")

# print(img_read.shape)
# print(img_read)

flatten_img = img_read.flatten()

print(flatten_img)  # gives a 1D array instead of matrix

print(len(flatten_img))

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

# edges = cv2.Canny(img_read, 200, 200)


# cv2.imshow("edged tiger", edges)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""Edge detection using webcam"""

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     # apply some effects , example edge detection
#     edges = cv2.Canny(frame, 100, 200)
#     cv2.imshow("webimg", edges)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break


# cap.release()
# cv2.destroyAllWindows()


"""Face Detection"""

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# gray = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)

# faces =  face_cascade.detectMultiScale(gray,1.1,4)

# # drwa rectangle around faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(img_read, (x, y), (x+w, y+h), (255, 0, 0), 2)

# cv2.imshow('Face Detection', img_read)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""Face detection using a webcam"""

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

face_id = 0

save_dir = "detected_faces"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print(f"Created directory: {save_dir}")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # crop the face detected
        cropped_face = frame[y : y + h, x : x + w]

        face_filename = os.path.join(save_dir, f"face_{face_id}.jpg")
        cv2.imwrite(face_filename, cropped_face)
        face_id += 1

    cv2.imshow("Video Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

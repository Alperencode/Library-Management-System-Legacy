import cv2


def DetectFaces(img):
    """
    Detect faces in the frame
    """
    # Using the Haar Cascade Classifier
    face_cascade = cv2.CascadeClassifier(
        'methods/haarcascade_frontalface_default.xml'
        )

    # Applying grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5)

    for (x, y, w, h) in faces:
        # These variables represents the coordinates of the rectangle
        # Respectively: x_start, y_start, x_end, y_end

        # Rectange BGR, thickness, width and height
        color = (0, 0, 255)
        border = 2
        width = x + w
        height = y + h

        # Drawing rectangle
        if faces.all():
            cv2.rectangle(img, (x, y), (width, height), color, border)
            cv2.putText(
                img, "Face Found",
                (x, y-5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9, color=color, thickness=2)


# Using haarcascade and Starting Capture
cap = cv2.VideoCapture(0)

while True:
    # Reading the frame
    _, frame = cap.read()

    # Detecting faces
    DetectFaces(frame)

    # Showing the frame
    cv2.imshow("Face Detection", frame)

    # If 'q' is pressed, the program will stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2

# Capture video from the default camera
video_cap = cv2.VideoCapture(0)

while True:
    # Read frame-by-frame
    ret, video_frame = video_cap.read()
    
    # If frame is read correctly
    if not ret:
        print("Failed to capture image")
        break

    # Display the resulting frame
    cv2.imshow("video_live", video_frame)
    
    # Break the loop when 'a' key is pressed
    if cv2.waitKey(10) == ord('a'):
        break

# Release the video capture object
video_cap.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()

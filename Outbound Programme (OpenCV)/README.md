# Basic Introduction to OpenCV with Python (Telkom University Outbound Programme)

## Required Installs

1. Open CV Library (See issues faced for installation solutions with pip)
2. Numpy
3. Matplotlib

## Issues Faced

1. "The function is not implemented. Rebuild the library with Windows" -> Solved through https://stackoverflow.com/questions/50783177/opencv-the-function-is-not-implemented-rebuild-the-library-with-windows
2. "cv2 python has no imread/imshow member" -> Solved through https://stackoverflow.com/questions/51593147/cv2-python-has-no-imread-member
3. dlib installation -> Possible solutions (still not found)
   https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f
   https://stackoverflow.com/questions/41912372/dlib-installation-on-windows-10

## Things Learned Outline

### 1st Session : Basics of the OpenCV Library

1. Basic importing of images, showing to window.
2. Size manipulation, cropping of images, writing of new result to file.
3. Color manipulation, correction.

### 2nd Session : Basic Image Detection

Pedestrian detection using imutils, cv2

### 3rd Session :

1. Static Face Detection using haarcascade library.
2. Face counting with webcam.
3. Motion detection

### Resources

1. Histogram of Oriented Gradients (HOG) -> https://www.learnopencv.com/histogram-of-oriented-gradients/
2. Haar Cascade Detection -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
3. Webcam Motion Detector -> https://www.geeksforgeeks.org/webcam-motion-detector-python/
4. Hand Detection -> https://medium.com/analytics-vidhya/hand-detection-and-finger-counting-using-opencv-python-5b594704eb08

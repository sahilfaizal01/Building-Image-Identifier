# Building-Image-Identifier
A classification project using feature detection and matching using OpenCV

## Summary:-
In this project, I used the OpenCV library to find, describe, and match features. This was done for the task of classifying buildings. Here, the feature descriptors of the query image are matched with the features of all the trained images. The best match is the trained image whose features match the query image the most. And the matching of feature descriptions is based on Euclidean distance. We have used the ORB (Oriented FAST and Rotated BRIEF), which is a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance the performance.

## Contents:-
* main.py -> contains the entire tool functionality
* checker.py -> contains code to check the matching between two images, so as to get an understanding of the threshold values and the in-built functions
* video.mp4 -> testing video
* train -> training images folder

## Steps Involved:-
1) Instantiate the ORB algorithm with parameter set to 1500 features 
2) Provide the train path and intialise lists for storing images and class names
3) Loop through the saved images and obtain class names and store them
4) Define function to obtain the feature descriptors
5) Define matching function to compute the distance and classify only if the images have more number of similar features than the threshold
6) Open video and call the functions to carry out the classification

## Libraries Needed:-
OpenCV (pip install opencv-python)

## Detection Output:-
### Eiffel Tower
<img width="824" alt="Screenshot 2023-01-01 at 7 27 19 PM" src="https://user-images.githubusercontent.com/106440078/210173130-c059290e-8af4-4383-9827-cfef8ca34fc8.png">

### Toronto Tower
<img width="824" alt="Screenshot 2023-01-01 at 7 27 27 PM" src="https://user-images.githubusercontent.com/106440078/210173244-470d0cae-f518-48b9-a8cd-c2da586134ef.png">

### White House
<img width="824" alt="Screenshot 2023-01-01 at 7 27 32 PM" src="https://user-images.githubusercontent.com/106440078/210173175-3a6a91c1-baf3-45e1-aebc-3924f0cbec81.png">

### Taj Mahal
<img width="824" alt="Screenshot 2023-01-01 at 7 27 23 PM" src="https://user-images.githubusercontent.com/106440078/210173189-20a56396-79e5-482b-84b4-4fcc02e2d56c.png">



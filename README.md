# facedetection-evaluation

make your own dataset for benchmarking face detection method like:
1. opencv - haarcascade
2. dlib - CNN
3. dlib - HOG
4. mobilenet-SSD 
5. Multi-Task Cascade (MTCNN)

these repository include:
1. occlusioning image 

   make the filled rectangle that cover faces based on dlib-cnn detection. there are four level: 100% occluded, 75% occluded, 50% occluded and 25% occluded
   
2. grayscalling image

   change the RGB color of image to GRAY color using OpenCV

(more to come, still develop it)

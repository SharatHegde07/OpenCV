#########################################>>>>>>>>>>>>>>>>>   FACE DETECTION   <<<<<<<<<<<<<<<<<<###########################################################################

The code uses haarcascade_frontalface_default.xml classifier to detect the face of the person 

Basically the function named CreateDataSet collects the samples of your face in GRAY_SCALE and saves them in the Images folder(You may change the number of samples in the code to get more accuarte detection)

After the Data Set is created we need to train oir Face_Model using face_LBPHFaceRecognizer.create(A openCV class to train the model with images....if you interested to know how algorithm works let me know)

After training VOILA!!!...Keep your face near the web cam and green rectangle box covers your face with your name on it(Again you can change the colour of the box and the text you want on the top of your box)

Also the algorithm uses the Histogram method to calculate the difference and predict the accuracy of the frame

if you want to increase the accuracy increase the pred value (A variable which I have used in the code) to increase the accuracy

THANK YOU!!!!!!!!!!!!!!!!!!!!!!!!!!!

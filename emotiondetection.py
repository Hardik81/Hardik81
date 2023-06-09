!pip install deepface &> /dev/null
print ("Deep Face installed sucessfully!!")
from deepface import DeepFace
##Load and display input image
import cv2
import matplotlib.pyplot as plt
img1=cv2.imread("/content/virat2.jfif")
plt.imshow(img1[:,:,::-1])
plt.show()
# Plotting the image
# Flipping the color from BGR to RGB
plt.imshow(img1[:, :, ::-1 ]) 
plt.show()
##Analyze Image
obj=DeepFace.analyze(img1, actions = ['age', 'gender', 'race', 'emotion'])
print(obj)##Print Result
print("Your age is",obj["age"],"and you are",obj["dominant_race"],"and current emotion is ",obj["dominant_emotion"],"and your gender capture is", obj["gender"])

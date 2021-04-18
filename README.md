# Signlingo

## What it does
Signlingo aims to automate the process of teaching sign language and make it  more engaging by gamifying it. Our solution takes input from the webcam, and a custom PyTorch based Convolutional Neural Network determines if the user is showing the correct sign. 

## How we built it
![](https://raw.githubusercontent.com/Mainakdeb/signlingo/main/images/ASL_preprocessing_2.png)
1. Searched for a suitable Dataset to train the Neural Network.
2. Experimented with multiple network architectures, like ResNet-18, VGG19, etc., but the inference time was too high for a real time application.
3. Defined a smaller custom network and trained it.
4. Once the accuracy was good enough on the validation dataset, we tested the performance on some unseen images.
5. Then we tested it out with live webcam feed, and it worked!
6. Added a GUI for ease-of use, and also a level based system to make the process more engaging.

## Challenges we ran into
1.  Finding the right training hyperparameters took more time that we expected.
2. Making sure the network didnt overfit was challenging. Heavy image augmentation and dropout layers did the trick. The diagram below represents the augmentation techniques we used.
![](https://raw.githubusercontent.com/Mainakdeb/signlingo/main/images/ASL_augmentation.png)
3. Getting the GUI to work in harmony with the script was tricky.

## Accomplishments that we're proud of
1. We were surprised when the trained neural network actually worked with real life webcam feed.
2. The performance of the model was great too, because of its small architecture.

## What we learned
1. Learned the importance of inference time when dealing with trained neural networks, specially for real-time applications.
3. Having some sort of reward mechanism is important to keep the user engaged, hence we decided to add the game element to it.
2. We tested the app multiple times,  and unknowingly taught sign language  to ourselves :)  

## What we used  
1. PyTorch
2. OpenCV
3. Tkinter (UI)
4. Python threads

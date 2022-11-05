# MNIST-Handwritten-Digit-Recognition
This a neural network implemented using tensorflow that recognizes handwritten digits from 0-9 based on the MNIST dataset.

<h2>About the MNIST:</h2>
The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. The MNIST database contains 60,000 training images and 10,000 testing images. The images are grayscale, 28x28 pixels, and centered to reduce preprocessing and get started quicker.

<h2>About the network:</h2>
The implemented neural network is a dense neural network has a total of 5 layers and 111,514 trainable parameters. The model was trained on 60,000 images of handwritten digits ranging from 0-9 and was tested on 10,000 images.

![Screenshot from 2022-11-05 20-53-16](https://user-images.githubusercontent.com/74414105/200128573-db5175d1-c2c1-45c6-827a-95729feebd4b.png)

<h2>Results:</h2>
After getting trained on a total of 60,000 images, a batch size of 32 and 30 epochs the model achieved an accuracy of 98%. Accuracy on the testing set was 97%. The model did not seem to overfit the traning data. Following is a snapshot of a number of predictions made by the model:

![Screenshot from 2022-11-03 21-08-42](https://user-images.githubusercontent.com/74414105/200129006-cb7219a4-18f6-4a9a-8a57-b2d4783883ae.png)

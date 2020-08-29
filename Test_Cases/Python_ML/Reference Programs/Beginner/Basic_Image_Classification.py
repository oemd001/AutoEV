# Critical packages. run 'pip3 install tensorflow' if Python doesn't recognize
# tensorflow. 
import tensorflow as tf
from tensorflow import keras

# Important packages. Make sure to include this.
import matplotlib.pyplot as plt
import numpy as np

# This sets the "fashion database" to the variable fashion_mnsit
fashion_mnist = keras.datasets.fashion_mnist
# train_images and train_labels is the data that will be used for ML
# test_images and test_labels are images that will be used to test ML from the training data
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# train_images just tells us how larget the array will be
train_images.shape
# len(train_labels) just tells us how many different labels are in this set
len(train_labels)

# train_labels basically tells us the labels for each image. (1 is shirt, 2 is blah...etc)
train_labels
# there are 10k test_labels in total. 
len(test_labels)

# Assigning names to the images in question
class_names = ["T-Shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

# Pre-processing the data.
# plt.imshow(train_images[x]) returns the image in question
# shows the colorbar. Perhaps, the intensity of said image?
"""
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
"""

# The colorbar's range is from 0-255. Divide that by 255 for easier processing. 
train_images = train_images / 255.0
test_images = test_images / 255

# This just tests whether the labels have been assigned correctly. 
"""
plt.figure(figsize = (10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.yticks([])
    plt.xticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap = plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
"""

# keras.layer.Flatter basically 'flattens' the image from (for example, 1920 x 1080) to a 28 x 28 frame.
# keras.layer.Dense. No good way to explain this. Each input node is connected to each output node.
# keras.Sequential is basically the Neural Network that has a ton of different layers. (Introduced in the 1980s)
model1 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
    ])

# losses = cost. Lower, the better.
# accuracy, we are looking for 95% accuracy. 
model1.compile(optimizer='adam',
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics=(['accuracy']))

# 'fit' method bascially trains the given model on a set number of 'epochs' (interations)
model1.fit(train_images, train_labels, epochs = 10)

# This function basically prints the accuracy of the given data
test_loss, test_acc = model1.evaluate(test_images, test_labels, verbose = 2)
print("\n Accuracy : ", test_acc)

# Softmax just calculates the probability of the ML getting the right answer. 
probability_model = tf.keras.Sequential([model1,
                                          tf.keras.layers.Softmax()])


predictions = probability_model.predict(test_images)

predictions[0]
                                        









































        
              


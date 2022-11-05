import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from keras.datasets import mnist

# get the data
(train_x, train_y), (test_x, test_y) = mnist.load_data()

# flatten and reshape the data
train_x = train_x.flatten().reshape(train_x.shape[0], 784)

# build the model
model = Sequential([
    Dense(128, activation="relu"),
    Dense(64, activation="relu"),
    Dense(32, activation="relu"),
    Dense(16, activation="relu"),
    Dense(10, activation="softmax")
])

# specify the loss and optimizer functions
model.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics = ["accuracy"]
)

# train the model
model.fit(train_x, train_y, epochs=30)

# calculate the testing accuracy
count = 0

test_x = test_x.flatten().reshape(test_x.shape[0], 784)

pred = model.predict(test_x)

for i in range(len(pred)):

  if(np.argmax(pred[i]) == test_y[i]):
    count += 1

print(f"Test Set accuray = {(count / test_x.shape[0])*100}")

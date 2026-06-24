# -*- coding: utf-8 -*-
"""CSE463_4.ipynb

# **QUESTION 1**
"""

import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.image import resize
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.applications import VGG19
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

dir = "/content/drive/MyDrive/Lab4/Cat-dog-dataset"

def data_preprocessing(folder_path, classes_folder, desired_shape = (224, 224)):
    images = []
    labels = []

    for i, label_name in enumerate(classes_folder):
        images_folder_path = os.path.join(folder_path, label_name)
        all_files = os.listdir(images_folder_path)
        for filename in all_files:
            if filename.endswith(('.png','.jpg', '.jpeg')):
                file_path = os.path.join(images_folder_path, filename)
                img = load_img(file_path, target_size = desired_shape)
                img_array = img_to_array(img)
                images.append(img_array)
                labels.append(i)
    return np.array(images), np.array(labels)

classes = ['cats', 'dogs']
data, labels = data_preprocessing(dir, classes)
labels = to_categorical(labels, num_classes = len(classes))
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2, random_state = 42)
X_train, X_test = X_train/255.0, X_test/255.0

input_shape = (224, 224, 3)
input_layer = Input(shape = input_shape)

filter_size = (3,3)

# Block 1
x = Conv2D(64, filter_size, activation = 'relu', padding = 'same')(input_layer)
x = Conv2D(64, filter_size, activation = 'relu', padding = 'same')(x)
x = MaxPooling2D((2,2), strides=(2,2))(x)

# Block 2
x = Conv2D(128, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(128, filter_size, activation = 'relu', padding = 'same')(x)
x = MaxPooling2D((2,2), strides=(2,2))(x)

# Block 3
x = Conv2D(256, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(256, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(256, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(256, filter_size, activation = 'relu', padding = 'same')(x)
x = MaxPooling2D((2,2), strides=(2,2))(x)

# Block 4
x = Conv2D(512, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(512, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(512, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(512, filter_size, activation = 'relu', padding = 'same')(x)
x = MaxPooling2D((2,2), strides=(2,2))(x)

# Block 5
x = Conv2D(512, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(512, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(512, filter_size, activation = 'relu', padding = 'same')(x)
x = Conv2D(512, filter_size, activation = 'relu', padding = 'same')(x)
x = MaxPooling2D((2,2), strides=(2,2))(x)

# Flatten
x = Flatten()(x)


# Fully connected layers
x = Dense(4096, activation = 'relu')(x)
x = Dense(4096, activation = 'relu')(x)

# Final Dense Layer
final_dense_layer = Dense(len(classes), activation = "softmax")(x)

# creating a model
model = Model(
    inputs = input_layer,
    outputs = final_dense_layer
    )

model.compile(optimizer = Adam(learning_rate = 0.001), loss = "categorical_crossentropy", metrics = ['accuracy'])

# Model summary
model.summary()

#training the model
training = model.fit(X_train,y_train, epochs = 10, batch_size = 32,validation_data = (X_test, y_test))

# accuracy
model_accuracy = model.evaluate(X_test, y_test, verbose = 0)

# Savin Model
model.save("VGG_19.h5")

plt.figure(figsize=(10, 6))
plt.title("Accuracy Plotting")
plt.plot(training.history['accuracy'], label = 'Accuracy')
plt.plot(training.history['val_accuracy'], label = "Validation Accuracy")
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.show()

"""---
###**Role of each layer in the architecture**
*   **Convolution:** used for feature extraction
*   **MaxPooling2D:** Detects the necessary details from an image

*   **ReLU:** An activation function that adds non linearity and thus helps learning non-linear patterns

*   **Flatten layer:** Converts the 3D feature maps to a 1D vector as an input for the dense layers following it.
*   **Dense layer:** Makes a fully connected layer, connecting all the neurons on one layer with all other of the next layer.
*   **Softmax layer:** An activation function that returns class probabilities as output
---

---
###**Why VGG-19 uses small filters (3x3)**
=> VGG-19 uses small filters because it requires less number of parameters. Besides it helps capturing more details and thus extracting more features than the larger ones

---

# **QUESTION 2**
"""

import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.image import resize
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.applications import VGG19
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt

from tensorflow.keras.applications import ResNet50

import kagglehub
path = kagglehub.dataset_download("paultimothymooney/chest-xray-pneumonia")

"""***
The dataset selected is called Chest X-Ray Images (Pneumonia), which has 5856 files in total. Among which there are 5216 training images and 624 test images and 16 validation images. Besides it has two classes : PNEUMONIA & NORMAL.

***
"""

base_dir = "/kaggle/input/chest-xray-pneumonia/chest_xray"

train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')

"""##**Data Preprocessing**"""

def data_preprocessing(folder_path, classes_folder, desired_shape = (224, 224)):
    images = []
    labels = []

    for i, label_name in enumerate(classes_folder):
        images_folder_path = os.path.join(folder_path, label_name)
        all_files = os.listdir(images_folder_path)
        for filename in all_files:
            if filename.endswith(('.png','.jpg', '.jpeg')):
                file_path = os.path.join(images_folder_path, filename)
                img = load_img(file_path, target_size = desired_shape)
                img_array = img_to_array(img)
                images.append(img_array)
                labels.append(i)
    return np.array(images), np.array(labels)

classes = ['NORMAL', 'PNEUMONIA']
data, labels = data_preprocessing(train_dir, classes)
labels = to_categorical(labels, num_classes = len(classes))
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2, random_state = 42)
X_train, X_test = X_train/255.0, X_test/255.0

"""## **Using ResNet50**"""

input_shape = X_train[0].shape

base_resnet = ResNet50(weights = 'imagenet', include_top = False, input_shape=input_shape)
base_resnet.trainable = False
flatten_layer = Flatten()(base_resnet.output)
Dense_layer = Dense(64, activation = "relu")(flatten_layer)
final_layer = Dense(len(classes), activation = "softmax")(Dense_layer)

model = Model(
    inputs = base_resnet.input,
    outputs = final_layer
    )

model.compile(optimizer = Adam(learning_rate=0.001),
              loss = "categorical_crossentropy", metrics = ['accuracy'])

model.summary()

resnet50 = model.fit(X_train, y_train, epochs = 10, batch_size = 32, validation_data = (X_test, y_test))

# accuracy
model_accuracy_resnet50 = model.evaluate(X_test, y_test, verbose = 0)

print("Test accuracy:",model_accuracy_resnet50[1])

y_predicted_probs = model.predict(X_test)

y_predicted_val = np.argmax(y_predicted_probs, axis = 1)

y_expected = np.argmax(y_test, axis = 1)

# Classification Report
from sklearn.metrics import classification_report

print(classification_report(y_expected, y_predicted_val, target_names = classes))



"""##**Using VGG-19**"""

from tensorflow.keras.applications import VGG19

input_shape = X_train[0].shape

base_Vgg19 = VGG19(weights = 'imagenet', include_top = False, input_shape=input_shape)
base_Vgg19.trainable = False
flatten_layer = Flatten()(base_Vgg19.output)
Dense_layer = Dense(64, activation = "relu")(flatten_layer)
final_layer = Dense(len(classes), activation = "softmax")(Dense_layer)

model_vgg = Model(
    inputs = base_Vgg19.input,
    outputs = final_layer
    )

model_vgg.compile(optimizer = Adam(learning_rate=0.001),
              loss = "categorical_crossentropy", metrics = ['accuracy'])

model_vgg.summary()

Vgg19 = model_vgg.fit(X_train, y_train, epochs = 10, batch_size = 32, validation_data = (X_test, y_test))

# accuracy
model_accuracy_vgg19 = model_vgg.evaluate(X_test, y_test, verbose = 0)

print("Test accuracy:",model_accuracy_vgg19[1])

y_predicted_probs = model_vgg.predict(X_test)

y_predicted_val = np.argmax(y_predicted_probs, axis = 1)

y_expected = np.argmax(y_test, axis = 1)

# Classification Report
from sklearn.metrics import classification_report

print(classification_report(y_expected, y_predicted_val, target_names = classes))

"""##**Using InceptionV3**"""

from tensorflow.keras.applications import InceptionV3

input_shape = X_train[0].shape

base_InceptionV3 = InceptionV3(weights = 'imagenet', include_top = False, input_shape=input_shape)
base_InceptionV3.trainable = False
flatten_layer = Flatten()(base_InceptionV3.output)
Dense_layer = Dense(64, activation = "relu")(flatten_layer)
final_layer = Dense(len(classes), activation = "softmax")(Dense_layer)

model_InceptionV3 = Model(
    inputs = base_InceptionV3.input,
    outputs = final_layer
    )

model_InceptionV3.compile(optimizer = Adam(learning_rate=0.001),
              loss = "categorical_crossentropy", metrics = ['accuracy'])

model_InceptionV3.summary()

inception = model_InceptionV3.fit(X_train, y_train, epochs = 10, batch_size = 32, validation_data = (X_test, y_test))

# accuracy
model_accuracy_InceptionV3 = model_InceptionV3.evaluate(X_test, y_test, verbose = 0)

print("Test accuracy:",model_accuracy_InceptionV3[1])

y_predicted_probs = model_InceptionV3.predict(X_test)

y_predicted_val = np.argmax(y_predicted_probs, axis = 1)

y_expected = np.argmax(y_test, axis = 1)

# Classification Report
from sklearn.metrics import classification_report

print(classification_report(y_expected, y_predicted_val, target_names = classes))

"""----
###**Comparison**
For the selected dataset, VGG19 gives the best performance with an accuracy of 0.99. Becasue it handles class imbalance better. This is followed by InceptionV3 model, which has an accuracy of 0.98. For both classes it was able to handle the imbalance and give a balanced prediction. Because of being unable to do similarly, the worst performance so far is from the ResNet50 model, with an accuracy of 0.73.

----
"""


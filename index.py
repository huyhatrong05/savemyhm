# Установка нужных библиотек
!pip install tensorflow tensorflow-datasets matplotlib kaggle

# Авторизация Kaggle (если скачиваете с Kaggle)
from google.colab import files
files.upload()  # загрузите сюда kaggle.json
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Скачивание Stanford Cars с Kaggle
!kaggle datasets download -d eduardo4jesus/stanford-cars-dataset
!unzip stanford-cars-dataset.zip -d dataset

# Структура: dataset/cars_train/, dataset/cars_test/ и метки
import os
print(os.listdir("dataset"))

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Пути
TRAIN_DIR = "dataset/cars_train"
TEST_DIR  = "dataset/cars_test"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.15,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

train_data = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_data = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model

base_model = EfficientNetB0(
    input_shape=IMG_SIZE + (3,),
    include_top=False,
    weights='imagenet'
)

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.4)(x)
predictions = Dense(train_data.num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

for layer in base_model.layers:
    layer.trainable = False  # initial freeze

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

EPOCHS = 25

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], label='train_acc')
plt.plot(history.history['val_accuracy'], label='val_acc')
plt.legend()
plt.title('Accuracy')

plt.subplot(1,2,2)
plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.legend()
plt.title('Loss')

plt.show()

html = f"""
<html>
<head><title>Car Recognition Report</title></head>
<body>
<h1>Результаты обучения сети</h1>
<h2>Accuracy: {history.history['val_accuracy'][-1]:.4f}</h2>
<h2>Loss: {history.history['val_loss'][-1]:.4f}</h2>

<img src="accuracy_plot.png" width="500">
<img src="loss_plot.png" width="500">

<p>Пример предсказаний:</p>
"""

import numpy as np
import random

# берем случайные изображения и показываем
for i in range(5):
    img, label = val_data.next()
    pred = model.predict(img[:1])
    pred_class = np.argmax(pred, axis=1)
    html += f"<p>Предсказано: {pred_class[0]}</p>"

html += "</body></html>"

with open("report.html", "w") as f:
    f.write(html)

print("Сгенерирован HTML отчет!")

from tensorflow.keras import datasets, models, layers, utils, optimizers
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import callbacks

(x_train, y_train),(x_test, y_test)=datasets.fashion_mnist.load_data()

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

flg, axs = plt.subplots(5,5, figsize=(10,10))
for i in range(5):
  for j in range(5):
    axs[i, j].imshow(x_train[i*5+j], cmap='gray_r')
    #axs[i, j].axis('off')
plt.show()

print(np.unique(y_train, return_counts=True))

x_train.shape

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

print(x_train.shape)
print(x_train[0:1][0:1])

x_train = x_train /255.0
x_test = x_test /255.0

print(x_train[0:1][0:1])

y_train = utils.to_categorical(y_train, num_classes=10)
y_test = utils.to_categorical(y_test, num_classes=10)

print(y_train.shape)
print(y_train[0:1])

print(y_train.shape, y_test.shape)
print(y_train[0:1])

model = models.Sequential()
conv = layers.Conv2D(32, (3,3), padding='same', activation='relu', strides=(1,1), input_shape=(28, 28, 1))
model.add(conv)
#model.add(layers.Conv2D(32, (3,3), padding='same', activation='relu', strides=(1,1), input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D(pool_size=(2,2), strides=2))
model.summary()

model.add(layers.Conv2D(filters=64, kernel_size=(3,3), padding='same', activation='relu', strides=(1,1)))
model.add(layers.MaxPooling2D(pool_size=(2,2), strides=2))
model.summary()

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics='acc')
modelcheckpoint = callbacks.ModelCheckpoint('best.h5')
hist = model.fit(x_train, y_train, epochs=10,callbacks=[modelcheckpoint] ,validation_split=0.2)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.legend(['train', 'val'])

plt.subplot(1,2,2)
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.legend(['train', 'val'])
plt.show()

model.load_weights('best.h5')
model.evaluate(x_test, y_test)
classes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirts', 'Sneaker', 'Bag', 'Ankie boot']

prob = model.predict(x_test[115:140])
print(np.round(prob, 2))

print(np.argmax(prob, axis=1))
print(np.argmax(y_test[115:140], axis=1))

x_test2d = x_test.reshape(-1, 28,28)

flg, axs = plt.subplots(5,5, figsize=(10,10))
for i in range(5):
  for j in range(5):
    axs[i, j].imshow(x_test2d[i*5+j+100], cmap='gray_r')
    #axs[i, j].axis('off')
plt.show()
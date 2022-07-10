import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train),(x_test, y_test) = \
  tf.keras.datasets.fashion_mnist.load_data()

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

np.unique(y_train, return_counts=True)

fig, axs = plt.subplots(5,5)
for i in range(5):
  for j in range(5):
    axs[i, j].imshow(x_train[i*5+j], cmap='gray_r')
plt.show()

print(y_train[0:25])

y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)
print(y_train[0:2])

print(y_train.shape, y_test.shape)

x_train = x_train / 255
x_test = x_test / 255

x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

dense1 = tf.keras.layers.Dense(100, activation='sigmoid', input_shape=(28*28,))
dropout = tf.keras.layers.Dropout(0.3)
dense2 = tf.keras.layers.Dense(50, activation='relu')
dense3 = tf.keras.layers.Dense(10, activation='softmax')

model = tf.keras.Sequential([dense1,dropout, dense2, dense3])

model.summary()

model.compile(loss='categorical_crossentropy', metrics='acc')

hist = model.fit(x_train, y_train, epochs=20, validation_split=0.2)

print(hist.history)

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train','val'])
plt.show()

plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.xlabel('epoch')
plt.ylabel('acc')
plt.legend(['train', 'val'])
plt.show()

model.evaluate(x_test, y_test)

prob = model.predict(x_test[0:5])
print(prob)

prod = np.argmax(prob, axis=1)

print(prod)
print(np.argmax(y_test[0:5],axis=1))

# save ------------------------
model.save('model.h5')
model1 = tf.keras.models.load_model('model.h5')

model.save_weights('model-weights.h5')
model.load_weights('model-weights.h5')
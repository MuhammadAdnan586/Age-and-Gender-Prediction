import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input, BatchNormalization, Dropout
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
import sys

# Check Python executable path
print(sys.executable)

# Check OpenCV version
print(cv2.__version__)

# Image directory and size
image_dir = r"D:\Data Science\Deep Learning\archive\UTKFace"
image_size = 128

X, gender_labels, age_labels = [], [], []
for file in os.listdir(image_dir):
    if file.endswith(".jpg") or file.endswith(".jpg.chip"):
        try:
            parts = file.split('_')
            age = int(parts[0])
            gender = int(parts[1])
            img_path = os.path.join(image_dir, file)
            img = cv2.imread(img_path)
            if img is None:
                continue
            img = cv2.resize(img, (image_size, image_size))
            X.append(img)
            gender_labels.append(gender)
            age_labels.append(age)
        except Exception as e:
            print(f"Skipping file {file}: {e}")
            continue

# Convert to numpy arrays
X = np.array(X, dtype=np.float32) / 255.0
gender_labels = to_categorical(gender_labels, 2)
age_labels = np.array(age_labels, dtype=np.float32)

# Train-test split
X_train, X_test, gender_train, gender_test, age_train, age_test = train_test_split(
    X, gender_labels, age_labels, test_size=0.2, random_state=42
)

# Model architecture
input_layer = Input(shape=(128, 128, 3))

x = Conv2D(64, (3, 3), activation='relu', padding='same')(input_layer)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(256, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2))(x)

x = Flatten()(x)
x = Dense(128, activation='relu')(x)
x = BatchNormalization()(x)
x = Dropout(0.5)(x)

gender_branch = Dense(64, activation='relu')(x)
gender_branch = Dropout(0.3)(gender_branch)
gender_output = Dense(2, activation='softmax', name='gender_output')(gender_branch)

age_branch = Dense(64, activation='relu')(x)
age_branch = Dropout(0.3)(age_branch)
age_output = Dense(1, activation='linear', name='age_output')(age_branch)

model = Model(inputs=input_layer, outputs=[gender_output, age_output])

# Compile the model
model.compile(
    optimizer='adam',
    loss={'gender_output': 'categorical_crossentropy', 'age_output': 'mse'},
    metrics={'gender_output': 'accuracy', 'age_output': 'mae'}
)

# Train the model
model.fit(
    X_train,
    {'gender_output': gender_train, 'age_output': age_train},
    validation_data=(X_test, {'gender_output': gender_test, 'age_output': age_test}),
    epochs=15,
    batch_size=64
)

# Save the model
model.save("D:\\Data Science\\Deep Learning\\archive\\UTKFace\\model.h5")

# Load the model (for predictions)
model = load_model("D:\\Data Science\\Deep Learning\\archive\\UTKFace\\model.h5")

# Function to predict age and gender
def predict_age_gender(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return
    img = cv2.resize(img, (128, 128)) / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict using the model
    gender_pred, age_pred = model.predict(img)
    gender = np.argmax(gender_pred)
    
    # Display predicted gender and age
    print(f"Predicted Gender: {'Male' if gender == 0 else 'Female'}")
    print(f"Predicted Age: {int(age_pred[0][0])}")
    
# Example usage (replace with your own image path)
predict_age_gender("D:\\Data Science\\Deep Learning\\archive\\UTKFace\\1_0_0_20161219140627985.jpg.chip")

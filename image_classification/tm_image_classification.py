from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def predict_exhibit_class(image_path:str):
  """
  Use: Predicts the exhibit of a given image from a specified path.

  Parameters:
    image_path: Path to the image to be predicted.

  Returns: A tuple containing the predicted class (index 0) and the confidence score (index 1).
  """

  # Disable scientific notation for clarity
  np.set_printoptions(suppress=True)

  # Load the model
  model = load_model("/content/drive/MyDrive/Dark Data Internship/image_classification/exhibit/keras_model.h5", compile=False)

  # Load the labels
  class_names = open("/content/drive/MyDrive/Dark Data Internship/image_classification/exhibit/labels.txt", "r").readlines()

  # Create the array of the right shape to feed into the keras model
  # The 'length' or number of images you can put into the array is
  # determined by the first position in the shape tuple, in this case 1
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  # Replace this with the path to your image
  image = Image.open(image_path).convert("RGB")

  # resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # turn the image into a numpy array
  image_array = np.asarray(image)

  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  # Load the image into the array
  data[0] = normalized_image_array

  # Predicts the model
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]

  # Print prediction and confidence score
  return class_name[2:].replace("\n", ""), confidence_score


def predict_pre_post_renovation(image_path:str):
  """
  Use: Predicts if an image was taken before or after 2020-2024 renovation.

  Parameters:
    image_path: Path to the image to be predicted.

  Returns: A tuple containing the predicted class (index 0) and the confidence score (index 1).
  """

  # Disable scientific notation for clarity
  np.set_printoptions(suppress=True)

  # Load the model
  model = load_model("/content/drive/MyDrive/Dark Data Internship/image_classification/pre-post-rennovation/keras_model.h5", compile=False)

  # Load the labels
  class_names = open("/content/drive/MyDrive/Dark Data Internship/image_classification/pre-post-rennovation/labels.txt", "r").readlines()

  # Create the array of the right shape to feed into the keras model
  # The 'length' or number of images you can put into the array is
  # determined by the first position in the shape tuple, in this case 1
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  # Replace this with the path to your image
  image = Image.open(image_path).convert("RGB")

  # resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # turn the image into a numpy array
  image_array = np.asarray(image)

  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  # Load the image into the array
  data[0] = normalized_image_array

  # Predicts the model
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]

  # Print prediction and confidence score
  return class_name[2:].replace("\n", ""), confidence_score


def predict_all(image_path:str):
  """
  Use: Predicts the exhibit and relative time of a given image from a specified path.

  Parameters:
    image_path: Path to the image to be predicted.

  Returns: A dictionary where the keys are the specific categories, and the key values are a
  tuple of the predicted class (index 0) and the confidence of that class (index 1).
  """
  #initialize dictionary
  predict_dict = dict()

  #predict the exhibit of the picture and add to the dictionary
  predict_dict["exhibit"] = predict_exhibit_class(image_path)
  #predict if the image was taken pre/post-renovation and add to the dictionary
  predict_dict["pre-post-renovation"] = predict_pre_post_renovation(image_path)

  #return the resulting dictioary
  return predict_dict

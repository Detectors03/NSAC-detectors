# from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
# from tensorflow.keras.applications import VGG16
# from keras.applications.vgg16 import preprocess_input, decode_predictions
# from keras.preprocessing.sequence import pad_sequences
# from keras.preprocessing import image
# from keras.models import load_model, Model

# import matplotlib.pyplot as plt
# import pickle
# import numpy as np

# import warnings
# warnings.filterwarnings("ignore")



# model = load_model("./model_weights/cyclone_model.h5")
# model._make_predict_function()

# model_temp = VGG16(weights="imagenet", input_shape=(224,224,3))
# model_temp= VGG16(weights="imagenet", include_top=False,input_tensor=Input(shape=(224, 224, 3)))

# # Create a new model, by removing the last layer (output layer of 1000 classes) from the resnet50
# model_vgg16 = Model(model_temp.input, model_temp.layers[-2].output)
# model_vgg16._make_predict_function()


    
# # Load the word_to_idx and idx_to_word from disk

# with open("./storage/word_to_idx.pkl", "rb") as w2i:
#     word_to_idx = pickle.load(w2i)

# with open("./storage/idx_to_word.pkl", "rb") as i2w:
#     idx_to_word = pickle.load(i2w)
    

# max_len = 35


# def preprocess_image(img):
#     img = image.load_img(img, target_size=(224,224))
#     img = image.img_to_array(img)
#     img = np.expand_dims(img, axis=0)
#     img = preprocess_input(img)
#     return img

# def encode_image(img):
#     img = preprocess_image(img)
#     feature_vector = model_vgg16.predict(img)
#     feature_vector = feature_vector.reshape(1, feature_vector.shape[1])
#     return feature_vector



# def predict_caption(photo):
#     in_text = "startseq"

#     for i in range(max_len):
#         sequence = [word_to_idx[w] for w in in_text.split() if w in word_to_idx]
#         sequence = pad_sequences([sequence], maxlen=max_len, padding='post')

#         ypred =  model.predict([photo,sequence])
#         ypred = ypred.argmax()
#         word = idx_to_word[ypred]
#         in_text+= ' ' +word

#         if word =='endseq':
#             break


#     final_caption =  in_text.split()
#     final_caption = final_caption[1:-1]
#     final_caption = ' '.join(final_caption)

#     return final_caption




# def caption_this_image(input_img): 

#     photo = encode_image(input_img)
    

#     caption = predict_caption(photo)
#     # keras.backend.clear_session()
#     return caption


#this is my code
#required modules
import tensorflow as tf 
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
model = tf.keras.models.load_model('/content/gdrive/My Drive/Data/cyclone_model.h5')
from keras.applications.vgg16 import preprocess_input

#processing image and returning in data form
#img will be the image that we will provide by input in web app
def preprocess_image(img):
  img = image.load_img(img, target_size=(224, 224)) #insert a random cyclone image
  imgplot = plt.imshow(img)
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  img_data = preprocess_input(x)
  return img_data

img_data=preprocess_image(img)

#returning prediction
def predict(img_data):
  classes = model.predict(img_data)
  New_pred = np.argmax(classes, axis=1)
  if New_pred==[1]:
    return "Prediction: No-hazard"
  else:
    return "Prediction: Cyclone"
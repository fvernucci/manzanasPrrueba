import os

from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow import keras
from skimage import transform
from skimage.io import imread
import numpy as np
  
app = Flask(__name__)

@app.route("/",methods=['POST'])
def recognize_image():
  img_url = request.get_json()['img_url']
  print("imagen",img_url)
  img_array = imread(img_url, as_gray=True)

  return ("hecho")
  
 


if __name__ == '__main__':
    #model = keras.experimental.load_from_saved_model('fashion_mnist_classifier')
    model = keras.models.load_model("./my_model.h5")
    app.run()

from django.apps import AppConfig
import tensorflow as tf
import os

BASE_DIR = '/home/pypanoli/myproject/static'

class StampsearchConfig(AppConfig):
    name = 'stampSearch'
    def ready(self):
        global ml_stamp_model
        path_to_model = "mlmodels/mnist_digit.model"
        path = os.path.join(BASE_DIR, path_to_model)
        ml_stamp_model = tf.keras.models.load_model(path)
        pass # startup code here

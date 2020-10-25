from django.apps import AppConfig
import tensorflow as tf
import os
ml_digit_model = None
tf_graph = None
class KidsmathConfig(AppConfig):
    name = 'kidsmath'
    def ready(self):
        global ml_digit_model
        global tf_graph
        staticdir = '/home/pypanoli/myproject/static'
        path_to_model = "mlmodels/mnist_digit.model"
        path = os.path.join(staticdir, path_to_model)
        ml_digit_model = tf.keras.models.load_model(path)
        tf_graph = tf.get_default_graph()
        print('digit_model_loaded')

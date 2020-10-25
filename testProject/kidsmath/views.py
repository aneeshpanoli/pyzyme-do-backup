from django.shortcuts import render
import os
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import math
from scipy import ndimage
# from kidsmath import ml_digit_model

# Create your views here.
#Preprocess query image for prediction

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
import uuid
import matplotlib.pyplot as plt

from . import apps


@csrf_exempt
def predict_request(request):
    #check if user exists upon new user careation
    # if not create user, and send back the created user data nd uid
    if request.method == 'PUT':
        image_name = str(uuid.uuid4())+'.jpeg'
        DATADIR ='/home/pypanoli/myproject/static/kidsmath/userimg'
        path = os.path.join(DATADIR,image_name)
        image = np.fromstring(request.body, dtype="uint8")
        # print(len(request.body))
        image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(path, image)
        #**single digit identifier=======**
        # predict_data = preprocess_image(path)
        # digit = predict_digit(predict_data)
        #**single digit identifier=======**
        digit = multi_digit_preprocess(path)
        return JsonResponse({'digit': digit})
        # except:
        #     return JsonResponse({'status':'false'}, status=500)

def predict_response(request):
    #check if user exists upon new user careation
    # if not create user, and send back the created user data nd uid
    if request.method == 'GET':
        return JsonResponse({'valid':'rOk'})

def image_refiner(gray):
    org_size = 22
    img_size = 28
    rows,cols = gray.shape

    if rows > cols:
        factor = org_size/rows
        rows = org_size
        cols = int(round(cols*factor))
    else:
        factor = org_size/cols
        cols = org_size
        rows = int(round(rows*factor))
    gray = cv2.resize(gray, (cols, rows))

    #get padding
    colsPadding = (int(math.ceil((img_size-cols)/2.0)),int(math.floor((img_size-cols)/2.0)))
    rowsPadding = (int(math.ceil((img_size-rows)/2.0)),int(math.floor((img_size-rows)/2.0)))

    #apply apdding
    gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')
    return gray

def sorted_hierarchy_index(contours, sorted_contours):
  index_list = []
  for cnt in sorted_contours:
    temp_list = [i for i, e in enumerate(contours) if e.tolist() == cnt.tolist()]
    index_list+=temp_list
  return index_list

def multi_digit_preprocess(path):
    number = ""
    img_org = cv2.imread(path)
    img = img_org.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    ret,thresh = cv2.threshold(img,127,255,0)
    # edged = cv2.Canny(img, 75, 200)
    im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])#left->right
    #index of heirarchy for corresponding sorted contours
    h_index = sorted_hierarchy_index(contours, sorted_contours)
    # hierarchy = hierarchy[0][1:]
    for j,cnt in enumerate(sorted_contours):
        this_h_index = h_index[j]
        epsilon = 0.01*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)

        hull = cv2.convexHull(cnt)
        k = cv2.isContourConvex(cnt)
        x,y,w,h = cv2.boundingRect(cnt)

        if hierarchy[0][this_h_index][3] == 0:
        #putting boundary on each digit
          cv2.rectangle(img_org,(x,y),(x+w,y+h),(0,255,0),2)

          #cropping each image and process
          roi = img[y:y+h, x:x+w]
          roi = cv2.bitwise_not(roi)
          roi = image_refiner(roi)
          th,fnl = cv2.threshold(roi,127,255,cv2.THRESH_BINARY)
          roi = remove_empty_pix(roi)
          number+=predict_digit(roi)
    return number

def preprocess_image(path):
    #preprocess image and returns regular cv2 img_array
    #if not conv layers are used this array can be fed directly for prediction
    #after normalization
    predict_data = []
    print(path)
    img_array = cv2.imread(path ,cv2.IMREAD_GRAYSCALE)  # convert to array
    if img_array is not None:
        img_array = cv2.bitwise_not(img_array)
        thresh = 110
        img_array = cv2.threshold(img_array, thresh, 255, cv2.THRESH_BINARY)[1]
        img_array = remove_empty_pix(img_array)
        predict_data.append(img_array)  # add this to our training_data
    return predict_data


def getBestShift(img):
  cy,cx = ndimage.measurements.center_of_mass(img)

  rows,cols = img.shape
  shiftx = np.round(cols/2.0-cx).astype(int)
  shifty = np.round(rows/2.0-cy).astype(int)

  return shiftx,shifty

#shift
def shift(img,sx,sy):
  rows,cols = img.shape
  M = np.float32([[1,0,sx],[0,1,sy]])
  shifted = cv2.warpAffine(img,M,(cols,rows))
  return shifted

def remove_empty_pix(gray):
  while np.sum(gray[0]) == 0:
    gray = gray[1:]

  while np.sum(gray[:,0]) == 0:
    gray = np.delete(gray,0,1)

  while np.sum(gray[-1]) == 0:
    gray = gray[:-1]

  while np.sum(gray[:,-1]) == 0:
    gray = np.delete(gray,-1,1)

  rows,cols = gray.shape

  #resize to fit 20X20 box
  if rows > cols:
    factor = 20.0/rows
    rows = 20
    cols = int(round(cols*factor))
    gray = cv2.resize(gray, (cols,rows))
  else:
    factor = 20.0/cols
    cols = 20
    rows = int(round(rows*factor))
    gray = cv2.resize(gray, (cols, rows))

    #put back removed pixels
  colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
  rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
  gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')
  shiftx,shifty = getBestShift(gray)
  shifted = shift(gray,shiftx,shifty)
  gray = shifted
  return gray


def predict_digit(predict_data):
    # global ml_digit_model
    # predict_data = preprocess_image()
    predict_data_norm = tf.keras.utils.normalize(predict_data, axis=1) #normalized image array for prediction
    predict_data_numpy = np.array(predict_data_norm).reshape(-1, 28, 28, 1) # nparray
    # print(predict_data_norm)
    with apps.tf_graph.as_default():
        predictions = apps.ml_digit_model.predict(predict_data_numpy)
    pred = predictions[0]
    # tf.keras.backend.clear_session()
    # print(apps.ml_digit_model.summary())
    # print(np.argmax(pred))
    if np.amax(pred) > 0.88:
        return str(np.argmax(pred))
    else:
        return ""


import numpy as np
import pickle
from PIL import Image
import os

def init_network():
    with open(os.getcwd()+"\introductionToDeepLearning\chapter3\sample_weight\sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    print('a1: ',a1)
    z1 = sigmoid(a1)
    print('z1: ',z1)
    a2 = np.dot(z1, W2) + b2
    print('a2: ',a2)
    z2 = sigmoid(a2)
    print('z2: ',z2)
    a3 = np.dot(z2, W3) + b3
    print('a3: ',a3)
    y = softmax(a3)
   
    return y

def sigmoid(x):
    return 1 / (1 + np.exp(-x))    

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # 溢出对策
    return np.exp(x) / np.sum(np.exp(x))

print('os.getcwd(): ',os.getcwd())
print('os.pardir: ',os.pardir)
network = init_network()
img = Image.open(os.getcwd()+'\introductionToDeepLearning\chapter3\sample_weight\pic4.png')
img_array = np.array(img).reshape(-1)
y = predict(network,img_array)
print('y: ',y)
print('sum y: ',np.sum(y))
p = np.argmax(y)
print(p)


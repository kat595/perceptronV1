import numpy as np


def learn():
    print("nauczyłeś perceptron")


def decide():
    print("rozstrzygnąłeś")

def fourier_transform(x):
    a = np.abs(np.fft.fft(x))
    a[0] = 0
    return a / np.amax(a)



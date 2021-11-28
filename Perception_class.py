import matplotlib.pyplot as plt
import numpy as np
import Funkcje

Zero_grid = [
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
]

Jeden_grid = [
    [0, 0, 0, 0, 1]
    [0, 0, 0, 1, 1]
    [0, 0, 1, 0, 1]
    [0, 1, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
]

Dwa_grid = [
    [1, 1, 1, 1, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]
]

Trzy_grid = [
    [1, 1, 1, 1, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 1, 1, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
]

Cztery_grid = [
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
]

Piec_grid = [
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
]

Szesc_grid = [
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
]

Siedem_grid = [
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
]

Osiem_grid = [
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
]

Dziewiec_grid = [
    [1, 1, 1, 1, 1]
    [1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1]
    [1, 1, 1, 1, 1]
]

class Adaline():
    def __init__(self, no_of_inputs, learning_rate=0.01, iterations=100):
        self.no_of_inputs = no_of_inputs
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = np.random.random(2 * self.no_of_inputs)  # Zadanie: dopisac bias.
        self.errors = []

    def train(self, training_data_x, training_data_y, name):
        training_data_x = self._standarize(training_data_x)
        for _ in range(self.iterations):
            e = 0
            for x, y in zip(training_data_x, training_data_y):  # Zadanie: losowy wybor przykladow uczacych.
                out = self.output(x)
                self.weights += self.learning_rate * (y - out) * x
                e += (y - out) ** 2
            self.errors.append(e)
        plt.plot(range(len(self.errors)), self.errors)
        plt.savefig('learning_curve_' + name + '.pdf')
        plt.close()

    def _standarize(self, training_data_x):
        pass
        # Zadanie: X' = (X - Mean(X))/Std(X)

    def _normalize(self, training_data_x):
        pass
        # Zadanie: X' = (X - min(X))/(max(X) - min(X))

    def _activation(x):
        # Zadanie: dopisac fragment kodu realizujacy
        # Adaline w przypadku funkcji aktywacji innej niz f(x)=x.
        return x

    def _activation_derivative(x):
            return 1

    def output(self, input):
        inp = np.concatenate([input, Funkcje.fourier_transform(input)])
        summation = self._activation(np.dot(self.weights, inp))
        return summation




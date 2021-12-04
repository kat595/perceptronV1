# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import PIL.Image
from PIL import ImageTk
from tkinter import *
import numpy as np


# PLAN DO ZROBIENIA: ZROBIĆ MACIERZ DO KLIKALNEJ MATRYCY, KTORA ZMIENIA SIE ROWNOLEGLE
# PRZYCISK UCZ SIE WYWOLUJE PETLE Z TRAIN
# DOROBIC PETLE Z OUTPUT(TAKA SAMA JAK TRAIN), PRZYCISK ROZSTRZYGNIJ BEDZIE JA WYWOLYWAL
# DODAC WYJSCIE KTORA LICZBA PASUJE W KONSOLI //WYKONANED

# COS JUZ ZWRACA, POBAWIC SIE TYM

def on_black(num):  # definicja funkcji zaimplementowanej pozniej
    on_black1(num)


def clear():  # definicja funkcji zaimplementowanej pozniej
    clear1()


def on_left():
    on_left1()


def on_up():
    on_up1()


def on_down():
    on_down1()


def on_right():
    on_right1()


# PRZYKLADY UCZACE
Matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

Data = [[]] * 10

Data[0] = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

Data[1] = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]

Data[2] = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

Data[3] = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]

]

Data[4] = [
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]

Data[5] = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

Data[6] = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

Data[7] = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]

Data[8] = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

Data[9] = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]


# PRZYKLADY UCZACE

# ADALINE

class Adaline(object):
    def __init__(self, no_of_inputs, learning_rate=0.01, iterations=100, bias=True):
        self.no_of_inputs = no_of_inputs
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = np.random.random(2 * self.no_of_inputs)
        self.bias = bias
        if self.bias:
            self.weights = (np.random.rand(2 * self.no_of_inputs + 1) - 0.5) / 1000
        else:
            self.weights = (np.random.rand(2 * self.no_of_inputs) - 0.5) / 1000
        self.errors = []

    def train(self, training_data_x, training_data_y):
        training_data_x = self.normalize(training_data_x) - 0.5 * 0.01
        training_data_y = self.normalize(training_data_y) - 0.5 * 0.01
        for _ in range(self.iterations):
            e = 0
            array = list(zip(training_data_x, training_data_y))
            random.shuffle(array)
            for x, y in array:  # Zadanie: losowy wybor przykladow uczacych.
                out = self.output(x)
                x = np.concatenate([x, self.fourier_transform(x)])
                if self.bias:
                    x = np.concatenate([x, [1]])
                self.weights += self.learning_rate * (y - out) * x
                e += (y - out) ** 2
            self.errors.append(e)

    def _standarize(self, training_data_x):
        pass
        # Zadanie: X' = (X - Mean(X))/Std(X)

    def fourier_transform(self, x):
        a = np.abs(np.fft.fft(x))
        a[0] = 0
        return a / np.amax(a)

    def normalize(self, x):
        return (x - np.min(x)) / (np.max(x) - np.min(x))

    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    def output(self, x):
        # print(x)
        inp = np.concatenate([x, self.fourier_transform(x)])
        if self.bias:
            inp = np.concatenate([inp, [1]])
        summation = self.activation(np.dot(self.weights, inp))
        return summation


# ADALINE

# MAIN

adalines = [Adaline(7 * 5), Adaline(7 * 5), Adaline(7 * 5), Adaline(7 * 5), Adaline(7 * 5), Adaline(7 * 5),
            Adaline(7 * 5), Adaline(7 * 5), Adaline(7 * 5), Adaline(7 * 5)]


def learn():
    data_x = [np.array(t).flatten() for t in Data]

    for i in range(10):
        data_y = np.zeros(10)
        data_y[i] = 1
        adalines[i].train(data_x, data_y)


def decide():
    data_matrix = np.array(Matrix).flatten()
    for i in range(10):
        print(i, ':', (int)(adalines[i].output(data_matrix) * 100), '%')


# MAIN

# GUI

window = Tk()  # instancja okna
window.geometry("785x850")
window.title("Perceptron")

img = PIL.Image.open('Images/logo_umk.png')  # logo okienka w lewym gornym rogu
img = ImageTk.PhotoImage(img)
window.iconphoto(True, img)

# img2 = PIL.Image.open('clear.png')  # ikonka do przycisku clear, zrobiona tak, zeby moc ją risajzować
# img2 = img2.resize((10, 10))
# resized_img2 = ImageTk.PhotoImage(img2)

button1 = Button(window, text="clear", command=clear, font=("Comic Sans", 20), width=15,
                 state=ACTIVE)  # przycisk wyczysc w lewym gornym rogu
button1.pack()
button1.place(x=0, y=0)

button2 = Button(window, text="ucz sie", command=learn, font=("Comic Sans", 20), width=15,
                 state=ACTIVE)  # przycisk ucz sie u góry ekranu
button2.pack()
button2.place(x=270, y=0)

button3 = Button(window, text="rozstrzygnij", command=decide, font=("Comic Sans", 20), width=15,
                 state=ACTIVE)  # przycisk rozstrzygnij w prawym gornym rogu
button3.pack()
button3.place(x=540, y=0)

button4 = Button(window, text="w lewo", command=on_left, font=("Comic Sans", 20), width=10,
                 state=ACTIVE)  # przycisk do przesuniecia cyfry w lewo

button4.pack()
button4.place(x=0, y=800)

button5 = Button(window, text="w góre", command=on_up, font=("Comic Sans", 20), width=10,
                 state=ACTIVE)  # przycisk do przesuniecia cyfry w góre

button5.pack()
button5.place(x=200, y=800)

button6 = Button(window, text="w dół", command=on_down, font=("Comic Sans", 20), width=10,
                 state=ACTIVE)  # przycisk do przesuniecia cyfry w dół

button6.pack()
button6.place(x=400, y=800)

button7 = Button(window, text="w prawo", command=on_right, font=("Comic Sans", 20), width=15,
                 state=ACTIVE)  # przycisk do przesuniecia cyfry w prawo

button7.pack()
button7.place(x=600, y=800)

frame = Frame(window, bg="green", bd=5)  # ramka w ktorej trzymamy board do perceptronu 5x7
frame.pack()
frame.place(x=215, y=100)

poleA1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A1'))  # 1 wiersz pól
poleA1.grid(row=0, column=0)
poleA2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A2'))
poleA2.grid(row=0, column=1)
poleA3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A3'))
poleA3.grid(row=0, column=2)
poleA4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A4'))
poleA4.grid(row=0, column=3)
poleA5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A5'))
poleA5.grid(row=0, column=4)

poleB1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B1'))  # 2 wiersz pól
poleB1.grid(row=1, column=0)
poleB2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B2'))
poleB2.grid(row=1, column=1)
poleB3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B3'))
poleB3.grid(row=1, column=2)
poleB4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B4'))
poleB4.grid(row=1, column=3)
poleB5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B5'))
poleB5.grid(row=1, column=4)

poleC1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C1'))  # 3 wiersz pól
poleC1.grid(row=2, column=0)
poleC2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C2'))
poleC2.grid(row=2, column=1)
poleC3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C3'))
poleC3.grid(row=2, column=2)
poleC4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C4'))
poleC4.grid(row=2, column=3)
poleC5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C5'))
poleC5.grid(row=2, column=4)

poleD1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D1'))  # 4 wiersz pól
poleD1.grid(row=3, column=0)
poleD2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D2'))
poleD2.grid(row=3, column=1)
poleD3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D3'))
poleD3.grid(row=3, column=2)
poleD4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D4'))
poleD4.grid(row=3, column=3)
poleD5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D5'))
poleD5.grid(row=3, column=4)

poleE1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E1'))  # 5 wiersz pól
poleE1.grid(row=4, column=0)
poleE2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E2'))
poleE2.grid(row=4, column=1)
poleE3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E3'))
poleE3.grid(row=4, column=2)
poleE4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E4'))
poleE4.grid(row=4, column=3)
poleE5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E5'))
poleE5.grid(row=4, column=4)

poleF1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F1'))  # 5 wiersz pól
poleF1.grid(row=5, column=0)
poleF2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F2'))
poleF2.grid(row=5, column=1)
poleF3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F3'))
poleF3.grid(row=5, column=2)
poleF4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F4'))
poleF4.grid(row=5, column=3)
poleF5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F5'))
poleF5.grid(row=5, column=4)

poleG1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G1'))  # 5 wiersz pól
poleG1.grid(row=6, column=0)
poleG2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G2'))
poleG2.grid(row=6, column=1)
poleG3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G3'))
poleG3.grid(row=6, column=2)
poleG4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G4'))
poleG4.grid(row=6, column=3)
poleG5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G5'))
poleG5.grid(row=6, column=4)

window.config(background='#100b40')  # kolor tła okna


# GUI


def on_black1(num):  # zamalowanie wybranego kafelka na czarno
    if num == 'A1':
        poleA1.configure(fg="black", bg="black")
        Matrix[0][0] = 1
    if num == 'A2':
        poleA2.configure(fg="black", bg="black")
        Matrix[0][1] = 1
    if num == 'A3':
        poleA3.configure(fg="black", bg="black")
        Matrix[0][2] = 1
    if num == 'A4':
        poleA4.configure(fg="black", bg="black")
        Matrix[0][3] = 1
    if num == 'A5':
        poleA5.configure(fg="black", bg="black")
        Matrix[0][4] = 1
    if num == 'B1':
        poleB1.configure(fg="black", bg="black")
        Matrix[1][0] = 1
    if num == 'B2':
        poleB2.configure(fg="black", bg="black")
        Matrix[1][1] = 1
    if num == 'B3':
        poleB3.configure(fg="black", bg="black")
        Matrix[1][2] = 1
    if num == 'B4':
        poleB4.configure(fg="black", bg="black")
        Matrix[1][3] = 1
    if num == 'B5':
        poleB5.configure(fg="black", bg="black")
        Matrix[1][4] = 1
    if num == 'C1':
        poleC1.configure(fg="black", bg="black")
        Matrix[2][0] = 1
    if num == 'C2':
        poleC2.configure(fg="black", bg="black")
        Matrix[2][1] = 1
    if num == 'C3':
        poleC3.configure(fg="black", bg="black")
        Matrix[2][2] = 1
    if num == 'C4':
        poleC4.configure(fg="black", bg="black")
        Matrix[2][3] = 1
    if num == 'C5':
        poleC5.configure(fg="black", bg="black")
        Matrix[2][4] = 1
    if num == 'D1':
        poleD1.configure(fg="black", bg="black")
        Matrix[3][0] = 1
    if num == 'D2':
        poleD2.configure(fg="black", bg="black")
        Matrix[3][1] = 1
    if num == 'D3':
        poleD3.configure(fg="black", bg="black")
        Matrix[3][2] = 1
    if num == 'D4':
        poleD4.configure(fg="black", bg="black")
        Matrix[3][3] = 1
    if num == 'D5':
        poleD5.configure(fg="black", bg="black")
        Matrix[3][4] = 1
    if num == 'E1':
        poleE1.configure(fg="black", bg="black")
        Matrix[4][0] = 1
    if num == 'E2':
        poleE2.configure(fg="black", bg="black")
        Matrix[4][1] = 1
    if num == 'E3':
        poleE3.configure(fg="black", bg="black")
        Matrix[4][2] = 1
    if num == 'E4':
        poleE4.configure(fg="black", bg="black")
        Matrix[4][3] = 1
    if num == 'E5':
        poleE5.configure(fg="black", bg="black")
        Matrix[4][4] = 1
    if num == 'F1':
        poleF1.configure(fg="black", bg="black")
        Matrix[5][0] = 1
    if num == 'F2':
        poleF2.configure(fg="black", bg="black")
        Matrix[5][1] = 1
    if num == 'F3':
        poleF3.configure(fg="black", bg="black")
        Matrix[5][2] = 1
    if num == 'F4':
        poleF4.configure(fg="black", bg="black")
        Matrix[5][3] = 1
    if num == 'F5':
        poleF5.configure(fg="black", bg="black")
        Matrix[5][4] = 1
    if num == 'G1':
        poleG1.configure(fg="black", bg="black")
        Matrix[6][0] = 1
    if num == 'G2':
        poleG2.configure(fg="black", bg="black")
        Matrix[6][1] = 1
    if num == 'G3':
        poleG3.configure(fg="black", bg="black")
        Matrix[6][2] = 1
    if num == 'G4':
        poleG4.configure(fg="black", bg="black")
        Matrix[6][3] = 1
    if num == 'G5':
        poleG5.configure(fg="black", bg="black")
        Matrix[6][4] = 1


def on_black2(numx, numy):  # funkcja do przesuwania cyfry na planszy, zamalowanie wybranego kafelka na czarno
    if numx == 0 and numy == 0:
        poleA1.configure(fg="black", bg="black")
        Matrix[0][0] = 1
    if numx == 0 and numy == 1:
        poleA2.configure(fg="black", bg="black")
        Matrix[0][1] = 1
    if numx == 0 and numy == 2:
        poleA3.configure(fg="black", bg="black")
        Matrix[0][2] = 1
    if numx == 0 and numy == 3:
        poleA4.configure(fg="black", bg="black")
        Matrix[0][3] = 1
    if numx == 0 and numy == 4:
        poleA5.configure(fg="black", bg="black")
        Matrix[0][4] = 1
    if numx == 1 and numy == 0:
        poleB1.configure(fg="black", bg="black")
        Matrix[1][0] = 1
    if numx == 1 and numy == 1:
        poleB2.configure(fg="black", bg="black")
        Matrix[1][1] = 1
    if numx == 1 and numy == 2:
        poleB3.configure(fg="black", bg="black")
        Matrix[1][2] = 1
    if numx == 1 and numy == 3:
        poleB4.configure(fg="black", bg="black")
        Matrix[1][3] = 1
    if numx == 1 and numy == 4:
        poleB5.configure(fg="black", bg="black")
        Matrix[1][4] = 1
    if numx == 2 and numy == 0:
        poleC1.configure(fg="black", bg="black")
        Matrix[2][0] = 1
    if numx == 2 and numy == 1:
        poleC2.configure(fg="black", bg="black")
        Matrix[2][1] = 1
    if numx == 2 and numy == 2:
        poleC3.configure(fg="black", bg="black")
        Matrix[2][2] = 1
    if numx == 2 and numy == 3:
        poleC4.configure(fg="black", bg="black")
        Matrix[2][3] = 1
    if numx == 2 and numy == 4:
        poleC5.configure(fg="black", bg="black")
        Matrix[2][4] = 1
    if numx == 3 and numy == 0:
        poleD1.configure(fg="black", bg="black")
        Matrix[3][0] = 1
    if numx == 3 and numy == 1:
        poleD2.configure(fg="black", bg="black")
        Matrix[3][1] = 1
    if numx == 3 and numy == 2:
        poleD3.configure(fg="black", bg="black")
        Matrix[3][2] = 1
    if numx == 3 and numy == 3:
        poleD4.configure(fg="black", bg="black")
        Matrix[3][3] = 1
    if numx == 3 and numy == 4:
        poleD5.configure(fg="black", bg="black")
        Matrix[3][4] = 1
    if numx == 4 and numy == 0:
        poleE1.configure(fg="black", bg="black")
        Matrix[4][0] = 1
    if numx == 4 and numy == 1:
        poleE2.configure(fg="black", bg="black")
        Matrix[4][1] = 1
    if numx == 4 and numy == 2:
        poleE3.configure(fg="black", bg="black")
        Matrix[4][2] = 1
    if numx == 4 and numy == 3:
        poleE4.configure(fg="black", bg="black")
        Matrix[4][3] = 1
    if numx == 4 and numy == 4:
        poleE5.configure(fg="black", bg="black")
        Matrix[4][4] = 1
    if numx == 5 and numy == 0:
        poleF1.configure(fg="black", bg="black")
        Matrix[5][0] = 1
    if numx == 5 and numy == 1:
        poleF2.configure(fg="black", bg="black")
        Matrix[5][1] = 1
    if numx == 5 and numy == 2:
        poleF3.configure(fg="black", bg="black")
        Matrix[5][2] = 1
    if numx == 5 and numy == 3:
        poleF4.configure(fg="black", bg="black")
        Matrix[5][3] = 1
    if numx == 5 and numy == 4:
        poleF5.configure(fg="black", bg="black")
        Matrix[5][4] = 1
    if numx == 6 and numy == 0:
        poleG1.configure(fg="black", bg="black")
        Matrix[6][0] = 1
    if numx == 6 and numy == 1:
        poleG2.configure(fg="black", bg="black")
        Matrix[6][1] = 1
    if numx == 6 and numy == 2:
        poleG3.configure(fg="black", bg="black")
        Matrix[6][2] = 1
    if numx == 6 and numy == 3:
        poleG4.configure(fg="black", bg="black")
        Matrix[6][3] = 1
    if numx == 6 and numy == 4:
        poleG5.configure(fg="black", bg="black")
        Matrix[6][4] = 1


def clear1():  # reset planszy do poziomu startowego
    poleA1.configure(fg="gray", bg="gray")
    poleA2.configure(fg="gray", bg="gray")
    poleA3.configure(fg="gray", bg="gray")
    poleA4.configure(fg="gray", bg="gray")
    poleA5.configure(fg="gray", bg="gray")

    poleB1.configure(fg="gray", bg="gray")
    poleB2.configure(fg="gray", bg="gray")
    poleB3.configure(fg="gray", bg="gray")
    poleB4.configure(fg="gray", bg="gray")
    poleB5.configure(fg="gray", bg="gray")

    poleC1.configure(fg="gray", bg="gray")
    poleC2.configure(fg="gray", bg="gray")
    poleC3.configure(fg="gray", bg="gray")
    poleC4.configure(fg="gray", bg="gray")
    poleC5.configure(fg="gray", bg="gray")

    poleD1.configure(fg="gray", bg="gray")
    poleD2.configure(fg="gray", bg="gray")
    poleD3.configure(fg="gray", bg="gray")
    poleD4.configure(fg="gray", bg="gray")
    poleD5.configure(fg="gray", bg="gray")

    poleE1.configure(fg="gray", bg="gray")
    poleE2.configure(fg="gray", bg="gray")
    poleE3.configure(fg="gray", bg="gray")
    poleE4.configure(fg="gray", bg="gray")
    poleE5.configure(fg="gray", bg="gray")

    poleF1.configure(fg="gray", bg="gray")
    poleF2.configure(fg="gray", bg="gray")
    poleF3.configure(fg="gray", bg="gray")
    poleF4.configure(fg="gray", bg="gray")
    poleF5.configure(fg="gray", bg="gray")

    poleG1.configure(fg="gray", bg="gray")
    poleG2.configure(fg="gray", bg="gray")
    poleG3.configure(fg="gray", bg="gray")
    poleG4.configure(fg="gray", bg="gray")
    poleG5.configure(fg="gray", bg="gray")

    for i in range(7):
        for j in range(5):
            Matrix[i][j] = 0


def on_left1():
    matrix_new = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(7):
        for j in range(5):
            if Matrix[i][j] == 1:
                if j-1 >= 0:
                    matrix_new[i][j-1] = 1

    for i in range(7):
        for j in range(5):
            Matrix[i][j] = 0

    clear1()
    for i in range(7):
        for j in range(5):
            if matrix_new[i][j] == 1:
                on_black2(i, j)


def on_up1():
    matrix_new = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(7):
        for j in range(5):
            if Matrix[i][j] == 1:
                if i-1 >= 0:
                    matrix_new[i-1][j] = 1

    for i in range(7):
        for j in range(5):
            Matrix[i][j] = 0

    clear1()
    for i in range(7):
        for j in range(5):
            if matrix_new[i][j] == 1:
                on_black2(i, j)


def on_down1():
    matrix_new = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(7):
        for j in range(5):
            if Matrix[i][j] == 1:
                if i+1 >= 0:
                    matrix_new[i+1][j] = 1

    for i in range(7):
        for j in range(5):
            Matrix[i][j] = 0

    clear1()
    for i in range(7):
        for j in range(5):
            if matrix_new[i][j] == 1:
                on_black2(i, j)


def on_right1():
    matrix_new = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(7):
        for j in range(5):
            if Matrix[i][j] == 1:
                if j+1 >= 0:
                    matrix_new[i][j+1] = 1

    for i in range(7):
        for j in range(5):
            Matrix[i][j] = 0

    clear1()
    for i in range(7):
        for j in range(5):
            if matrix_new[i][j] == 1:
                on_black2(i, j)


window.mainloop()  # zatrzymanie okna na ekranie komputera

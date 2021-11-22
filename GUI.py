# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import PIL.Image
from PIL import ImageTk
from tkinter import *
from Funkcje import *


def on_black(num): # definicja funkcji zaimplementowanej pozniej
    on_black1(num)


def clear(): # definicja funkcji zaimplementowanej pozniej
    clear1()


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


def on_black1(num): # zamalowanie wybranego kafelka na czarno
    if num == 'A1':
        poleA1.configure(fg="black", bg="black")
    if num == 'A2':
        poleA2.configure(fg="black", bg="black")
    if num == 'A3':
        poleA3.configure(fg="black", bg="black")
    if num == 'A4':
        poleA4.configure(fg="black", bg="black")
    if num == 'A5':
        poleA5.configure(fg="black", bg="black")
    if num == 'B1':
        poleB1.configure(fg="black", bg="black")
    if num == 'B2':
        poleB2.configure(fg="black", bg="black")
    if num == 'B3':
        poleB3.configure(fg="black", bg="black")
    if num == 'B4':
        poleB4.configure(fg="black", bg="black")
    if num == 'B5':
        poleB5.configure(fg="black", bg="black")
    if num == 'C1':
        poleC1.configure(fg="black", bg="black")
    if num == 'C2':
        poleC2.configure(fg="black", bg="black")
    if num == 'C3':
        poleC3.configure(fg="black", bg="black")
    if num == 'C4':
        poleC4.configure(fg="black", bg="black")
    if num == 'C5':
        poleC5.configure(fg="black", bg="black")
    if num == 'D1':
        poleD1.configure(fg="black", bg="black")
    if num == 'D2':
        poleD2.configure(fg="black", bg="black")
    if num == 'D3':
        poleD3.configure(fg="black", bg="black")
    if num == 'D4':
        poleD4.configure(fg="black", bg="black")
    if num == 'D5':
        poleD5.configure(fg="black", bg="black")
    if num == 'E1':
        poleE1.configure(fg="black", bg="black")
    if num == 'E2':
        poleE2.configure(fg="black", bg="black")
    if num == 'E3':
        poleE3.configure(fg="black", bg="black")
    if num == 'E4':
        poleE4.configure(fg="black", bg="black")
    if num == 'E5':
        poleE5.configure(fg="black", bg="black")
    if num == 'F1':
        poleF1.configure(fg="black", bg="black")
    if num == 'F2':
        poleF2.configure(fg="black", bg="black")
    if num == 'F3':
        poleF3.configure(fg="black", bg="black")
    if num == 'F4':
        poleF4.configure(fg="black", bg="black")
    if num == 'F5':
        poleF5.configure(fg="black", bg="black")
    if num == 'G1':
        poleG1.configure(fg="black", bg="black")
    if num == 'G2':
        poleG2.configure(fg="black", bg="black")
    if num == 'G3':
        poleG3.configure(fg="black", bg="black")
    if num == 'G4':
        poleG4.configure(fg="black", bg="black")
    if num == 'G5':
        poleG5.configure(fg="black", bg="black")


def clear1(): # reset planszy do poziomu startowego
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

window.mainloop()  # zatrzymanie okna na ekranie komputera
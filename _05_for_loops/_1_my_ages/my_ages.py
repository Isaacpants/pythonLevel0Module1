from tkinter import Tk, messagebox, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    for i in range(16):
        print(str(i+1))
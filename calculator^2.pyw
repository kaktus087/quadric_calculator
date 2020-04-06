import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox


root = Tk()

label_x_1 = Label(root, text='', font="1")
label_x_2 = Label(root, text='', font="1")

def ckicked():
	a_1=[]
	b_1=[]
	a = float(a_entry.get())
	b = float(b_entry.get())
	c = float(c_entry.get())
	Discriminant = b**2-4*(a*c)
	if Discriminant >= 0:
		x_1 = (-b + (Discriminant**0.5)) / (2*a)
		x_2 = (-b - (Discriminant**0.5)) / (2*a)
		x_1_text = "x1=: " + str(x_1)
		x_2_text = "x2=: " + str(x_2)
		label_x_1.config(text=x_1_text)
		label_x_2.config(text=x_2_text)
		label_x_1.place(x=210, y=30)
		label_x_2.place(x=210, y=50)
		a = 0
		b = 0
		c = 0

	else:
		messagebox.showerror("Error", "Дискриминант меньше нуля.")
		a = 0
		b = 0
		c = 0

def schedule():
	function = other_func_entry.get()
	if "^" in function:
		messagebox.showinfo("Error", "Пишите знак степени так - **")
	else:
		fig, ax = plt.subplots()
		x = np.linspace(-10, 10, 100)
		y = eval(function)
		ax.plot(x, y)
		plt.grid()
		plt.show()


quadratic_equation = Label(root, text="ax^2 + bx + c = 0", font="1")
quadratic_equation.place(x=60, y=0)

a_label = Label(root, text="a =", font=1)
a_label.place(x=60, y=25)

b_label = Label(root, text="b =", font=1)
b_label.place(x=60, y=55)

c_label = Label(root, text="c =", font=1)
c_label.place(x=60, y=85)

a_entry = Entry(root)
a_entry.place(x=85, y=30)

b_entry = Entry(root)
b_entry.place(x=85, y=60)

c_entry = Entry(root)
c_entry.place(x=85, y=85)

button_answers = Button(root, text="Получить ответы", command=ckicked, width = 17)
button_answers.place(x=85, y=110)

button_other_func = Button(root, text="Получить график", command = schedule)
button_other_func.place(x=85, y=170)

other_func_entry = Entry(root, width=20)
other_func_entry.place(x=85, y=145)

root.geometry("450x250")
root.title("Discriminant")

root.mainloop()

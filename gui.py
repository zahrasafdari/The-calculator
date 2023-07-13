import tkinter as tk
from tkinter import *
from .main import calculator

class InputFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # --------------New
        self.history_list = []
        self.expression = ''
        self.new_expression = ''
        self.count = 1
        self.history_status = "close"
        self.his_root = None
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(
            self.parent, font=('arial', 18, 'bold'), textvariable=self.input_text,
            width=37, bg="white", borderwidth=0)
        self.input_field.focus()
        self.input_field.grid(row=0, column=0)
        # 'ipady' is internal padding to increase the height of input field
        self.input_field.pack(ipady=8)

    def btn_click(self, item):
        cursor_position = self.input_field.index(tk.INSERT)
        expression = self.input_field.get()
        expression = expression[:cursor_position] + \
            str(item) + expression[cursor_position:]
        self.input_text.set(expression)
        self.input_field.icursor(cursor_position + 1)
        # print(cursor_position)

    def btn_function_click(self, item):
        s = str(item) + '()'
        expression = self.input_field.get()
        cursor_position = self.input_field.index(tk.INSERT)
        expression = expression[:cursor_position] + \
            s + expression[cursor_position:]
        self.input_text.set(expression)
        self.input_field.icursor(cursor_position + len(s) - 1)

    def bt_clear(self):
        self.input_text.set("")

    # -----------------New
    def del_button(self):
        cursor_position = self.input_field.index(tk.INSERT)
        first = str(self.input_text.get())
        second = list(first)
        third = second[:cursor_position - 1] + second[cursor_position:]
        fourth = ''.join(third)
        self.input_text.__del__()
        self.input_text.set(fourth)
        self.input_field.icursor(cursor_position - 1)

    # -----------------
    def cursor_previous(self):
        cursor_position = self.input_field.index(tk.INSERT)
        self.input_field.icursor(cursor_position - 1)

    def cursor_next(self):
        cursor_position = self.input_field.index(tk.INSERT)
        self.input_field.icursor(cursor_position + 1)

    def bt_equal(self, ):

        self.expression = self.input_field.get()
        self.new_expression = str(self.expression)  # --new
        result = calculator(self.expression)
        self.expression = ''
        if result[0] != 0:
            self.expression += str(result[0])
        if result[0] != 0 and result[1] != 0 and result[1] > 0:
            self.expression += '+'
        if result[1] != 0:
            self.expression += str(result[1])
        if result[0] == 0 and result[1] == 0:
            self.expression += '0'
        self.input_text.set(self.expression)
        self.history_list.append(
            f"({self.count}) {self.new_expression}={self.expression}")
        self.count += 1  # counting the number of history labels

    # History window
    def history(self):
        self.his_root = tk.Tk()
        self.his_root.title("Calculator History")
        self.his_root.geometry("630x550")
        self.his_root.resizable(0, 0)
        self.his_root.configure(bg='gray')
        scroll_1 = tk.Scrollbar(self.his_root)
        scroll_2 = tk.Scrollbar(self.his_root, orient=HORIZONTAL)

        mylist = Listbox(self.his_root, yscrollcommand=scroll_1.set, bg="#919993", fg="white",
                         width=55, height=20, bd=0, font=('arial', 15, 'bold'))

        for his in self.history_list[::-1]:
            mylist.insert(END, his)
        scroll_1.config(command=mylist.yview)
        scroll_2.config(command=mylist.xview)
        scroll_2.pack(side=BOTTOM, fill=X)
        mylist.pack(side=LEFT)
        scroll_1.pack(side=RIGHT, fill=Y)


class ButtonFrame(tk.Frame):
    def __init__(self, parent, input_frame, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.input_frame = input_frame
        self.parent = parent
        # first row
        self.clear = tk.Button(
            self, text="C", fg="black", width=5, height=2, bd=-5, bg="#827875", cursor="hand2",
            font=('arial', 15, 'bold'),
            command=lambda: self.input_frame.bt_clear()
        ).grid(row=0, column=0, padx=1, pady=1)
        self.previous = tk.Button(
            self, text="\u23ea", fg="black", width=5, height=2, bd=-5, bg="#827875", cursor="hand2",
            font=('arial', 15, 'bold'),
            command=lambda: self.input_frame.cursor_previous()
        ).grid(row=0, column=1, padx=1, pady=1)
        self.before = tk.Button(
            self, text="\u23e9", fg="black", width=5, height=2, bd=-5, bg="#827875", cursor="hand2",
            font=('arial', 15, 'bold'),
            command=lambda: self.input_frame.cursor_next()
        ).grid(row=0, column=2, padx=1, pady=1)

        self.divide = tk.Button(
            self, text="\u2797", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click("\u00f7")
        ).grid(row=0, column=3, padx=1, pady=1)
        self.open = tk.Button(
            self, text="(", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click("(")
        ).grid(row=0, column=4, padx=1, pady=1)
        self.close = tk.Button(
            self, text=")", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(")")
        ).grid(row=0, column=5, padx=1, pady=1)

        # second row

        self.seven = tk.Button(
            self, text="7", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(7)
        ).grid(row=1, column=0, padx=1, pady=1)
        self.eight = tk.Button(
            self, text="8", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(8)
        ).grid(row=1, column=1, padx=1, pady=1)
        self.nine = tk.Button(
            self, text="9", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(9)
        ).grid(row=1, column=2, padx=1, pady=1)
        self.multiply = tk.Button(
            self, text="\u2716", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click("*")
        ).grid(row=1, column=3, padx=1, pady=1)
        self.sin = tk.Button(
            self, text="sin", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("sin")
        ).grid(row=1, column=4, padx=1, pady=1)
        self.cos = tk.Button(
            self, text="cos", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("cos")
        ).grid(row=1, column=5, padx=1, pady=1)

        # third row

        self.four = tk.Button(
            self, text="4", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(4)
        ).grid(row=2, column=0, padx=1, pady=1)
        self.five = tk.Button(
            self, text="5", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(5)
        ).grid(row=2, column=1, padx=1, pady=1)
        self.six = tk.Button(
            self, text="6", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(6)
        ).grid(row=2, column=2, padx=1, pady=1)
        self.minus = tk.Button(
            self, text="\u2796", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click("-")
        ).grid(row=2, column=3, padx=1, pady=1)
        self.tan = tk.Button(
            self, text="tan", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("tan")
        ).grid(row=2, column=4, padx=1, pady=1)
        self.cot = tk.Button(
            self, text="cot", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("cot")
        ).grid(row=2, column=5, padx=1, pady=1)

        # fourth row

        self.one = tk.Button(
            self, text="1", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(1)
        ).grid(row=3, column=0, padx=1, pady=1)
        self.two = tk.Button(
            self, text="2", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(2)
        ).grid(row=3, column=1, padx=1, pady=1)
        self.three = tk.Button(
            self, text="3", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(3)
        ).grid(row=3, column=2, padx=1, pady=1)
        self.plus = tk.Button(
            self, text="\u2795", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click("+")
        ).grid(row=3, column=3, padx=1, pady=1)
        self.log = tk.Button(
            self, text="log", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("log")
        ).grid(row=3, column=4, padx=1, pady=1)
        self.ln = tk.Button(
            self, text="ln", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("ln")
        ).grid(row=3, column=5, padx=1, pady=1)

        # fifth row

        self.zero = tk.Button(
            self, text="0", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", cursor="hand2",
            font=('arial', 15, 'bold'),
            command=lambda: self.input_frame.btn_click(0)
        ).grid(row=4, column=0, columnspan=1, padx=1, pady=1)
        self.delete = tk.Button(
            self, text="\u232B", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", cursor="hand2",
            font=('arial', 15, 'bold'),
            command=lambda: self.input_frame.del_button()
        ).grid(row=4, column=1, columnspan=1, padx=1, pady=1)
        self.point = tk.Button(
            self, text=".", fg="black", width=5, height=2, bd=-5, bg="#a9a9a9", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click(".")
        ).grid(row=4, column=2, padx=1, pady=1)
        self.equals = tk.Button(
            self, text="=", fg="black", width=5, height=2, bd=-5, bg="cyan", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.bt_equal()
        ).grid(row=4, column=3, padx=1, pady=1)
        self.pi = tk.Button(
            self, text="\u03C0", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click("\u03C0")
        ).grid(row=4, column=4, padx=1, pady=1)
        self.i = tk.Button(
            self, text="^", fg="black", width=5, height=2, bd=-5, bg="#827875", font=('arial', 15, 'bold'),
            cursor="hand2", command=lambda: self.input_frame.btn_click("^")
        ).grid(row=4, column=5, padx=1, pady=1)

        self.history = tk.Button(
            self, text='History', fg="black", width=8, height=20, bd=0, bg="#827875", font=('arial', 10, 'bold'),
            command=lambda: self.input_frame.history()
        ).grid(row=0, column=6, rowspan=5)


def run_gui():
    root = tk.Tk()
    root.geometry("480x375")
    root.resizable(0, 0)
    root.title("Calculator")
    root.configure(bg="white")
    input_frame = InputFrame(
        root, bd=-20,
        highlightbackground="black", highlightcolor="black",
        highlightthickness=2
    )
    input_frame.pack(side=tk.TOP)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="length", command=lambda: openlength())
    menubar.add_cascade(label="other calculators", menu=filemenu)
    root.config(menu=menubar)

    def openlength():
        unit_dict = {
            "cm": 0.01,
            "m": 1.0,
            "km": 1000.0,
            "feet": 0.3048,
            "miles": 1609.344,
            "inches": 0.0254
        }

        lengths = ["cm", "m", "km", "feet", "miles", "inches"]
        # Options for drop-down menu
        OPTIONS = ["select units",
                   "cm",
                   "m",
                   "km",
                   "feet",
                   "miles",
                   "inches"]

        root2 = tk.Tk()
        root2.geometry("400x350")
        root2.resizable(0,0)
        root2.title("length Converter")
        root2['bg'] = 'gray'

        def ok():
            inp = float(inputentry.get())
            inp_unit = inputopt.get()
            out_unit = outputopt.get()

            cons = [inp_unit in lengths and out_unit in lengths]
            if any(cons):
                outputentry.delete(0, END)
                outputentry.insert(
                    0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))


        canvas = tk.Canvas(root2, bg='#a4aba6', bd=0,
                           highlightthickness=0, height=400)
        canvas.pack(padx=15, pady=30)

        inputlabel = Label(canvas, text='Enter the length:')
        inputlabel.grid(row=1, column=0, padx=4, pady=4)

        inputentry = Entry(canvas, font="bold",justify=CENTER)
        inputentry.grid(row=1, column=1, padx=4, pady=4)

        inputopt = tk.StringVar()
        inputopt.set(OPTIONS[0])
        inputmenu = tk.OptionMenu(root2, inputopt, *OPTIONS)
        inputmenu.place(x=90, y=100)

        tolabel = Label(root2, text='to', height=1, width=2)
        tolabel.place(x=210, y=105)

        outputopt = tk.StringVar()
        outputopt.set(OPTIONS[0])
        outputmenu = tk.OptionMenu(root2, outputopt, *OPTIONS)
        outputmenu.place(x=245, y=100)

        convertlabel = Label(root2, text='The converted number:')
        convertlabel.place(x=50, y=200)

        outputentry = Entry(root2, font="bold",justify=CENTER)
        outputentry.place(x=180, y=200)

        okbtn = Button(root2, text="Result", command=lambda: ok(), width=18)
        okbtn.place(x=150, y=150)

    btn_frame = ButtonFrame(root, input_frame=input_frame, bg="white")
    btn_frame.pack()
    root.mainloop()

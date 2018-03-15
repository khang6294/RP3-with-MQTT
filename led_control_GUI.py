from tkinter import *
from mqtt_publisher import *

window = Tk()
window.wm_title("Control LED by GUI")


def conled1_command():
    def turn_on():
        input1 = "on"
        mqtt_connect(input1)

    def turn_off():
        input1 = "off"
        mqtt_connect(input1)

    def increase_speed():
        input1 = "increase_speed"
        mqtt_connect(input1)

    def quit_win():
        top.destroy()
        b1.config(state='normal')
        b2.config(state='normal')
        b3.config(state='normal')
        b4.config(state='normal')
    top = Toplevel()
    top.wm_title = "Control LED1"
    b1.config(state='disable')
    b2.config(state='disable')
    b3.config(state='disable')
    b4.config(state='disable')
    b1_1=Button(top,text="Turn on",width=15,command=turn_on)
    b1_1.grid(row=0,column=0)
    b1_2=Button(top,text="Turn off",width=15,command=turn_off)
    b1_2.grid(row=0,column=1)
    b1_3=Button(top,text="Increase speed",width=15,command=increase_speed)
    b1_3.grid(row=1,column=0)
    b1_4=Button(top,text="Close",width=15,command=quit_win)
    b1_4.grid(row=1,column=1)
    top.protocol("WM_DELETE_WINDOW", quit_win)


def conled2_command():
    def turn_on():
        input1 = "on"
        mqtt_connect(input1)

    def turn_off():
        input1 = "off"
        mqtt_connect(input1)

    def increase_speed():
        input1 = "increase_speed"
        mqtt_connect(input1)

    def quit_win():
        top.destroy()
        b1.config(state='normal')
        b2.config(state='normal')
        b3.config(state='normal')
        b4.config(state='normal')
    top = Toplevel()
    top.wm_title = "Control LED1"
    b1.config(state='disable')
    b2.config(state='disable')
    b3.config(state='disable')
    b4.config(state='disable')
    b1_1 = Button(top,text="Turn on",width=15,command=turn_on)
    b1_1.grid(row=0,column=0)
    b1_2 = Button(top,text="Turn off",width=15,command=turn_off)
    b1_2.grid(row=0,column=1)
    b1_3 = Button(top,text="Increase speed",width=15,command=increase_speed)
    b1_3.grid(row=1,column=0)
    b1_4 = Button(top,text="Close",width=15,command=quit_win)
    b1_4.grid(row=1,column=1)
    top.protocol("WM_DELETE_WINDOW", quit_win)

b1 = Button(window,text="Control LED1",width=15,command=conled1_command)
b1.grid(row=0, column=0)

b2 = Button(window,text="Info",width=15)
b2.grid(row=1, column=0)

b3 = Button(window, text="Control LED2", width=15,command=conled2_command)
b3.grid(row=0, column=1)

b4 = Button(window, text="Exit", width=15,command=window.destroy)
b4.grid(row=1, column=1)

window.mainloop()
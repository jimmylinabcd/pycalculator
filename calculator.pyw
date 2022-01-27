#! python3
import tkinter as tk
import re
window = tk.Tk()
window.geometry("350x550")
window.resizable(0,0)
window.title("Calculator")
try:
    window.iconphoto(False, tk.PhotoImage(file="icon.png"))
except:
    print("Icon image could not be loaded.")
window.configure(background="#768088")
digits = 0
temp = ""
equals = 0
#numbers
def num(i):
    global equals
    if equals == 1:
        allclear.invoke()
        equals = 0
    screen.insert(tk.INSERT,i)
    global digits
    digits += 1
    screen.xview_moveto(1) 
#functions
def symbol(i):
    global equals
    equals = 0
    global digits
    if digits > 0:
        screen.insert(tk.INSERT,i)
        digits += 1
        screen.xview_moveto(1)
    elif i == "-":
        screen.insert(tk.INSERT,i)
        digits += 1
        screen.xview_moveto(1)
def exponent():
    global equals
    equals = 0
    global digits
    if digits > 0:
        screen.insert(tk.INSERT,"\u00b2")
        digits += 1
        screen.xview_moveto(1)
def brackets():
    global equals
    equals = 0
    global digits
    screen.insert(tk.INSERT,"()")
    digits += 2
    screen.icursor(screen.index(tk.INSERT) - 1)
def allclear():
    global equals
    equals = 0
    try:
        for i in range(10):
            window.unbind(str(i))
    except:
        pass
    screen.delete(0, "end")
    global digits
    digits = 0
def delete():
    global equals
    equals = 0
    global digits
    if screen.index(tk.INSERT) == 0:
        screen.delete(0,screen.index(tk.INSERT)+1)
    else:
        screen.delete(screen.index(tk.INSERT)-1,tk.INSERT)
def fix():
    global equals
    equals = 0
    global temp
    temp = screen.get()
    temp = re.sub("[^0-9-+*/%()÷×.=²]+","",temp)
def equal():
    global digits
    if digits > 0:
        try:
            fix()
            global temp
            temp=temp.replace("×","*").replace("÷","/").replace("()","").replace("\u00b2","**2 ") 
            temp = re.sub(r"([+-/])\1+", r"\1", temp)
            temp = re.sub("[-+÷×*/.]+$", "",temp)
            screen.delete(0, "end")
            ans.configure(text="Ans = " + str(eval(temp)))
            screen.insert(0,eval(temp))
            digits = len(screen.get())
            screen.xview_moveto(0)
        except ZeroDivisionError: 
            screen.delete(0, "end")
            digits = 0
            screen.insert(0,"ZeroDivisionError")
            screen.xview_moveto(1)
        except:
            screen.delete(0, "end")
            digits = 0
            screen.insert(0,"error")
            screen.xview_moveto(1)
        global equals
        equals = 1
        for i in range(10):
            window.bind(str(i), equalss)
def equalss(event):
    global equals
    if equals == 1:
        allclear.invoke()
        screen.insert(0,event.char)
def key(event):
    fix()
    global digits
    global temp
    temp=temp.replace("*","×")
    temp=temp.replace("/","÷")
    temp = re.sub(r"([÷+-])\1+", r"\1", temp)
    if digits == 0:
        temp = re.sub("[+÷×.]","",temp)
    screen.delete(0,tk.END)
    screen.insert(0,temp)
    digits = len(screen.get())
    if event.char == "=":
        delete.invoke()
        equal.invoke()
    elif event.char == "\r":
        equal.invoke()
    elif event.keycode == 46:
        delete.invoke()
    elif event.keysym == "Left" or "Right":
        screen.xview_moveto(screen.index(tk.INSERT)/ 1000)
            

screen = tk.Entry(window,width = 312,font=("arial", 30, "bold"),justify="right")
ans = tk.Label(window,text="",font=("arial", 10),fg="#d3d3d3",bg="#ffffff")

#row 1
allclear = tk.Button(window,text="AC", command=allclear, fg ="#FF5733",bg = "#33D7FF")
delete = tk.Button(window, text="Del", command=delete,bg = "#33D7FF")
exponent = tk.Button(window, text="x\u00b2", command=exponent,bg = "#33D7FF")
brackets = tk.Button(window, text="( )", command=brackets,bg = "#33D7FF")
#row 2
num1 = tk.Button(window,text="1", command = lambda :num(1),bg="#ffffff")
num2 = tk.Button(window,text="2", command = lambda :num(2),bg="#ffffff")
num3 = tk.Button(window,text="3", command = lambda :num(3),bg="#ffffff")
multiply = tk.Button(window,text="×", command = lambda : symbol("×"),bg = "#33D7FF")
#row 3
num4 = tk.Button(window,text="4", command = lambda :num(4),bg="#ffffff")
num5 = tk.Button(window,text="5", command = lambda :num(5),bg="#ffffff")
num6 = tk.Button(window,text="6", command = lambda :num(6),bg="#ffffff")
divide = tk.Button(window,text="÷", command = lambda : symbol("÷"),bg = "#33D7FF")
#row 4
num7 = tk.Button(window,text="7", command = lambda :num(7),bg="#ffffff")
num8 = tk.Button(window,text="8", command = lambda :num(8),bg="#ffffff")
num9 = tk.Button(window,text="9", command = lambda :num(9),bg="#ffffff")
add = tk.Button(window,text="+", command = lambda : symbol("+"),bg = "#33D7FF")
#row 5
num0 = tk.Button(window,text="0", command = lambda :num(0),bg="#ffffff")
point = tk.Button(window,text=".", command = lambda : symbol("."),bg="#ffffff")
equal = tk.Button(window,text="=", command = equal,bg="#ffffff")
minus  = tk.Button(window,text="-", command = lambda : symbol("-"),bg = "#33D7FF")

screen.place(relwidth = 1.0, relheight = 0.165)
ans.place(x="350",y="5",anchor="ne")
#row 1
allclear.place(relwidth = 0.25, relheight = 0.2, y = 90)
delete.place(relwidth = 0.25, relheight = 0.2, y = 90, x = 87)
exponent.place(relwidth = 0.25, relheight = 0.2, y = 90,x = 174)
brackets.place(relwidth = 0.25, relheight = 0.2, y = 90, x = 261)
#row 2
num1.place(relwidth = 0.25, relheight = 0.2, y = 180)
num2.place(relwidth = 0.25, relheight = 0.2, y = 180, x = 87)
num3.place(relwidth = 0.25, relheight = 0.2, y = 180,x = 174)
multiply.place(relwidth = 0.25, relheight = 0.2, y = 180, x = 261)
#row 3
num4.place(relwidth = 0.25, relheight = 0.2, y = 270)
num5.place(relwidth = 0.25, relheight = 0.2, y = 270, x = 87)
num6.place(relwidth = 0.25, relheight = 0.2, y = 270,x = 174)
divide.place(relwidth = 0.25, relheight = 0.2, y = 270, x = 261)
#row 4
num7.place(relwidth = 0.25, relheight = 0.2, y = 360)
num8.place(relwidth = 0.25, relheight = 0.2, y = 360, x = 87)
num9.place(relwidth = 0.25, relheight = 0.2, y = 360,x = 174)
add.place(relwidth = 0.25, relheight = 0.2, y = 360, x = 261)
#row 5
num0.place(relwidth = 0.25, relheight = 0.2, y = 450)
point.place(relwidth = 0.25, relheight = 0.2, y = 450, x = 87)
equal.place(relwidth = 0.25, relheight = 0.2, y = 450,x = 174)
minus.place(relwidth = 0.25, relheight = 0.2, y = 450, x = 261)

window.bind("<Key>",key)
window.bind("<Escape>", lambda e: window.destroy())
window.wm_attributes("-topmost", 1)
ans.lift()
screen.focus()
window.mainloop()

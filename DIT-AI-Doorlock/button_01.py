from tkinter import *

root=Tk()

root.title("GUI test")

root.geometry("800x450")

root.resizable(False,False)




def button_pressed(value):
    number_entry.insert("end",value) #텍스트 창으로 숫자 전송.'end'는 오른쪽끝에 추가하라는 의미.
    print(value,"pressed")

def clear(event):            # C 버튼과 Esc 키를 위한 함수 입니다.
    number_entry.delete(0, END)


entry_value = StringVar(root, value='')

number_entry = Entry(root, textvariable = entry_value, width=30)
number_entry.place(x=550, y=20)



btn1 = Button(root, text="1", width=7, height=4, command = lambda:button_pressed('1'))
btn1.place(x =550, y = 50)

btn2 = Button(root, text="2", width=7, height=4, command = lambda:button_pressed('2'))
btn2.place(x =630, y = 50)

btn3 = Button(root, text="3", width=7, height=4, command = lambda:button_pressed('3'))
btn3.place(x = 710, y = 50)

btn4 = Button(root, text="4", width=7, height=4, command = lambda:button_pressed('4'))
btn4.place(x = 550, y = 140)

btn5 = Button(root, text="5", width=7, height=4, command = lambda:button_pressed('5'))
btn5.place(x = 630, y = 140)

btn6 = Button(root, text="6", width=7, height=4, command = lambda:button_pressed('6'))
btn6.place(x = 710, y = 140)

btn7 = Button(root, text="7", width=7, height=4, command = lambda:button_pressed('7'))
btn7.place(x = 550, y = 230)

btn8 = Button(root, text="8", width=7, height=4, command = lambda:button_pressed('8'))
btn8.place(x = 630, y = 230)

btn9 = Button(root, text="9", width=7, height=4, command = lambda:button_pressed('9'))
btn9.place(x = 710, y = 230)

btn10 = Button(root, text="-", width=7, height=4, command = lambda:button_pressed('-'))
btn10.place(x = 550, y = 320)

btn11 = Button(root, text="0", width=7, height=4, command = lambda:button_pressed('0'))
btn11.place(x = 630, y = 320)

btn12 = Button(root, text="지우기", width=7, height=4)
btn12.bind('<Button-1>',clear)
btn12.place(x = 710, y = 320)

root.bind('<Escape>', clear)

root.mainloop()
"""
    Tkinter, Pillow - 디스플레이

    최종 수정일 : 2021/08/07
    작성자 : 한규, 박주영
    최종 수정 내용 : 전체적인 코드에 주석 추가
"""
# 화면 구성을 위한 Tkinter
import tkinter as tk
from tkinter import END
from tkinter.tix import Tk
import tkinter.font as tkFont

import openWeatherMap # OpenWeatherMap.py 가져옴

from PIL import ImageTk, Image # 이미지 처리를 위한 Pillow
import cv2 as cv # 영상처리를 위한 OpenCV
import os

# 날짜와 시간을 가져오는 datatime / time
import datetime
import time
import json

text = openWeatherMap.city

"""

    함수및 이벤트 정의
    (Function and Event Definition)

"""


def transDay(day): # 숫자로 받아온 요일을 한글로 변경
    if day == 0:
        return "월"
    elif day == 1:
        return "화"
    elif day == 2:
        return "수"
    elif day == 3:
        return "목"
    elif day == 4:
        return "금"
    elif day == 5:
        return "토"
    else:
        return "일"

def getWeather(text): # 화면에 날씨를 나타내주는 부분

    now = time.localtime() # 오늘 날짜를 가져옴
    city = openWeatherMap.weather(text) # OpenWeatherMap.py애서 도시 이름을 가져옴

    # 화면에 나타낼 정보를 선언
    msg = f"""
{now.tm_year}-{now.tm_mon}-{now.tm_mday} / {transDay(now.tm_wday)}

도시 : {city[0]}

최저온도 : {city[2]}°C

최고온도 : {city[3]}°C

습도 : {city[4]}%

    날씨 : {city[1]}
            """

    label['text'] = msg
    win.update()

def add_Face(event): # 얼굴 등록 이벤트
    newf = tk.Tk() # 얼굴 등록 창을 만들어줌

    newf.title("Add Face") # 창의 이름을 Add Face로 설정
    newf.geometry('800x450+0+0') # 창의 크기를 800x450, 위치를 0,0으로 설정
    newf.resizable(False, False) # 창의 크기 변경 불가

    frm = tk.Frame(newf, bg="white", width=480, height=320)  # 프레임 너비, 높이 설정
    frm.place(x=20, y=40)  # 격자 행, 열 배치

    cap = cv.VideoCapture(0)  # VideoCapture 객체 정의

    def video_play():  # 카메라 화면을 불러오는 부분
        ret, frame = cap.read()  # 프레임이 올바르게 읽히면 ret은 True
        if not ret:
            cap.release()  # 작업 완료 후 해제
            return
        frame = cv.resize(frame, (480, 340)) # 영상의 크기를 480x340으로 조정
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) # BGR 방식을 RGB로 변환
        img = Image.fromarray(frame)  # Image 객체로 변환
        imgtk = ImageTk.PhotoImage(image=img, master=newf)  # ImageTk 객체로 변환 (master로 이미지가 사용될 창의 이름을 정해줘야함) -> 위에서 사용된 창의 이름은 newf
        # OpenCV 동영상
        lbl1.imgtk = imgtk
        lbl1.configure(image=imgtk) # image속성을 imgtk로 변경
        lbl1.after(10, video_play) # 10ms 이후에 video_play를 실행

    def captureFace(text):
        path = r'C:\Users\adwin\PycharmProjects\pythonProject\doorlock\ImageBasic'  # 사진 저장 위치 ( 자신의 위치로 바꿔줘야함 )

        text_eng = ["Mom", "Dad", "Child", "GrandMa", "GrandFa"]

        if text == '엄마':
            text = text_eng[0]
        elif text == '아빠':
            text = text_eng[1]
        elif text == '자녀':
            text = text_eng[2]
        elif text == '할머니':
            text = text_eng[3]
        elif text == '할아버지':
            text = text_eng[4]

        if text == "Child":
            text = "Child1"

        for i in range(0, 1):
            success, cap_img = cap.read() # 프레임을 가져옴

            img = text + '.jpg'  # 일단 임시로 파일 이름은 시간으로 정해줌

            cv.imwrite(os.path.join(path, img), cap_img) # 이미지 저장

    capBtn = tk.Button(newf, text="엄마", height=5, width=9, command = lambda: captureFace(capBtn['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn.place(x=510, y=100)  # capBtn의 위치 설정

    capBtn1 = tk.Button(newf, text="아빠", height=5, width=9, command=lambda: captureFace(capBtn1['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn1.place(x=610, y=100)  # capBtn의 위치 설정

    capBtn2 = tk.Button(newf, text="자녀", height=5, width=9, command=lambda: captureFace(capBtn2['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn2.place(x=710, y=100)  # capBtn의 위치 설정

    capBtn3 = tk.Button(newf, text="할머니", height=5, width=9, command=lambda: captureFace(capBtn3['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn3.place(x=560, y=200)  # capBtn의 위치 설정

    capBtn4 = tk.Button(newf, text="할아버지", height=5, width=9, command=lambda: captureFace(capBtn4['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn4.place(x=660, y=200)  # capBtn의 위치 설정


    lbl1 = tk.Label(frm)
    lbl1.place(x=0, y=0)
    video_play() # video_play 실행
    newf.mainloop() # newf 창 활성화

def copy_phone_num(num):
    return num

def setting_win(event):
    snw = tk.Tk()
    snw.title("Phone Setting")
    snw.geometry('800x450+0+0')

    def button_pressed(value):
        number_entry.insert("end", value)  # 텍스트 창으로 숫자 전송.'end'는 오른쪽끝에 추가하라는 의미.
        print(value, "pressed")

    def clear(event):  # C 버튼과 Esc 키를 위한 함수 입니다.
        number_entry.delete(0, END)



    def save_phone(event):

        phone_num = number_entry.get()
        openWeatherMap.fb_phoneUp(phone_num)




    entry_value = tk.StringVar(snw, value='')

    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    lbl1 = tk. Label(snw, text="010을 제외한 8자리를 입력해주세요!", font=fontStyle)
    lbl1.place(x=180, y = 60, width=300, height=40)

    number_entry = tk.Entry(snw, textvariable=entry_value)
    number_entry.place(x=200, y=120, width=260, height=30)

    btn1 = tk.Button(snw, text="1", width=7, height=4, command=lambda: button_pressed('1'))
    btn1.place(x=550, y=70)

    btn2 = tk.Button(snw, text="2", width=7, height=4, command=lambda: button_pressed('2'))
    btn2.place(x=630, y=70)

    btn3 = tk.Button(snw, text="3", width=7, height=4, command=lambda: button_pressed('3'))
    btn3.place(x=710, y=70)

    btn4 = tk.Button(snw, text="4", width=7, height=4, command=lambda: button_pressed('4'))
    btn4.place(x=550, y=160)

    btn5 = tk.Button(snw, text="5", width=7, height=4, command=lambda: button_pressed('5'))
    btn5.place(x=630, y=160)

    btn6 = tk.Button(snw, text="6", width=7, height=4, command=lambda: button_pressed('6'))
    btn6.place(x=710, y=160)

    btn7 = tk.Button(snw, text="7", width=7, height=4, command=lambda: button_pressed('7'))
    btn7.place(x=550, y=250)

    btn8 = tk.Button(snw, text="8", width=7, height=4, command=lambda: button_pressed('8'))
    btn8.place(x=630, y=250)

    btn9 = tk.Button(snw, text="9", width=7, height=4, command=lambda: button_pressed('9'))
    btn9.place(x=710, y=250)

    btn10 = tk.Button(snw, text="저장", width=7, height=4)
    btn10.bind('<Button-1>', save_phone)
    btn10.place(x=550, y=340)

    btn11 = tk.Button(snw, text="0", width=7, height=4, command=lambda: button_pressed('0'))
    btn11.place(x=630, y=340)

    btn12 = tk.Button(snw, text="지우기", width=7, height=4)
    btn12.bind('<Button-1>', clear)
    btn12.place(x=710, y=340)

    # snw.bind('<Escape>', clear)



def new_win(event):  # 설정 부분 새창을 만들어줌
    nw = tk.Tk()
    nw.title("Setting")
    nw.geometry('800x450+0+0')

    # select_city = tkinter.ttk.Combobox(nw, height=5, values=c_kor_arr)
    # select_city.grid(row=2, column=0)

    c_kor_arr = ["서울", "인천", "대전", "대구", "광주", "울산"]

    # 콤보박스가 잘 안되서 일단 버튼으로 만듬

    """ 도시 버튼 클릭시 이벤트 (최적화 예정) """

    def onClick(text):
        a = []
        b = []
        num = 0

        with open('./city_name.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
            a = json_data

        with open('./city_name_eng.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
            b = json_data

        def cityKorToEng(a, b, city):

            for i in range(0, len(a)):
                if a[i] == city:
                    print(b[i])
                    nw.destroy()
                    getWeather(b[i])
                    win.destroy()
                    os.system(r'C:\Users\adwin\PycharmProjects\pythonProject\doorlock\tkinter_part.py')

        cityKorToEng(a, b, text)


    # 설정에서 도시이름 붙여줌
    btn1 = tk.Button(nw, text="울산", width=10, height=5, command = lambda: onClick(btn1['text']))
    btn1.place(x=50, y=30)

    btn2 = tk.Button(nw, text="부산", width=10, height=5, command = lambda: onClick(btn2['text']))
    btn2.place(x=150, y=30)

    btn3 = tk.Button(nw, text="대구", width=10, height=5, command = lambda: onClick(btn3['text']))
    btn3.place(x=250, y=30)

    btn4 = tk.Button(nw, text="원주", width=10, height=5, command = lambda: onClick(btn4['text']))
    btn4.place(x=350, y=30)

    btn5 = tk.Button(nw, text="마산", width=10, height=5, command = lambda: onClick(btn5['text']))
    btn5.place(x=450, y=30)

    btn6 = tk.Button(nw, text="진주", width=10, height=5, command = lambda: onClick(btn6['text']))
    btn6.place(x=550, y=30)

    btn7 = tk.Button(nw, text="광주", width=10, height=5, command = lambda: onClick(btn7['text']))
    btn7.place(x=650, y=30)

    btn8 = tk.Button(nw, text="제주", width=10, height=5, command = lambda: onClick(btn8['text']))
    btn8.place(x=50, y=130)

    btn9 = tk.Button(nw, text="춘천", width=10, height=5, command = lambda: onClick(btn9['text']))
    btn9.place(x=150, y=130)

    btn10 = tk.Button(nw, text="포항", width=10, height=5, command = lambda: onClick(btn10['text']))
    btn10.place(x=250, y=130)

    btn11 = tk.Button(nw, text="천안", width=10, height=5, command = lambda: onClick(btn11['text']))
    btn11.place(x=350, y=130)

    btn12 = tk.Button(nw, text="군산", width=10, height=5, command = lambda: onClick(btn12['text']))
    btn12.place(x=450, y=130)

    btn13 = tk.Button(nw, text="목포", width=10, height=5, command = lambda: onClick(btn13['text']))
    btn13.place(x=550, y=130)

    btn14 = tk.Button(nw, text="전주", width=10, height=5, command = lambda: onClick(btn14['text']))
    btn14.place(x=650, y=130)

    btn15 = tk.Button(nw, text="여수", width=10, height=5, command = lambda: onClick(btn15['text']))
    btn15.place(x=50, y=230)

    btn16 = tk.Button(nw, text="속초", width=10, height=5, command = lambda: onClick(btn16['text']))
    btn16.place(x=150, y=230)

    btn17 = tk.Button(nw, text="강릉", width=10, height=5, command = lambda: onClick(btn17['text']))
    btn17.place(x=250, y=230)

    btn18 = tk.Button(nw, text="순천", width=10, height=5, command = lambda: onClick(btn18['text']))
    btn18.place(x=350, y=230)

    btn19 = tk.Button(nw, text="경주", width=10, height=5, command = lambda: onClick(btn19['text']))
    btn19.place(x=450, y=230)

    btn20 = tk.Button(nw, text="삼척", width=10, height=5, command = lambda: onClick(btn20['text']))
    btn20.place(x=550, y=230)

    btn21 = tk.Button(nw, text="여주", width=10, height=5, command = lambda: onClick(btn21['text']))
    btn21.place(x=650, y=230)

    btn22 = tk.Button(nw, text="의정부", width=10, height=5, command = lambda: onClick(btn22['text']))
    btn22.place(x=50, y=330)

    btn23 = tk.Button(nw, text="대전", width=10, height=5, command = lambda: onClick(btn23['text']))
    btn23.place(x=150, y=330)

    btn24 = tk.Button(nw, text="수원", width=10, height=5, command = lambda: onClick(btn24['text']))
    btn24.place(x=250, y=330)

    btn25 = tk.Button(nw, text="서울", width=10, height=5, command = lambda: onClick(btn25['text']))
    btn25.place(x=350, y=330)

    btn26 = tk.Button(nw, text="광주", width=10, height=5, command = lambda: onClick(btn26['text']))
    btn26.place(x=450, y=330)

    btn27 = tk.Button(nw, text="인천", width=10, height=5, command = lambda: onClick(btn27['text']))
    btn27.place(x=550, y=330)

    btn28 = tk.Button(nw, text="창원", width=10, height=5, command = lambda: onClick(btn28['text']))
    btn28.place(x=650, y=330)

    nw.mainloop()


""" 

    디스플레이 화면
    (Display)

"""

win = tk.Tk()  # 창을 하나 만들어줌

win.title("AI DoorLock")  # 창의 이름을 AI DoorLock으로 설정
win.geometry("800x450+0+0")  # 창의 크기를 800x450으로 창의 위치를 0, 0으로 설정
win.resizable(False, False)  # 사이즈 변경 불가


lower_frame = tk.Frame(win, bg='#80c1ff', bd=10) # 날씨 정보를 나타내줄 프레임 생성
label = tk.Label(lower_frame, font=("휴먼매직체", 13)) # 라벨을 프레임에 붙혀줌


btn1 = tk.Button(win, text="얼굴 등록", height=5, width=30) # 메인 화면에 얼굴 등록 버튼 생성
btn1.place(x=20, y=50) # 얼굴 등록 버튼 위치 설정
btn1.bind("<Button-1>", add_Face) # 얼굴 등록 버튼 이벤트 설정
btn2 = tk.Button(win, text="등록된 얼굴 검색", height=5, width=30) # 메인화면에 얼굴 검색 버튼 생성
btn2.place(x=20, y=185) # 얼굴 검색 버튼 위치 설정
# btn2.bind("<Button-1>", listFace)

lower_frame.place(relx=0.8, rely=0.09, relwidth=0.3, relheight=0.8, anchor='n') # 날씨 정보 프레임의 크기와 위치 설정
label.place(relwidth=1, relheight=1) # 라벨의 위치 설정

newWin = tk.Button(win, text="설정", height=5, width=30) # 메인화면에 설정 버튼 생성
newWin.place(x=20, y=320) # 설정 버튼 위치 설정
newWin.bind("<Button-1>", new_win) # 설정 버튼 이벤트 설정

setting = tk.Button(win, text="전화번호 설정", height=5, width=30)
setting.place(x=270, y=320)
setting.bind("<Button-1>", setting_win)


getWeather(text) # getWeather 실행










# 라벨1 추가


win.mainloop()  # GUI 시작

# os.system("C:/Users/adwin/PycharmProjects/pythonProject/AI_DoorLock/face_recognition1.py")


# def listFace(event):
#     listf = tk.Tk()
#
#     listf.title("List Face")
#     listf.geometry('800x450+0+0')
#     listf.resizable(False, False)
#
#     path='ImageBasic'
#     myList = os.listdir(path)
#
#     # img1 = ImageTk.PhotoImage(file='./ImageBasic/hangyu.jpg', master=listf)
#     # img2 = Image.open('./ImageBasic/hangyu.jpg')
#     # img2 = img2.resize((100, 100))
#     # img2.save('test.jpg')
#     # lb1 = tk.Label(listf, image=img2)
#     # lb1.place(x=10, y=10)
#
#
#
#     for j in (0, len(myList)-1):
#         # img0 = Image.open(f'./ImageBasic/{myList[j]}')
#         # img0 = img0.resize((200, 200))
#         # img0.save(f'./saveImg/{myList[j]}')
#
#         # image0 = ImageTk.PhotoImage(file='./saveImg/hangyu.jpg', master=listf)
#         globals()['image{}'.format(j)] = ImageTk.PhotoImage(file=f'saveImg/{myList[j]}', master=listf)
#         globals()['label{}'.format(j)] = tk.Label(listf, image=f'image{j}')
#         globals()['label{}'.format(j)].pack()
#         #
#         # lb0 = tk.Label(listf, image=image0)
#         # lb0.pack()
#
#     listf.mainloop()
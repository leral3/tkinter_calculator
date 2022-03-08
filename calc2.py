from tkinter import *  # import tkinter 과의 차이는 사용법상으로 모듈 이름을 계속 붙여주느냐 아니냐의 차이입니다. 
                       # 만약에 import 모듈 했으면 모듈.매서드() 이런식으로 계속 작성해야하지만, from 모듈 import * 이렇게라면 매서드() 이렇게만 써주면 된다. 
from tkinter import ttk  # 기존 Tk() 클래스보다 그래픽이 개선 되었다. 


# 함수를 추가할 부분 

def button_pressed(value):
    number_entry.insert("end", value)    # 텍스트 창으로 숫자 전송.. 'end'는 오른쪽 끝에 추가하라는 의미
    print(value, "pressed")


root = Tk()
root.title("Calculator")
root.geometry("250x200")   # 버튼 크기에 맞출 것


# 인터페이스 (버튼, 창) 추가할 부분

# 텍스트창의 값 저장할 변수. 

entry_value = StringVar(root, value = '')


# 숫자 및 결과 표시창. 
# textvariable 속성으로 변수 설정. 

number_entry = ttk.Entry(root, textvariable= entry_value, width = 20)  # width = 20 초기에는 이렇게 되어 있었다. 
number_entry.grid(row = 0, columnspan= 3)                              # columnspan 은 여러칸에 걸쳐서 표시함 


# 숫자 버튼.
# command = lambda : 뒤에 명령 작성. 

# button 9개 추가

button7 = ttk.Button(root, text = "7", command = lambda : button_pressed("7"))
button7.grid(row = 1, column = 0)
button8 = ttk.Button(root, text = "8", command = lambda : button_pressed("8"))
button8.grid(row = 1, column = 1)
button9 = ttk.Button(root, text = "9", command = lambda : button_pressed("9"))
button9.grid(row = 1, column = 2)

button4 = ttk.Button(root, text = "4", command = lambda : button_pressed("4"))
button4.grid(row = 2, column = 0)
button5 = ttk.Button(root, text = "5", command = lambda : button_pressed("5"))
button5.grid(row = 2, column = 1)
button6 = ttk.Button(root, text = "6", command = lambda : button_pressed("6"))
button6.grid(row = 2, column = 2)

button1 = ttk.Button(root, text = '1', command = lambda : button_pressed("1"))
button1.grid(row = 3, column = 0)
button2 = ttk.Button(root, text = "2", command = lambda : button_pressed("2"))
button2.grid(row = 3, column = 1)
button3 = ttk.Button(root, text = "3", command = lambda : button_pressed("3"))
button3.grid(row = 3, column = 2)

root.mainloop()
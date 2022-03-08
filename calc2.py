from tkinter import *  # import tkinter 과의 차이는 사용법상으로 모듈 이름을 계속 붙여주느냐 아니냐의 차이입니다. 
                       # 만약에 import 모듈 했으면 모듈.매서드() 이런식으로 계속 작성해야하지만, from 모듈 import * 이렇게라면 매서드() 이렇게만 써주면 된다. 
from tkinter import ttk  # 기존 Tk() 클래스보다 그래픽이 개선 되었다. 


# 함수를 추가할 부분 


root = Tk()
root.title("Calculator")
root.geometry("200x200")


# 인터페이스 (버튼, 창) 추가할 부분

# 숫자 및 결과 표시창. 

number_entry = ttk.Entry(root, width = 20)
number_entry.grid(row = 0, columnspan= 1)


# 숫자 버튼.

button1 = ttk.Button(root, text = '1')
button1.grid(row = 1, column = 0)

root.mainloop()
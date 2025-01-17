"""
tkinter 计算器
"""

import math
import tkinter

root = tkinter.Tk()
root.resizable(width=False, height=False)  # 界面大小不可变
'''hype_parameter'''
IS_CALC = False  # 是否按下了运算符
STORAGE = []  # 存储数字
MAX_SHOW_LEN = 18  # 显示框最多显示多少个字符
CurrentShow = tkinter.StringVar()  # 当前显示的数字
CurrentShow.set('0')


def press_number(number):
    '''按下数字键(0-9)'''
    global IS_CALC
    if IS_CALC:
        CurrentShow.set('0')
        IS_CALC = False
    if CurrentShow.get() == '0':
        CurrentShow.set(number)
    else:
        if len(CurrentShow.get()) < MAX_SHOW_LEN:
            CurrentShow.set(CurrentShow.get() + number)


def press_dp():
    '''按下小数点'''
    global IS_CALC
    if IS_CALC:
        CurrentShow.set('0')
        IS_CALC = False
    if len(CurrentShow.get().split('.')) == 1:
        if len(CurrentShow.get()) < MAX_SHOW_LEN:
            CurrentShow.set(CurrentShow.get() + '.')


def clear_all():
    '''清零'''
    global STORAGE
    global IS_CALC
    STORAGE.clear()
    IS_CALC = False
    CurrentShow.set('0')


def clear_current():
    '''清除当前显示框内所有数字'''
    CurrentShow.set('0')


def del_one():
    '''删除显示框内最后一个数字'''
    global IS_CALC
    if IS_CALC:
        CurrentShow.set('0')
        IS_CALC = False
    if CurrentShow.get() != '0':
        if len(CurrentShow.get()) > 1:
            CurrentShow.set(CurrentShow.get()[:-1])
        else:
            CurrentShow.set('0')


def modify_result(result):
    '''计算答案修正'''
    result = str(result)
    if len(result) > MAX_SHOW_LEN:
        if len(result.split('.')[0]) > MAX_SHOW_LEN:
            result = 'Overflow'
        else:
            # 直接舍去不考虑四舍五入问题
            result = result[:MAX_SHOW_LEN]
    return result


def press_operator(operator):
    '''按下运算符'''
    global STORAGE
    global IS_CALC
    if operator == '+/-':
        if CurrentShow.get().startswith('-'):
            CurrentShow.set(CurrentShow.get()[1:])
        else:
            CurrentShow.set('-' + CurrentShow.get())
    elif operator == '1/x':
        try:
            result = 1 / float(CurrentShow.get())
        except:
            result = 'illegal operation'
        result = modify_result(result)
        CurrentShow.set(result)
        IS_CALC = True
    elif operator == 'sqrt':
        try:
            result = math.sqrt(float(CurrentShow.get()))
        except:
            result = 'illegal operation'
        result = modify_result(result)
        CurrentShow.set(result)
        IS_CALC = True
    # elif operator == 'MC':
    #     STORAGE.clear()
    # elif operator == 'MR':
    #     if IS_CALC:
    #         CurrentShow.set('0')
    #     STORAGE.append(CurrentShow.get())
    #     expression = ''.join(STORAGE)
    #     try:
    #         result = eval(expression)
    #     except:
    #         result = 'illegal operation'
    #     result = modifyResult(result)
    #     CurrentShow.set(result)
    #     IS_CALC = True
    # elif operator == 'MS':
    #     STORAGE.clear()
    #     STORAGE.append(CurrentShow.get())
    # elif operator == 'M+':
    #     STORAGE.append(CurrentShow.get())
    # elif operator == 'M-':
    #     if CurrentShow.get().startswith('-'):
    #         STORAGE.append(CurrentShow.get())
    #     else:
    #         STORAGE.append('-' + CurrentShow.get())
    elif operator in ['+', '-', '*', '/', '%']:
        STORAGE.append(CurrentShow.get())
        STORAGE.append(operator)
        IS_CALC = True
    elif operator == '=':
        if IS_CALC:
            CurrentShow.set('0')
        STORAGE.append(CurrentShow.get())
        expression = ''.join(STORAGE)
        try:
            result = eval(expression)
        # 除以0的情况
        except:
            result = 'illegal operation'
        result = modify_result(result)
        CurrentShow.set(result)
        STORAGE.clear()
        IS_CALC = True


def main():
    root.minsize(320, 420)
    root.title('Calculator')
    # 布局
    # --文本框
    label = tkinter.Label(root, textvariable=CurrentShow, bg='white',
                          anchor='e', bd=5, fg='black', font=('楷体', 20))
    label.place(x=20, y=50, width=280, height=50)
    # --第一行

    # # ----Memory clear
    # button1_1 = tkinter.Button(text='MC', bg='#F5F5F5', bd=2, command=lambda: press_operator('MC'))
    # button1_1.place(x=20, y=110, width=50, height=35)
    # # ----Memory read
    # button1_2 = tkinter.Button(text='MR', bg='#F5F5F5', bd=2, command=lambda: press_operator('MR'))
    # button1_2.place(x=77.5, y=110, width=50, height=35)
    # # ----Memory save
    # button1_3 = tkinter.Button(text='MS', bg='#F5F5F5', bd=2, command=lambda: press_operator('MS'))
    # button1_3.place(x=135, y=110, width=50, height=35)
    # # ----Memory +
    # button1_4 = tkinter.Button(text='M+', bg='#F5F5F5', bd=2, command=lambda: press_operator('M+'))
    # button1_4.place(x=192.5, y=110, width=50, height=35)
    # # ----Memory -
    # button1_5 = tkinter.Button(text='M-', bg='#F5F5F5', bd=2, command=lambda: press_operator('M-'))
    # button1_5.place(x=250, y=110, width=50, height=35)

    # --第二行
    # ----删除单个数字
    button2_1 = tkinter.Button(text='del', bg='#F5F5F5', bd=2, command=lambda: del_one())
    button2_1.place(x=20, y=155, width=50, height=35)
    # ----清除当前显示框内所有数字
    button2_2 = tkinter.Button(text='CE', bg='#F5F5F5', bd=2, command=lambda: clear_current())
    button2_2.place(x=77.5, y=155, width=50, height=35)
    # ----清零(相当于重启)
    button2_3 = tkinter.Button(text='C', bg='#F5F5F5', bd=2, command=lambda: clear_all())
    button2_3.place(x=135, y=155, width=50, height=35)
    # ----取反
    button2_4 = tkinter.Button(text='+/-', bg='#F5F5F5', bd=2, command=lambda: press_operator('+/-'))
    button2_4.place(x=192.5, y=155, width=50, height=35)
    # ----开根号
    button2_5 = tkinter.Button(text='sqrt', bg='#F5F5F5', bd=2, command=lambda: press_operator('sqrt'))
    button2_5.place(x=250, y=155, width=50, height=35)
    # --第三行
    # ----7
    button3_1 = tkinter.Button(text='7', bg='#bbbbbb', bd=2, command=lambda: press_number('7'))
    button3_1.place(x=20, y=200, width=50, height=35)
    # ----8
    button3_2 = tkinter.Button(text='8', bg='#bbbbbb', bd=2, command=lambda: press_number('8'))
    button3_2.place(x=77.5, y=200, width=50, height=35)
    # ----9
    button3_3 = tkinter.Button(text='9', bg='#bbbbbb', bd=2, command=lambda: press_number('9'))
    button3_3.place(x=135, y=200, width=50, height=35)
    # ----除
    button3_4 = tkinter.Button(text='/', bg='#808069', bd=2, command=lambda: press_operator('/'))
    button3_4.place(x=192.5, y=200, width=50, height=35)
    # ----取余
    button3_5 = tkinter.Button(text='%', bg='#808069', bd=2, command=lambda: press_operator('%'))
    button3_5.place(x=250, y=200, width=50, height=35)
    # --第四行
    # ----4
    button4_1 = tkinter.Button(text='4', bg='#bbbbbb', bd=2, command=lambda: press_number('4'))
    button4_1.place(x=20, y=245, width=50, height=35)
    # ----5
    button4_2 = tkinter.Button(text='5', bg='#bbbbbb', bd=2, command=lambda: press_number('5'))
    button4_2.place(x=77.5, y=245, width=50, height=35)
    # ----6
    button4_3 = tkinter.Button(text='6', bg='#bbbbbb', bd=2, command=lambda: press_number('6'))
    button4_3.place(x=135, y=245, width=50, height=35)
    # ----乘
    button4_4 = tkinter.Button(text='*', bg='#808069', bd=2, command=lambda: press_operator('*'))
    button4_4.place(x=192.5, y=245, width=50, height=35)
    # ----取导数
    button4_5 = tkinter.Button(text='1/x', bg='#808069', bd=2, command=lambda: press_operator('1/x'))
    button4_5.place(x=250, y=245, width=50, height=35)
    # --第五行
    # ----1
    button5_1 = tkinter.Button(text='1', bg='#bbbbbb', bd=2, command=lambda: press_number('1'))
    button5_1.place(x=20, y=290, width=50, height=35)
    # ----2
    button5_2 = tkinter.Button(text='2', bg='#bbbbbb', bd=2, command=lambda: press_number('2'))
    button5_2.place(x=77.5, y=290, width=50, height=35)
    # ----3
    button5_3 = tkinter.Button(text='3', bg='#bbbbbb', bd=2, command=lambda: press_number('3'))
    button5_3.place(x=135, y=290, width=50, height=35)
    # ----减
    button5_4 = tkinter.Button(text='-', bg='#808069', bd=2, command=lambda: press_operator('-'))
    button5_4.place(x=192.5, y=290, width=50, height=35)
    # ----等于
    button5_5 = tkinter.Button(text='=', bg='#808069', bd=2, command=lambda: press_operator('='))
    button5_5.place(x=250, y=290, width=50, height=80)
    # --第六行
    # ----0
    button6_1 = tkinter.Button(text='0', bg='#bbbbbb', bd=2, command=lambda: press_number('0'))
    button6_1.place(x=20, y=335, width=107.5, height=35)
    # ----小数点
    button6_2 = tkinter.Button(text='.', bg='#bbbbbb', bd=2, command=lambda: press_dp())
    button6_2.place(x=135, y=335, width=50, height=35)
    # ----加
    button6_3 = tkinter.Button(text='+', bg='#808069', bd=2, command=lambda: press_operator('+'))
    button6_3.place(x=192.5, y=335, width=50, height=35)
    root.mainloop()


if __name__ == '__main__':
    main()

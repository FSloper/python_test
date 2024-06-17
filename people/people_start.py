import tkinter
import tkinter.messagebox

import background_initialize as bi
import organ_initialize as oi

heart_weight = 0
# 心脏重量
left_atrium = 0
left_ventricle = 0
right_atrium = 0
right_ventricle = 0


class Archive(object):
    def __init__(self, goods, state):
        self.goods = goods
        self.state = state

    # 保存游戏数据，参数名与参数值
    def data_save(self):
        # TODO 使用数据库或json，xml保存游戏进度
        with open('people_data.json', 'w+') as file:
            f = (self.goods, self.state)
            f_list = f
            file.write(str(f_list))
            return 0

    def data_load(self):
        with open('people_data.json', 'r') as file:
            f_list = ()
            f_list = file.read()
            return f_list


def initialize_data():
    # 随机父母，出生地区，出生地，出生年月日
    bi.all_initialize()
    oi.all_initialize()


def main():
    # TODO 使用pygame、wxPython、PyQt、PyGTK增加图形化界面
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') \
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('960x540')
    # 设置窗口标题
    top.title('people')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    exit_game = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    exit_game.pack(side='right')
    panel.pack(side='bottom')
    # 创建一个装按钮的容器
    panel1 = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    continue_game = tkinter.Button(panel1, text='继续游戏', command=change_label_text)
    continue_game.pack(side='left')
    read_game = tkinter.Button(panel1, text='读取存档', command=Archive.data_save)
    read_game.pack(side='left')
    start_new_game = tkinter.Button(panel1, text='开始新游戏', command=initialize_data)
    start_new_game.pack(side='left')
    panel1.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()

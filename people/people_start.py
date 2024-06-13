import background_initialize as bi
import organ_initialize as oi

heart_weight = 0
# 心脏重量
left_atrium = 0
left_ventricle = 0
right_atrium = 0
right_ventricle = 0


# 保存游戏数据，参数名与参数值
def data_save(goods, state):
    # TODO 使用数据库或json，xml保存游戏进度
    with open('people_data.txt', 'w') as file:
        f = [goods, state]
        f_list = [f]
        file.write(str(f_list))


def data_load():
    with open('people_data.txt', 'r') as file:
        f_list = file.read()


def initialize_data():
    # 随机父母，出生地区，出生地，出生年月日
    bi.all_initialize()
    oi.all_initialize()


def main():
    # 获取当前窗口的宽度,返回元组xy
    # width = pyautogui.position()[0]
    # print(width)
    # print('请选择游戏进度：'.center(50, " "))
    print('1.继续上次存档')
    print('2.读取他人存档存档')
    print('3.删除存档重新开始')
    people_start = input("请输入：")
    if people_start == "1":
        # TODO:继续上次存档
        print('d')
    elif people_start == "2":
        # TODO:读取存档，拖入存档文件，回车进行加载。
        game_data = input('拖入存档文件，回车进行加载。')
    elif people_start == "3":
        initialize_data()
    elif people_start == "0":
        exit()
    else:
        print('输入有误，请出现选择')


if __name__ == '__main__':
    main()

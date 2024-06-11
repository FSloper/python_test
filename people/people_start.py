import organ_initialize as oi
import background_initialize as bi

heart_weight = 0
# 心脏重量
left_atrium = 0
left_ventricle = 0
right_atrium = 0
right_ventricle = 0


# 保存游戏数据，参数名与参数值
def data_save_txt(goods, state):
    with open('people_data.txt', 'w') as file:
        file.write(str(goods))
        file.write(' : ')
        file.write(str(state))


def initialize_data():
    # 随机父母，出生地区，出生地，出生年月日
    bi.all_initialize()
    oi.all_initialize()


if __name__ == '__main__':
    print('请选择游戏进度：')
    print('1.继续上次存档')
    print('2.读取他人存档存档')
    print('3.删除存档重新开始')
    people_start = input()
    if people_start == "1":
        # TODO:继续上次存档
        print('d')
    elif people_start == "2":
        # TODO:读取存档，拖入存档文件，回车进行加载。
        game_data = input('拖入存档文件，回车进行加载。')
    elif people_start == "3":
        initialize_data()

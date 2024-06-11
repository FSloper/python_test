import random


# 保存游戏数据，参数名与参数值
def data_save_txt(goods, state):
    with open('people_data.txt', 'w') as file:
        file.write(str(goods))
        file.write(' : ')
        file.write(str(state))


# 随机数据
def random_data(a, b):
    data = random.randrange(a, b + 1)
    return data


def all_initialize():
    print('All initialize')


def create_heart_data(heart_start, heart_end):
    heart_exist = random_data(heart_start, heart_end)
    # 先天性心脏病发病率千分之6，意味着大于457或小于503就发病
    if heart_exist >= 228 | heart_exist <= 257:
        print(heart_exist)
        if heart_exist == 250:
            print('先天性心脏病发病率千分之6左右，很不幸您夭折了')
        # 以下为隐性心脏疾病，为后期生活，健康系统，后代做铺垫
        # 左心位发病率万分之2，可能情节‘受伤完美避开心脏’
        heart_location = random_data(1, 5000)
        if heart_location == 1:
            data_save_txt('heart_location_tag', "1")

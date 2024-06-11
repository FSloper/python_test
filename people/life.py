import random

heart_weight = 0
# 心脏重量
left_atrium = 0
left_ventricle = 0
right_atrium = 0
right_ventricle = 0


def create_data_txt(goods, state):
    with open('people_data.txt', 'w') as file:
        file.write(str(goods))
        file.write(' : ')
        file.write(str(state))


def create_heart_data(heart_start, heart_end):
    heart_exist = random.randrange(heart_start, heart_end)
    # 先天性心脏病发病率千分之6，意味着大于457或小于503就发病
    create_data_txt('heart_exist', heart_exist)
    if heart_exist >= 228 | heart_exist <= 257:
        print(heart_exist)
        if heart_exist == 250:
            print('先天性心脏病发病率千分之6左右，很不幸您夭折了')
        # 左心位发病率万分之2
        heart_location = random.randrange(1, 5001)
        if heart_location == 1:
            create_data_txt('heart_location_tag', "左心位")
        # 心脏位置


def father_mather_data():
    # 随机父母，出生地区，出生地，出生年月日
    create_heart_data(1, 501)


people_start = input("继续上次存档请输入1，读档请输入2，从头开始请输入3：")
if people_start == "1":
    print("d")
elif people_start == "2":
    open('people_data.txt', 'w')
elif people_start == "3":
    father_mather_data()

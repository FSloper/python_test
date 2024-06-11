import random


def all_initialize():
    return None


def random_data(a, b):
    data = random.randrange(a, b + 1)
    return data


# 出生地区根据各区人口占比
def start_continent():
    continent_probability = random_data(1, 1000)
    if continent_probability <= 606:
        continent = '亚洲'
    elif continent_probability <= 774:
        continent = '非洲'
    elif continent_probability <= 848:
        continent = '欧洲'
    elif continent_probability <= 898:
        continent = '北美'
    elif continent_probability <= 979:
        continent = '南美'
    else:
        continent = '大洋洲'
    return continent

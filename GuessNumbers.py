import random


def guess_number():
    try:
        imin = int(input('请输入范围最小数: ').strip())
        imax = int(input('请输入范围最大数: ').strip())
        if imin >= imax:
            print('输入的最小数不能小于等于最大数（＝。＝）')
        else:
            print(f'范围：{imin}-{imax}')
            answer = random.randrange(imin, imax + 1)
            counter = 0
            while True:
                counter += 1
                num = int(input('请输入你的猜测: ').strip())
                if num < answer:
                    print(f'(っ*´Д`)っ.大一点.范围：{num}-{imax}')
                    if num < imin:
                        imin = num
                elif num > answer:
                    print(f'(っ*´Д`)っ.小一点.范围：{imin}-{num}')
                    if num > imin:
                        imax = num
                else:
                    print(f'♪(^∇^*).猜对了.答案是：{num}')
                    break
            print(f'你一共猜了:{counter}次.\n')
    except ValueError:
        print('不是什么都能比的好吗？只能说数啊！！！,o(≧口≦)o')


print('Version: 1.0\nAuthor: 卓燃&fsloper\n')
while True:
    guess_number()

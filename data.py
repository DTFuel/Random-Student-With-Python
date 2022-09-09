import random as rd
from cfg import name  #调用cfg.py中name变量

value = []
dis = []


def RepeatlessChoice(value, dislist, cell):
    item = rd.choice(value)
    if len(cell) >= 20:
        del cell[0]
    if dislist.count(item) != 0:
        return item
    if cell.count(item) == 0:
        cell.append(item)
        return item
    return RepeatlessChoice(value, dislist, cell)


#根据权重生成列表
for Name in name:
    for Value in range(int(Name[1])):
        value.append(Name[0])
#根据权重生成黑名单
#如果权不等于1，加入黑名单
for Name in name:
    if Name[1] != "1":
        dis.append(Name[0])

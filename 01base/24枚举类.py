from enum import Enum

Week = Enum('aaa', ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'))
# print(aaa.Sun)
print(Week.Sun)
for name, member in Week.__members__.items():
    print(name, '=>', member, ',', member.value)
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
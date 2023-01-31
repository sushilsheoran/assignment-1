import math
for i in range(0,360,15):
    print(i,"---",round(math.sin((i*3.14)/180),4) ,",", round(math.cos((i*3.14)/180),4))
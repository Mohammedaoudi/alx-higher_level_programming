#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (float(0))
    else:
        scr = 0
        wg = 0
        for i in my_list:
            scr += (i[0] * i[1])
            wg += i[1]
        return (scr / wg)

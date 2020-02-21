from copy import copy
from math import floor

#ナンプレ全体に矛盾がないか判断する
def Judge(NP):
    #行の判定(矛盾があればFalseを返す)

    NP_result=copy(NP)
    for i in range(0,9):
        inspection=[0]*9
        for n in range(0,9):
            inspection[n]=NP_result[i][n]
        while 0 in inspection:
            inspection.remove(0)
        for k in range(1,10):
            if k in inspection:
                inspection.remove(k)

        num=len(inspection)
        if num>0:
            return False

    #列の判定(矛盾があればFalseを返す)

    NP_result=copy(NP.T)
    for i in range(0,9):
        inspection=[0]*9
        for n in range(0,9):
            inspection[n]=NP_result[i][n]
        while 0 in inspection:
            inspection.remove(0)
        for k in range(1,10):
            if k in inspection:
                inspection.remove(k)

        num=len(inspection)
        if num>0:
            return False

    #３✖３の判定(矛盾があればFalseを返す)

    NP_result=copy(NP.reshape(27,3))
    for i in range(0,3):
        for n in range(0,3):
                inspection=[]
                inspection.extend(NP_result[i*9+n])
                inspection.extend(NP_result[i*9+n+3])
                inspection.extend(NP_result[i*9+n+6])
                while 0 in inspection:
                    inspection.remove(0)
                for k in range(1,10):
                    if k in inspection:
                        inspection.remove(k)

                num=len(inspection)
                if num>0:
                    return False

    #Trueを返す
    return True

#入力された座標の行、列,3×3,内にに矛盾がないか判断する
def Judge_pin(NP,y,x):
    #行の判定(矛盾があればFalseを返す)

    NP_result=copy(NP)

    inspection=[0]*9
    for n in range(9):
        inspection[n]=NP_result[y][n]

    while 0 in inspection:
        inspection.remove(0)
    for k in range(1,10):
        if k in inspection:
            inspection.remove(k)

    num=len(inspection)
    if num>0:
        return False

    #列の判定(矛盾があればFalseを返す)

    NP_result=copy(NP.T)
    for i in range(9):
        inspection=[0]*9
        for n in range(9):
            inspection[n]=NP_result[x][n]
        while 0 in inspection:
            inspection.remove(0)
        for k in range(1,10):
            if k in inspection:
                inspection.remove(k)

    num=len(inspection)
    if num>0:
        return False

    #３✖３の判定(矛盾があればFalseを返す)

    NP_result=copy(NP.reshape(27,3))

    a=floor(y/3)
    b=floor(x/3)

    inspection=[]
    inspection.extend(NP_result[a*9+b])
    inspection.extend(NP_result[a*9+b+3])
    inspection.extend(NP_result[a*9+b+6])

    while 0 in inspection:
        inspection.remove(0)
    for k in range(1,10):
        if k in inspection:
            inspection.remove(k)

    num=len(inspection)
    if num>0:
        return False

    #Trueを返す
    return True

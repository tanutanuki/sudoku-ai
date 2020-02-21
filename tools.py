from copy import copy
from def_Judge import Judge
from def_Judge import Judge_pin
from Test_Data import NP_array
import numpy as np

#入力されたナンプレを綺麗に出力
def Projecter(NP):

    for i in range(9):
        if i%3==0:
            print("━"*21)
        print("|",end="")

        for n in range(9):

            print(str(NP[i][n]),end=" ")

            if n%3==2:
                print("|",end="")
        print("\n",end="")
    print("━"*21)

    return 0

#自作Solver　数独を解く（解けない問題あり）
def Solver(NP):

    while 0 in NP:

        check=0

        for i in range(0,9):
            for n in range(0,9):
                if NP[i][n]==0:
                    count=0
                    num=0
                    for k in range(1,10):
                        NP[i][n]=k
                        if Judge(NP):
                            num=k
                            count+=1
                    if count==1:
                        NP[i][n]=num
                        check+=1

                    else:
                        NP[i][n]=0
        #無限ループ回避
        if check==0:
            return False

    return Judge(NP)

#数独を解く（何でも解ける、インターネットからアイデアをもらいました）
def Solver_2(NP,y=0,x=0):
    if y>8:
        return Judge(NP)

    elif NP[y][x]!=0:
        if x==8:
            if Solver_2(NP,y+1,0):#次の関数に判断を任せる
                return True
        else:
            if Solver_2(NP,y,x+1):#次の関数に判断を任せる
                return True

    else:
        for i in range(1,10):
            NP[y][x]=i
            if Judge_pin(NP,y,x):
                if x==8:
                    if Solver_2(NP,y+1,0):#次の関数に判断を任せる
                        return True
                else:
                    if Solver_2(NP,y,x+1):#次の座標の関数に判断を任せる
                        return True
        NP[y][x]=0
        return False

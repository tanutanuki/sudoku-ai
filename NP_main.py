#ナンプレを解析して出力する

from time import time
#private
from Test_Data import NP_array
from tools import Solver
from tools import Projecter

#解析前のナンプレ(配列)を出力
Projecter(NP_array)

t_1=time()

#解析して０に適切な値を入れたものを返す
result=Solver(NP_array)

t_2=time()

elapsed_time=t_2-t_1
elapsed_time=round(elapsed_time,2)

print("-"*10+"解析結果"+"-"*10)

    #resultを出力
if result:
    print("実行結果:成功")
else:
    print("実行結果:失敗")


print("解析時間:"+str(elapsed_time)+"秒")

Projecter(NP_array)

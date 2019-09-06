import math

def getValue(b, r, n):
    v = round(b*math.pow(1+r, n),2)
    print('您的最终收益为：' + str(v))
    return 1

b = float(input('请输入您的本金：'))
r = float(input('请输入您所选产品的年利率：'))
n = float(input('请输入您购买的年数：'))
getValue(b, r, n)

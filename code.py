# 開 n 次方根函式

def nroot(x, y):
  return x**(1/y)

a = int(input("請輸入被開方數字："))
b = int(input("請輸入開方數字："))

result = nroot(a, b)

print("{}開{}次方為{}".format(a, b, result))
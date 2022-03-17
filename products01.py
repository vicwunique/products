# 讓使用者輸入
products = []
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':     # quit
        break
    price = input('請輸入商品價格： ')
    quantity = input('請輸入商品數量： ')
    products.append([name, price, quantity])
print(products)

# 印出所有資料
for p in products:
    print(p[0], '的價格為', p[1], '元，數量', p[2], '份')

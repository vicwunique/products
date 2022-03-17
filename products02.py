# 讓使用者輸入
products = []
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':     # quit
        break
    price = input('請輸入商品價格： ')
    price = int(price)
    quantity = input('請輸入商品數量： ')
    quantity = int(quantity)
    products.append([name, price, quantity])
print(products)

# 印出所有資料
for p in products:
    print(p[0], '的價格為', p[1], '元，數量', p[2], '份')

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('名稱,價格,數量\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + '\n')

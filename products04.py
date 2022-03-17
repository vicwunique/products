# 1.確認檔案是否存在及讀取檔案
import os       # operating system

products = []
if os.path.isfile('products.csv'):
    print('耶！找到檔案了！')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '名稱,價格,數量' in line:
                continue        # 暫時停住不往下執行，而跳到迴圈起始處繼續執行
            name, price, quantity = line.strip().split(',')     # 先使用strip()去除換行符號，再使用split(',')做分割
            products.append([name, price, quantity])
    print(products)
else:
    print('糟糕，找不到檔案耶......')

# 2.讓使用者輸入
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

# 3.印出所有資料
for p in products:
    print(p[0], '的價格為', p[1], '元，數量', p[2], '份')

# 4.寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('名稱,價格,數量\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + '\n')

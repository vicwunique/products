# 1.讀取檔案
import os       # operating system

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '名稱,價格,數量' in line:
                continue        # 暫時停住不往下執行，而跳到迴圈起始處繼續執行
            name, price, quantity = line.strip().split(',')     # 先使用strip()去除換行符號，再使用split(',')做分割
            products.append([name, price, quantity])
    return products

# 2.讓使用者輸入
def user_input(products):
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
    return products

# 3.印出所有資料
def print_products(products):
    for p in products:
        print(p[0], '的價格為', p[1], '元，數量', p[2], '份')

# 4.寫入檔案
def write_to_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('名稱,價格,數量\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + '\n')

def main():
    filename = 'products.csv'
    products = []       # 找不到檔案時作為宣告使用
    if os.path.isfile(filename):        # 確認檔案是否存在
        print('耶！找到檔案了！')
        products = read_file(filename)
    else:
        print('糟糕，找不到檔案耶......')
    products = user_input(products) 
    print_products(products)
    write_to_file(filename, products)

main()      # 程式的進入點


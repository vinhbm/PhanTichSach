from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# URL của Lazada.vn
url = 'https://www.lazada.vn/sach/'

# Mở trang web
driver.get(url)

# Đợi một thời gian cho trang web tải xong (có thể điều chỉnh thời gian này)
driver.implicitly_wait(10)

# Trích xuất dữ liệu
names = driver.find_elements(By.CLASS_NAME, 'RfADt')
prices = driver.find_elements(By.CLASS_NAME, 'aBrP0')
discounts = driver.find_elements(By.CLASS_NAME, 'WNoq3')
sold_discounts = driver.find_elements(By.CLASS_NAME, '_1cEkb')

data = []

for name, price, discount, sold_discount in zip(names, prices, discounts, sold_discounts):
    book_name = name.text.strip()
    book_price = price.text.strip()
    book_discount = discount.text.strip()
    book_sold_discount = sold_discount.text.strip()

    data.append([book_name, book_price, book_discount, book_sold_discount])

# Tắt trình duyệt
driver.quit()

# Tạo DataFrame và lưu dữ liệu vào CSV
df = pd.DataFrame(data, columns=['Tên sách', 'Giá tiền', 'Giảm giá', 'Đã bán'])
df.to_csv('lazada_books.csv', index=False, encoding='utf-8-sig')

print("Dữ liệu đã được ghi vào tệp CSV 'lazada_books.csv'")

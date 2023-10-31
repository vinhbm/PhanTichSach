import requests
from bs4 import BeautifulSoup
import pandas as pd

# Hàm để lấy dữ liệu từ URL và trả về DataFrame
def scrape_books_data(url, sort):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    params = {'sort': sort}
    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_blocks = soup.find_all('div', class_='product-item')
    
    data = []

    for product in product_blocks:
        book_title = product.find('div', class_='title').text.strip()
        book_price = product.find('div', class_='price-discount__price').text.strip()
        book_discount = product.find('div', class_='price-discount__discount').text.strip()
        book_quantity = product.find('span', class_='quantity has-border').text.strip()
        book_rating = product.find('div', class_='styles__StyledStars-sc-1grrwd5-0 fsYaBc').text.strip()

        data.append([book_title, book_price, book_discount, book_quantity, book_rating])

    return data

# Tạo danh sách các URL cho các trang và sắp xếp
tiki_urls = {
    'Mới nhất': 'https://tiki.vn/nha-sach-tiki/c8322?sort=newest',
    'Bán chạy nhất': 'https://tiki.vn/nha-sach-tiki/c8322?sort=top_seller',
}

# Tạo một danh sách chứa dữ liệu từ tất cả các trang và sắp xếp
all_book_data = []
for sort, url in tiki_urls.items():
    book_data = scrape_books_data(url, sort)
    all_book_data.extend(book_data)

# Tạo DataFrame từ danh sách dữ liệu
df = pd.DataFrame(all_book_data, columns=['Tên sản phẩm', 'Giá tiền', 'Giảm giá', 'Số lượng', 'Đánh giá'])

# Xuất DataFrame thành tệp CSV
df.to_csv('books_tiki1.csv', index=False, encoding='utf-8-sig')

print("Dữ liệu đã được ghi vào tệp CSV 'books_tiki1.csv'")

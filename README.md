# 📊 Excel Reader App

Ứng dụng Streamlit để đọc, xem và xử lý file Excel một cách dễ dàng.

## ✨ Tính năng

- 📁 **Upload file Excel** (.xlsx, .xls)
- 📊 **Xem dữ liệu** từ nhiều sheet
- 🔍 **Tìm kiếm và lọc** dữ liệu
- 📈 **Thống kê mô tả** chi tiết
- 💾 **Xuất dữ liệu** ra CSV/Excel
- 📋 **Thông tin chi tiết** về các cột
- 🎨 **Giao diện thân thiện** và dễ sử dụng

## 🚀 Cài đặt

### 1. Clone repository
```bash
git clone <repository-url>
cd Rexcel
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Chạy ứng dụng
```bash
streamlit run app.py
```

Ứng dụng sẽ mở tại: `http://localhost:8501`

## 📖 Hướng dẫn sử dụng

### 1. Upload file Excel
- Sử dụng sidebar bên trái để chọn file Excel
- Hỗ trợ định dạng .xlsx và .xls

### 2. Chọn sheet
- Chọn sheet muốn xem từ dropdown
- Xem thông tin cơ bản về sheet (số dòng, cột, dữ liệu thiếu...)

### 3. Khám phá dữ liệu
- **Xem dữ liệu**: Hiển thị dữ liệu dạng bảng
- **Tùy chọn hiển thị**: Chọn số dòng hiển thị, hiển thị index
- **Thống kê mô tả**: Xem các thống kê cơ bản
- **Thông tin cột**: Xem kiểu dữ liệu, số giá trị null, unique

### 4. Tìm kiếm và lọc
- Nhập từ khóa để tìm kiếm trong tất cả các cột
- Kết quả sẽ được highlight và hiển thị

### 5. Xuất dữ liệu
- **CSV**: Tải xuống dữ liệu dạng CSV
- **Excel**: Tải xuống dữ liệu dạng Excel

## 🛠️ Công nghệ sử dụng

- **Streamlit**: Framework web app
- **Pandas**: Xử lý dữ liệu
- **OpenPyXL**: Đọc/ghi file Excel
- **xlrd**: Đọc file Excel cũ (.xls)

## 📋 Requirements

```
streamlit==1.28.1
pandas==2.1.3
openpyxl==3.1.2
xlrd==2.0.1
```

## 🎯 Tính năng nổi bật

### Giao diện thân thiện
- Layout responsive
- Sidebar để upload file
- Các tùy chọn hiển thị linh hoạt

### Xử lý dữ liệu mạnh mẽ
- Hỗ trợ nhiều sheet
- Thống kê chi tiết
- Tìm kiếm thông minh

### Xuất dữ liệu linh hoạt
- Xuất CSV với encoding UTF-8
- Xuất Excel với format chuẩn
- Tên file tự động

## 🔧 Troubleshooting

### Lỗi khi đọc file Excel
- Kiểm tra định dạng file (.xlsx, .xls)
- Đảm bảo file không bị hỏng
- Kiểm tra quyền truy cập file

### Lỗi khi cài đặt dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Lỗi khi chạy Streamlit
```bash
streamlit --version
streamlit run app.py --server.port 8501
```

## 📝 Changelog

### Version 1.0.0
- ✅ Upload và đọc file Excel
- ✅ Hiển thị dữ liệu từ nhiều sheet
- ✅ Tìm kiếm và lọc dữ liệu
- ✅ Thống kê mô tả
- ✅ Xuất dữ liệu CSV/Excel
- ✅ Giao diện thân thiện

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:
1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push và tạo Pull Request

## 📄 License

MIT License - xem file LICENSE để biết thêm chi tiết.

## 👨‍💻 Tác giả

Made with ❤️ by Streamlit

import streamlit as st
import pandas as pd
import io
from io import BytesIO

# Cấu hình trang
st.set_page_config(
    page_title="Excel Reader App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tiêu đề ứng dụng
st.title("📊 Excel Reader App")
st.markdown("---")

# Sidebar để upload file
st.sidebar.header("📁 Upload File Excel")
uploaded_file = st.sidebar.file_uploader(
    "Chọn file Excel để đọc",
    type=['xlsx', 'xls'],
    help="Hỗ trợ định dạng .xlsx và .xls"
)

# Hàm đọc file Excel
def read_excel_file(file):
    """Đọc file Excel và trả về dictionary chứa các sheet"""
    try:
        # Đọc tất cả các sheet
        excel_file = pd.ExcelFile(file)
        sheets_data = {}
        
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(file, sheet_name=sheet_name)
            sheets_data[sheet_name] = df
            
        return sheets_data, excel_file.sheet_names
    except Exception as e:
        st.error(f"Lỗi khi đọc file: {str(e)}")
        return None, None

# Hàm xuất dữ liệu
def export_to_csv(df):
    """Chuyển DataFrame thành CSV để download"""
    output = BytesIO()
    df.to_csv(output, index=False, encoding='utf-8-sig')
    output.seek(0)
    return output.getvalue()

def export_to_excel(df, sheet_name="Sheet1"):
    """Chuyển DataFrame thành Excel để download"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    output.seek(0)
    return output.getvalue()

# Xử lý khi có file được upload
if uploaded_file is not None:
    # Đọc file
    sheets_data, sheet_names = read_excel_file(uploaded_file)
    
    if sheets_data is not None:
        # Hiển thị thông tin file
        st.success(f"✅ Đã tải thành công file: {uploaded_file.name}")
        
        # Chọn sheet để hiển thị
        col1, col2 = st.columns([1, 3])
        
        with col1:
            selected_sheet = st.selectbox(
                "Chọn sheet để xem:",
                sheet_names,
                key="sheet_selector"
            )
        
        with col2:
            if selected_sheet:
                df = sheets_data[selected_sheet]
                st.info(f"📋 Sheet '{selected_sheet}' có {len(df)} dòng và {len(df.columns)} cột")
        
        # Hiển thị dữ liệu
        if selected_sheet and not df.empty:
            st.subheader(f"📊 Dữ liệu từ sheet: {selected_sheet}")
            
            # Thống kê cơ bản
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Số dòng", len(df))
            with col2:
                st.metric("Số cột", len(df.columns))
            with col3:
                st.metric("Dữ liệu thiếu", df.isnull().sum().sum())
            with col4:
                st.metric("Dữ liệu trùng lặp", df.duplicated().sum())
            
            # Tùy chọn hiển thị
            st.subheader("⚙️ Tùy chọn hiển thị")
            col1, col2 = st.columns(2)
            
            with col1:
                show_head = st.checkbox("Chỉ hiển thị 100 dòng đầu", value=True)
                show_index = st.checkbox("Hiển thị index", value=False)
            
            with col2:
                if st.button("🔄 Làm mới dữ liệu"):
                    st.rerun()
            
            # Hiển thị dữ liệu
            if show_head:
                display_df = df.head(100)
            else:
                display_df = df
            
            st.dataframe(
                display_df,
                width='stretch',
                hide_index=not show_index
            )
            
            # Thống kê mô tả
            if st.checkbox("📈 Hiển thị thống kê mô tả"):
                st.subheader("Thống kê mô tả")
                st.dataframe(df.describe(), width='stretch')
            
            # Thông tin về các cột
            if st.checkbox("ℹ️ Thông tin về các cột"):
                st.subheader("Thông tin chi tiết các cột")
                col_info = pd.DataFrame({
                    'Tên cột': df.columns,
                    'Kiểu dữ liệu': df.dtypes,
                    'Số giá trị null': df.isnull().sum(),
                    'Số giá trị unique': df.nunique()
                })
                st.dataframe(col_info, width='stretch')
            
            # Tìm kiếm và lọc dữ liệu
            st.subheader("🔍 Tìm kiếm và lọc dữ liệu")
            search_term = st.text_input("Nhập từ khóa để tìm kiếm:", placeholder="Tìm kiếm trong tất cả các cột...")
            
            if search_term:
                # Tìm kiếm trong tất cả các cột
                mask = df.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)
                filtered_df = df[mask]
                st.write(f"Tìm thấy {len(filtered_df)} dòng chứa '{search_term}'")
                if not filtered_df.empty:
                    st.dataframe(filtered_df, width='stretch')
            
            # Xuất dữ liệu
            st.subheader("💾 Xuất dữ liệu")
            col1, col2 = st.columns(2)
            
            with col1:
                csv_data = export_to_csv(df)
                st.download_button(
                    label="📄 Tải xuống CSV",
                    data=csv_data,
                    file_name=f"{selected_sheet}_data.csv",
                    mime="text/csv"
                )
            
            with col2:
                excel_data = export_to_excel(df, selected_sheet)
                st.download_button(
                    label="📊 Tải xuống Excel",
                    data=excel_data,
                    file_name=f"{selected_sheet}_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        
        else:
            st.warning("⚠️ Sheet được chọn không có dữ liệu")
    
    else:
        st.error("❌ Không thể đọc file Excel. Vui lòng kiểm tra định dạng file.")

else:
    # Hiển thị hướng dẫn khi chưa có file
    st.markdown("""
    ## 👋 Chào mừng đến với Excel Reader App!
    
    Ứng dụng này giúp bạn:
    - 📁 **Upload và đọc file Excel** (.xlsx, .xls)
    - 📊 **Xem dữ liệu** từ nhiều sheet khác nhau
    - 🔍 **Tìm kiếm và lọc** dữ liệu
    - 📈 **Xem thống kê** mô tả
    - 💾 **Xuất dữ liệu** ra CSV hoặc Excel
    
    ### 🚀 Cách sử dụng:
    1. **Upload file**: Sử dụng sidebar bên trái để chọn file Excel
    2. **Chọn sheet**: Chọn sheet muốn xem từ dropdown
    3. **Khám phá dữ liệu**: Sử dụng các tùy chọn hiển thị và tìm kiếm
    4. **Xuất dữ liệu**: Tải xuống dữ liệu đã xử lý
    
    ### 📋 Hỗ trợ định dạng:
    - ✅ .xlsx (Excel 2007+)
    - ✅ .xls (Excel 97-2003)
    """)
    
    # Hiển thị ví dụ dữ liệu
    st.subheader("📝 Ví dụ dữ liệu")
    sample_data = pd.DataFrame({
        'Tên': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C'],
        'Tuổi': [25, 30, 35],
        'Thành phố': ['Hà Nội', 'TP.HCM', 'Đà Nẵng'],
        'Lương': [15000000, 20000000, 25000000]
    })
    st.dataframe(sample_data, width='stretch')

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Streamlit")

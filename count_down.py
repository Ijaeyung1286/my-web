import streamlit as st

# ذخیره تاریخچه پیام‌ها
if "messages" not in st.session_state:
    st.session_state.messages = []  # ایجاد لیست برای پیام‌ها

# گرفتن ورودی از کاربر
user_input = st.chat_input("پیغام خود را وارد کنید...")

if user_input:
    # اضافه کردن پیام جدید به تاریخچه
    st.session_state.messages.append(user_input)

# نمایش همه پیام‌ها
for message in st.session_state.messages:
    st.markdown(
        f"""
        <div dir="rtl" style="
        margin-bottom: 10px;">
            <div style="
            border-radius: 5px 0 5px 5px;
             width: fit-content;
              padding: 10px;
               border: 1px solid #f800b6; 
               background-color: #f800b6;
                color: white;">
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
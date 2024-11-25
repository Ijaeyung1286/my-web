import streamlit as st
import json


FILE_NAME = 'messages2.json'

def load_messages_from_json():
    try:
        with open(FILE_NAME, 'r') as file:
            content = file.read().strip()
            if not content:
                return {"ms": []}  # اگر فایل خالی است، یک لیست خالی بازگردانید
            return json.loads(content)
    except FileNotFoundError:
        return {"ms": []}
    except json.JSONDecodeError:
        # اگر داده‌ها فرمت معتبری ندارند، فایل را نادیده بگیرید و لیست خالی بازگردانید
        return {"ms": []}

for message in load_messages_from_json()["ms"]:
    st.html(
        f"""
        <div  style="margin-bottom: 10px;">
            <div style="border-radius: 5px 0 5px 5px;
             width: fit-content;
              padding: 10px;
               border: 1px solid #2c2e2d;
                background-color: #2c2e2d;
                 color: white;">
                {message}
            </div>
        </div>
        """
    )


# فایل JSON برای ذخیره پیام‌ها
FILE_sent_NAME = 'messages.json'

# تابع برای ذخیره پیام‌ها در فایل JSON
def save_messages_to_json(messages):
    with open(FILE_sent_NAME, 'w') as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)

# تابع برای خواندن پیام‌ها از فایل JSON
def load_messages_from_json():
    try:
        with open(FILE_sent_NAME, 'r') as file:
            content = file.read().strip()
            if not content:
                return {"ms":[]}  # اگر فایل خالی است، یک لیست خالی بازگردانید
            return json.loads(content)
    except FileNotFoundError:
        return {"ms":[]}
    except json.JSONDecodeError:
        # اگر داده‌ها فرمت معتبری ندارند، فایل را نادیده بگیرید و لیست خالی بازگردانید
        return {"ms":[]}

# بارگذاری پیام‌ها از فایل JSON به st.session_state
if "messages" not in st.session_state:
    st.session_state.messages = load_messages_from_json()

# گرفتن ورودی از کاربر
user_input = st.chat_input("پیغام خود را وارد کنید...")

if user_input:
    # اضافه کردن پیام جدید به تاریخچه
    st.session_state.messages["ms"].append(user_input)
    # ذخیره کردن پیام‌ها در فایل JSON
    save_messages_to_json(st.session_state.messages)

# نمایش همه پیام‌ها
for message in st.session_state.messages["ms"]:
    st.html(
        f"""
        <div dir="rtl" style="margin-bottom: 10px;">
            <div style="border-radius: 5px 0 5px 5px; width: fit-content; padding: 10px; border: 1px solid #008924; background-color: #008924; color: white;">
                {message}
            </div>
        </div>
        """
    )

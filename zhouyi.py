import openai

import streamlit as st

# 设置 OpenAI API 密钥

openai.api_key = "YOUR_API_KEY_HERE"

# 创建 Streamlit 应用程序

def main():

    st.title("周易算命")

    # 添加用户输入框

    name = st.text_input("请输入您的姓名")

    birth_date = st.text_input("请输入您的出生日期（格式为 YYYY-MM-DD）")

    birth_time = st.text_input("请输入您的出生时间（格式为 HH:MM）")

    location = st.text_input("请输入您的居住地")

    question = st.text_input("请输入您的问题")

    # 添加“提交”按钮

    if st.button("提交"):

        # 调用 OpenAI API 进行自然语言处理

        response = openai.Completion.create(

            engine="davinci",

            prompt=f"姓名：{name}\n出生日期：{birth_date}\n出生时间：{birth_time}\n居住地：{location}\n问题：{question}",

            temperature=0.7,

            max_tokens=1024,

            top_p=1,

            frequency_penalty=0,

            presence_penalty=0

        )

        # 显示 OpenAI API 的响应

        st.write(response.choices[0].text)

if __name__ == "__main__":

    main()
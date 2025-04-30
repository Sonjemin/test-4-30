import streamlit as st
st.text_input(label, type="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")

from openai import OpenAI
client = OpenAI()
response = client.responses.create(
 model="gpt-4o",
 input=[
 {
 "role": "user",
 "content": "Write a onesentence bedtime story about a unicorn."
 }
 ]
)
print(response.output_text)

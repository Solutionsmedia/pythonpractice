import streamlit as st
data = [
    ["  ada ", "1200", "Nigeria"],
    ["  bola ", "2500", "Ghana"],
    ["  chidi ", "500", "Nigeria"],
    ["  dayo ", "1500", "Kenya"],
]
cleaned = []


def clean_data():
    for user in data:
        name = user[0]
        price = user[1]
        country = user[2]

        cleaned_name = name.strip().title()
        cleaned_price = int(price)
        if country.strip().title() == "Nigeria":
            cleaned.append([cleaned_name, cleaned_price, country])
    return cleaned


st.title("Layout demo")

col1, col2 = st.columns(2)  # two columns

with col1:
    st.write("Column 1 content")
    if st.button("Button 1"):
        st.write("You clicked button 1!")
        st.write(clean_data())

with col2:
    st.write("Column 2 content")
    if st.button("Button 2"):
        st.write("You clicked button 2!")

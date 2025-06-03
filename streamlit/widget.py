import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

# creating a text box
name = st.text_input("Enter your name")

# creating a slider
age = st.slider("Select your age",0,100,25)

st.write(f"your age is {age}")

if name:
    st.write(f"Hello learner {name}")

# create a dropdown or selectbox
options = ['Python','Java','C++','RUST']
choice = st.selectbox("Choose your favorite programming language :",options)
st.write(f'You have selected {choice}, Good Choice!!!')


# simple dataframe

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Score': [85.5, 92.0, 88.5, 79.0]
}

# Create DataFrame
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

# uplode files

uploaded_file = st.file_uploader('Choose a CSV file',type="csv")

if uploaded_file is not None:
    newdf = pd.read_csv(uploaded_file)
    st.write(newdf)


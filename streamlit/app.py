import streamlit as st
import pandas as pd
import numpy as np

# Title of application 
st.title("hello programmer")

# Display text
st.write("This is simple text")


# Create a simple DataFrame

df = pd.DataFrame({
    'Column A':["X","HDS","KSHD"],
    'Column B':[1123,4323,3536] 
})

# Display the DataFrame
st.write("Sample DataFrame")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(30,3),columns=['s','t','w']

)
st.line_chart(chart_data)
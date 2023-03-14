import streamlit as st
import pandas
st.set_page_config(layout="wide")
# col1, col2 = st.columns(2)

# with col1:
#     st.image("Images/IMG.png",width=300)

# with col2:
st.header("The Best Company")
content = """
The Best Company is a rapidly growing software service provider and executed IT solutions in different verticals. We aim to provide the best services in the industry by integrating expertise with innovative technology. 
"""
st.info(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns([1.5, 1.5, 1.5])

df = pandas.read_csv("data.csv")
with col1:
    for index, row in df[0:4].iterrows():
        st.subheader(f'{row["first name"].capitalize()}  {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("Images-2/" + row["image"])
        # st.write(f"[Source Code]({row['url']})")
with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].capitalize()}  {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("Images-2/"+row["image"])
        # st.write(f"[Source Code]({row['url']})")
with col3:
    for index,row in df[8:12].iterrows():
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("Images-2/"+row["image"])
        # st.write(f"[Source Code]({row['url']})")



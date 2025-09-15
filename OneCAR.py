import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
from PIL import Image 
import plotly.graph_objects as go

df=pd.read_csv(r"C:\Users\kulde\Desktop\STREMLIT\CARDATASET.csv")
st.set_page_config(layout="wide")

image=Image.open("car image.jpg")
col1,col2=st.columns([0.4,0.67])

with col1:
    st.image(image,width=300)

with col2:
    st.markdown('<center><h1 style="color: purple; font-weight: bold; padding: 5px; border-radius: 6px; font-size:60px;">'
        'Cars Sales Dashboard</h1></center>',unsafe_allow_html=True)
    

col3,col4,col5=st.columns([0.2,0.45,0.45])
with col3:
    box_date=str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last update by:  \n{box_date}")
    
    image1=Image.open("imgbh.webp")
    image1

    image2=Image.open("car.jpg")
    image2

with col4:
    fig=px.box(df,x="seller_type",y="selling_price",title="👉 Box plot of seller_type and selling_price")
    st.plotly_chart(fig)

with col5:
    grouped_df = df.groupby("seller_type", as_index=False)["selling_price"].sum()
    fig = px.bar(grouped_df, x="seller_type", y="selling_price", title="👉 📊Total selling price by seller type",color_discrete_sequence=["violet"])
    st.plotly_chart(fig)


col6,col7=st.columns([0.1,0.1])
with col6:
    grouped_df1=df.head(50).groupby("fuel",as_index=False)["selling_price"].mean()
    fig=px.bar(grouped_df1,x="fuel",y="selling_price",title="👉 📊Avg of Total Selling Price by Fuel",color_discrete_sequence=["green"])
    st.plotly_chart(fig)

with col7:
    fig=px.pie(df,names="transmission",values="selling_price",title="👉 🥧Pie chart between transmission and selling_price")
    st.plotly_chart(fig)

col8=st.columns(1)[0]
with col8:
    fig=px.histogram(df,x="seller_type",y="selling_price",title="👉 📊Histogram Chat between selling_type and selling_price",color_discrete_sequence=["teal"])
    st.plotly_chart(fig)

col9=st.columns(1)[0]
with col9:
    fig=px.treemap(df,path=["owner","year"],title="👉 Treegraph Between Owner and Year")
    st.plotly_chart(fig) 

col10,col11=st.columns([0.50,0.50])
with col10:
    fig=px.area(df,x="fuel",y="selling_price",title="👉 Areachart Between fuel and selling_price")
    st.plotly_chart(fig)

with col11:
    fig = px.scatter(df, x="fuel", y="selling_price",title="👉 Scatter Plot fuel and selling_price")
    st.plotly_chart(fig)
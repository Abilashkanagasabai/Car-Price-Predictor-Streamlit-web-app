import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("car price.pkl","rb")
price_finder=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def car_price_predictor(year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner):
    
    
   
    prediction=price_finder.predict([[year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]])
    print(prediction)
    return prediction



def main():
    st.title("CAR PRICE PREDICTOR")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Car Price Prediction  ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    year = st.text_input("year","Type Here")
    Present_Price = st.text_input("Present_Price(in lacs)","Type Here")
    Kms_Driven = st.text_input("Kms_Driven","Type Here")
    Fuel_Type = st.selectbox("Fuel_Type",("Petrol","Diesel"))
    if Fuel_Type=="Petrol":
        Fuel_Type=0
    else:
        Fuel_Type=1
    Seller_Type = st.selectbox("Seller_Type",("Dealer","Individual"))
    if Seller_Type=="Dealer":
        Seller_Type=0
    else:
        Seller_Type=1
    Transmission = st.selectbox("Transmission",("Manual","Automatic"))
    if Transmission=="Manual":
        Transmission=0
    else:
        Transmission=1
    Owner = st.text_input("Owner","Type Here")


    result=0
    if st.button("Predict"):
        result=car_price_predictor(year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner)
    st.success('The output is {} lacks'.format(result))
    if st.button("About"):
        st.text("Project Done by Abilash K")
        st.text("Mail:kabilash1999@gmail.com")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    

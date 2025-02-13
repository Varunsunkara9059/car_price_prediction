import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
from sklearn.linear_model import LinearRegression

regressor = pk.load(open('regressor.pkl','rb'))


st.header('car price prediction ML model')

data = pd.read_csv('Cardetails.csv')

def get_brand_name(car_name):
  car_name=car_name.split(' ')[0]
  return car_name.strip()
data['name']=data['name'].apply(get_brand_name)

name=st.selectbox('select Car brand',data['name'].unique())
year=st.slider('car Manufactured Year',1994,2024)
km_driven=st.slider('No of kms Driven',11,200000)
fuel=st.selectbox('Fuel type',data['fuel'].unique())
seller_type=st.selectbox('Seller type',data['seller_type'].unique())
transmission=st.selectbox('Transmission type',data['transmission'].unique())
owner=st.selectbox('Seller type',data['owner'].unique())
mileage=st.slider('car Mileage',10,40)
engine=st.slider('Engine CC',700,5000)
max_power=st.slider('Max power',0,200)
seats=st.slider('No of seats',5,10)

if st.button("predict"):
  input_data_model = pd.DataFrame(
    [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,	seats]],
    columns=['name',	'year',	'km_driven',	'fuel',	'seller_type','transmission','owner','mileage','engine','max_power','seats'])

  input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'],[1,2,3,4,5],inplace = True)
  input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4],inplace = True)
  input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3],inplace = True)
  input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2],inplace = True)
  input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai' ,'Toyota', 'Ford' ,'Renault', 'Mahindra',
 'Tata' ,'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi' ,'Audi',
 'Volkswagen' ,'BMW', 'Nissan', 'Lexus' ,'Jaguar', 'Land','MG' ,'Volvo', 'Daewoo',
 'Kia' ,'Fiat', 'Force', 'Ambassador', 'Ashok' ,'Isuzu' ,'Opel'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],inplace=True)
  
  car_price =regressor.predict(input_data_model)

  st.markdown('Car price is going to be '+str(car_price[0]))
# yo tala ko chai if maile education ko yeutai column ma rakhya thiye bhaney like using astype int garera    

import streamlit as st
import pandas as pd

st.image("https://pianalytix.com/wp-content/uploads/2020/12/Salary-Prediction-Model-using-ML-1024x427.jpg&quot")

st.title("salary prediction system")
age = st.number_input("enter your age")
exp = st.number_input("Enter your years of experience")
gender = st.radio("Gender = ", ["Male","Female"])
edu = st.selectbox("Education =", ["Bachelor", "Master", "PHD"])

if gender == 'Male':
   m = True
else:
   m = False

if edu == "Bachelor":
     edu = 1
     
elif edu == "master's":
    Master = 1

else:
    PhD= 1


# Age   Years of Experience Male    Bachelor's  Master's    PhD ( yo chai aba dataframe part ma same chainxa so liyeko)
if st.button("predict"):
   df = pd.DataFrame({
      'Age':[age],
      'Years of Experience':[exp],
      'Male':[m],
      "Education":[edu],
   })
   st.dataframe(df)

#wrong input kina aayo
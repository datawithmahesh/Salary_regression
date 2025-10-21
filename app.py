#this is for salary regression 
import streamlit as st
import pandas as pd
import pickle as pk
st.image("https://pianalytix.com/wp-content/uploads/2020/12/Salary-Prediction-Model-using-ML-1024x427.jpg&quot")

st.write("SALARY PREDICTION MODEL")

# load model
load_model= pk.load(open('salary.pickle','rb'))

#input data from user
st.title("salary prediction system")
age = st.number_input("enter your age",18,60)  # age yeti dekhi yeti bhnna rakheko
exp = st.number_input("Enter your years of experience", 0,40)
gender = st.radio("Gender = ", ["Male","Female"])
edu = st.selectbox("Education =", ["Bachelor", "Master", "PHD"])

if gender == 'Male':
   male = True
else:
   male = False

if edu == "Bachelor":
    b = 1; m = 0; p = 0
elif edu == "Master":
    b =0; m = 1; p = 0
else:
    b = 0; m= 0; p =1


# Age   Years of Experience Male    Bachelor's  Master's    PhD ( yo chai aba dataframe part ma same chainxa so liyeko)
if st.button("predict"):
   df = pd.DataFrame({
      'Age':[age],
      'Years of Experience':[exp],
      'Male':[male],   #yesma male ko thau ma gender rakhna mildaina kina ki mathi ko data frame ho hamley input dida chai true false garya thiyeu so true false wala nai variable rakhney
      "Bachelor's":[b],
      "Master's":[m],
      'PhD':[p]
   })
   st.dataframe(df)
   result = load_model.predict(df)
   st.balloons()
   st.write("your salary is=" ,int(result.tolist()[0][0]))




st.write("This model is done by mahesh Thapa")




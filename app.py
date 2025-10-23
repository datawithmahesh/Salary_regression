# Salary Prediction Model
import streamlit as st
import pandas as pd
import pickle as pk

# Page config
st.set_page_config(
    page_title="Salary Prediction Model",
    page_icon="💵",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Load model
load_model = pk.load(open('salary.pickle','rb'))

# --- Custom CSS ---
st.markdown("""
<style>
/* Background gradient */
body {
    background: linear-gradient(to right, #f7971e, #ffd200);
}

/* Title card */
.title-card {
    background: linear-gradient(to right, #36D1DC, #5B86E5);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-family: 'Arial Black', sans-serif;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Input styling */
.stNumberInput, .stRadio, .stSelectbox {
    background: #ffffffcc;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 15px;
}

/* Predict button */
.stButton>button {
    background-color: #ff7e5f;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 25px;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #feb47b;
}

/* Output card */
.output-card {
    background: linear-gradient(to right, #43e97b, #38f9d7);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

/* Footer */
.footer {
    text-align:center;
    color: #555;
    margin-top: 40px;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="title-card"><h1>💵 Salary Prediction Model</h1></div>', unsafe_allow_html=True)

# --- Image ---
st.image("https://pianalytix.com/wp-content/uploads/2020/12/Salary-Prediction-Model-using-ML-1024x427.jpg", use_container_width=True)

# --- Inputs ---
st.title("Salary Prediction System")
age = st.number_input("Enter your age", 18, 60)
exp = st.number_input("Enter your years of experience", 0, 40)
gender = st.radio("Gender =", ["Male","Female"])
edu = st.selectbox("Education =", ["Bachelor", "Master", "PHD"])

# --- Mapping ---
male = True if gender == 'Male' else False
if edu == "Bachelor":
    b, m, p = 1, 0, 0
elif edu == "Master":
    b, m, p = 0, 1, 0
else:
    b, m, p = 0, 0, 1

# --- Prediction ---
if st.button("Predict 🟢"):
    df = pd.DataFrame({
        'Age':[age],
        'Years of Experience':[exp],
        'Male':[male],
        "Bachelor's":[b],
        "Master's":[m],
        'PhD':[p]
    })
    
    st.dataframe(df)
    result = load_model.predict(df)
    st.balloons()
    st.markdown(f'<div class="output-card">💰 Predicted Salary: {int(result.tolist()[0][0])}</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown('<div class="footer">This model is done by <b>Mahesh Thapa</b></div>', unsafe_allow_html=True)




# #this is for salary regression 
# import streamlit as st
# import pandas as pd
# import pickle as pk
# st.image("https://pianalytix.com/wp-content/uploads/2020/12/Salary-Prediction-Model-using-ML-1024x427.jpg&quot")

# st.write("SALARY PREDICTION MODEL")

# # load model
# load_model= pk.load(open('salary.pickle','rb'))

# #input data from user
# st.title("salary prediction system")
# age = st.number_input("enter your age",18,60)  # age yeti dekhi yeti bhnna rakheko
# exp = st.number_input("Enter your years of experience", 0,40)
# gender = st.radio("Gender = ", ["Male","Female"])
# edu = st.selectbox("Education =", ["Bachelor", "Master", "PHD"])

# if gender == 'Male':
#    male = True
# else:
#    male = False

# if edu == "Bachelor":
#     b = 1; m = 0; p = 0
# elif edu == "Master":
#     b =0; m = 1; p = 0
# else:
#     b = 0; m= 0; p =1


# # Age   Years of Experience Male    Bachelor's  Master's    PhD ( yo chai aba dataframe part ma same chainxa so liyeko)
# if st.button("predict"):
#    df = pd.DataFrame({
#       'Age':[age],
#       'Years of Experience':[exp],
#       'Male':[male],   #yesma male ko thau ma gender rakhna mildaina kina ki mathi ko data frame ho hamley input dida chai true false garya thiyeu so true false wala nai variable rakhney
#       "Bachelor's":[b],
#       "Master's":[m],
#       'PhD':[p]
#    })
#    st.dataframe(df)
#    result = load_model.predict(df)
#    st.balloons()
#    st.write("your salary is=" ,int(result.tolist()[0][0]))




# st.write("This model is done by mahesh Thapa")




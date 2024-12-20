import streamlit as st
from utils import encode, predict
st.set_page_config(page_title="Default Risk Prediction", page_icon=":moneybag:", layout="wide")
st.title("Default Risk Prediction")

person_info, credit_history = st.columns(2, border=True)

with person_info:
    st.header("Personal Information")
    name = st.text_input("Name: ", placeholder='enter a name', label_visibility='hidden')
    age = st.number_input("Age: ", min_value=18, max_value=100, value=25, step=1, placeholder='insert age', label_visibility='hidden')
    gender = st.selectbox("Gender: ", options=('Male','Female'),index=None, placeholder='select one gender', label_visibility='hidden')
    mstat = st.selectbox("Marital Status: ", options=('Married','Single','Other'),index=None, placeholder='select marital status', label_visibility='hidden')
    edu = st.selectbox("Education: ", options=('Graduate School', 'University', 'High School', 'Others'),index=None, placeholder='select education level', label_visibility='hidden')
    limit_bal = st.number_input("Credit Limit: ", min_value=0, max_value=1000000, value=5000, step=100, placeholder='insert credit limit', label_visibility='hidden')
    
with credit_history:
    st.header("Credit History")
    stat, bill, pay = st.columns(3, border=True)
    # payment status
    pay_1 = stat.number_input("Repayment Status (this month): ", min_value=-2, max_value=8, value=None, placeholder='repayment delay')
    pay_2 = stat.number_input("Repayment Status (last month): ", min_value=-2, max_value=8, value=None, placeholder='repayment delay')
    pay_3 = stat.number_input("Repayment Status (2 months ago): ", min_value=-2, max_value=8, value=None, placeholder='repayment delay')
    pay_4 = stat.number_input("Repayment Status (3 months ago): ", min_value=-2, max_value=8, value=None, placeholder='repayment delay')
    pay_5 = stat.number_input("Repayment Status (4 months ago): ", min_value=-2, max_value=8, value=None, placeholder='repayment delay')
    pay_6 = stat.number_input("Repayment Status (5 months ago): ", min_value=-2, max_value=8, value=None, placeholder='repayment delay')
    # bill amount
    bill_amt1 = bill.number_input("Bill Amount (this month): ", min_value=0, max_value=1_000_000, value=None, placeholder='billed amount')
    bill_amt2 = bill.number_input("Bill Amount (last month): ", min_value=0, max_value=1_000_000, value=None, placeholder='billed amount')
    bill_amt3 = bill.number_input("Bill Amount (2 months ago): ", min_value=0, max_value=1_000_000, value=None, placeholder='billed amount')
    bill_amt4 = bill.number_input("Bill Amount (3 months ago): ", min_value=0, max_value=1_000_000, value=None, placeholder='billed amount')
    bill_amt5 = bill.number_input("Bill Amount (4 months ago): ", min_value=0, max_value=1_000_000, value=None, placeholder='billed amount')
    bill_amt6 = bill.number_input("Bill Amount (5 months ago): ", min_value=0, max_value=1_000_000, value=None, placeholder='billed amount')
    # payment amount
    pay_amt1 = pay.number_input("Payment Amount (this month): ", min_value=0, max_value=1_000_000, value=None, placeholder='paid amount')
    pay_amt2 = pay.number_input("Payment Amount (last month): ", min_value=0, max_value=1_000_000, value=None, placeholder='paid amount')
    pay_amt3 = pay.number_input("Payment Amount (2 months ago): ", min_value=0, max_value=1_000_000, value=None, placeholder='paid amount')
    pay_amt4 = pay.number_input("Payment Amount (3 months ago): ", min_value=0, max_value=1_000_000, value=None, placeholder='paid amount')
    pay_amt5 = pay.number_input("Payment Amount (4 months ago): ", min_value=0, max_value=1_000_000, value=None, placeholder='paid amount')
    pay_amt6 = pay.number_input("Payment Amount (5 months ago): ", min_value=0, max_value=1_000_000, value=None, placeholder='paid amount')
    
feat = [limit_bal, 
        encode("Gender", gender), 
        encode('Education',edu), 
        encode('Marital Status',mstat), 
        age, pay_1, pay_2, pay_3, pay_4, pay_5, pay_6, 
        bill_amt1, bill_amt2, bill_amt3, bill_amt4, bill_amt5, bill_amt6, 
        pay_amt1, pay_amt2, pay_amt3, pay_amt4, pay_amt5, pay_amt6]

btn_pred = st.button("Predict Default Risk", use_container_width=True)
if btn_pred:
    st.write("Prediction result here...")
    st.write(name)
    result = predict(feat)
    st.write(result)
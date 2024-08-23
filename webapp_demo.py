import numpy as np
import pickle
import streamlit as st 
import background_test as bgd
loaded_model = pickle.load(open('GBM_model.sav', 'rb'))

def loan_eligibility_prediction(input_data):
    #change into the numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict([input_data])
    print(prediction)
    if (prediction[0] == 0):
        return'the customer is Eligible for the services'
    else:
        return "The subscriber is not eligible for the services"
def main():
    
    # provide title for the App
    st.title("Loan Eligibility Prediction")
    #bgd.sidebar_bg('/home/ubuntu/streamlite_doc/ethio-telecom-office.jpg')
    # getting the input data
    SERVICE_NUMBER = st.text_input("Service number of user")
    CUST_TYPE_NAME = st.text_input("customer type name")
    NET_BUSI_TYPE = st.text_input("Network business of user")
    STATUS_NAME = st.text_input("customer current service status number of user")
    CUST_AGE = st.text_input("customer service age number of user")
    GENDER_NAME = st.text_input("customer gender name")
    OPER_TYPE = st.text_input("operation type of the user")
    INIT_LOAN_AMT = st.text_input("Initial loan amount taken by subscriber")
    LOAN_AMT = st.text_input("subscriber loan amount  of user")
    REPAY_AMT = st.text_input("Service repay  amount of user")
   # LOAN_PENALTY = st.text_input("Customer Loan_penality")
   # LOAN_PENALTY_LEFT = st.text_input("Customer Loan_penality left")
    LOAN_GRADE = st.text_input("customer grade level number of user")
    RECHARGE_CATEGORY = st.text_input("customer recharge category")
    RECHARGE_AMNT = st.text_input("Service charge of subscriberr")
    SMS_LOCAL_USAGE = st.text_input("SMS Local usage")
    SMS_LOCAL_FEE_ETB = st.text_input("service charge fee")
    DATA_USAGE_MB = st.text_input("Service data usage user")
    DATA_REVENUE_ETB = st.text_input("service data revenue user")

    #code prediction
    diagnosis = ''
    # ccreate button for submitting data
    if st.button("Prediction Results"):
        diagnosis = loan_eligibility_prediction([SERVICE_NUMBER, CUST_TYPE_NAME, NET_BUSI_TYPE, STATUS_NAME, CUST_AGE, GENDER_NAME,OPER_TYPE,INIT_LOAN_AMT,LOAN_AMT,REPAY_AMT, LOAN_GRADE, RECHARGE_CATEGORY, RECHARGE_AMNT, SMS_LOCAL_USAGE, SMS_LOCAL_FEE_ETB, DATA_USAGE_MB, DATA_REVENUE_ETB])
        
        st.success(diagnosis)
        
        
if __name__ == '__main__':
    main()
    
    

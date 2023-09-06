# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:44:01 2023

@author: dell1
"""

import numpy as np
import pickle
import streamlit as st


def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList


loaded_model = pickle.load(open('Model/trained_model.sav', 'rb'))
loaded_model_scaled = pickle.load(open('Model/trained_model_scaled.sav', 'rb'))

def churn_predict(input_data):
    input_data_flat = flat(input_data)
    print(input_data_flat)
    input_data_array = np.array([input_data_flat],dtype=(object))
    input_data_scaled = loaded_model_scaled.transform(input_data_array)
    input_data_reshape = input_data_scaled.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    
    
    if prediction[0] == 1:
        return 'the customer is churn'
    else:
        return 'the customer is not churn'
    
def main():
    st.title("Telecom Customer Churn Prediction")
    st.header("Enter the value of the following parameters:")
    
    SeniorCitizen = st.selectbox('Is the person Senior Citizen', ('yes','no'))
    if SeniorCitizen == 'yes':
        SeniorCitizen = 1
    else:
        SeniorCitizen=0
    Partner = st.selectbox('Do the person have partner', ('yes','no'))
    if Partner == 'yes':
        Partner = 1
    else:
        Partner=0
    Dependents = st.selectbox('Do the person have dependents', ('yes','no'))
    if Dependents == 'yes':
        Dependents = 1

    else:
        Dependents=0
    tenure = st.number_input('tenure')
    PaperlessBilling = st.selectbox('Paperless billing', ('yes','no'))
    if PaperlessBilling == 'yes':
        PaperlessBilling = 1
    else:
        PaperlessBilling=0
    MonthlyCharges = st.number_input('Monthly Charges')
    TotalCharges = st.number_input('Total Charges')
    MultipleLines = st.selectbox('Multiple lines used', ('yes','no','No phone service'))
    if MultipleLines == 'yes':
        MultipleLines = [0,0,1]
    elif MultipleLines == 'no':
        MultipleLines = [1,0,0]
    else:
        MultipleLines = [0,1,0]
    InternetService = st.selectbox('Internet Service used', ('DSL','no','Fiber Optic'))
    if InternetService == 'DSL':
        InternetService = [1,0,0]
    elif InternetService == 'Fiber Optic':
        InternetService = [0,1,0]
    else:
        InternetService = [0,0,1]
    OnlineSecurity = st.selectbox('Online Security', ('yes','no','No internet service'))
    if OnlineSecurity == 'No internet service':
        OnlineSecurity = [0,1,0]
    elif OnlineSecurity == 'yes':
        OnlineSecurity = [0,0,1]
    else:
        OnlineSecurity = [1,0,0]
    OnlineBackup = st.selectbox('Online Backup', ('yes','no','No internet service'))
    if OnlineBackup == 'No internet service':
        OnlineBackup = [0,1,0]
    elif OnlineBackup == 'yes':
        OnlineBackup = [0,0,1]
    else:
        OnlineBackup = [1,0,0]
    DeviceProtection = st.selectbox('Device Protection', ('yes','no','No internet service'))
    if DeviceProtection == 'No internet service':
        DeviceProtection = [0,1,0]
    elif DeviceProtection == 'yes':
        DeviceProtection = [0,0,1]
    else:
        DeviceProtection = [1,0,0]
    TechSupport = st.selectbox('Tech Support', ('yes','no','No internet service'))
    if TechSupport == 'No internet service':
        TechSupport = [0,1,0]
    elif TechSupport == 'yes':
        TechSupport = [0,0,1]
    else:
        TechSupport = [1,0,0]
    StreamingTV = st.selectbox('Streaming TV', ('yes','no','No internet service'))
    if StreamingTV == 'No internet service':
        StreamingTV = [0,1,0]
    elif StreamingTV == 'yes':
        StreamingTV = [0,0,1]
    else:
        StreamingTV = [1,0,0]
    StreamingMovies = st.selectbox('Streaming movies', ('yes','no','No internet service'))
    if StreamingMovies == 'No internet service':
        StreamingMovies = [0,1,0]
    elif StreamingMovies == 'yes':
        StreamingMovies = [0,0,1]
    else:
        StreamingMovies = [1,0,0]
    Contract = st.selectbox('Contract', ('Month-to-month','One year','Two year'))
    if Contract == 'One year':
        Contract = [0,1,0]
    elif Contract == 'Two year':
        Contract = [0,0,1]
    else:
        Contract = [1,0,0]
    PaymentMethod = st.selectbox('Payment Method', ('Bank transfer (automatic)','Credit card (automatic)','Electronic check','Mailed check'))
    if PaymentMethod == 'Bank transfer (automatic)':
        PaymentMethod = [1,0,0,0]
    elif PaymentMethod == 'Credit card (automatic)':
        PaymentMethod = [0,1,0,0]
    elif PaymentMethod == 'Electronic check':
        PaymentMethod = [0,0,1,0]
    else:
        PaymentMethod = [0,0,0,1]
        
    print([[SeniorCitizen,Partner,Dependents,tenure,PaperlessBilling,
                                     MonthlyCharges,TotalCharges,MultipleLines,InternetService,
                                     OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,
                                     StreamingTV,StreamingMovies,Contract,PaymentMethod]])
    Churn_pred = ' '
    
    if st.button("Predict customer Churn"):
        Churn_pred = churn_predict([SeniorCitizen,Partner,Dependents,tenure,PaperlessBilling,
                                     MonthlyCharges,TotalCharges,MultipleLines,InternetService,
                                     OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,
                                     StreamingTV,StreamingMovies,Contract,PaymentMethod])
    st.success(Churn_pred)
    
if __name__ == '__main__':
    main()
    


        
    
    
    
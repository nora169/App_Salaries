import streamlit as st
import numpy as np
import pandas as pd
import joblib 
from dummies import *

st.title('What influences Adults Salaries')
st.info('you will just enter some values to predict your salary will be more than 50k or less')

pipe=joblib.load('pipeline--.h5')
age=st.number_input("Age: ")
fnlwgt=st.number_input("fnlwgt: ")
educational_num=st.number_input("Educational-num: ")
capital_gain=st.number_input("capital-gain: ")
capital_loss=st.number_input("capital-loss: ")
hours_per_week=st.number_input("hours-per-week: ")

#hours_per_week=st.slider("hours-per-week: ",0,168,45)
workclass_selection=st.selectbox('workclass',['Local-gov','Private','Self-emp-inc','Self-emp-not-inc','tate-gov','Without-pay','Federal-gov'])
workclass=workclass_dummies[workclass_selection]


education_selection=st.selectbox('education : ',['11th','12th','1st-4th','5th-6th','7th-8th','9th','Assoc-acdm','Assoc-voc','Bachelors',
                                                 'Doctorate','HS-grad','Masters','Preschool','Prof-school','Some-college','10th'] )
education=education_dummies[education_selection]


marital_status_selection=st.selectbox('marital_status: ',['married','single','divorced'])
marital_status=marital_status_dummies[marital_status_selection]


occupation_selection=st.selectbox('occupation: ',['Armed-Forces','Craft-repair','Exec-managerial','Farming-fishing','Handlers-cleaners','Machine-op-inspct',
                                                'Other-service''Priv-house-serv','Prof-specialty','Protective-serv' ,'Sales','Tech-support' ,'Transport-moving',
                                                'Adm-clerical'])
occupation=occupation_dummies[occupation_selection]


relationship_selection=st.selectbox('relationship :',['Not-in-family','Other-relative','Own-child ','Unmarried','Wife','Husband'])
relationship= relationship_dummies[relationship_selection]


race_selection=st.selectbox('race' ,['Asian-Pac-Islander','Black','Other','White','Amer-Indian-Eskimo'])
race=race_dummies[race_selection]

gender_selection=st.selectbox('gender',['Male','Female'])
gender =gender_dummies[gender_selection]

country_selection=st.selectbox('native-country',['United-States','Other'])
country= country_dummies[country_selection]


#st.write(age,fnlwgt,educational_num,capital_gain,capital_loss,hours_per_week,workclass_selection,workclass,
 #        education_selection,education,marital_status_selection,marital_status,occupation_selection,occupation,relationship_selection,relationship,
  #       race_selection,race,gender_selection,gender)
data=[age,fnlwgt,educational_num,capital_gain,capital_loss,hours_per_week]
#st.write(data)
data=data+ workclass+education+marital_status+occupation+relationship+race+gender+country
#st.write(data)

result=pipe.predict([data] )
st.write('is it >50k:',result )
if result == 0:
    result ='<=50k'
else:
    result='>50k'
st.write('your salary will be:',result )

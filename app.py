import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the app.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the model file
ckd_model_path = os.path.join(working_dir, 'kidney.sav')

# Load the pre-trained model
with open(ckd_model_path, 'rb') as model_file:
    CKD_model = pickle.load(model_file)

# Sample values from the provided data
sample_values = {
    "age": 48, "bp": 70, "sg": 1.005, "al": 4, "su": 0, "rbc": 'normal', "pc": 'abnormal',
    "pcc": 'present', "ba": 'notpresent', "bgr": 117, "bu": 56, "sc": 3.8, "sod": 111,
    "pot": 2.5, "hemo": 11.2, "pcv": 32, "wc": 6700, "rc": 3.9, "htn": 'yes', "dm": 'no',
    "cad": 'no', "appet": 'poor', "pe": 'yes', "ane": 'yes'
}

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Health Assistant',
                           ['CKD Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity'],
                           default_index=0)

# ckd prediction page
if selected == 'Chronic kidney disease prediction':
    # page title
    st.title('CKD Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 ,col4 = st.columns(4)
    
    with col1:
        Id = st.text_input('patient ID')

    with col2:
        age = st.text_input('Age')

    with col3:
        bp = st.text_input('Blood Pressure')

    with col4:
        al = st.text_input('Albumin')

    with col1:
        su = st.text_input('Sugar Level')

    with col2:
        bgr = st.text_input('Blood Glucose Random(BGR)')

    with col3:
        bu = st.text_input('Blood Urea')

    with col4:
        sc = st.text_input('Serum Creatinine')
        
    with col1:
        sod = st.text_input('Sodium Level')
        
    with col2:
        hemo = st.text_input('Hemoglobin (Hb) Level')
        
    with col3:
        pcv = st.text_input('Packed Cell Volume(PCV)')
        
        
    # code for Prediction
    ckd_diagnosis = ''

    # creating a button for Prediction

    if st.button('CKD Test Result'):

        user_input = [Id,age,bp,al,su,bgr,bu,sc,sod,hemo,pcv]

        user_input = [float(x) for x in user_input]

        ckd_prediction = ckd_model.predict([user_input])

        if ckd_prediction[0] == 1 :
            ckd_diagnosis = 'THE PATIENT HAS CHRONIC KIDNEY DISEASE'
        else:
            ckd_diagnosis = 'THE PATIENT DOES NOT HAVE CHRONIC KIDNEY DISEASE'

    st.success(ckd_diagnosis)
    
        except ValueError as ve:
            st.error(f'Please enter valid numbers for all fields. ValueError: {ve}')
        except Exception as e:
            st.error(f'An error occurred: {str(e)}')

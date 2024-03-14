import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Multiple Disease Prediction",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/models/diabetes_pred_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/models/heart_pred_model.sav', 'rb'))

asthma_pred_model = pickle.load(open(f'{working_dir}/models/asthma_pred_model.sav', 'rb'))

lungcancer_pred_model = pickle.load(open(f'{working_dir}/models/lungcancer_pred_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes',
                            'Heart Disease',
                            'Asthma','Lung Cancer'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'lungs','cancer'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.slider('Number of Pregnancies', 0, 17, 0)

    with col2:
        Glucose = st.slider('Glucose Level', 0.0, 199.0, 0.0)

    with col3:
        BloodPressure = st.slider('Blood Pressure value', 0.0, 122.0, 0.0)

    with col1:
        SkinThickness = st.slider('Skin Thickness value', 0.0, 99.0, 0.0)

    with col2:
        Insulin = st.slider('Insulin Level', 0.0, 846.0, 0.0)

    with col3:
        BMI = st.slider('BMI value', 0.0, 67.0, 0.0)

    with col1:
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value', 0.07, 2.42, 0.07)

    with col2:
        Age = st.slider('Age of the Person', 21, 81, 21)


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        # user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider('Age', 20, 77, 20)

    with col2:
        sex = st.slider('Sex: 0 = Female; 1 = Male', 0, 1, 0)

    with col3:
        cp = st.slider('Chest Pain types', 0, 3, 0)

    with col1:
        trestbps = st.slider('Resting Blood Pressure', 94, 200, 94)

    with col2:
        chol = st.slider('Serum Cholestoral in mg/dl', 126, 564, 126)

    with col3:
        fbs = st.slider('Fasting Blood Sugar > 120 mg/dl', 0, 1, 0)

    with col1:
        restecg = st.slider('Resting Electrocardiographic results', 0, 2, 0)

    with col2:
        thalach = st.slider('Maximum Heart Rate achieved', 71, 202, 71)

    with col3:
        exang = st.slider('Exercise Induced Angina', 0, 1, 0)

    with col1:
        oldpeak = st.slider('ST depression induced by exercise', 0.0, 6.0, 0.0)

    with col2:
        slope = st.slider('Slope of the peak exercise ST segment', 0, 2, 0)

    with col3:
        ca = st.slider('Major vessels colored by flourosopy', 0, 4, 0)

    with col1:
        thal = st.slider('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', 0, 3, 0)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        # user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)



# asthma Disease Prediction Page
if selected == 'Asthma':

    # page title
    st.title('Asthma Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider('Age', 18, 65, 18)

    with col2:
        Gender = st.slider('Gender: 0 = Female; 1 = Male', 0, 1, 0)

    with col3:
        ss = st.slider('Smoking Status', 0, 2, 0)

    with col1:
        peak = st.slider('Peak Flow  ', 150, 400,150)


    
    # code for Prediction
    asthma_diagnosis = ''

    # creating a button for Prediction

    if st.button('Asthma Disease Test Result'):

        user_input = [age, Gender, ss, peak]

        # user_input = [float(x) for x in user_input]

        asthma_prediction = asthma_pred_model.predict([user_input])

        if asthma_prediction[0] == 1:
            asthma_diagnosis = 'The person is not having asthma'
        else:
            asthma_diagnosis = 'The person does have asthma'

    st.success(asthma_diagnosis)



    
# lungs cancer Disease Prediction Page
if selected == 'LungCancer':

    # page title
    st.title('LungCancer Disease Prediction using ML')

    col1, col2, col3,col4 = st.columns(4)

    with col1:
        age = st.slider('Age', 21, 87, 21)

    with col2:
        Gender = st.slider('Gender: 0 = Female; 1 = Male', 0, 1, 0)

    with col3:
        smoking = st.slider('Smoking Status', 1, 2, 1)

    with col4:
        Yellowfinger = st.slider('Yellow Fingers',1,2,1)

    with col1:
        Anxity = st.slider('Anxity', 1,2,1)

    with col2:
        Pp = st.slider('Peer Pressure',1,2,1)

    with col3:
        Chronic_Des = st.slider('Cronic Disease', 1, 2, 1)

    with col4:
        Fatigue = st.slider('Fatigue',1, 2, 1)   

    with col1:
        Allergy = st.slider('Allergy',1, 2, 1)

    with col2:
        Wheezing = st.slider('Weezing', 1, 2, 1)

    with col3:
       Alcohol_Con  = st.slider('Alcohol Consumption',1, 2, 1)

    with col4:
        Cough= st.slider('Coughing ', 1, 2, 1)   


    with col1:
        Shortnes_Breath = st.slider('Shortness of Breath',1, 2, 1)

    with col2:
     Swallowing_Diff = st.slider('Swallowing Difficulty',1, 2, 1)

    with col3:
      Chest_Pain = st.slider('Chest Pain',1, 2, 1)

   




    
    # code for Prediction
    lungcancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('LungCancer Disease Test Result'):

        user_input = [age, Gender, smoking,Yellowfinger, Anxity,Pp,Chronic_Des,Fatigue,Allergy,Wheezing,Alcohol_Con,Cough,Shortnes_Breath,Swallowing_Diff,Chest_Pain]

        # user_input = [float(x) for x in user_input]

        lungcancer_prediction = lungcancer_pred_model.predict([user_input])

        if lungcancer_prediction[0] == 1:
            lungcancer_diagnosis = 'The person is not having lungcancer'
        else:
            lungcancer_diagnosis = 'The person does have lungcancer'

    st.success(lungcancer_diagnosis)
    

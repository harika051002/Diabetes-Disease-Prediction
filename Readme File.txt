Readme File:

Attained Objectives:

1) Diabetes Prediction
2) Risk Percentage 
3) Food Recommendation
4) Yoga Recommendation
5) Improved Accuracy of Model
6) User Authentication
7) Password Reset using Email 

Project File Structure:

    \---Diabetes 
        |   diabetes.csv
        |   diabetes_data_upload.csv
        |   Early stage diabetes prediction analysis.ipynb
        |   final_asan1_1new.csv
        |   food__dataset new1.csv
        |   manage.py
        |   model.pkl
        |   
        \---DiabetesDiseaseApp
            |    
            +---static
            |   |   diabetes.png
            |   |   gd.jpg
            |   |   img01.jpg
            |   |   style_index.css
            |   |   t1.jpg
            |   |   ty1.webp
            |   |   ty2
            |   |   
            |   +---css
            |   |       Common_css.css
            |   |       Predict_style.css
            |   |       style.css
            |   |       style_yoga.css
            |   |       swiper-bundle.min.css
            |   |       
            |   \---js
            |           DP_script.js
            |           Predict_script.js
            |           script.js
            |           swiper-bundle.min.js
            |           
            +---templates
            |       About.html
            |       AdminScreen.html
            |       analysis.html
            |       BGValues.html
            |       DPridict.html
            |       Food_index.html
            |       index.html
            |       Login.html
            |       password_reset.html
            |       password_reset_complete.html
            |       password_reset_confirm.html
            |       password_reset_done.html
            |       password_reset_email.html
            |       Predict.html
            |       Register.html
            \------ Yoga.html


Modules used:

1) Django, render, request, url
2) pymysql
3) pandas
4) scikit-learn
5) numpy
6) hashlib
7) pickle
8) seaborn
9) matplotlib

Installation and running of project:

1) mkdir Diabetes
2) cd Diabetes
3) pip install django
4) pip install pymysql
5) pip install pandas
6) pip install cryptography 
7) Python manage.py migrate
8) Python manage.py runserver

Datasets:

1) Diabetes Prediction:

     -We have used Early Stage Diabetes Risk Prediction datset.
     -This dataset consists of 16 diseases which will help us to identify, a person is diabetic or not.
     -Dataset link: https://www.kaggle.com/datasets/ishandutta/early-stage-diabetes-risk-prediction-dataset
 
     About the columns in the dataset:

     1. Age               :     The age of the patient in years, ranging from 20 to 65.
     2. Gender            :     The gender of the patient, either Male or Female.
     3. Polyuria          :     Excessive urination, indicated as Yes or No.
     4. Polydipsia        :     Excessive thirst, indicated as Yes or No.
     5. Sudden weight loss:     Rapid weight loss, indicated as Yes or No.
     6. Weakness          :     Generalized weakness, indicated as Yes or No.
     7. Polyphagia        :     Excessive hunger, indicated as Yes or No.
     8. Genital Thrush    :     Yeast infection in the genital area, indicated as Yes or No.
     9. Visual blurring   :     Blurred vision, indicated as Yes or No.
     10. Itching          :     Generalized itching, indicated as Yes or No.
     11. Irritability     :     Generalized irritability, indicated as Yes or No.
     12. Delayed healing  :     Slow wound healing, indicated as Yes or No.
     13. Partial Paresis  :     Partial paralysis, indicated as Yes or No.
     14. Muscle stiffness :     Stiffness in muscles, indicated as Yes or No.
     15. Alopecia         :     Hair loss, indicated as Yes or No.
     16. Obesity          :     Excessive body weight, indicated as Yes or No.
     17. Class            :     The target variable, indicating whether the patient is diabetic (Positive) or not (Negative).
 
    -Random Forest Model Used to train the model with an acuuracy of 97%.

2) Food Recommendation:

    -Dataset consists of various food items list.
    -Columns in the dataset:

     Name       : Name of the food item
     catagory   : Categorize items based on whether they belong to soup, sweets, snacks, etc.
     description: Description on what are the ingredients necessary to prepare the item.
     Veg_Non    : Classify item as Veg or Non_Veg.
     Nutrient   : Provides which nutrient is present in the item.
     Disease    : Provides for which patients these items to be recommended.
     
    
3) Yoga Recommendation:
  
    -Dataset consists of various yoga asanas description along with some benifits and awareness about who to perform those asanas.
    -Columns in the dataset:
  
    AName       : Name of the asanas.
    Description : How to perform the asanas step by step process is explained.
    Benefits    : What are the benifits that we get from this asana.
  Contraindications: Who should not perform these anasas.
    Level       : Indicate asanas are for beginners level,Intermediate level or Advanced level.

            
                                        
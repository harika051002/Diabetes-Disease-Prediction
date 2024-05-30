from django.shortcuts import render
from django.template import RequestContext
import pymysql
from sklearn.model_selection import train_test_split
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
import hashlib
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import connection
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier


def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})
    
def Login(request):
    if request.method == 'GET':
       return render(request, 'Login.html', {})

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})


    
def home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'About.html')

def Yoga(request):
    return render(request,'Yoga.html',{})

    
def DPridict(request):
    if request.method == 'GET':
       return render(request, 'DPridict.html', {})
    
def Logs(request):
    if request.method == 'GET':
       return render(request, 'Logs.html', {})


@login_required
def admin_screen(request):
    return render(request, 'AdminScreen.html')



# Your MySQL connection configuration
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'harika',
    'database': 'DiabetesDisease',
    'autocommit': True,
}

# Create a connection to the database
conn = pymysql.connect(**db_config)

def check_password(input_password, stored_password):
    # Check if the hashed input password matches the stored password
    return encrypt_password(input_password) == stored_password

def encrypt_password(password):
    # Use a secure method to encrypt the password, such as hashlib.sha256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

glo_username = None

def UserLogin(request):
    global glo_username
    if request.method == 'POST':
        username = request.POST['t1']
        password = request.POST['t2']

        glo_username = username
        
        # Connect to MySQL and check user credentials
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM register WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and check_password(password, user[1]):  # Assuming the password is in the second column
            cursor.close()
            return render(request, "AdminScreen.html", {'error': 'Welcome ' + username})
        else:
            cursor.execute("SELECT * FROM register WHERE username = %s", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                cursor.close()
                return render(request, "Login.html", {'error': 'Password is Incorrect'})
            else:
                cursor.close()
                return render(request, "Login.html", {'error': 'User not Registered!!'})

    return render(request, "Login.html", {'error': ''})

def password_reset(request):
    return render(request,'password_reset.html',{})

def password_reset_done(request):
    return render(request,'password_reset_done.html',{})

from django.contrib.auth.views import PasswordResetConfirmView

def password_reset_confirm(request, uidb64, token, *args, **kwargs):
    return PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url='/password_reset_done.html/'  # Redirect to a success page after password reset
    )(request, uidb64=uidb64, token=token, *args, **kwargs)



from django.utils.encoding import force_str

glo_email = None
def password_reset(request):
    global glo_email
    if request.method == 'POST':
        email = request.POST.get('t1','')
        checkbox = request.POST.get('t2','')
        print(checkbox)
        glo_email = email

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM register WHERE email = %s", [email])
            existing_user_data = cursor.fetchone()

        if not existing_user_data:
            return render(request, "Register.html", {'error': 'User Does not exist.'})

        user_name = existing_user_data[0]
        # Convert the tuple to a User model instance
        existing_user = User(email=existing_user_data[2])

        # Generate a unique token for the user
        token = default_token_generator.make_token(existing_user)

        # Construct the password reset link
        reset_url = request.build_absolute_uri(reverse('password_reset_confirm', args=[existing_user.pk, token]))

        # Send the password reset email
        subject = 'Password Reset Request'
        message = f'Click the following link to reset your password:\n\n{reset_url}'

        if checkbox == 'on':
            message = f'Your username is : {user_name} \n\n Click the following link to reset your password:\n\n{reset_url}'
       
        recipient_list = [email]

        send_mail(subject, message,'mamidipalliharika@gmail.com', recipient_list)
        

        cursor.close()
        return render(request, "password_reset_done.html")
    
    return render(request, "password_reset.html")


def password_reset_done(request, uidb64=None, token=None):
    return render(request, 'password_reset_done.html', {'uidb64': uidb64, 'token': token})

def password_reset_update(request):
    global glo_email
    if request.method == 'POST':
        new_password = request.POST['t1']
        con_password = request.POST['t2']

        if new_password != con_password :
            return render(request,'password_reset_confirm.html',{'error': 'Passwords Do Not Match'})
        
        email = glo_email
        cursor = conn.cursor()
        encrypted_password = encrypt_password(new_password)
        cursor.execute("update register set password = %s where email = %s",(encrypted_password,email))
        conn.commit()
        cursor.close()

        return render(request,'Login.html',{'error': 'Password reset completed'})
    return render(request,"password_reset_done.html")


def Signup(request):
    if request.method == 'POST':
        username = request.POST['t3']
        password = request.POST['t4']
        conform_password = request.POST['t7']
        email = request.POST['t5']

        # Check if the user already exists
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM register WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            return render(request, "Register.html", {'error': 'Username exists!'})

        cursor.execute("SELECT * FROM register WHERE email = %s", (email,))
        existing_email = cursor.fetchone()

        if existing_email:
            cursor.close()
            return render(request, "Register.html", {'error': 'Email already registered'})

        if password != conform_password:
            cursor.close()
            return render(request, "Register.html", {'error': 'Passwords do not match.'})

        # Encrypt the password
        encrypted_password = encrypt_password(password)

        # Insert the new user into the database
        cursor.execute("INSERT INTO register (username, password, email) VALUES (%s, %s, %s)",
               (username, encrypted_password, email))

        conn.commit()
        cursor.close()
        return render(request, "Login.html", {'error': 'You can log in now'})

    return render(request, "Register.html", {'error': ''})

def save(request):
    global glo_username
    if request.method == 'POST' :
        glucosevalue = request.POST['t1']
        date = request.POST['t2']
        username = glo_username

        cursor = conn.cursor()
        cursor.execute("INSERT INTO glucosedata(username,glucose_value,date) VALUES (%s,%s,%s)",(username,glucosevalue,date))
        conn.commit()
        cursor.close()

        cursor = conn.cursor()
        desired_username = username
        query = f"SELECT glucose_value, date FROM glucosedata WHERE username = '{desired_username}'"
        cursor.execute(query)
        data = cursor.fetchall()

        result_data = [{'glucose_value': glucose, 'date': date} for glucose, date in data]
        return render(request,"BGValues.html",{'result_data': result_data})
    return render(request,"BGValues.html")



def analysisevl(request):
    global glo_username
    if request.method == 'POST':
        username = glo_username
        cursor = conn.cursor()
        cursor.execute("SELECT glucose_value, date FROM glucosedata WHERE username=%s", (username,))

        data = cursor.fetchall()
        conn.commit()
        cursor.close()

        result_data = [{'glucose_value': glucose_value, 'date': date.strftime('%Y-%m-%d')} for glucose_value, date in data]

        return render(request,"analysis.html",{'data': result_data})
    return render(request,"analysis.html")
from datetime import datetime
df = pd.read_csv(r"C:\Users\HP\Downloads\Diabetes Disease-20240225T083028Z-001 (2)\Diabetes Disease-20240225T083028Z-001\Diabetes Disease\diabetes_data_upload.csv")
df['class'] = df['class'].apply(lambda x: 0 if x=='Negative' else 1)
Y = df['class']
X = df.drop('class', axis=1)
objectList = X.select_dtypes(include = "object").columns
#Label Encoding for object to numeric conversion
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for feature in objectList:
    X[feature] = le.fit_transform(X[feature].astype(str))
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size = 0.3,random_state=1)
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)
X = ss.fit_transform(X)
rf_model = RandomForestClassifier(n_estimators=15, random_state = 0)
rf_model.fit(X_train,y_train)
rf_pred = rf_model.predict(X_test)

def pridictAc(request):
    global glo_username
    if request.method == 'POST':
        age = request.POST.get('t1')
        gender = request.POST.get('t2')
        polyuria = request.POST.get('t3')
        polydipsia = request.POST.get('t4')
        partial_paresis = request.POST.get('t5')
        swl = request.POST.get('t6')
        irritability = request.POST.get('t7')
        delayed_healing = request.POST.get('t8')
        alopecia = request.POST.get('t9')
        itching = request.POST.get('t10')
        obesity = request.POST.get('t14')
        muscle_stiffness = request.POST.get('t13')
        visual_blurring = request.POST.get('t12')
        genital_thrush = request.POST.get('t11')
        weakness = request.POST.get('t15')
        polyphagia = request.POST.get('t16')
        arr = [age, gender, polyuria, polydipsia, swl,
       weakness, polyphagia, genital_thrush, visual_blurring,
       itching, irritability, delayed_healing, partial_paresis,
       muscle_stiffness, alopecia, obesity]
        username = glo_username
       
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        temp = np.asarray(arr).reshape(1,-1)
        predictions = rf_model.predict_proba(temp)[0,1]
        risk = predictions
        output1 = ""
        output2 = ""

        if risk < 0.3:
            output1 = "You are probably in good health, keep it up."
            output2 = "Your Diabetes Risk Index is {:.2f}%".format(risk * 100)
        elif risk >= 0.9:
            output1 = "Sorry to say this, you may have diabetes."
            output2 = "Your Diabetes Risk Index is {:.2f}%".format(risk * 100)
        elif 0.5 < risk < 0.9:
            output1 = "Odds are high you have diabetes."
            output2 = "Your Diabetes Risk Index is {:.2f}%".format(risk * 100)
        else:
            output1 = "You should be alright for the most part, but take care not to let your health slip."
            output2 = "Your Diabetes Risk Index is {:.2f}%".format(risk * 100)

        output = output1 + " " + output2
        cursor = conn.cursor()
        cursor.execute("INSERT INTO HealthData (username, Age, Gender, Polyuria, Polydipsia, `sudden_weight_loss`, weakness, Polyphagia, `Genital_thrush`, `visual_blurring`, Itching, Irritability, `delayed_healing`, `partial_paresis`, `muscle_stiffness`, Alopecia, Obesity, output,Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
        (username, age, gender, polyuria, polydipsia, swl,
        weakness, polyphagia, genital_thrush, visual_blurring,
        itching, irritability, delayed_healing, partial_paresis,
        muscle_stiffness, alopecia, obesity, output,current_date))



        return render(request, "DPridict.html", {'error': output1 + " " + output2})
    
    return render(request,"DPridict.html")

def log(request):
    global glo_username
    data = None
    if request.method == 'POST':
        cursor = conn.cursor()
        desired_username = glo_username
        query = f"SELECT * from HealthData WHERE username = '{desired_username}'"
        cursor.execute(query)
        
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        print(data)

        return render(request,"Logs.html",{'data':data})
    return render(request,"Logs.html")


def filter_food(nutrient, disease):
    foods_df = pd.read_csv(r"C:\Users\HP\Downloads\Diabetes Disease-20240225T083028Z-001 (2)\Diabetes Disease-20240225T083028Z-001\Diabetes Disease\food__dataset new1.csv",encoding_errors="ignore")
    filtered_food = foods_df[
        (foods_df['Veg_Non'].str.contains(nutrient, case=False)) &
        (foods_df['Disease'].str.contains(disease, case=False))
    ]
    return filtered_food


def Food_index(request):
    return render(request, 'Food_index.html')

def result(request):
    if request.method == 'POST':
        nutrient = request.POST.get('nutrient')
        disease = request.POST.get('disease')

        filtered_food = filter_food(nutrient, disease)
        hide = ['Disease', 'Diet', 'Meal_Id', 'Price']
        df = filtered_food.drop(columns=hide)

        if df.empty:
            return render(request, 'Food_index.html', {'message': "Sorry, no recommendations found"})
        else:
            result_data = df.to_dict(orient='records')
            return render(request, 'Food_index.html', {'result_data': result_data, 'table_type': 'food'})

    return render(request, 'Food_index.html', {'message': ''})


asanas_df = pd.read_csv(r"C:\Users\HP\Downloads\Diabetes Disease-20240225T083028Z-001 (2)\Diabetes Disease-20240225T083028Z-001\Diabetes Disease\final_asan1_1new.csv")
columns = ['AID', 'You tube Vdo link','Photo', 'References','Variations','Contraindications','Level','Breathing','awareness']
asanas_df.drop(columns=columns,inplace=True)
asanas_df['Benefits'].fillna(0, inplace=True)
asanas_df['Description'].fillna(0, inplace=True)
asanas_df = asanas_df.drop(asanas_df[asanas_df['Benefits']==0].index) 
asanas_df = asanas_df.drop(asanas_df[asanas_df['Description']==0].index) 

def filter_asana(disease):
    filtered_asanas = asanas_df[
        (asanas_df['Benefits'].str.contains(disease)) 
    ]
    return filtered_asanas

def result_yoga(request):
    if request.method == 'POST':
        disease = request.POST.get('disease')
        filtered_asanas = filter_asana( disease)
        df = filtered_asanas
        if df.empty:
            return render(request, 'Yoga.html', {'message': "Sorry, no recommendations found"})
        else:
            result_data =  df.to_dict(orient='records')
            return render(request, 'Yoga.html', {'result_data': result_data})

    return render(request, 'Yoga.html', {'message': ''})








 
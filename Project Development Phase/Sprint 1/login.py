#imports

import pyrebase
import streamlit as st
from datetime import datetime
import joblib
import pandas as pd
from collections.abc import Mapping

from email_validator import validate_email, EmailNotValidError

#configuration key

firebaseConfig = {
    'apiKey': "AIzaSyBW9IPsQGqk9qrXsgyL8TZpnQ4MacWgc70",
    'authDomain': "test-firestore-streamlit-13160.firebaseapp.com",
    'projectId': "test-firestore-streamlit-13160",
    'databaseURL': "https://console.firebase.google.com/u/0/project/test-firestore-streamlit-13160/database/test-firestore-streamlit-13160-default-rtdb/data/~2F",
    'storageBucket': "test-firestore-streamlit-13160.appspot.com",
    'messagingSenderId': "703800935011",
    'appId': "1:703800935011:web:60fd49fa5c4d09eb002e56",
    'measurementId': "G-GR57GQVJC3"
  }

#firebase authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#database

db = firebase.database()
storage = firebase.storage()

st.sidebar.title("Heart Disease Prediction")

#authentication
choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

email = st.sidebar.text_input("Please enter your email address")
password = st.sidebar.text_input("Please enter your password")


if choice == 'Sign up':
    handle = st.sidebar.text_input("Please input your username", value = 'Default')
    submit = st.sidebar.button("Create my Account")

    if submit:
        try:
            if email=='' or password=='':
                st.error("Please fill the empty email or password")
            else:
                
                try:                
                    validation = validate_email(email)        
                    user = auth.create_user_with_email_and_password(email, password)
                    st.success("Your account is created successfully")
                    #st.balloons()
                    st.title("Welcome "+handle+" !!")
                    st.header("Login to view dashboard")
                except EmailNotValidError as e:
                    st.error("enter valid email")

        except:
            st.error("email already exists")
        
if choice == 'Login':
    login = st.sidebar.button('Login')
    if login:
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            st.write("please wait while you are being redirected to the dashboard...")

        except:
            st.error("incorrect email/password")
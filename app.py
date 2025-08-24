from flask import Flask, redirect, request, jsonify, render_template, url_for
from flask import session
import requests
import os


BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8500')

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "saas_secret_key"

@app.route('/')
def hello_world():
    # Check if user is logged in
    user_name = session.get("user_name")
    user_email = session.get("user_email")
    initial = session.get("initial")
    
    return render_template('index.html', 
                         user_name=user_name,
                         user_email=user_email,
                         initial=initial,
                         is_logged_in=bool(user_name))

@app.route('/submit_signup', methods=['POST'])
def submit_signup():
    form_data = dict(request.form)
    
    try:
        response = requests.post(f"{BACKEND_URL}/signup", json=form_data)
        response_data = response.json()
        
        if response.status_code == 200:
            # Successful signup - redirect to hello_world
            return redirect(url_for('hello_world'))
        else:
            # Show error message
            error_msg = response_data.get("message", "Failed to create account")
            return render_template('SignUp.html', error=error_msg), response.status_code
            
    except requests.exceptions.RequestException as e:
        return render_template('SignUp.html', error="Server connection error"), 500

@app.route('/signin', methods=['POST'])
def signin():
    credentials = {
        "email": request.form.get("email"),
        "password": request.form.get("password")
    }
    
    try:
        response = requests.post(f"{BACKEND_URL}/login", json=credentials)
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("status") == "success":
                user_name = response_data.get("user_name")
                user_email = response_data.get("user_email")
                initial = response_data.get("initial")
                
                # Store in session
                session['initial'] = initial
                session['user_name'] = user_name
                session['user_email'] = user_email

                # Redirect to index page instead of dashboard
                return redirect(url_for('hello_world'))
            else:
                return render_template('SignIn.html', error="Invalid credentials"), 401
        else:
            return render_template('SignIn.html', error="Login failed"), response.status_code

    except requests.exceptions.RequestException as e:
        return render_template('SignIn.html', error="Server connection error"), 500

@app.route('/logout')
def logout():
    # Clear session
    session.clear()
    return redirect(url_for('hello_world'))

@app.route('/signup_page')
def signup_page():
    return render_template('SignUp.html')  # Make sure this matches your actual file name

@app.route('/signin_page')
def signin_page():  
    return render_template('SignIn.html')

@app.route('/dashboard')
def dashboard():
    user_name = session.get("user_name")
    user_email = session.get("user_email")
    initial = session.get("initial")
    
    # Redirect to signin if not logged in
    if not user_name:
        return redirect(url_for('signin_page'))
        
    return render_template("dashboard/Dashboard.html",
                           user_name=user_name,
                           user_email=user_email,
                           initial=initial)

@app.route('/achievement')
def achievement():
    user_name = session.get("user_name")
    user_email = session.get("user_email")
    initial = session.get("initial")
    
    # Redirect to signin if not logged in
    if not user_name:
        return redirect(url_for('signin_page'))
        
    return render_template("dashboard/Achievements.html",
                           user_name=user_name,
                           user_email=user_email,
                           initial=initial)

@app.route('/ai_coach')
def ai_coach():
    user_name = session.get("user_name")
    user_email = session.get("user_email")
    initial = session.get("initial")
    
    # Redirect to signin if not logged in
    if not user_name:
        return redirect(url_for('signin_page'))
        
    return render_template("dashboard/AI-Coach.html",
                           user_name=user_name,
                           user_email=user_email,
                           initial=initial)

@app.route('/habits')
def habits():
    user_name = session.get("user_name")
    user_email = session.get("user_email")
    initial = session.get("initial")
    
    # Redirect to signin if not logged in
    if not user_name:
        return redirect(url_for('signin_page'))
        
    return render_template("dashboard/Habits.html",
                           user_name=user_name,
                           user_email=user_email,
                           initial=initial)

@app.route('/moodtracker')
def moodtracker():
    user_name = session.get("user_name")
    user_email = session.get("user_email")
    initial = session.get("initial")
    
    # Redirect to signin if not logged in
    if not user_name:
        return redirect(url_for('signin_page'))
        
    return render_template("dashboard/MoodTracker.html",
                           user_name=user_name,
                           user_email=user_email,
                           initial=initial)

@app.route('/setting')
def setting():
    user_name = session.get("user_name")
    user_email = session.get("user_email")
    initial = session.get("initial")
    
    # Redirect to signin if not logged in
    if not user_name:
        return redirect(url_for('signin_page'))
        
    return render_template("dashboard/Settings.html",
                           user_name=user_name,
                           user_email=user_email,
                           initial=initial)

if __name__ == '__main__':
    app.run(port=9500, host='0.0.0.0', debug=True)
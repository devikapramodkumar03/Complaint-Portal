from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_for_dev'

# --- Corrected Data Structures ---

# SINGLE source of truth for user data.
VALID_USERS = {
    "citizen@email.com": {
        "password": "password123",
        "name": "Priya Sharma",
        "member_since": "2024-08-15"
    },
    "official@citizenconnect.gov.in": {
        "password": "adminpass",
        "name": "Rohan Gupta",
        "member_since": "2024-01-26"
    }
}

# FIXED: Added the 'citizen' key to link complaints to users.
MOCK_COMPLAINTS = [
    {
        "id": "CC001",
        "title": "Broken streetlight on Sector 15 main road",
        "date_submitted": "2025-09-15",
        "status": "Resolved",
        "citizen": "Priya Sharma" # <-- This was missing
    },
    {
        "id": "CC002",
        "title": "Pothole near Alpha I commercial belt",
        "date_submitted": "2025-09-12",
        "status": "In Progress",
        "citizen": "Priya Sharma" # <-- This was missing
    },
    {
        "id": "CC003",
        "title": "Irregular garbage collection in Gamma II",
        "date_submitted": "2025-09-17",
        "status": "Submitted",
        "citizen": "Amit Kumar" # <-- Added another citizen for example
    },
    {
        "id": "CC004",
        "title": "Leaking water pipe near the city park",
        "date_submitted": "2025-09-16",
        "status": "Submitted",
        "citizen": "Priya Sharma" # <-- This was missing
    }
]


# --- Routes ---

@app.route('/')
def home():
    """Renders the main landing page."""
    # Ensure you have a 'home.html' in your templates folder.
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles the login process."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # FIXED: Authenticate against the single VALID_USERS dictionary.
        user_data = VALID_USERS.get(email)
        if user_data and user_data['password'] == password:
            session['user_email'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        flash('You must be logged in to view this page.', 'warning')
        return redirect(url_for('login'))

    user_email = session['user_email']
    user_data = VALID_USERS.get(user_email)
    
    if user_email == "citizen@email.com":
        # This code now works because the 'citizen' key exists.
        citizen_complaints = [c for c in MOCK_COMPLAINTS if c.get('citizen') == user_data['name']]
        return render_template('dashboard.html', user=user_data, complaints=citizen_complaints)
    
    elif user_email == "official@citizenconnect.gov.in":
        stats = {
            'total': len(MOCK_COMPLAINTS),
            'submitted': len([c for c in MOCK_COMPLAINTS if c['status'] == 'Submitted']),
            'in_progress': len([c for c in MOCK_COMPLAINTS if c['status'] == 'In Progress']),
            'resolved': len([c for c in MOCK_COMPLAINTS if c['status'] == 'Resolved'])
        }
        return render_template('official_dashboard.html', user=user_data, complaints=MOCK_COMPLAINTS, stats=stats)
    
    else:
        return redirect(url_for('logout'))

@app.route('/add_complaint', methods=['POST'])
def add_complaint():
    if 'user_email' not in session:
        return redirect(url_for('login'))
    flash('Your complaint has been registered successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/update_status/<complaint_id>', methods=['POST'])
def update_status(complaint_id):
    """Handles updating the status of a complaint."""
    if 'user_email' not in session or session['user_email'] != "official@citizenconnect.gov.in":
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('login'))
    
    new_status = request.form.get('status')
    
    complaint_found = False
    for complaint in MOCK_COMPLAINTS:
        if complaint['id'] == complaint_id:
            complaint['status'] = new_status
            complaint_found = True
            break
    
    if complaint_found:
        flash(f'Status for complaint {complaint_id} updated to "{new_status}".', 'success')
    else:
        flash(f'Complaint {complaint_id} not found.', 'danger')
        
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    """Logs the user out by clearing the session."""
    session.pop('user_email', None)
    flash('You have been successfully logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
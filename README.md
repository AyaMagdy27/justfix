# Just Fix - Home Service Application

A Python Flask web application for connecting customers with home service professionals in 4 key areas: Electrical, Plumbing, Carpentry, and Locksmith services.

## Features

- **Homepage**: Overview of all 4 service areas with detailed descriptions
- **User Authentication**: Secure login and signup system
- **Service Requests**: Submit detailed complaints/requests for any of the 4 service areas
- **Professional Design**: Blue and black themed responsive interface
- **Database Integration**: SQLite database for user and complaint management

## Service Areas

1. **Electrical Services** ⚡
   - Circuit repairs and installations
   - Lighting fixtures and switches
   - Electrical safety inspections
   - Power outlet installations

2. **Plumbing Services** 🔧
   - Leak detection and repair
   - Pipe installations and replacements
   - Drain cleaning and unclogging
   - Fixture installations

3. **Carpentry Services** 🔨
   - Furniture assembly and repair
   - Custom shelving and storage
   - Door and window installations
   - Deck and fence construction

4. **Locksmith Services** 🔑
   - Lock installation and replacement
   - Emergency lockout assistance
   - Key duplication and cutting
   - Security system installations

## Installation

1. **Install Python 3.7+** if not already installed

2. **Clone or download** this project to your local machine

3. **Navigate to the project directory**:
   ```bash
   cd just_fix_app
   ```

4. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **The application will automatically**:
   - Create the SQLite database (`justfix.db`)
   - Set up the necessary tables for users and complaints
   - Start the development server

## Usage

### For New Users:
1. Visit the homepage to learn about our services
2. Click "Sign Up" to create a new account
3. Fill out the registration form with username, email, and password
4. Login with your credentials

### For Existing Users:
1. Click "Login" and enter your username and password
2. Once logged in, you can submit service requests
3. Click "New Complaint" to access the service request form

### Submitting Service Requests:
1. Select your service type (Electrical, Plumbing, Carpentry, or Locksmith)
2. Provide a clear title for your request
3. Write a detailed description of your needs
4. Include your phone number for contact
5. Provide the full service address
6. Submit your request

## File Structure

```
just_fix_app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── justfix.db         # SQLite database (created automatically)
└── templates/         # HTML templates
    ├── base.html      # Base template with navigation and styling
    ├── homepage.html  # Homepage with service information
    ├── login.html     # User login page
    ├── signup.html    # User registration page
    └── complaint.html # Service request form
```

## Database Schema

### Users Table:
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- created_at

### Complaints Table:
- id (Primary Key)
- user_id (Foreign Key)
- service_type (electrical, plumbing, carpenter, locksmith)
- title
- description
- phone
- address
- status (default: 'pending')
- created_at

## Security Features

- Password hashing using Werkzeug security
- Session management for user authentication
- Form validation and error handling
- SQL injection prevention with parameterized queries

## Customization

You can easily customize the application by:

1. **Changing colors**: Edit the CSS in `templates/base.html`
2. **Adding new service types**: Update the dropdown options in `complaint.html`
3. **Modifying the database schema**: Edit the `init_db()` function in `app.py`
4. **Adding new pages**: Create new templates and routes

## Production Deployment

For production use, consider:

1. **Change the secret key** in `app.py` to a secure random value
2. **Use a production database** like PostgreSQL instead of SQLite
3. **Set up proper logging** and error handling
4. **Configure HTTPS** for secure communications
5. **Use a production WSGI server** like Gunicorn instead of Flask's development server

## Support

For support or questions about this application, contact:
- Email: support@justfix.app
- Phone: (555) 123-4567

## License

This project is open source and available under the MIT License.

# Django CRM
Django CRM is a web application that allows users to manage their customers, products, orders, and invoices. It is built with Django, a high-level Python web framework that follows the model-template-view (MTV) pattern. It also uses Bootstrap, a popular front-end framework, to create responsive and user-friendly interfaces.
# Features
**User authentication**: Users can register, log in, and log out of the application. They can also reset and change their passwords using email verification.
**Session handling**: Users can see their session information and activity on the profile page. They can also end their sessions on other devices.
**CRM**: Users can view, create, update, and delete customers, products, orders, and invoices. They can also filter, search, and sort the data using various criteria.
**Admin access**: Users with admin privileges can access the Django admin site, where they can manage the models, users, groups, and permissions of the application.
**Future features**: Some of the features that are planned to be added in the future are:
    **Pagination**: Users can navigate through the data using pagination buttons.
    **Charts**: Users can see the statistics and trends of the data using charts and graphs.
    **Export**: Users can export the data to different formats, such as CSV, PDF, etc.

# Installation
To install and run this project on your local machine, follow these steps:

**Prerequisites**: Make sure you have Python 3.6 or higher and Django 3.0 or higher installed on your system. You can check the versions using these commands:
`python --version`
`django-admin --version`

**Clone the repository**: Clone the repository using this command:
`git clone https://github.com/your-username/django-crm.git`

**Create and activate a virtual environment**: Create a virtual environment using this command:
`python -m venv venv`

Then, activate it using this command:

`source venv/bin/activate # Linux/macOS`
`venv\Scripts\activate # Windows`

**Install the requirements**: Install the required packages using this command:
`pip install -r requirements.txt`

**Migrate the database**: Migrate the database using this command:
`python manage.py migrate`

**Create a superuser**: Create a superuser account using this command:
`python manage.py createsuperuser`

**Run the server**: Run the server using this command:
`python manage.py runserver`

**Access the application**: Open your browser and go to http://127.0.0.1:8000/ to access the application. You can also go to http://127.0.0.1:8000/admin/ to access the admin site.

# Usage
To use this application, follow these steps:

**Register**: To create a new user account, go to the register page and fill in the required fields. You will receive an email with a link to activate your account.
**Log in**: To log in to the application, go to the login page and enter your username and password. You will be redirected to the home page, where you can see your dashboard with the summary of the data.
**Reset and change password**: To reset your password, go to the password reset page and enter your email address. You will receive an email with a link to reset your password. To change your password, go to the password change page and enter your old and new passwords.
**Manage customers**: To manage your customers, go to the customers page, where you can see the list of all your customers. You can also create, update, or delete a customer by clicking on the corresponding buttons. You can also filter, search, and sort the customers by various criteria, such as name, email, phone, etc.
**Access the admin site**: To access the admin site, go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials. You can manage the models, users, groups, and permissions of the application on this site.

# Support
If you have any questions or issues with this project, you can contact me at muhammedafsalafzz@gmail.com. You can also report bugs or request features by creating an issue on GitHub.

# Contribution
If you want to contribute to this project, you are welcome to do so. Please follow these steps:

**Fork the repository**: Fork the repository on GitHub by clicking on the fork button on the top right corner of the page.
**Clone the repository**: Clone the forked repository on your local machine using this command:
`git clone https://github.com/your-username/django-crm.git`

**Create a branch**: Create a new branch for your feature or bug fix using this command:
`git checkout -b feature-or-bug-fix`

**Make changes**: Make your changes to the code and commit them using this command:
`git commit -am "Add feature or fix bug"`

**Push changes**: Push your changes to the remote repository using this command:
`git push origin feature-or-bug-fix`

**Create a pull request**: Create a pull request on GitHub by clicking on the pull request button on the repository page. Provide a clear and concise description of your changes and the purpose of your pull request.

**Wait for feedback**: Wait for feedback from the project maintainer or other contributors. If there are any comments or suggestions, address them accordingly.

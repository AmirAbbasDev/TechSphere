# TechSphere

**TECHSPHERE** is a full-stack blog application developed using the Django web framework. The application allows users to create, manage, and share blog posts with a clean, user-friendly interface. The project integrates a responsive front-end powered by Tailwind CSS and provides robust back-end features such as user authentication, post creation, and database management.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation Instructions](#installation-instructions)
5. [Usage](#usage)
6. [Linux Setup using Bash Script](#linux-setup-using-bash-script)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Overview

TechSphere is designed as a simple, yet feature-rich blogging platform that leverages the power of Django for the back-end and Tailwind CSS for the front-end. It includes essential features like user registration, post management, and a seamless user experience. The application is intended for both beginners who want to learn Django and developers who wish to contribute to an open-source project.

---

## Features

- **User Authentication:** Secure user registration, login, and logout functionality.
- **Blog Post Management:** Create, edit, delete, and display blog posts.
- **Responsive Design:** Clean and responsive UI built with Tailwind CSS for an optimized experience on all devices.
- **Database Integration:** Simple database operations (migrations, schema setup) to ensure data integrity.
- **Development Environment:** A virtual environment to manage project dependencies effectively.

---

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** Tailwind CSS
- **Database:** SQLite (default for development)
- **Version Control:** Git & GitHub
- **Virtual Environment:** Python `venv`
- **Package Management:** pip (requirements.txt)

---

## Installation Instructions

## Linux Setup using Bash Script

For Linux users, you can simplify the setup process by using the provided Bash script to automatically configure the environment and run the application.

### Steps to Use the Bash Script:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/TechSphere.git
   cd TechSphere
   ```

2. **Make the script executable:**

   ```bash
   chmod +x setup.sh
   ```

3. **Run the script:**
   ```bash
   ./setup.sh
   ```

This script will automatically:

- Create and activate the Python virtual environment.
- Install the required dependencies from `requirements.txt`.
- Apply database migrations.
- Start the Django development server on port 5600.

---

### For All Users:

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   https://github.com/AmirAbbasDev/TechSphere.git
   cd TechSphere
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database migrations:**

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Run the Django development server:**

   ```bash
   python3 manage.py runserver 5600
   ```

   The application will be accessible at `http://127.0.0.1:5600` in your web browser.

---

## Usage

After starting the development server, you can access the following pages in the browser:

- **Homepage:** Displays a list of recent blog posts.
- **Login Page:** Users can log in to their account to manage their posts.
- **Registration Page:** New users can sign up for an account.
- **Create Post:** Users can create and publish blog posts.
- **Post Detail:** View the details of individual blog posts.

---

## Contributing

We welcome contributions to **TechSphere**! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your modifications.
4. Submit a pull request with a description of your changes.

Please ensure your code adheres to the project's coding standards and passes all tests before submitting a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

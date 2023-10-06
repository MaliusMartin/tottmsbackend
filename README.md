

# Django TOTTMS Backend



## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

The Django TOTTMS Backend is the server-side component of the Tamisemi Online Teacher Transfer Management System. It provides the backend logic and API endpoints for managing teachers, their attendance, and related data.

## Project Overview
This project consists of two main components that work seamlessly together:
### Backend (Django)- 
The backend of this project is built using Django, a powerful Python web framework. It serves as the server-side component responsible for managing data, authentication, and handling requests from the frontend.

### Frontend (Next.js, TypeScript, Tailwind CSS)- 
The frontend of this project is developed with Next.js, a popular React framework. It uses TypeScript for type safety and Tailwind CSS for styling, providing a responsive and visually appealing user interface.

- To facilitate communication between the backend and frontend, Axios, a promise-based HTTP client, is utilized. Axios enables seamless data exchange, allowing the frontend to make API requests to the Django backend.
By combining the strengths of Django, Next.js, TypeScript, Tailwind CSS, and Axios, this project provides a robust and efficient web application solution. The backend handles data and logic, while the frontend delivers an engaging user experience.

## Features

- User authentication and authorization.
- CRUD (Create, Read, Update, Delete) operations for teachers.
- Attendance tracking for teachers.
- Comprehensive API for integration with frontend applications.
- Customizable and extendable to suit your specific requirements.

## Getting Started

To get started with the Django TOTTMS Backend, follow the instructions below.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/tottms-backend.git


2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv tottms_env
   ```

3. Activate the virtual environment:

   - **Windows**:

     ```bash
     tottms_env\Scripts\activate
     ```

   - **Linux/macOS**:

     ```bash
     source tottms_env/bin/activate
     ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the backend, you need to configure the database and other settings. 


Copy the `.env.example` file to `.env` and adjust the configuration settings as needed.

```bash
cp .env.example .env
```

Edit the `.env` file to set your database credentials and other configuration options.

## Usage

To start the Django TOTTMS Backend, run the following commands:

```bash
python manage.py migrate
python manage.py createsuperuser  # Create an admin user (follow the prompts)
python manage.py runserver
```

You can now access the API at `http://localhost:8000/api/`. Use the admin interface at `http://localhost:8000/admin/` to manage users and data.

## Contributing

We welcome contributions to improve the Django TOTTMS Backend. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

Please ensure your code follows PEP 8 style guidelines and includes tests for new features.

## License


This project is licensed under the [GNU General Public License (GNU GPL)](LICENSE). You are free to modify, distribute, and use this software according to the terms and conditions of the GNU GPL. See the [LICENSE](LICENSE) file for details.

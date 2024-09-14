# Djirection Web Application

Welcome to the Djirection Web Application repository! This project is a sophisticated Django-based web application that showcases a British-Irish band, Djirection. The application includes a rich set of features, ensuring an interactive and engaging experience for users. Below, you'll find detailed information about the application's structure, features, and implementation.

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [HTML Templates](#html-templates)
- [Setup Instructions](#setup-instructions)
- [Deployment](#deployment)
- [License](#license)

## Project Overview

Djirection is a web application designed to manage and display information about a popular band, including concert details, songs, and photos. The application is built with Django, a powerful Python web framework, and leverages modern web technologies to deliver a seamless user experience.

## Tech Stack

The Djirection Web Application is built using the following technologies:

- **Backend Framework:**
  - **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
  
- **Frontend Technologies:**
  - **HTML5**: For structuring the content and layout of the web pages.
  - **CSS3**: For styling and designing the web pages with modern, responsive design techniques.
  - **Bootstrap**: A front-end framework that provides responsive design components and styles.
  - **JavaScript**: For dynamic content and interactive elements.
  
- **Containerization & Deployment:**
  - **Docker**: For containerizing the application, ensuring consistency across different environments.
  - **Kubernetes**: For orchestrating the deployment and scaling of containerized applications.

- **Authentication:**
  - **Django Authentication System**: Built-in support for user authentication, including login, signup, and session management.
  
## Features

### 1. User Authentication

- **Login & Signup:** Users can create accounts and log in to access personalized features.
- **Session Management:** Secure session handling with JWT and Express Session for user authentication.

### 2. Concert Management

- **Dynamic Concert Details:** Users can view detailed information about concerts, including name, date, city, and duration.
- **RSVP Functionality:** Users can RSVP for concerts using a dropdown menu to select their attendance status.

### 3. Song Management

- **Interactive Song List:** Browse a list of songs with modals that display lyrics on demand.
- **Responsive Design:** The song list and modals are fully responsive, providing a consistent experience across devices.

### 4. Photo Gallery

- **Photo Display:** A gallery showcasing event photos, including date and location details.
- **Responsive Layout:** The photo gallery adjusts to different screen sizes, ensuring a great user experience on all devices.


## HTML Templates

### Base Template (`base.html`)

The `base.html` template serves as the foundation for all other templates, providing a consistent layout and styling across the application.

- **Header:** Includes navigation links, user authentication status, and responsive design for mobile devices.
- **Main Content Area:** A flexible section where different content blocks are inserted based on the specific page requirements.
- **Footer and Scripts:** Incorporates essential JavaScript files and stylesheets to ensure a polished look and functionality.

### Home Page (`index.html`)

- **Introduction Section:** Features a captivating background image with a brief introduction to the band, Djirection.
- **Responsive Design:** Ensures the content is visually appealing and accessible on all devices.

### Concert Details Page (`concert_detail.html`)

- **Concert Information:** Displays detailed information about a specific concert.
- **RSVP Form:** Allows authenticated users to select their attendance status and submit their response.

### Concert List Page (`concerts.html`)

- **Concert Table:** Lists all concerts with sortable columns and action buttons for viewing more details.
- **Interactive Elements:** Provides a user-friendly interface for managing concert information.

### Login Page (`login.html`)

- **Login Form:** Secure login form for users to access their accounts.
- **Form Validation:** Handles user input with appropriate error messages and feedback.

### Signup Page (`signup.html`)

- **Signup Form:** Allows new users to create an account with validation and feedback.
- **User-Friendly Design:** Ensures a smooth and intuitive registration process.

### Photo Gallery Page (`photos.html`)

- **Photo Cards:** Displays event photos in a responsive grid layout with detailed captions.
- **Visual Appeal:** Utilizes modern design techniques to present photos attractively.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/InfectedDuck/ProductHub-API-Scalable-Product-Management-with-Flask.git
    cd ProductHub-API-Scalable-Product-Management-with-Flask
    ```

2. Set up a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run Migrations:

    ```bash
    python manage.py migrate
    ```

4. Create Superuser:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the application:

    ```bash
    python manage.py runserver
    ```

## Deployment

To deploy the application, follow the instructions in the Docker and Kubernetes files provided in the repository.

### Docker

- **Containerize the Application**: Use the `Dockerfile` and `entrypoint.sh` to build and run the Docker container.

### Kubernetes

- **Deploy the Application**: Use the provided Kubernetes deployment configuration to deploy the application to your Kubernetes cluster.

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details. <br>
This project is made as a part of IBM Course.

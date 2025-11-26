
# HaliCare API

## Overview

Halicare is a healthcare platform that addresses the challenges faced by HIV/AIDS patients due to the closure of USAID-funded clinics. By connecting patients with operational clinics and counseling centers, Halicare ensures access to critical medical and counseling services. The platform supports two main user types-patients and clinicians-and provides a robust, scalable backend with a well-defined database schema to manage users, centers, services, ARV availability, and appointments.

## Features

* **User Management:** Secure registration and authentication for patients and clinicians.
* **Clinic and Service Directory:** Comprehensive database of operational clinics, their services (e.g., HIV testing, ARV refills, counseling), and geolocation data.
* **Appointment Booking:** Patients can book appointments with clinics, including transfer letter uploads for new patients.
* **ARV Availability Tracking:** Real-time updates on ARV stock availability at clinics.
* **Scalable Architecture:** Modular Django-based backend for easy integration and maintenance.
* **Secure Data Handling:** Robust authentication and data encryption to protect sensitive patient information.

## Technology Stack

* **Python 3.13+:** Modern Python for reliable development.
* **Django 4.2+:** A high-level web framework for rapid development.
* **Django REST Framework:** For building secure and scalable APIs.
* **PostgreSQL:** A robust relational database for managing healthcare data.
* **drf-yasg:** Generates interactive Swagger documentation.
* **Token Authentication:** Secure access to APIs and user sessions.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
*   Python 3.10
*   pip
*   virtualenv

### Installation

1.  **Clone the repository:**

    ```sh
    git clone git@github.com:akirachix/halicare-backend.git
    cd halicare-backend
    ```
2.  **Create and activate a virtual environment:**

    ```sh
    python -m venv halicareenvenv
    source halicareenv/bin/activate
    ```
3.  **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```
5.  **Run the development server:**

    ```sh
    python manage.py runserver
    ```
The API will be available at https://halicare-7bfc32637910.herokuapp.com/api/.

## API Documentation

API documentation is available through Swagger UI and ReDoc.
*   **Swagger UI:** https://halicare-7bfc32637910.herokuapp.com/api/schema/swagger-ui/
*   **ReDoc:** https://halicare-7bfc32637910.herokuapp.com/api/schema/redoc/






   
  

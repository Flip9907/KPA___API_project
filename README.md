# KPA___API_project

# 🚀 KPA Form Data API Assignment  
### 🔧 by Priyansh Agarwal

## 📌 Overview

This is a backend API project built using **FastAPI** and **PostgreSQL**, developed as part of an assignment for **Suvidhaen**. The task involved implementing RESTful APIs according to the provided Swagger and Postman documentation. A total of **4 endpoints** were developed — 2 for submitting form data and 2 for retrieving it.

The project follows a modular architecture and uses **SQLAlchemy** for ORM and **Pydantic** for schema validation. The API supports both Swagger UI and OpenAPI documentation.

---

## 🛠 Tech Stack

- **Framework**: FastAPI  
- **Database**: PostgreSQL  
- **ORM**: SQLAlchemy  
- **Validation**: Pydantic  
- **API Testing**: Postman  
- **Documentation**: Swagger UI (`/docs`), OpenAPI (`/openapi.json`)  
- **Environment Configuration**: `.env` file with `python-dotenv`

---

## 📁 Project Structure

app/
├── main.py # FastAPI entry point
├── database.py # PostgreSQL connection setup
├── models/ # SQLAlchemy database models
├── schemas/ # Pydantic models for request/response
├── routers/ # API route definitions
├── utils/ # Utility functions (e.g., JSON flattening)
.env # Environment variables (excluded from Git)
requirements.txt # Python dependencies

---

## ✅ Implemented APIs

### 🔧 1. Bogie Checksheet Form

- `POST /api/forms/bogie-checksheet/`  
  → Validates and stores form data after flattening nested fields.

- `GET /api/forms/bogie-checksheet/{id}`  
  → Retrieves a form entry using its unique identifier.

### 🔧 2. Axle Wheel Form

- `POST /api/forms/axle-wheel/`  
  → Accepts and stores validated axle-wheel form data.

- `GET /api/forms/axle-wheel/{id}`  
  → Returns the axle-wheel form entry by its ID.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/kpa-form-api.git
cd kpa-form-api

# 2. Install Dependencies
pip install -r requirements.txt

# 3. Create a .env File
Add the following environment variable:
env
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<your_db_name>


# 4. Run the Server

uvicorn app.main:app --reload
Visit the documentation at:

Swagger UI: http://localhost:8000/docs

OpenAPI JSON: http://localhost:8000/openapi.json


# KPA Form Data API Assignment  
### by Priyansh Agarwal

## 📌 Overview

This project is a backend API implementation assignment for Suvidhaen, built using **FastAPI** and **PostgreSQL**. The goal was to develop APIs based on the provided Postman collection and Swagger documentation. I have implemented **4 fully functional endpoints** — 2 for form submission and 2 for fetching data.

The backend is integrated with a modular project structure and includes database persistence using SQLAlchemy ORM.

---

## 🚀 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Schema Validation**: Pydantic
- **API Testing**: Postman
- **Documentation**: Swagger UI (`/docs`) & OpenAPI (`/openapi.json`)
- **Environment Management**: `.env` file using `python-dotenv`

---

## 📂 Project Structure

app/
├── main.py # FastAPI entry point
├── database.py # DB connection and engine
├── models/ # SQLAlchemy models
├── schemas/ # Pydantic models for validation
├── routers/ # API routers (endpoints)
├── utils/ # Utility functions (e.g., flattening JSON)
.env # DB credentials (not committed)
requirements.txt # Dependencies

yaml
Copy
Edit

---

## ✅ Implemented APIs

I have implemented **2 APIs per form** (1 POST + 1 GET), for two distinct forms from the Swagger/Postman reference.

### 1. Bogie Checksheet Form

- `POST /api/forms/bogie-checksheet/`  
  Accepts form data, validates against a strict schema, flattens nested JSON, and stores into PostgreSQL.

- `GET /api/forms/bogie-checksheet/{id}`  
  Fetches form entry by unique ID from the database.

### 2. Axle Wheel Form

- `POST /api/forms/axle-wheel/`  
  Similar to above, handles submission with validation and structured storage.

- `GET /api/forms/axle-wheel/{id}`  
  Retrieves stored axle-wheel form data by ID.

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <project-folder>

2. Install Dependencies
pip install -r requirements.txt
3. Create .env File
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<your_db_name>

4. Run Migrations / Create Tables
Ensure the PostgreSQL database exists, then:

#If using manual table creation
python create_tables.py


Run the FastAPI Server

uvicorn app.main:app --reload


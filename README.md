# Zeotap Rule Engine

This project is a rule engine application built with a Flask backend and a React frontend. It allows users to create, update, delete, and evaluate rules. The backend uses SQLite for data storage.

## Features
- **Backend**: Flask API to manage rules and evaluate them.
- **Frontend**: React-based interface to interact with the backend.
- **Database**: SQLite for storing rules.
- **Docker**: Dockerized setup for easy deployment.

## Prerequisites
- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/PrakharGupta2001/RuleEngineWithAST.git
cd zeotap_rule_engine
```

### 2. Run the Application using Docker Compose
```bash
docker-compose up --build
```
- This will start the backend server at http://127.0.0.1:5000/ and the frontend at http://localhost:3000/.

###  3. Access the Application

- Frontend: Open http://localhost:3000 to access the React interface.
- Backend: The Flask API is available at http://127.0.0.1:5000.

### 4. Stopping the Application
```bash
docker-compose down
```

## Project Structure
```bash
zeotap_rule_engine/
├── backend/                # Flask backend files
│   ├── app.py              # Main application file
│   ├── rule_engine.py      # Logic for rule creation, evaluation
│   ├── models.py           # AST data structure
│   ├── database.py         # Database operations
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Dockerfile for backend
├── frontend/               # React frontend files
│   ├── public/             # Public files
│   ├── src/                # Source files for React
│   ├── Dockerfile          # Dockerfile for frontend
│   └── package.json        # Frontend dependencies
├── docker-compose.yml      # Docker Compose configuration
└── README.md               # This file
```

## API Endpoints

### 1. Create a Rule
- URL: POST /create_rule
- Body:
```bash
{
  "rule": "age > 30 and salary > 50000"
}
```

### 2. List All Rules
- URL: GET/ rules

### 3. Get a Rule by ID
- URL: GET /rules/<rule_id>

### 4. Update a Rule
- URL: PUT /rules/<rule_id>
- Body:
```bash
{
  "rule": "age > 35 and salary > 60000"
}
```

### 5. Delete a Rule
- URL: DELETE /rules/<rule_id>

### 6. Evaluate a Rule
- URL: POST /evaluate_rule
- Body:
```bash
{
  "rule_id": 1,
  "data": {
    "age": 40,
    "salary": 70000
  }
}
```

## Run the Application on Local

After cloning the application:

### 1. Backend:
```bash
cd backend
python app.py
```

### 2. Frontend:
```bash
cd ../frontend
npm start
```

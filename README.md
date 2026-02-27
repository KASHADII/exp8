# Backend REST API Lab - Experiment 8

## Overview

This project demonstrates the development of RESTful APIs using Flask framework. The application implements a student management system with full CRUD operations using Flask Blueprints for modular organization.

## Project Structure

```
backend/
└── rest-api-lab/
    ├── virenv/                 # Virtual environment
    ├── routes/                 # Blueprint modules
    │   └── student_routes.py   # Student management routes
    ├── app.py                  # Flask application factory
    ├── run.py                  # Application entry point
    ├── requirements.txt        # Python dependencies
    └── README.md              # This file
```

## Setup Instructions

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd backend/rest-api-lab
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv virenv
   # On Windows:
   .\virenv\Scripts\activate
   # On Unix/MacOS:
   source virenv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the backend server:
```bash
python run.py
```

The server will run on:
- **Host**: 0.0.0.0 (accessible from any IP)
- **Port**: 5000
- **Debug Mode**: Enabled

## API Endpoints

### Base URL: `http://localhost:5000`

### Home Endpoint
- **GET** `/` - Server status check
  - **Response**: `{"message": "Backend Server is running"}`

### Student Management Endpoints

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| POST | `/students` | Create new student | `{"name": "John", "age": 20}` | Student object with ID |
| GET | `/students` | Get all students | None | Array of students |
| GET | `/students/<id>` | Get specific student | None | Student object |
| PUT | `/students/<id>` | Update student | `{"name": "John", "age": 21}` | Updated student object |
| DELETE | `/students/<id>` | Delete student | None | Success message |

## Sample API Usage

### Create a Student
```bash
curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "age": 22}'
```

### Get All Students
```bash
curl http://localhost:5000/students
```

### Get Specific Student
```bash
curl http://localhost:5000/students/1
```

### Update Student
```bash
curl -X PUT http://localhost:5000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Smith", "age": 23}'
```

### Delete Student
```bash
curl -X DELETE http://localhost:5000/students/1
```

## Code Structure Explanation

### Flask Application Factory Pattern
- `app.py` uses the application factory pattern with `create_app()` function
- Allows for better configuration and testing
- Separates app creation from running the app

### Flask Blueprints
- `student_routes.py` defines a Blueprint for student-related routes
- Blueprints help organize routes into logical groups
- Makes the application more modular and maintainable

### In-Memory Storage
- Currently uses in-memory storage (Python lists)
- Data is lost when server restarts
- Can be easily replaced with database storage

## Key Concepts Demonstrated

1. **RESTful API Design**: Proper HTTP methods and status codes
2. **Flask Blueprints**: Modular route organization
3. **Application Factory Pattern**: Flexible app configuration
4. **JSON Request/Response Handling**: Proper data serialization
5. **Error Handling**: Appropriate HTTP status codes and error messages
6. **CRUD Operations**: Complete Create, Read, Update, Delete functionality

## Testing with Postman

### Collection Setup
1. Create a new collection in Postman
2. Add the following requests:

#### 1. Create Student
- **Method**: POST
- **URL**: `http://localhost:5000/students`
- **Headers**: `Content-Type: application/json`
- **Body** (raw JSON):
```json
{
    "name": "John Doe",
    "age": 20
}
```

#### 2. Get All Students
- **Method**: GET
- **URL**: `http://localhost:5000/students`

#### 3. Get Specific Student
- **Method**: GET
- **URL**: `http://localhost:5000/students/1`

#### 4. Update Student
- **Method**: PUT
- **URL**: `http://localhost:5000/students/1`
- **Headers**: `Content-Type: application/json`
- **Body** (raw JSON):
```json
{
    "name": "John Smith",
    "age": 21
}
```

#### 5. Delete Student
- **Method**: DELETE
- **URL**: `http://localhost:5000/students/1`

## Future Enhancements

1. **Database Integration**: Replace in-memory storage with SQLite/PostgreSQL
2. **Input Validation**: Add request validation using libraries like Marshmallow
3. **Authentication**: Add JWT-based authentication
4. **Logging**: Implement structured logging
5. **API Documentation**: Add Swagger/OpenAPI documentation
6. **Unit Testing**: Add comprehensive test suite
7. **Error Handling**: Implement global error handling middleware
8. **Rate Limiting**: Add rate limiting to prevent abuse

## Troubleshooting

### Common Issues

1. **Port Already in Use**:
   - Change port in `run.py` or stop other services using port 5000

2. **Virtual Environment Issues**:
   - Ensure virtual environment is activated before running
   - Recreate virtual environment if needed

3. **Import Errors**:
   - Verify all dependencies are installed
   - Check Python path and working directory

### Debug Mode
- Debug mode is enabled by default
- Detailed error messages will be shown in the console
- Auto-reload on code changes

## Dependencies

See `requirements.txt` for the complete list of dependencies:
- **Flask**: Web framework
- **Werkzeug**: WSGI utility library
- **Jinja2**: Template engine
- **Click**: Command line interface
- **itsdangerous**: Security utilities
- **MarkupSafe**: HTML escaping
- **blinker**: Signal support

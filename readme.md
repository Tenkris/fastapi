# FastAPI DynamoDB Starter

A starter project for building APIs with FastAPI and DynamoDB.

## Features

- FastAPI framework for building high-performance APIs
- PynamoDB for DynamoDB integration
- Docker support for containerization
- Environment variable configuration
- Structured project layout
- CORS middleware configured

## Prerequisites

- Python 3.11+
- pip (Python package manager)
- Git
- AWS account with DynamoDB access (for full functionality)
- Docker (optional, for containerization)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-dynamodb-starter.git
cd fastapi-dynamodb-starter
```

### Create a New Branch

```bash
git checkout -b feature/your-feature-name
```

### Set Up Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### Install Dependencies

```bash
# Install requirements
pip install -r requirements.txt
```

### Configure Environment Variables

```bash
# Copy the example .env file
cp .env.example .env

# Edit .env with your configuration
# Set your AWS credentials and DynamoDB settings
```

### Run the Application

```bash
# Start the FastAPI server
uvicorn app.main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Freezing Dependencies

To update the requirements.txt file with your current environment's packages:

```bash
pip freeze > requirements.txt
```

## Docker Support

Build and run the application using Docker:

```bash
# Build the Docker image
docker build -t fastapi-dynamodb-app .

# Run the container
docker run -d -p 8000:8000 --name fastapi-app fastapi-dynamodb-app
```

## Project Structure

```
fastapi-dynamodb-starter/
├── app/                      # Application package
│   ├── models/               # PynamoDB models
│   ├── routers/              # API routes
│   ├── schemas/              # Pydantic schemas
│   ├── services/             # Business logic
│   ├── utils/                # Utility functions
│   └── main.py               # Application entry point
├── .env                      # Environment variables (create from .env.example)
├── .env.example              # Example environment variables
├── .gitignore                # Git ignore rules
├── Dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
├── set_key.py                # AWS credential setup utility
└── README.md                 # This file
```

## Development Guidelines

1. Create a new branch for each feature or bug fix
2. Follow the project structure when adding new functionality
3. Add appropriate documentation
4. Write tests for new features
5. Update requirements.txt when adding new dependencies

## License

This project is licensed under the MIT License - see the LICENSE file for details.

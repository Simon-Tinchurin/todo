# ToDo FastAPI Service

This is a simple ToDo API service built with **FastAPI** and **PostgreSQL**. \
The service is containerized with Docker and managed using Docker Compose.

## Features

- FastAPI backend for handling CRUD operations on tasks.
- PostgreSQL as the database for storing task data.
- JWT-based authentication for secure access to API endpoints.
- Automatic table creation with a provided SQL script during the initialization of the PostgreSQL container.

## Prerequisites

Make sure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.10 (for local development, if needed): [Install Python](https://www.python.org/downloads/)

## Environment Variables

The project uses a `.env` file to configure environment variables for both FastAPI and PostgreSQL.

Create a `.env` file in the root directory of the project and add the following content:

```bash
# FastAPI Settings
DATABASE_URL=postgresql://myuser:mypassword@db:5432/mydatabase
SECRET_KEY=mysecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# PostgreSQL Settings
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=mydatabase
```

## How to Run
1. Clone the repository:

    ```bash
    git clone https://github.com/Simon-Tinchurin/todo.git
    cd todo
    ```
2. Create a .env file:

    As described above, create the .env file with the necessary environment variables.

3. Build and run the project with Docker Compose:

    ```bash
    docker-compose up --build
    ```
This will build the Docker image for the FastAPI app, initialize the PostgreSQL container, and run both services. The FastAPI app will be accessible at http://localhost:8000.

## Access API documentation:

FastAPI automatically generates documentation for the API. You can access it by visiting:

Swagger UI: http://localhost:8000/docs \
ReDoc: http://localhost:8000/redoc

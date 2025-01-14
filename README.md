# Multi-Service App Template 

### Overview

This Docker Compose project is designed to streamline the development of a multi-service application. The project includes three interconnected applications: MySQL for database management, React for the frontend, and Flask for the backend.

#### MySQL:

- The MySQL service is defined with the official MySQL Docker image.
- Environment variables are set for MySQL root user and database configuration.
- The ./db volume is used to persist MySQL data.

#### Flask:
- The Flask service is built from the ./backend/Dockerfile.
- Flask runs on port 5000.

#### React:
- The React service is built from the ./frontend/Dockerfile.
- It restarts always and runs on port 3000.





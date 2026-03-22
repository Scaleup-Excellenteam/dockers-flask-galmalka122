## Dockerized Flask App
A simple Flask web application containerized with Docker to ensure consistent environments across development and production.

### Project Structure
* **`app/`**: Contains the Flask application logic and routes.
* **`Dockerfile`**: Defines the container image, including the Python runtime and dependencies.
* **`docker-compose.yml`**: Manages the container services, port mapping, and environment variables.
* **`requirements.txt`**: Lists necessary Python packages (Flask, Gunicorn, etc.).

### Features
* **Containerization**: Fully isolated environment using Docker.
* **Orchestration**: Simplifies multi-container setup (if using databases like Redis or PostgreSQL) via Docker Compose.
* **Production Ready**: Configured to run behind a WSGI server like Gunicorn.

### Quick Start
1. **Build and Run**:
   ```bash
   docker-compose up --build
   ```
2. **Access**:
   Open `http://localhost:5000` in your browser.

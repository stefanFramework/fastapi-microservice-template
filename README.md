# 🚀 FastAPI Microservice Template  

A production-ready **FastAPI microservice boilerplate** designed for speed, scalability, and developer productivity. With everything pre-configured, you can **focus on building features** instead of setting up the foundation.  

## 🎯 Why Use This Template?  

- ✅ **FastAPI** - Blazing fast, asynchronous, and easy-to-use API framework.  
- ✅ **SQLModel** - A perfect blend of SQLAlchemy & Pydantic for effortless ORM.  
- ✅ **Poetry** - Modern dependency management.  
- ✅ **Alembic** - Database migrations made easy.  
- ✅ **Logging** - Pre-configured logging with structured output.  
- ✅ **Docker & Docker Compose** - Seamless containerization and deployment.  

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed on your system. You can download it from the [official website](https://www.docker.com/get-started).

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/stefanFramework/fastapi-microservice-template.git
   cd fastapi-microservice-template
   ```

2. **Configure Environment Variables**:

   - Create a `.env` file on the project root:

     ```bash
     touch .env
     ```

   - Open the `.env` file with a text editor and set the environment variables as needed. Below is a description of the key variables:
     - `ENVIRONMENT`: The environment in which the app is running; typically `development` or `production`.
     - `JWT_SECRET_KEY`: A private key that will be used to sign the token used for authentication.
     - `SQLALCHEMY_DATABASE_URI`: The database connection URL. For example, for a PostgreSQL database: `postgresql://user:password@localhost:5432/database_name`.

     Ensure that the `SQLALCHEMY_DATABASE_URI` matches the database configuration specified in the `docker-compose.yml` file if you're using Docker for the database service.

3. **Start the Application with Docker**:

   - Build and start the Docker containers:

     ```bash
     docker-compose up --build
     ```

     This command will build the Docker images and start the services defined in the `docker-compose.yml` file. By default, this includes the Flask application and a PostgreSQL database.

   - To stop the services:

     ```bash
     docker-compose down
     ```

     This command stops and removes the containers defined in the `docker-compose.yml` file.

## Project Structure

```
fastapi-microservice-template/
├── app/
│   ├── api/
|   ├── models/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── database.py
│   └── ...
├── migrations/
├── tests/
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
└── README.md
```

- `app/`: Contains the main application code.
- `migrations/`: Directory for Alembic database migrations.
- `tests/`: Contains test cases for the application.
- `.env`:  Environment variables file.
- `Dockerfile`: Docker configuration for the Flask application.
- `docker-compose.yml`: Docker Compose configuration for multi-container applications.
- `pyproject.toml & poetry.lock`: Python dependencies.

## Running Migrations

To handle database migrations with Alembic:

1. **Generate a New Migration**:

   ```bash
   docker-compose exec -it fastapi_app
   poetry run alembic revision --autogenerate -m "Migration message"
   ```

2. **Apply Migrations**:

   ```bash
   docker-compose exec -it fastapi_app
   poetry run alembic upgrade head
   ```

## 🛠️ Tech Stack  
- **FastAPI** 🚀  
- **SQLModel** (SQLAlchemy + Pydantic)  
- **Alembic** for database migrations  
- **Poetry** for dependency management  
- **Docker & Docker Compose** for easy deployment  
- **Pre-configured Logging**  

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the AGPL-3.0 License. See the [LICENSE](LICENSE) file for details.

---

🔥 **Kickstart your FastAPI microservice today!** 🚀  

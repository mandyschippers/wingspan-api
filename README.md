# Flask Application with SQLAlchemy

This is a simple Flask application that demonstrates the usage of SQLAlchemy for interacting with a relational database.

## Overview

The application is built using the Flask web framework and SQLAlchemy ORM (Object-Relational Mapper) for database operations. It provides basic CRUD (Create, Read, Update, Delete) functionality for managing resources in the database.

## Features

- **Flask Framework**: Web framework for building the application.
- **SQLAlchemy**: ORM for interacting with the relational database.
- **SQLite Database**: Lightweight database for development and testing purposes.

## Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/mandyschippers/aiexp-api.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd aiexp-api
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3a. **rename config.template.py to config.py and paste your parameters**:

4. **Run the Application**:

    ```bash
    FLASK_APP=factory:create_app flask --debug run
    ```

    The application will be accessible at `http://localhost:5000`.

## Configuration

- **Database Configuration**: Update the database connection URI in `config.py` to point to your desired database.

```bash
FLASK_APP=factory:create_app flask db init
FLASK_APP=factory:create_app flask db migrate -m "migration message"
FLASK_APP=factory:create_app flask db upgrade
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

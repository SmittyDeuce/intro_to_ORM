# intro_to_ORM

# Gym Management API

This Flask application manages gym members and workout sessions using MySQL as the database backend.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- Flask-Marshmallow
- mysql-connector-python

## Setup

1. **Set up MySQL database:**

   - Create your database.
   - Configure MySQL user credentials (`user`, `password`, `host`) in `app.py`.

2. **Run the application:**

   ```bash
   python app.py
   ```

   The application will run on `http://localhost:5000/`.

## API Endpoints

### Members

- **GET** `/members`

  Retrieves all gym members.

- **POST** `/members`

  Adds a new member.

- **PUT** `/members/<int:id>`

  Updates a specific member.

- **DELETE** `/members/<int:id>`

  Deletes a specific member.

### Workouts

- **POST** `/workout-sessions`

  Schedules a workout session.

- **PUT** `/workout-sessions/<int:id>`

  Updates a workout session.

- **GET** `/workout-sessions`

  Retrieves all workout sessions.

- **GET** `/members/<int:member_id>/workout-sessions`

  Retrieves all workout sessions for a specific member.

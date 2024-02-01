# Task

- [Task](#task)
	- [Project Setup Guide](#project-setup-guide)
		- [Prerequisites](#prerequisites)
		- [Environment Variables](#environment-variables)
		- [Setting Up Virtual Environment](#setting-up-virtual-environment)
		- [Database Setup](#database-setup)
		- [Running the Server](#running-the-server)
	- [API Documentation](#api-documentation)
		- [User Authentication](#user-authentication)
			- [Register User](#register-user)
			- [Login and Get Token](#login-and-get-token)
		- [CRUD Operations for Tasks (Bearer Token Authentication)](#crud-operations-for-tasks-bearer-token-authentication)
	- [CRUD Operations for Tasks (Bearer Token Authentication)](#crud-operations-for-tasks-bearer-token-authentication-1)
			- [Retrieve List of Tasks](#retrieve-list-of-tasks)
			- [Create a New Task](#create-a-new-task)
			- [Retrieve Task Details](#retrieve-task-details)
			- [Update Task](#update-task)
			- [Delete Task](#delete-task)

## Project Setup Guide

### Prerequisites
- Ensure you have `pipenv` and `node.js` installed on your computer.

### Environment Variables
1. Copy the content of `.env.example`.

2. Create a new file named `.env` in the project root.

3. Paste the copied content into `.env`.

4. Replace `your_secret_key` with your actual secret key and `db_url_string` with a valid PostgreSQL database URL (e.g., `postgresql://username:password@host:port/database`).

### Setting Up Virtual Environment
1. Create a virtual environment folder named `.venv`:
    ```bash
    mkdir .venv
    ```

2. Install `pnpm` globally:
    ```bash
    npm install -g pnpm
    ```

3. Install Python dependencies:
    ```bash
    pnpm install
    pipenv install
    ```

### Database Setup

1. Run migrations:
    ```bash
    pipenv shell
    python manage.py migrate
    ```

2. Create a superuser:
    ```bash
    python manage.py createsuperuser --username <username> --email <email>
    ```

### Running the Server

Run the Django development server:
```bash
pipenv shell
python manage.py runserver
```

Now you can access the Django admin interface at `http://localhost:8000/admin/` and your application at `http://localhost:8000/`

## API Documentation

### User Authentication

#### Register User
- **URL:** `/api/users/register/`
- **Method:** POST
- **Description:** Register a new user.
- **Request Body:**
  - `username` (string): User's username.
  - `email` (string): User's email.
  - `password` (string): User's password.

#### Login and Get Token
- **URL:** `/api/users/login/`
- **Method:** POST
- **Description:** Log in a user and receive an authentication token.
- **Request Body:**
  - `username` (string): User's username.
  - `password` (string): User's password.
- **Response:**
  - `Token` (string): Authentication token for the logged-in user.

### CRUD Operations for Tasks (Bearer Token Authentication)

> Include the obtained token in the request headers with the format: `Token <your_token>`.

## CRUD Operations for Tasks (Bearer Token Authentication)

Include the obtained token in the request headers with the format: `Bearer <your_token>`.

#### Retrieve List of Tasks
- **URL:** `/api/tasks/`
- **Method:** GET
- **Permission:** Authenticated Users
- **Description:** Retrieve a list of tasks owned by the authenticated user.

#### Create a New Task
- **URL:** `/api/tasks/`
- **Method:** POST
- **Permission:** Authenticated Users
- **Description:** Create a new task for the authenticated user.
- **Request Body:**
  - `title` (string): Task title.
  - `description` (string): Task description.
  - `due_date` (string, format: "YYYY-MM-DDTHH:mm"): Due date and time of the task.
  - `priority` (string): Priority level of the task (e.g., "low", "medium", "high").
  - `is_complete` (boolean): Task completion status (true or false).

#### Retrieve Task Details
- **URL:** `/api/tasks/<pk>/`
- **Method:** GET
- **Permission:** Authenticated Users
- **Description:** Retrieve details of a specific task owned by the authenticated user.

#### Update Task
- **URL:** `/api/tasks/<pk>/`
- **Method:** PUT/PATCH
- **Permission:** Authenticated Users
- **Description:** Update details of a specific task owned by the authenticated user.
- **Request Body:**
  - `title` (string): Updated task title.
  - `description` (string): Updated task description.
  - `due_date` (string, format: "YYYY-MM-DDTHH:mm"): Updated due date and time.
  - `priority` (string): Updated priority level (e.g., "low", "medium", "high").
  - `is_complete` (boolean): Updated task completion status (true or false).

#### Delete Task
- **URL:** `/api/tasks/<pk>/`
- **Method:** DELETE
- **Permission:** Authenticated Users
- **Description:** Delete a specific task owned by the authenticated user.


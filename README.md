# Sunny Todo List

Sunny Todo List is a Django-based web application for managing tasks and tracking weather conditions associated with task locations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Environment Variables](#environment-variables)

## Features

- Create, edit, delete, and view tasks
- View tasks by location
- Track weather conditions associated with task locations
- Dynamic weather information fetching from an external API

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yuliiabodnar/sunny_todo_list.git
    cd sunny-todo-list
    ```

2. **Create a `.env` file:**

    Create a `.env` file in the root directory and add the following content. Obtain your API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).
   
    ```env
    API_KEY=<your_openweathermap_api_key>
    ```

3. **Build and run the Docker containers:**

    ```sh
    docker-compose up --build
    ```

    This command will build the Docker images and start the containers.

4. **Apply migrations:**

    Open a new terminal and run the following command to apply the database migrations:

    ```sh
    docker-compose run web python manage.py migrate
    ```

## Usage

1. **Access the web application:**

    Open your browser and navigate to `http://localhost:8080`.

2. **Create tasks and view weather information:**

    Use the web interface to create, edit, and delete tasks, and view associated weather information.

## API Endpoints

### Tasks

- **List Tasks:** `GET /task/`
- **Task Detail:** `GET /task/<int:pk>/`
- **Create Task:** `POST /task/add/`
- **Edit Task:** `PUT /task/<int:pk>/edit/`
- **Delete Task:** `POST /task/<int:pk>/delete/`

### Task Locations context

- **List Locations Context:** `GET /task/location-context/`
- **Location Detail Context:** `GET /task/location-context/<int:pk>/`

### Weather

- **Get Weather:** `GET /weather/get/?location=<location_name>`

## Running Tests

To run tests for the project:

   ```sh
    docker-compose run web python manage.py test  
   ```

## Environment Variables

The following environment variables are used in the project:

- `DATABASE_NAME`: Name of the database
- `DATABASE_USER`: Database user
- `DATABASE_PASSWORD`: Database password
- `DATABASE_HOST`: Database host
- `DATABASE_PORT`: Database port
- `API_KEY`: API key for accessing the weather service

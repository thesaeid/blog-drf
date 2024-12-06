# Blog API Project

This project is a simple Blog API implemented using Django and Django REST Framework (DRF). It provides basic CRUD operations for blog posts, comments, and user authentication.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blog-api.git

2. Navigate to the project directory:
   ```bash
   cd blog-api

3. [OPTIONAL STEP] create a virtual environment.
   ```bash 
   python -m venv .venv
   
4. activate the venv.
   ```bash 
   source .venv/bin/activate

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

6. rename .env.sample to .env and put your env vars in that file (it's a blueprint of what you may have need).

7. Configure your database settings in the ```blog/settings/base.py``` file.

8. start your project:
   ```bash 
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

## Project Structure

The project structure is organized into multiple apps for separation of concerns:

``` bash
├── blog/                   # Main project settings and configurations
├── core/                   # User authentication and profile management
├── post/                   # Blog post, comments, and related functionality
├── docker/                 # Docker-related files
├── requirements.txt        # List of required dependencies
└── manage.py               # Django project management script
├── .gitignore              # git ignore file
└── docker-compose.yml      # docker-compose file
├── README.md               # readme file
└── .env.sample             # .env sample 
```

#### Key Apps
   - core: Handles user authentication and profiles.
   - post: Manages blog posts, comments, and other related functionalities.


## Docker Setup
This project can be dockerized for easier deployment. To run the project in a Docker container, follow these steps:

1. Build and Start the Docker image:
   ```bash
   docker-compose up --build

2. Access the application at http://0.0.0.0:8030


3. To stop the Docker containers, use:
   ```bash
   docker-compose down

## Usage
Once the project is up and running, you can access the following API endpoints:

- ```POST /auth/users/``` - User registration
- ```POST /auth/jwt/create``` - get jwt token
- ```GET /posts/``` - List all blog posts
- ```POST /posts/``` - Create a new blog post
- ```GET /posts/{id}/``` - Retrieve a single blog post
- ```DELETE /posts/{id}/``` - Delete a blog post
- ```PUT /posts/{id}/``` - Update a blog post
- ```GET /posts/{id}/comments/``` - List all comments of a post
- ```POST /posts/{}/comments/``` - Create a new comment on a post

## Contributing
Contributions are welcome! Please follow these steps to contribute:

- Fork the repository.
- Create a new branch ```git checkout -b feature-branch```.
- Make your changes and commit them.
- Push to your forked repository ```git push origin feature-branch```.
- Open a pull request.


## License
This project is licensed under the MIT License.
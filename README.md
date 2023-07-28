
# Project Description and Installation Guide

a professional to-do list using Django and other technologies...
The purpose of building this project is to implement the acquired knowledge and combine different technologies with each other.
This repository contains a Django project setup using Docker. Follow the instructions below to build and run the project.

## Installation

1. Make sure you have Docker installed on your system.
2. Clone this repository to your local machine.

## Build Docker Image

To build the Docker image, execute the following command:

```
sudo docker build -t djangosetup .
```

## Run the Project with Docker

To run the project using Docker, execute the following commands:

```
sudo docker run -p 8000:8000 -it djangosetup
```

This will start the Django project and make it accessible at `http://localhost:8000`.

Please note that you may need to adjust the port number (`8000`) in the above command if it conflicts with any other service running on your machine.

That's it! You have successfully installed and run the Django project using Docker.
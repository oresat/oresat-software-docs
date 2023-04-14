# Docker Primer

Docker is an open-source platform that simplifies the process of building, deploying, and running applications in 
containers. Containers are lightweight, portable, and self-contained environments that package an application, 
along with its dependencies, libraries, and runtime, to ensure consistent behavior across different platforms and environments.

## Main concepts and components of Docker:

**Docker Engine**: The core component of Docker, responsible for creating and managing containers. It runs on the 
host operating system and communicates with the Docker client using a REST API.

**Dockerfile**: A script containing instructions to build a Docker image. It defines the base image, application 
source code, dependencies, and configurations required to create a containerized application.

**Docker Image**: A read-only template used to create Docker containers. Images are created from Dockerfiles and 
stored in a registry, such as Docker Hub or a private registry.

**Docker Container**: A lightweight, portable, and self-contained environment created from a Docker image. 
Containers run the application and its dependencies, isolated from the host system and other containers.

**Docker Hub**: A public registry for sharing and distributing Docker images. It provides a centralized platform for 
developers to store, manage, and share container images.

**Docker Compose**: A tool for defining and running multi-container Docker applications. It uses a YAML file 
(docker-compose.yml) to configure the application's services, networks, and volumes.

## Basic Commands
Here are some basic Docker commands that are essential when working with Docker:

1. **Build an image**: Build a Docker image from a Dockerfile in the current directory.

```
docker build -t image-name:tag .
```

2. **List images**: Display a list of Docker images available on your local system.
```
docker images
```

3. **Run a container**: Create and start a new Docker container from an image.

```
docker run -d -p host-port:container-port --name container-name image-name:tag
-d: Run the container in detached mode (in the background).
-p: Map the host port to the container port.
--name: Assign a name to the container for easier reference.
```

4. **List containers**: Show a list of all running containers.

```docker ps```

To list all containers, including stopped ones, use:

```docker ps -a```

5. **Stop a container**: Stop a running container.

```docker stop container-name-or-id```

6. **Start a container**: Start a stopped container.

```docker start container-name-or-id```

7. **Remove a container**: Delete a stopped container.

```docker rm container-name-or-id```

8. **Remove an image**: Delete a Docker image from your local system.

```docker rmi image-name:tag```

9. **Container logs**: Display logs from a running container.

```docker logs container-name-or-id```

10. **Execute a command inside a container**: Run a command within a running container.

```docker exec -it container-name-or-id command```

For example, to open a shell inside a running container, use:

```docker exec -it container-name-or-id /bin/bash```

11. **Pull an image**: Download a Docker image from a registry (e.g., Docker Hub).

```docker pull image-name:tag```

12. **Push an image**: Upload a Docker image to a registry (e.g., Docker Hub). Make sure you are logged in with docker 
login and the image is tagged with your username.

```docker push username/image-name:tag```

To get started with Docker, follow these steps:

1. **Install Docker**: Download and install Docker for your operating system from the official website (https://www.docker.com/get-started).
2. **Use the provided dockerfile** in the repository
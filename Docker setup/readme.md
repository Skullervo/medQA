# 🐳 Introduction to Docker

**Docker** is an open platform for developing, shipping, and running applications. It allows developers to package an application and its dependencies into a standardized unit called a **container**.

## 💡 Why Docker?

- ✅ Consistency across environments (dev, test, prod)
- 🚀 Fast startup and isolated runtime
- 🔁 Easy to share and reuse application environments
- 🧩 Clean separation between application and infrastructure

## 📦 What Is a Container?

A **container** is a lightweight, standalone, and executable package that includes:
- Application code
- System tools
- Libraries
- Configuration files

All bundled together and running isolated from the host system.

> Containers are built from **images**, which are like snapshots of your application environment.

## 🛠️ Core Concepts

| Concept     | Description |
|-------------|-------------|
| **Image**   | A template used to create containers (built from Dockerfile) |
| **Container** | A running instance of an image |
| **Dockerfile** | Script that defines how an image is built |
| **Volume** | Persistent storage for containers |
| **Network** | Isolated network for containers to communicate |

## 🚀 Basic Workflow

1. Write a `Dockerfile` to define your application image.
2. Build the image:
   ```bash
   docker build -t my-app .
   ```
3. Run the container:
   ```bash
   docker run -d --name my-app-container -p 8080:80 my-app
   ```
4. Stop the container:
   ```bash
   docker stop my-app-container
   ```

## 📚 Learn More

- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub (Image Registry)](https://hub.docker.com/)
- [Play with Docker (Interactive Labs)](https://labs.play-with-docker.com/)

---

_This project includes dedicated Docker instructions per microservice inside their respective folders._

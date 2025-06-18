# 🐳 Docker Guide Overview

This directory contains **subfolders**, each providing Docker instructions for a specific topic shown in the previous diagram. The goal is to help user of this project to understand and apply Docker in modular steps across different services and use cases.

Each subfolder includes:
- A relevant `Dockerfile`
- Docker usage examples
- Environment variable setup
- Image build and run instructions

---

## 🐳 Introduction to Docker

**Docker** is an open platform for developing, shipping, and running applications. It allows developers to package an application and its dependencies into a standardized unit called a **container**.

### 💡 Why Docker?

- ✅ Consistency across environments (dev, test, prod)
- 🚀 Fast startup and isolated runtime
- 🔁 Easy to share and reuse application environments
- 🧩 Clean separation between application and infrastructure

### 📦 What Is a Container?

A **container** is a lightweight, standalone, and executable package that includes:
- Application code
- System tools
- Libraries
- Configuration files

All bundled together and running isolated from the host system.

> Containers are built from **images**, which are like snapshots of your application environment.

---

## 🛠️ Core Concepts

| Concept       | Description |
|---------------|-------------|
| **Image**     | A template used to create containers (built from Dockerfile) |
| **Container** | A running instance of an image |
| **Dockerfile**| Script that defines how an image is built |
| **Volume**    | Persistent storage for containers |
| **Network**   | Isolated network for containers to communicate |

---

## 🚀 Basic Docker Workflow

1. **Write a Dockerfile** to define your application environment.
2. **Build an image**:
   ```bash
   docker build -t my-app .
   ```
3. **Run a container**:
   ```bash
   docker run -d --name my-app-container -p 8080:80 my-app
   ```
4. **Stop the container**:
   ```bash
   docker stop my-app-container
   ```

---

## 📚 Resources

- [Docker Official Docs](https://docs.docker.com/)
- [Docker Hub Registry](https://hub.docker.com/)
- [Play with Docker (Labs)](https://labs.play-with-docker.com/)

---

🗂 Explore the subfolders in this directory for topic-specific Docker usage.


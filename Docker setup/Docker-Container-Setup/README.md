## 🐳 General Docker Container Creation Process

### 1. Create Dockerfiles

Define the container setup in a `Dockerfile`, including:
- 🧱 Base image to build upon
- 📦 Required dependencies and libraries
- 📁 Files to copy into the container
- ▶️ Command to run when the container starts

---

## 📦 Docker Images in the `distributedQA` Project (LV Automation)

### 🔍 ANALYZE MICROSERVICE

**Dockerfile: `Dockerfile.analyze`**
```Dockerfile
FROM python:3.12-slim
WORKDIR /app

# Install dependencies (e.g., for OpenCV)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    protobuf-compiler

# Install Python dependencies
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code and required files
COPY analyze_service.py analyze_service.proto test_analyze_service.py fetch_service.proto US_IQ_analysis3.py LUT_table_codes.py LUT_taulukko_lisaa.py probe-LUT.xls .

# Generate gRPC code
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. analyze_service.proto fetch_service.proto

# Expose gRPC port (check if is it free)
EXPOSE 50052

# Start service
CMD ["python", "analyze_service.py"]
```

```Dockerfile
FROM python:3.12-slim
WORKDIR /app

# Asenna tarvittavat paketit (esim. pydicom + gRPC + Excel + psycopg2 + OpenCV)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    protobuf-compiler \
    gcc \
    libpq-dev \
    python3-dev

# 🔧 Ympäristömuuttujat (oletukset – voidaan yliajaa docker run -e ...)
ENV ORTHANC_URL=http://localhost:8042
ENV FETCH_SERVICE_ADDRESS=fetch-service:50051
ENV DATABASE_NAME=QA-results
ENV DATABASE_USER=postgres
ENV DATABASE_PASSWORD=securepassword
ENV DATABASE_HOST=postgres-db
ENV DATABASE_PORT=5432

# Kopioi requirements ja asenna riippuvuudet
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopioi koodit ja datatiedostot
COPY analyze_service.py analyze_service.proto test_analyze_service.py fetch_service.proto US_IQ_analysis3.py LUT_table_codes.py LUT_taulukko_lisaa.py probe-LUT.xls .

# Generoi gRPC Python -tiedostot
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. analyze_service.proto fetch_service.proto

# Portti ulospäin
EXPOSE 50052

# Käynnistä palvelu
CMD ["python", "analyze_service.py"]

```


**Run the container:**
```bash
docker run -d --name analyze-service-container analyze-service:distributedQA
```

---

### 📥 FETCH MICROSERVICE

**Dockerfile: `Dockerfile.fetch`**
```Dockerfile
FROM python:3.12-slim
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y protobuf-compiler

# Install Python dependencies
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code and proto file
COPY fetch_service.py fetch_service.proto .

# Generate gRPC code
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. fetch_service.proto

# 🔹 Optional but recommended: expose the gRPC port
EXPOSE 50051

# Start the service
CMD ["python", "fetch_service.py"]

```

```Dockerfile
FROM python:3.12-slim
WORKDIR /app

# 🔧 Asenna tarvittavat paketit
RUN apt-get update && apt-get install -y protobuf-compiler

# 🔧 Ympäristömuuttujat (voit yliajaa docker run -e ...)
ENV ORTHANC_URL=http://localhost:8042
ENV PORT=50051

# 🔧 Asenna Python-riippuvuudet
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 🔧 Kopioi palvelun koodi
COPY fetch_service.py fetch_service.proto .

# 🔧 Generoi gRPC-koodi
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. fetch_service.proto

# 🔧 Dokumentoi portti
EXPOSE 50051

# 🔧 Käynnistä palvelu
CMD ["python", "fetch_service.py"]

```

**Run the container:**
```bash
docker run -d --name fetch-service-container fetch-service:distributedQA
```

---

### 🗄️ POSTGRES MICROSERVICE

**Run PostgreSQL directly from Docker Hub:**
```bash
docker run -d \
  --name postgres-db-distributedQA \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=salasana123 \
  -e POSTGRES_DB=analyysitietokanta \
  -p 55432:5432 \
  postgres:16
```

---

## ⚙️ 2. Build the Container Images

```bash
docker build -f Dockerfile.analyze -t analyze-service:distributedQA .
docker build -f Dockerfile.fetch -t fetch-service:distributedQA .
```

---

## 🔍 3. Verify Images

```bash
docker images
```

---

## 🛠️ 4. Interact With a Running Container

**Access a container shell:**
```bash
docker exec -it <container_name_or_ID> bash
```

**Mount local code (for development):**
```bash
docker run -it -v "$(pwd):/app" my-app
```

---

## 💾 5. Save or Share an Image (Optional)

**Export to `.tar`:**
```bash
docker save my-app > my-app.tar
```

**Push to Docker Hub:**
```bash
docker login
docker tag my-app username/my-app:latest
docker push username/my-app:latest
```

---

## ✅ Summary: Workflow

| Step                   | Command Example                              |
|------------------------|----------------------------------------------|
| 1. Create Dockerfile   | (edit Dockerfile)                             |
| 2. Build image         | `docker build -t name .`                      |
| 3. Run container       | `docker run -it name`                         |
| 4. Develop or access   | `docker exec -it` / `docker run -v "$(pwd):/app"` |
| 5. Share or push       | `docker push`                                 |

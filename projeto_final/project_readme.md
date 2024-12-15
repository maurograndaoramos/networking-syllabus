# Project Overview

This project demonstrates a simple secure, scalable application running inside Docker containers. It includes:

- A Python (Flask) REST API with endpoints for GET, POST, PUT, and DELETE.
- An Nginx reverse proxy as a load balancer, terminating SSL/TLS with a self-signed certificate.
- A simple HTML/JS front-end to view and manipulate items via the API.
- A custom Docker network with a defined CIDR to segment the API service behind the load balancer.
- A `Makefile` that provides convenient shortcuts to build, run, and test the application.

## Documentation
- The `README.md` file documents:
  - How to run the project (`make up`)  
  - How to generate and use the self-signed certificate  
  - The network configuration and endpoints for the API  
  - Example `curl` commands to test the API
  - Explanation of the front-end and how to interact with items

- [Project Overview](#project-overview)
- [Documentation](#documentation)
- [Project Requirements](#project-requirements)
  - [1. Network Infrastructure](#1-network-infrastructure)
  - [2. Security](#2-security)
  - [3. REST API](#3-rest-api)
- [Project Structure](#project-structure)
- [Features](#features)
  - [Network Infrastructure](#network-infrastructure)
  - [Security](#security)
  - [REST API](#rest-api)
  - [Front-End](#front-end)
- [Prerequisites](#prerequisites)
- [Setup Steps](#setup-steps)
  - [0. Generate Self-Signed Certificate](#0-generate-self-signed-certificate)
  - [1. Build and Run the Containers](#1-build-and-run-the-containers)
  - [2. Accessing the Application](#2-accessing-the-application)
  - [3. Testing the API via Make Commands](#3-testing-the-api-via-make-commands)
  - [4. Interacting via the Front-End](#4-interacting-via-the-front-end)
  - [5. Shutting Down](#5-shutting-down)
- [Additional Documentation](#additional-documentation)
- [Docker Compose Configuration](#docker-compose-configuration-composeyml)
  - [API Service](#api-service)
  - [Nginx Service](#nginx-service)
  - [Network Configuration](#network-configuration)
- [Dockerfile Configuration](#dockerfile-configuration)
- [Nginx Configuration](#nginx-configuration-nginxconf)

### Project Requirements

1. **Network Infrastructure**
   - **Use load balancing**:  
      I used NGINX as a reverse proxy and load balancer defined in `server/nginx.conf`. It points requests to the `api` service internally.*  
   - **Apply network segmentation**:  
     *In `compose.yml` I created a `custom_network` with a defined CIDR (`172.20.0.0/16`) and assigned static IPs to the `api` and `nginx` services. This ensures the API is only accessible through the load balancer.*

2. **Security**
   - **Implement HTTPS (SSL/TLS)**:  
     *`server/nginx.conf` configures `listen 443 ssl;` and uses `ssl_certificate /etc/nginx/certs/self-signed.crt;` and `ssl_certificate_key /etc/nginx/certs/self-signed.key;`. The `certs/` directory contains the self-signed certificate, ensuring secure communication despite the warning by most common browsers as the cert is self-assigned*

3. **REST API**
   - **Develop an API that follows HTTP Protocol**:  
     *In `api/app.py`, I have endpoints for GET, POST, PUT, and DELETE at `/items`. Each endpoint returns appropriate status codes (e.g., 200 for GET, 201 for POST, 200 or 404 for PUT/DELETE when items are not found).*
   - **Return proper status codes**:  
     *`app.py` returns `200 OK` for successful GET and PUT operations, `201 Created` for successful POST, and `404 Not Found` if an item does not exist. DELETE returns `200 OK` if deletion succeeds and `404` if not.*

## Project Structure

```
.
├── api/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
├── certs/
│   ├── self-signed.key
│   └── self-signed.crt
├── server/
│   └── nginx.conf
├── dockerfile
├── compose.yml
├── Makefile
└── README.md
```

## Features

1. **Network Infrastructure**
   - Custom Docker network with a defined CIDR block.
   - Nginx as a load balancer exposing only HTTPS to the host.
   - Flask API runs internally and is only accessible through Nginx.

2. **Security**
   - Self-signed TLS certificate for HTTPS communication.
   - API not exposed directly to the host; only through Nginx.

3. **REST API**
   - GET /items returns a list of items (200 OK)
   - POST /items creates a new item (201 Created)
   - PUT /items/<id> updates an item (200 OK or 404 Not Found)
   - DELETE /items/<id> deletes an item (200 OK or 404 Not Found)

4. **Front-End**
   - A simple HTML page served by Flask.
   - On-page buttons and forms to add, edit, and delete items.
   - Uses JavaScript fetch() calls to interact with the API.

## Prerequisites

- Docker and Docker Compose installed on your system.
- Make (for using the Makefile commands).

## Setup Steps

### 0. (Skip if already present) Generate Self-Signed Certificate

```bash
cd certs
openssl req -x509 -newkey rsa:2048 -nodes -keyout self-signed.key -out self-signed.crt -days 365 -subj "/CN=app.com"
cd ..
```
The provided configuration expects these files in `certs/`.

### 1. Build and Run the Containers

From the project root directory:

```bash
make up
```

This runs `docker-compose up --build -d`, building the API image and starting both API and Nginx services.

### 2. Accessing the Application

Open a browser and go to:

```
https://localhost
```

You'll see a self-signed certificate warning (normal in development). Proceed to the site to see the front-end.

### 3. Testing the API via Make Commands

After running `make up`, you can test the API:
   * `make test-get` Tests the GET endpoint at `/items`.
   * `make test-post` Tests the POST endpoint at `/items` with a default item name.
   * `make test-put` Tests the PUT endpoint at `/items/0`.
   * `make test-delete` Tests the DELETE endpoint at `/items/0`.


to specify a custom item name for the POST request.

### 4. Interacting via the Front-End

   * On `https://localhost`, you can view the current list of items.
   * Press F12 on your keyboard and make sure throttling is disabled
   * Add items by typing a name and clicking "Add".
   * Edit or delete items using the corresponding buttons.
   * Confirm on Chrome's DevTools (Or your browser's equivalent) the status codes

### 5. Shutting Down

When done, run:

```bash
make down
```

This stops and removes the containers.

# Additional Documentation



## Docker Compose Configuration (`compose.yml`)
### API Service
- **Build Configuration**
  - Context: Project root directory
  - Dockerfile: Uses the custom `dockerfile` in the project root
  - Exposed Port: 5000 (internal container port)
  - Network Configuration:
    - Network Name: `custom_network`
    - Assigned IPv4 Address: `172.20.0.2`

### Nginx Service
- **Image**: Official Nginx latest image
- **Volumes**:
  1. `./server/nginx.conf` mounted to `/etc/nginx/conf.d/default.conf`
     - Provides custom Nginx configuration
  2. `./certs` mounted to `/etc/nginx/certs`
     - Provides SSL/TLS certificates
- **Ports**:
  - Maps host port 443 to container port 443 (HTTPS)
- **Network Configuration**:
  - Network Name: `custom_network`
  - Assigned IPv4 Address: `172.20.0.3`

### Network Configuration
- **Name**: `custom_network`
- **Driver**: Bridge
- **IP Address Management (IPAM)**:
  - Subnet: `172.20.0.0/16`
  - Allows static IP assignments for services

* Review `compose.yml` for network and service definitions.
* Check `dockerfile` for Python API build steps.
* Inspect `server/nginx.conf` for load balancing and HTTPS.
* Examine the `Makefile` to understand all available commands.

# Dockerfile Configuration

### Base Image
- **Image**: `python:3.13-slim`
  - Lightweight Python image based on Debian slim
  - Provides a minimal Python runtime environment

### Working Directory
- **Path**: `/app`
  - Sets the working directory for subsequent instructions

### File Copying
1. **Application Code**
   - Copies `api/app.py` to `/app/app.py`
2. **Template Files**
   - Copies `api/templates` directory to `/app/templates`

### Dependencies
- **Installation**: `pip install Flask`
  - Installs the Flask web framework
  - Minimal dependencies for the application

### Networking
- **Exposed Port**: 5000
  - Indicates the container will listen on port 5000
  - Matches the Flask application's default port

### Startup Command
- **CMD**: `["python", "app.py"]`
  - Runs the Python Flask application directly
  - Ensures the application starts when the container launches


# Nginx Configuration (`nginx.conf`)

- **Name**: `api`
- **Server**: `api:5000`
  - Directs traffic to the API service
  - Uses service name resolution in Docker network

### SSL/HTTPS Configuration
- **Listen Port**: 443 (HTTPS)
- **Server Name**: `your_domain.com` (placeholder)

### SSL Certificate Paths
- **Certificate**: `/etc/nginx/certs/self-signed.crt`
- **Certificate Key**: `/etc/nginx/certs/self-signed.key`

### Proxy Configuration
- **Proxy Pass**: `http://api`
  - Forwards requests to the upstream API service

### Header Modifications
1. `Host`: Preserves original host header
2. `X-Real-IP`: Passes client's real IP address
3. `X-Forwarded-For`: Tracks proxy traversal path
4. `X-Forwarded-Proto`: Indicates original request protocol

### Security and Performance Considerations
- Terminates SSL/TLS at the Nginx layer
- Hides application server details
- Enables additional request header information for the backend
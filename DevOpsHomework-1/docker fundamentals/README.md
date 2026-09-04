# Docker Fundamentals Homework

Hello World web apps, each with its own folder and Dockerfile.

| Folder | Stack | Host port |
|---|---|---|
| `nodejs-app` | Node.js + Express | 3001 |
| `python-app` | Python + Flask | 5001 |
| `java-app` | Java HTTP server | 8080 |
| `Apache-app` | Apache httpd | 8081 |
| `React-app` | React (Vite) + Nginx | 8082 |
| `nginx-app` | Nginx | 8083 |

## Build and run

```bash
# Node.js
docker build -t hw-nodejs "./nodejs-app"
docker run -d --name hw-nodejs -p 3001:3000 hw-nodejs

# Python
docker build -t hw-python "./python-app"
docker run -d --name hw-python -p 5001:5000 hw-python

# Java
docker build -t hw-java "./java-app"
docker run -d --name hw-java -p 8080:8080 hw-java

# Apache
docker build -t hw-apache "./Apache-app"
docker run -d --name hw-apache -p 8081:80 hw-apache

# React
docker build -t hw-react "./React-app"
docker run -d --name hw-react -p 8082:80 hw-react

# Nginx
docker build -t hw-nginx "./nginx-app"
docker run -d --name hw-nginx -p 8083:80 hw-nginx
```

Open:

- http://localhost:3001 — Hello World from Node.js + Docker!
- http://localhost:5001 — Hello World from Python + Docker!
- http://localhost:8080 — Hello World from Java + Docker!
- http://localhost:8081 — Hello World from Apache + Docker!
- http://localhost:8082 — Hello World from React + Docker!
- http://localhost:8083 — Hello World from Nginx + Docker!

## Verified

All six images were built and run. `curl` showed Hello World on each page (React serves it from the JS bundle).

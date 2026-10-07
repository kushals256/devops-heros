FROM python:3.12-alpine
WORKDIR /app
COPY app.py .
CMD ["python", "-c", "from app import add; print('Hello from CI/CD', add(2, 3))"]

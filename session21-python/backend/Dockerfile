FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && useradd --create-home --uid 10001 appuser
COPY alembic.ini ./
COPY alembic ./alembic
COPY app ./app
USER 10001
EXPOSE 8000
CMD ["sh", "-c", "i=0; until alembic upgrade head; do i=$((i+1)); if [ \"$i\" -ge 15 ]; then exit 1; fi; sleep 2; done; exec uvicorn app.main:app --host 0.0.0.0 --port 8000"]

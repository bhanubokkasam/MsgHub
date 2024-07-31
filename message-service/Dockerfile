FROM python:3.9-slim

# Create a group and user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Change ownership of the app directory
RUN chown -R appuser:appgroup /app

# Use a non-root user
USER appuser

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]

FROM python:3.11-slim-bullseye

# Define environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production
ENV DJANGO_SETTINGS_MODULE=setup.settings
ENV PYTHONPATH=/gascontrolproject

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /gascontrolproject

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create staticfiles directory with proper permissions
RUN mkdir -p /gascontrolproject/staticfiles && \
    chmod -R 755 /gascontrolproject/staticfiles

# Create and set user with proper permissions
RUN useradd -r -s /bin/bash django-user && \
    chown -R django-user:django-user /gascontrolproject && \
    chmod -R 755 /gascontrolproject

USER django-user

# Expose port
EXPOSE 8000

# Command to run the application - CORRIGIDO
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn gascontrolproject.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile -"]
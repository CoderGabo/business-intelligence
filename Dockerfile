FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo dentro del contenedor
WORKDIR /code

# Copiar el archivo de requerimientos
COPY requirements.txt /code/

# Actualizar el índice de paquetes y luego instalar paquetes esenciales
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        build-essential \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project directory to the working directory
COPY . /code/

# Add a non-root user to run the application
RUN useradd -m appuser
USER appuser

# Expose port 8000 (si es necesario)
EXPOSE 8000

# Command to run the application with Gunicorn
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "--timeout", "60", "businessinteligence.wsgi:application"]

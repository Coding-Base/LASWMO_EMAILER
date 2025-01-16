# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Expose the port (you can change 8000 if your app uses a different port)
EXPOSE 8000

# Run the command to start the server
#CMD ["sh", "-c", "python manage.py send_birthday_emails_script && gunicorn birthday_system.wsgi:application --bind 0.0.0.0:8000"]
CMD ["sh", "-c", "python manage.py send_birthday_emails_script && gunicorn birthday_system.wsgi:application --bind 0.0.0.0:$PORT"]

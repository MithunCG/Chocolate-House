# Use an official Python runtime as a parent image
FROM python:3.9-slim



# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run the Django development server on port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

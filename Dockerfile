# Uses the official Python base image
FROM python:3.11.5-slim

# Sets the working directory inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copies the rest of the application files to the working directory
COPY . .

# Specifies the default command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
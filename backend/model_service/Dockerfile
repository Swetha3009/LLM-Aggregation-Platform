# Use the official Python 3.10 image as the base
FROM python:3.10-slim

# Set environment variables to minimize interaction
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Mention env variables
ENV GEMINI_API_KEY=AIzaSyCd93UdB80cvCDfSwpcMqFAQF5qmS1O0pU

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port on which the app will run
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

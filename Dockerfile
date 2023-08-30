FROM python:3.9

# Install ping utility
RUN apt-get update && apt-get install -y iputils-ping

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables as empty (default values)
ENV USER_NAME=""
ENV USER_PWD=""
ENV DB_URL=""

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]


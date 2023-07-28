# Use the official Python 3.9 image as the base
FROM python:3.9

# Set the working directory to the current directory
WORKDIR .

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Copy all files from the current directory to the working directory
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run database migrations using Django's manage.py script
RUN python3 manage.py migrate

# Expose port 8000 to the outside world
EXPOSE 8000

# Start the Django development server
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

#FROM python:2.7
#ADD sum_nums.py /
#RUN pip install Flask 
#EXPOSE 8000
#CMD ["python", "sum_nums.py"]
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "run.py"]

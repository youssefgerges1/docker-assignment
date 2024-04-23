# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /stopwords

# Copy the current directory contents into the container at /app
COPY . /stopwords
COPY . /paragraphs.txt
# Install any needed dependencies specified in requirements.txt
RUN pip install nltk && \
    python -m nltk.downloader stopwords && \
    python -m nltk.downloader punkt
# Download NLTK data
RUN python -m nltk.downloader stopwords

# Run the Python script
CMD ["python", "stopwords.py"]

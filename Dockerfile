# Extend the base Python image
FROM python:3.8

# Add the NodeSource PPA
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -  # Updated to Node.js 14

# Install any additional OS-level packages
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client nodejs npm

# Verify PATH includes npm
ENV PATH /usr/local/bin:$PATH

# Inside the container, create an app directory and switch into it
RUN mkdir /app
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy package.json and install Node dependencies
COPY ./package.json /app/package.json
RUN npm install --verbose  # Added verbose flag for more detailed output

# Copy the rest of the application
COPY . /app

# Add a bogus env var for the Django secret key
ENV DJANGO_SECRET_KEY 'foobar'

# Build static files into the container
RUN python manage.py collectstatic --noinput
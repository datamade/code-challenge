# Extend the base Python image
FROM python:3.8

# Add the NodeSource PPA and install Node.js and npm
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get update && \
    apt-get install -y --no-install-recommends postgresql-client nodejs && \
    node -v && npm -v && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Install ESLint globally and check its version
RUN npm install -g eslint && eslint -v

# Create an app directory and set it as the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy package.json and package-lock.json and install Node.js dependencies
COPY ./package.json ./package-lock.json /app/
RUN npm install

# Copy the rest of the application code
COPY . /app

# Add a bogus env var for the Django secret key
ENV DJANGO_SECRET_KEY 'foobar'

# Build static files into the container
RUN python manage.py collectstatic --noinput

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "parserator_web.wsgi:application"]

# DataMade Parserator Challenge Solution

Hi DataMade Team,

**My name is Ahmad, and I work at the New York City Council**. Welcome to my code challenge solution! 👋

At the City Council, I frequently engage in civic projects, often involving the display of data on interactive Leaflet maps. This challenge was a delightful experience, and I thoroughly enjoyed working on it.

## Overview

The challenge was both fun and educational. Below is a summary of what I accomplished during this project:


## Demo: Handling Various Address Entry Scenarios
!["Address Entry Scenarios](images/parserator-solved-demo.gif)

## Accomplishments

### Backend Development

**Implemented the `parse` Method:**
- Used `usaddress` to parse address strings into components.
- Handled various edge cases including repeated address labels and invalid addresses.

**Enhanced Error Handling:**
- Implemented specific error responses for unparseable addresses and repeated labels.
- Ensured the API returns meaningful error messages to guide the user.

### Frontend Development

**Wired Up the Form:**
- Connected the form to the backend API using JavaScript.
- Ensured the form sends address data to the API and receives the parsed components.

**Displayed Results and Errors:**
- Implemented dynamic display of parsed address components.
- Handled and displayed error messages directly on the frontend to enhance user experience.

### Docker File

**Docker Setup:**
- Used Docker and Docker Compose for containerized development and testing.
- Ensured smooth setup and teardown of the application environment.
- Integrated ESLint for JavaScript linting.
- Added npm installation and ESLint setup in the Dockerfile.

### Testing

**Added Unit Tests:**
- Created unit tests to ensure the API returns correct responses for valid and invalid addresses.
- Verified that error messages are returned appropriately for different failure cases.

**Passed All Tests:**
- Successfully passed all unit tests and ESLint checks.
  - Python linting passed! 👍
  - JavaScript linting passed! 👍
  - `tests/test_views.py::test_api_parse_succeeds` PASSED
  - `tests/test_views.py::test_api_parse_raises_error` PASSED

## Installation Instructions

Development requires a local installation of [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/). These are the only two system-level dependencies you should need.

Once you have Docker and Docker Compose installed, build the application containers:
```
docker-compose build
```
Next, run the app:
```
docker-compose up
```

The app will log to the console, and you should be able to visit it at http://localhost:8000.

You can run the tests using Docker:
```
docker-compose -f docker-compose.yml -f tests/docker-compose.yml run --rm app
```

This project involved recreating the address parsing functionality of DataMade's Parserator service. Key tasks included implementing the parsing logic, enhancing error handling, wiring up the frontend form to the backend API, and ensuring comprehensive testing with unit tests.

So excited and looking forward to your feedback!
Thank you!

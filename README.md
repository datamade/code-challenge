# DataMade Code Challenge: Parserator
### **Table of Contents**
- [About the Challenge](#about-the-challenge)
- [Development Process](#development-process)
- [Helpful Resources](#helpful-resources)
- [Where To Find Me](#where-to-find-me)

## **About the Challenge**
Hi, I'm Emma and welcome to my submission for the DataMade code challenge! 👋

For this challenge I recreated the **address parsing form** in DataMade's
[Parserator](https://parserator.datamade.us) web service. Parserator can take
input strings that represent addresses (like `123 main st chicago il`)
and split them up into their component parts:

![Example of Parserator parsing the string "123 main st chicago il"](images/usaddress.gif)

To complete this challenge, I had to teach myself enough about Python and Django to set up the backend, and use my knowledge
of vanilla JavaScript to finish building out the front end. In this README I'll highlight some of the resources I used to complete 
this challenge and some takeaway learnings from this process.

### Tech Stack
   * Python/Django
   * Pytest
   * Vanilla JavaScript
   * Docker

### Running the App Locally
* run `docker-compose up`
* Open  http://localhost:8000 and check out the app!

## Run Unit Tests
* run `docker-compose -f docker-compose.yml -f tests/docker-compose.yml run --rm app`

## **Development Process**
### **Timing**
Though the prompt suggested a 2 hour time block to complete,  I spent significantly longer completing this challenge. While I highly value work-life balance, I enjoyed this opportunity to learn and put in extra effort due to my high interest in working with DataMade.

I anticipated needing to familiarize myself with Python and Django, since my area of familiarity lies primarily in JavaScript/HTML/CSS.

Before I started coding, I spent time exploring the existing code base. I figured out key functions and flows, and also identified what I could ignore. Even with a small application as this challenge, it’s easy to get too many fingers into too many code pies, so I needed to stay focused on deliverables. After understanding the flow of data, it was time to start coding.

### **Work Flow**
Completing Steps 1 and 2 was challenging, mostly due to being unsure of syntax or how to read the feedback from my code since I’d never used Python or Docker to print logs. 

To continue progressing, I switched to Step 5, the testing portion.  That way, I could get my tests to shed light on what my get requests from the `Parserator` API were returning. My experience with TDD using Mocha/Chai helped me understand the basics of Pytest unit testing. 

I also set up a mock server on Postman to get practice sending requests for testing, though the Parserator docs were my primary source for understanding the shape of my request responses.

I completed the vanilla JS portion smoothly and even added some styling!

### **Documentation**
After implementing TypeScript in my last few React projects, I’ve grown to appreciate the value typing code to reduce pesky type errors. It also helps developers unfamiliar with the code understand the flow of data faster and feel more confident when contributing to a project. 

I implemented block tags such as `@param` and `@returns`, to provide documentation for what data types each function should expect and return, as well as code comments to provide further context for any developers reading through the code.

### **Linter Note**
* Known linter error related to ES6 module export syntax. Code follows ES6 standards.

## **Helpful Resources**
I struggled to find helpful documentation on Django. I started with their docs, but found them difficult to use for someone so unfamiliar with the framework (and with Python in general). I relied heavily on my googling skills, as well as several of DataMade's docs to get the information I needed to complete this challenge.

Despite these hurdles, I'm excited to expand my knowledge of Python and Django. I hope the following resources can help other developers get up to speed more quickly.

***Resources***
* [Testing Django with Pytest](https://djangostars.com/blog/django-pytest-testing/)
* [Django REST API Tutorial](https://www.askpython.com/django/django-rest-api)
* [Another Django REST Tutorial](https://www.simplifiedpython.net/django-rest-api-tutorial/)
* [DataMade Pytest Docs](https://github.com/datamade/testing-guidelines/blob/master/framework-specific-patterns.md#django)
* [Parserator API Docs](https://parserator.datamade.us/api-docs/)
* [Morale Booster](https://www.youtube.com/watch?v=MvOE2ZwWrKE)

## **Where To Find Me**
Emma Brooke-Davidson | [GitHub](https://github.com/emmacbd) &#124; [LinkedIn](https://www.linkedin.com/in/emmacbd/)
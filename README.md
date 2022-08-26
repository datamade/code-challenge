# DataMade Code Challenge: Parserator
### **Table of Contents**
- [About the Challenge](#about-the-challenge)
- [Key Takeaways](#key-takeaways)
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

## **Key Takeaways**
For the sake of honoring the ethos of work-life balance, I initially set out to give myself a limit of 10 hours to complete this challenge. Though the prompt suggested a 2 hour time block to complete, I anticipated I would need to spend a fair amount of time at the onset to familiarize myself with Python and Django, since my area of familiarity lies primarily in JavaScript/HTML/CSS land. To be honest, I lost track of how much time I spent, because once I got in the groove I had a lot of fun learning about building out a back end and getting a refresher on vanilla JS. 

Before I started coding, I spent solid hour poking around the existing code base to see what I could parse out. I learned that the views, urls, settings, etc. were typical Python file structures. I tried to figure out what would be helpful to understand and what I could ignore, because even with a small application as this challenge I found it easy to get too many fingers in too many figerative code pies, and the last thing I wanted to do was psych myself out of giving it my best shot. After I felt I had a decent understanding of the flow of data, it was time to start coding.

I muddled through various shades of productive struggle to complete Steps 1 and 2 of the challenge, mostly due to being unsure how to receive and read the feedback from my code. I decided to switch to Step 5, the testing portion, to see if I could get my tests to shed light on what my get requests from the `Parserator` API were returning. My experience with TDD using Mocha/Chai helped me understand the basics of Pytest unit testing. I also decided to set up a mock server on Postman to get practice sending requests for testing, though the Parserator docs were my primary source for understanding the shape of my request responses.

I was able to complete the vanilla JS portion with only minor hiccups (after spending the last couple months writing React/TypeScript, I had to brush up a bit on old school DOM manipulation). After implementing TypeScript in my last few React projects, I've grown to appreciate the value of providing types for my code in JS, as it reduces pesky type errors and in my experience, makes it easier for developers unfamiliar with the code to understand the flow of data faster and to feel more confident in contributing to the project. I implemented block tags such as `@param` and `@returns`, which I recently learned about and have used for the first time in this challenge, to provide documentation for what data types each function should expect and return, as well as code comments to provide further context for any developers reading through the code. 

## **Helpful Resources**
I really struggled to find helpful documentation on Django. I started with their docs, but found them difficult to use for someone so unfamiliar with the framework (and with Python in general). I'm definitely interested in spending more time learning both Python and Django with resources more geared at junior developers. I relied heavily on my googling skills, as well as several of DataMade's docs to get the information I needed to complete this challenge.

***Resources***
* [Testing Django with Pytest](https://djangostars.com/blog/django-pytest-testing/)
* [Django REST API Tutorial](https://www.askpython.com/django/django-rest-api)
* [Another Django REST Tutorial](https://www.simplifiedpython.net/django-rest-api-tutorial/)
* [DataMade Pytest Docs](https://github.com/datamade/testing-guidelines/blob/master/framework-specific-patterns.md#django)
* [Parserator API Docs](https://parserator.datamade.us/api-docs/)
* [Morale Booster](https://www.youtube.com/watch?v=MvOE2ZwWrKE)

## **Where To Find Me**
Emma Brooke-Davidson | [GitHub](https://github.com/emmacbd) &#124; [LinkedIn](https://www.linkedin.com/in/emmacbd/)
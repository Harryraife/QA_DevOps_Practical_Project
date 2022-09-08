# QA-DevOps-Practical-Project  
This repository contains my deliverable for the QA DevOps practical project.

## Contents:  
*  [Project Brief](#Project-Brief)
*  [Project Planning](#Project-Planning)
*  [App Design](#App-Design)
*  [CI/CD Pipeline](#CI/CD-Pipeline)
*  [Known Issues](#Known-Issues)
*  [Future Work](#Future-Work)

## Project Brief:  
The brief for this project was to deliver a webapp consisiting of four microservices, which interact with one another to generate objects using some defined logic. This application was to be produced and maintained using a fully automated CI/CD pipeline. The full tech stack required was as follows:  
* Trello board for project tracking
* Git for version control
* Jenkins as a CI server
* Ansible for configuration management
* GCP cloud platform
* Docker as a containerisation tool
* Docker swarm for container orchestration
* NGINX as a reverse proxy  

## Project Planning:
When planning this project, a full risk assessment was undertaken in order to identify hazards associated with this project and aim to solve problems before they arise; this is shown below:

![RA](https://imgur.com/gCzq6wt.png)

Since users are not submitting any information to this app, the main focus of this risk assessment was on operational risks: i.e. those associated with building and deployment. As can be seen, for each hazard, the probability and impact factor were quantified before and after the implementation of control measures in order to guide development.

## App Design:  
In response to this brief, I have chosen to develop a random workout generate. This utilises a microservice architecture as follows:  
* Frontend (service 1): The service with which the user interacts. This service sends requests to the other services to generate random exercises with random reps and sets, displays the generated exercises to the user, as well as storing them in a database.
* Movement API (service 2): This service receives HTTP GET requests from service 1 and responds with a randomly selected exercise chosen from a list of names using random.choice().
* Sets API (service 3): This service receives HTTP GET requests from service 1, and responds with a random number of sets and reps, again by random.choice().
* Exercise API (service 4): This service receives HTTP POST requests from service 1, which provide the randomly generated exercise, sets and reps as JSON objects, service 4 has a dictionary which uses this data to determine the accesory movements associated with the main workout; the exercise name determines the accesory movements to be added to the workout.

In addition to these main services, a reverse proxy using NGINX was implemented; the NGINX service listens to port 80 on the host machine and performs a proxy pass, directing traffic from port 80 on the host to port 5000 on the front-end container, where the app is accessible. The images below show the front-end in action:  

![front-end-home](https://imgur.com/0S9BABA.png) ![front-end-history](https://imgur.com/j40rVMK.png)

The first image shows the home page, this was originally the only route the front end had, to make the page more readable a history page was added to display the full history of generated exercises, so the home page could be limited to just the current exercise and the five most recent exercises; this history page is shown in the second image above. The exercises generated were stored in a database, the entity diagram (ED) for this is shown below:

![ED](https://imgur.com/j40rVMK.png)

Currently, the database is stored in an sqlite file, due to issues connecting the app to a MySQL service

## CI/CD Pipeline:
This project utilises a full CI/CD pipeline to test, build, deploy and maintain the application. The major components of this pipeline are:
* Project tracking
* Version control
* Development environment
* CI server
* Deployment environment  

Project tracking was done using Trello. Tasks were assigned based off of the project brief and moved through the stages from project backlog to complete as the project progressed. 

![trello-board](https://imgur.com/XQqcUqx.png)  

For more details, the trello board can be accessed [here](https://trello.com/b/CJwP506b/qa-project-2)

Git was used for version control, with the repository hosted on github. A feature-branch model was implemented in this project to protect the stable version of the application from ongoing development. 

The development environment used was a Ubuntu virtual machine, hosted on GCP, accessed via VSCode. 

Jenkins was used as a CI server. In response to a github webhook, Jenkins cloned down the repo. 

Then from the app an Ansible playbook was utilised to spin up the 4 microservices.

The front-end and all APIs had unit tests written to test all areas of functionality. To test the HTTP requests made by the front-end, requests_mock was used to simulate responses from the APIs. To test the functionality of the APIs themselves, the random.choice function was patched with unittest.mock to ensure reproducible test performance.  

100% coverage was achieved for all tests; this ensured that all of the functions of the app worked exactly as intended.

The ideal overall structure of the CI/CD pipeline is:

![CI/CD](https://i.imgur.com/OCDefsv.png)

## Known Issues:
* Due to the use of an sqlite database, data is not persisted between services. Future work would address this as a matter of priority

## Future Improvements:  
The first future improvement would, as mentioned, be the use of a database which can persist data. The app could also be further improved in future sprints by using a locally hosted Nexus repository to speed up deployment, as the images would then not have to be fetched from Dockerhub, and by using another NGINX service as an external load balancer, to provide a single point of entry to the application.

## Updates:
update test

Introduction:
  This repository contains the solution for the BankAPI Assignment, which involves creating an API server to provide information about        banks and their branch details.

Table of Contents:
  - Submission
  - Assignment Overview
  - Methodology
  - Dependencies
  - Usage
  - Deployment
  - Unit tests
  - Time Taken
  - Challenges faced during assignment

Submission:
  The assignment has been submitted via a GitHub repository. You can access the repository by following this https://github.com/Abhi-         Sen/BankAPI_DRF

Assignment Overview:
  The assignment requires the creation of an API server that provides information about banks and their branch details. The server should     have REST API endpoints to retrieve a list of banks and details about a specific branch.

Methodology:
  To complete this assignment, I have used a Python web framework to create the API service. The framework chosen is DjangoRestFramework.     The following steps outline the methodology used:

    1. Setting Up the Environment: I created a virtual environment to manage project dependencies and isolate them from other projects.
    
    2. Database Integration: I imported the provided data from the repository into the database used by the API server.
    
    3. API Endpoints:
       - POST /api/banks_api/bank/ : This endpoint created a Bank with the given name
                 curl --location 'localhost:8000/api/banks_api/bank/' \
                --header 'Content-Type: application/json' \
                --data '{
                          "name": "SBI Ropar"
                        }'
       - GET /api/banks_api/bank : This end point return all thye banks in the database.
                 curl --location --request GET 'localhost:8000/api/banks_api/bank/' \
                 --header 'Content-Type: application/json' \
                  --data ''
       - GET /api/banks_api/bank/{bank_id} : This end point return the the bank with the given id.
               curl --location --request GET 'localhost:8000/api/banks_api/bank/2' \
               --header 'Content-Type: application/json' \
               --data ''
       - POST api/ banks_api/ bank/<bank_id>/branch/: This endpoint creates a branch of a specific bank with the given bank_id.
             curl --location --request GET 'localhost:8000/api/banks_api/bank/1/branch/' \
              --header 'Content-Type: application/json' \
              --data '{
                          "ifsc": "TEST1234567",
                          "branch": "Test Branch",
                          "address": "Test Address",
                          "city": "Test City",
                          "district": "Test District",
                          "state": "Test State"
                       }' 
       - GET api/ banks_api/ bank/<bank_id>/branch/<ifsc>/: This endpoint return details of a specific bank branch withnthe given IFSC code.
              curl --location 'localhost:8000/api/banks_api/bank/1/branch/TEST1234567' \
              --data ''
    
    5. Code Structure:
         I have organized the code into well-defined modules, following best practices to ensure clean and maintainable code.

Dependencies:
    The project has the following dependencies:
    - [Python](https://www.python.org/)
    - [Django REST Framework]
    - [MySQL]
    
    All other dependencies are listed in the `requirements.txt` file in the repository.

Usage:
    To run the API server locally, follow these steps:
    1. Clone the repository to your local machine.
    2. Set up a virtual environment and activate it.
    3. Install the project dependencies using `pip install -r requirements.txt`.
    4. Run the server using `python app.py`.

    The API will be accessible at `http://localhost:8000`.

Unit tests:
  Run the file banks_api/tests.py directly in Pycharm. Make sure to select "target" -> module as well as the file name to be                  tests.BankAPITestCase

Time Taken:
    The assignment was completed in total 10 hours. Given that I have given few hours per day.

Challenges faced:
  1. Tried running the unit tests via terminal but got stuck. Here is what I have tried:
      a. export DJANGO_SETTINGS_MODULE=BankAPI.settings  
      b.  python -m unittest discover


# Hudl Login Page Front End Tests

This project focuses on front end testing of Hudl login functionality which can be found at "https://www.hudl.com/login". 
The tests have been setup to run on Chrome Browser, which can be expanded in future for cross browser testig by installing the required drivers.

## Requirements:

- `python3`
- `Chrome`
- `Chromedriver`

### Python
This repository has been created and tested using python 3.11.2

### Chrome
This repository has been created and tested using Chrome Version 111.0.5563.146 and Chromedriver 111.0.5563.64
Move the unpacked chromedriver to be in your PATH (https://selenium-python.readthedocs.io/installation.html#drivers)[https://selenium-python.readthedocs.io/installation.html#drivers]

## Setup

1. Clone the repository
2. Open the terminal, navigate to the root of the Hudl folder
3. Install dependencies - `pip install -r requirements.txt`

## Run Tests
1. Run `behave` to run all scenarios within the repo
2. Alternatively run `behave -n "scenario_name"` to run one single scenario



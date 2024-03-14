# Auction Website

A full stack auction website created using Django and MySQL, designed to connect sellers and buyers in an accessible online marketplace. Users can list items for auction, bid on items, and manage their listings, all within a user-friendly interface.

## Table of Contents

- [Quick Start](#quick-start)
- [Technologies](#technologies)

## Quick Start

### Prerequisites

Ensure you have Python 3.8 or newer, MySQL, and MySQL Workbench set up on your local machine. You should have a database created for this project, with a user granted all privileges on the database. 


### Clone Repository

Clone this repository to your local machine using the following command:

`git clone https://github.com/uzo-ogbanufe/cs_capstone.git`


### Install Dependencies

Install the required Python packages using pip:

`pip install mysqlclient django`


### Configuration

In the project file `auction_site/settings.py`, replace `USER` and `PASSWORD` with your MySQL root username and password.

In your MySQL database, open the SQL scripts from the `database` folder and run `create_database.sql` and `database_procedures.sql`.


### Run Server

Navigate to the project's directory and run the Django development server with:

`python manage.py runserver`

The server will start, and you can access the application through `localhost:8000` in your browser.


## Technologies

Django, HTML and CSS, and MySQL

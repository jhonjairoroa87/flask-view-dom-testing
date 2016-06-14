# flask-view-dom-testing
Example of how flask views DOM is tested

## Configuring the application

1. Clone the project:
`$ git clone https://github.com/jhonjairoroa87/flask-view-dom-testing`
2. Install project requirements:
`pip install -r requirements.txt`
3. Add meetup.com key to settings.py file
`MEETUP_API_KEY = "INSERT MEETUP API KEY"`

## Running the application
Run the following command
`python runserver.py`

## Verifying the application is up
Call one of the following urls in your browser:
 - http://0.0.0.0:5000/
 - http://0.0.0.0:5000/groups

## Testing the application
Run the following command
`nosetests -sv`

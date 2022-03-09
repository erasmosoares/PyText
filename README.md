# Sending text messages with python

You need a twilio account:

https://www.twilio.com/

Add a config.py file to the project and create the following variables

```
account_sid = "your twilio account sid"
auth_token = "your twilio account auth token"
from_number = "from number"
to_numer = "to number"
```

For new projects install twilio

```
pipenv install twilio
```

Run

```
python .\app.py
```

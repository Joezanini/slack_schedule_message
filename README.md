# Slack Message Scheduler

a simple bot that can be added to a channel to gather time data to schedule a 
message to kick off the next day. 

## set up
Please go to https://api.slack.com/apps to register a new app for your workspace. 
Name the app something like "Schedule Bot"

### OAuth scopes
Then go to the Apps OAuth Scopes & Permissions section and add the below scopes
* app_mentions:read
* chat:write
* links:write
  
once the scopes are added, copy the YOUR BOT USER OAUTH TOKEN and paste it in the
appropriate sections of the code (lines 12, 19 of nextdaybot.py).

## Event API
Go to the apps Basic Info Section and copy the apps SIGNING SECRET. Paste it in the
appropriate sections of the code (line 20 of nextdaybot.py)

go to the Events Subscription page and input the URL in which you will host the app
for example. https://www.myapp.com/slack/events BE SURE TO APPEND /slack/events to the
url for the sdk to properly listen for events.

https://api.slack.com/apis/connections/events-api

## Interactive messages
subscribe to interactive messages by going to the Interactive & Shortcuts section in 
the apps home page. Then use the same url that is subscribed for Events to register 
for interactive triggers. This will make the datetime action work. 

## Running the app
Change the ```channel_id``` variable on line 35 to the actual channel in which the 
bot lives.

I tested the app using ```ngrok http 5000``` in a terminal. Then using 
```python3 nextdaybot.py``` to run the code. Then append /slack/events
in the above steps to the ngrok https url for testing. 

## Using the app
Once the app is added to a Workspace and then added to a space, users can @mention the 
bot and hit send. The bot will respond by sending a interactive block kit message asking for a time. When a time is entered, the bot will schedule a message to happen the next day.




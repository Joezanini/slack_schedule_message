
import logging
import os
import json
import schedule
import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token="YOUR BOT USER OAUTH TOKEN")
logger = logging.getLogger(__name__)
# Import Bolt for Python (github.com/slackapi/bolt-python)
from slack_bolt import App

# Initializes your Bolt app with a bot token and signing secret
app = App(
    token="YOUR BOT USER OAUTH TOKEN",
    signing_secret="SIGNING SECRET"
)


# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
#client = WebClient(token='xoxb-5251405066354-5252591971330-GNGUkmwuRl6A3bneDk6cCnFp')

# Channel you want to post message to
channel_id = "#bots"

@app.action("timepicker-action")
def update_message(ack, body, client) :
    #print(body['user']['username'])
    username = body['user']['username']
    #print('time : ', body['actions'][0]['selected_time'])
    time = body['actions'][0]['selected_time']
    # Create a timestamp for tomorrow at 9AM
    h = time[0] + time[1]
    m = time[3] + time[4]
    #print("hour : ", h)
    #print("minutes : ", m)
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    scheduled_time = datetime.time(hour=int(h), minute=int(m))
    schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')

    schedule_message(username, schedule_timestamp)
    ack()

#@slack_event_adapter.on('app_mention')
@app.event("app_mention")
def handle_mention(event, say, logger):
    print("Received event: {event}")
    send_onboarding(channel_id)

'''
Function Name : send_onboarding()
Function Description : Sends onboarding message to Channel
                       when the bot is mentioned. 
'''
def send_onboarding(channel_id) : 
        
    try:
        # Call the chat.postMessage method using the WebClient
        result = client.chat_postMessage(
            channel=channel_id,
            text="Hello", 
            blocks=[
		    {
			    "type": "header",
			    "text": {
				    "type": "plain_text",
				    "text": "Schedule Message",
				    "emoji": True
			    }
		    },
		    {
			    "type": "section",
			    "text": {
				    "type": "mrkdwn",
				    "text": "Select a Time"
			    },
			    "accessory": {
				    "type": "timepicker",
				    "initial_time": "13:37",
				    "placeholder": {
					    "type": "plain_text",
					    "text": "Select time",
					    "emoji": True
				    },
				    "action_id": "timepicker-action"
			    }
		    }
		])

        logger.info(result)

    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")
    return

'''
Function Name : schedule_message()
Function Description : a function that schedules a message
                       to be sent daily to the channel.
'''
def schedule_message(username, time) : 

    try:
        # Call the chat.scheduleMessage method using the WebClient
        result = client.chat_scheduleMessage(
            channel=channel_id,
            text="hello " + username + ", please vist https://www.example.com",
            post_at=time
        )
        print(result)
        # Log the result
        logger.info(result)

    except SlackApiError as e:
        logger.error("Error scheduling message: {}".format(e))
    return


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))
from deta import app

from twilio.rest import Client
from settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from detabase import PoemTable


@app.lib.cron()
def cron_job(event):
  client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

  pending_poems = PoemTable.fetch(query=[{"is_verified": True}])
  msg = f"You have {pending_poems.count} pending poems"
  message = client.messages.create(
    body=msg,
    from_='+13608380336',
    to='+84948224950'
  )
  return str(message.sid)

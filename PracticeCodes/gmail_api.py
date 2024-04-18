from simplegmail import Gmail

gmail = Gmail()

# Sending an email
# params = {
#   "to": "amanverma7231236@gmail.com",
#   "sender": "noname7231236@gmail.com",
#   "subject": "My first email Sample Email",
#   "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
#   "msg_plain": "Hi\nThis is a plain text email.",
#   "signature": True  # use my account signature
# }
# message = gmail.send_message(**params)  # equivalent to send_message(to="you@youremail.com", sender=...)


# Unread messages in your inbox
# messages = gmail.get_unread_inbox()
#
# # Starred messages
# # messages = gmail.get_starred_messages()
#
# # ...and many easier to use functions can be found in gmail.py!
#
# # Print them out!
# for message in messages:
#     print("To: " + message.recipient)
#     print("From: " + message.sender)
#     print("Subject: " + message.subject)
#     print("Date: " , message.date)
#     print("Preview: ", message.snippet)
#
#     print("Message Body: " , message.plain)  # or message.html
#

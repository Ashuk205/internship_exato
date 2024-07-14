from instagrapi import Client

# Initialize the client
cl = Client()

# Login to your account
username = 'heyy.ashutosh_singh'
password = 'Shobhakamlesh@456123#'
cl.login(username, password)

# Specify the recipient and message
recipient_username = 'kris_krishna__'
message_text = 'hii'

# Get user id
user_id = cl.user_id_from_username(recipient_username)

# Send the message
cl.direct_send(message_text, [user_id])

print("Message sent successfully!")

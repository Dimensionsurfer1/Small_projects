
sent_message = 'Hey there! This is a secret message.'
try:
    with open('sent_message.txt', 'w') as file:
        file.write(sent_message)
finally:
    file.close()
with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()
      
  # Move the cursor to the beginning of the file
  file.seek(0)
# Modify the message to simulate unsending
unsent_message = 'This message has been unsent.'
with open('sent_message.txt', 'r+') as file:
    file.truncate(len(unsent_message))
    file.write(unsent_message)
    print("Original Message:", original_message)
    print("Unsent Message:", unsent_message)

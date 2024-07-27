#!/usr/bin/env python3
# All time is in UTC time (I cannot be bothered fixing it)
# Download your data dump and place this file in the messages folder of your data dump.
# Then run it!

import json
import os
import re

messages_array =[]
dates = []

print("Would you like this to be an exact search? (y/n)")
xy = input()


print("Enter what you would like to search for: ")
x = input()


if xy.lower() == "n":
    print(f"reading messages...")
    for dir in os.listdir("."):
        if (os.path.isdir(dir)):
            with open(dir + '/messages.json', 'r') as json_file:
                json2 = json.load(json_file)
                for message in json2:
                    message2 = message["Contents"]
                    if x.lower() in message2.lower():
                        if "cdn.discordapp.com" in message2.lower():
                            messages_array.append(message["Timestamp"] + " " +  message2.replace("cdn.discordapp.com", "cdn.discordapp.xyz"))
                        elif "cdn.discordapp.net" in message2.lower():
                            messages_array.append(message["Timestamp"] + " " +  message2.replace("cdn.discordapp.net", "cdn.discordapp.xyz"))
                        elif "media.discordapp.net" in message2.lower():
                            messages_array.append(message["Timestamp"] + " " +  message2.replace("media.discordapp.net", "media.discordapp.xyz"))
                        elif "media.discordapp.com" in message2.lower():
                            messages_array.append(message["Timestamp"] + " " +  message2.replace("media.discordapp.com", "media.discordapp.xyz"))
                        else:
                            messages_array.append(message["Timestamp"] + " " +  message2)
                    message3 = message["Attachments"]
                    if x.lower() in message3.lower():
                        if "cdn.discordapp.com" in message3.lower():
                            messages_array.append(message["Timestamp"] + " " +  message3.replace("cdn.discordapp.com", "cdn.discordapp.xyz"))
                        elif "cdn.discordapp.net" in message3.lower():
                            messages_array.append(message["Timestamp"] + " " +  message3.replace("cdn.discordapp.net", "cdn.discordapp.xyz"))
                        elif "media.discordapp.net" in message3.lower():
                            messages_array.append(message["Timestamp"] + " " + message3.replace("media.discordapp.net", "media.discordapp.xyz"))
                        elif "media.discordapp.com" in message3.lower():
                            messages_array.append(message["Timestamp"] + " " + message3.replace("media.discordapp.com", "media.discordapp.xyz"))
                        else:
                            messages_array.append(message["Timestamp"] + " " + message2)
                json_file.close()
elif xy.lower() == "y":
    print(f"reading messages...")
    for dir in os.listdir("."):
        if (os.path.isdir(dir)):
            with open(dir + '/messages.json', 'r') as json_file:
                json2 = json.load(json_file)
                for message in json2:
                    message2 = message["Contents"]
                    if re.search(fr'\b{x.lower()}\b', message2.lower()):
                        if "cdn.discordapp.com" in message2.lower():
                            messages_array.append(message["Timestamp"] + " " +  message2.replace("cdn.discordapp.com", "cdn.discordapp.xyz"))
                        elif "cdn.discordapp.net" in message2.lower():
                            messages_array.append(message["Timestamp"] + " " +  message2.replace("cdn.discordapp.net", "cdn.discordapp.xyz"))
                        elif "media.discordapp.net" in message2.lower():
                            messages_array.append(message["Timestamp"] + " " +  message2.replace("media.discordapp.net", "media.discordapp.xyz"))
                        elif "media.discordapp.com" in message2.lower():
                            messages_array.append(message["Timestamp"] + " " +  message2.replace("media.discordapp.com", "media.discordapp.xyz"))
                        else:
                            messages_array.append(message["Timestamp"] + " " +  message2)
                    message3 = message["Attachments"]
                    if re.search(fr'\b{x.lower()}\b', message3.lower()):
                        if "cdn.discordapp.com" in message3.lower():
                            messages_array.append(message["Timestamp"] + " " +  message3.replace("cdn.discordapp.com", "cdn.discordapp.xyz"))
                        elif "cdn.discordapp.net" in message3.lower():
                            messages_array.append(message["Timestamp"] + " " +  message3.replace("cdn.discordapp.net", "cdn.discordapp.xyz"))
                        elif "media.discordapp.net" in message3.lower():
                            messages_array.append(message["Timestamp"] + " " + message3.replace("media.discordapp.net", "media.discordapp.xyz"))
                        elif "media.discordapp.com" in message3.lower():
                            messages_array.append(message["Timestamp"] + " " + message3.replace("media.discordapp.com", "media.discordapp.xyz"))
                        else:
                            messages_array.append(message["Timestamp"] + " " + message2)
                json_file.close()
else:
    print("Invalid input")
    exit()

print(f"{len(messages_array)} total messages found containing {x}")

print("sorting messages...")

messages_array.sort()
print("done sorting!")

print("would you like to write the messages to a file? (y/n)")
x = input()

if x.lower() == "n":
    pass
elif x.lower() == "y":
    print("writing to file...")
    with open("output.txt", "w", encoding="utf-8") as file:
        for messages in messages_array:
            file.write(messages + "\n")
    file.close()
else:
    pass

print("would you like to print the messages to the console? (y/n)")
y = input()

if y.lower() == "y":
    for messages in messages_array:
        print(messages)
else:
    print("Done!")
    exit()
    
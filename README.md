# CHLib-Bot-For-Chatango
My take on a simple to use bot for chatango. This is my base source code only. Not the full bot

Update Log:
      Added Youtube Command To Source code. You still need your own API Key for Youtube v3 to use the command
      Fixed a glitch where posts were being ignored. This was due to a bug in the prefix code and thew bot trying to use the old prefix
      
To do list:
      Add a money ranking system.
      Add XP and Leaderboards
      Add a bot personality
      Set up definitions
      Add a nickname command to the bot
      Add Ranking for users, Example: Whitelisted, half master, Master, Elite Master, Owner, Debug etc
      Allow the bot to use xmpp
      Give the bot a way to use notification messages for use with lottery, notes between friends, etc.
      Russian Roulette game mode
      Hangman game mode
      Clean up file system and source code to make it run smoothly.


How to set up commands within the bot:
      If you have never used chlib then the code may be confusing to you.
      Send a message to a group:
            for example, if you wanted the bot to reply to you saying hello. You would add this above the prefix part in RecvPost:
                  if post.post == "yourbotname":
                        group.sendPost("Hello "+user+" ^^")
            Would reply with the message: Hello YourUsernameHere
      Sending PM Messages to users within the bot:
            To do this you will be utilizing the sendPM command. It is used like so.
                  if cmd == "pmuser" and len(args) > 0:
                        try:
                              name, msg = args.split(" ", 1)
                              self.sendPM(user, msg+" - Sent by: "+user+"")
                              group.sendPost(user+" Your message was successfully sent to "+name+"")
                        except:
                              group.sendPost("I failed to send the message.")
If you happen to find any bugs with this bot please start an issue request and I will get back to you asap.

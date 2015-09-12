# CHLib-Bot-For-Chatango<br>
My take on a simple to use bot for chatango. This is my base source code only. Not the full bot<br>

Update Log:<br>
      Added Youtube Command To Source code. You still need your own API Key for Youtube v3 to use the command<br>
      Fixed a glitch where posts were being ignored. This was due to a bug in the prefix code and thew bot trying to use the old prefix<br>
      
To do list:<br>
      Add a money ranking system.<br>
      Add XP and Leaderboards<br>
      Add a bot personality<br>
      Set up definitions<br>
      Add a nickname command to the bot<br>
      Add Ranking for users, Example: Whitelisted, half master, Master, Elite Master, Owner, Debug etc<br>
      Allow the bot to use xmpp<br>
      Give the bot a way to use notification messages for use with lottery, notes between friends, etc.<br>
      Russian Roulette game mode<br>
      Hangman game mode<br>
      Clean up file system and source code to make it run smoothly.<br>


How to set up commands within the bot:<br>
      If you have never used chlib then the code may be confusing to you.<br>
      Send a message to a group:<br>
            for example, if you wanted the bot to reply to you saying hello. You would add this above the prefix part in RecvPost:<br>
                  if post.post == "yourbotname":<br>
                        group.sendPost("Hello "+user+" ^^")<br>
            Would reply with the message: Hello YourUsernameHere<br>
      Sending PM Messages to users within the bot:<br>
            To do this you will be utilizing the sendPM command. It is used like so.<br>
                  if cmd == "pmuser" and len(args) > 0:<br>
                        try:<br>
                              name, msg = args.split(" ", 1)<br>
                              self.sendPM(user, msg+" - Sent by: "+user+"")<br>
                              group.sendPost(user+" Your message was successfully sent to "+name+"")<br>
                        except:<br>
                              group.sendPost("I failed to send the message.")<br>
If you happen to find any bugs with this bot please start an issue request and I will get back to you asap.<br>

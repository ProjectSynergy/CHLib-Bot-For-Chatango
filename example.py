import chlib
import json
import random
import re
import time
import urllib.request as urlreq

groups = []
f = open("filesystem/groupvariables/groups.txt", "r")
print("[INFO][DATA]Loading Room list...")
time.sleep(1)
for name in f.readlines():
    if len(name.strip())>0: groups.append(name.strip())
f.close()
print("Rooms successfully loaded...")

whitelist = []
f = open("filesystem/groupvariables/whitelist.txt", "r")
print("[INFO][DATA]Loading Whitelist...")
time.sleep(1)
for name in f.readlines():
    if len(name.strip())>0: whitelist.append(name.strip())
f.close()
print("whitelist successfully loaded...")

Masters = []
f = open("filesystem/groupvariables/Masters.txt", "r")
print("[INFO][DATA]Loading Masters...")
time.sleep(1)
for name in f.readlines():
    if len(name.strip())>0: Masters.append(name.strip())
f.close()
print("Masters successfully loaded...")

HalfM = []
f = open("filesystem/groupvariables/HalfMasters.txt", "r")
print("[INFO][DATA]Loading Half Masters...")
time.sleep(1)
for name in f.readlines():
    if len(name.strip())>0: HalfM.append(name.strip())
f.close()
print("HalfMasters successfully loaded...")

##Ranking System
ranks=dict()
f = open("filesystem/Games/UserVariables.txt", "r") # read-only
print("[INFO]LOADING Ranking Structure...")
time.sleep(1)
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user, exp,lvl, money= json.loads(line.strip())
      ranks[user] = json.dumps([exp,lvl,money])
  except:
    print("[ERROR]Cant load Rank: %s" % line)
f.close()
nicks = dict() 
f = open("filesystem/groupvariables/nicks.txt", "r") # read-only
print("[INFO][DATA]Loading Nicknames...")
time.sleep(1)
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user, nick= json.loads(line.strip())
      nicks[user] = json.dumps(nick)
  except:
    print("[ERROR]Cant load nick: %s" % line)
f.close()

class Bot(chlib.ConnectionManager):
                                
                                def start(self):
                                                for group in groups:
                                                                self.addGroup(group)
                                                self.prefix = "!" #optional, just won't call any commands if not specified. EDIT: Not Needed as the prefix is loaded in recvPost instead.
                                                self.fColor = "8B6914"
                                                self.nColor = "8B6914"

                                def getAccess(self, user):
                                                if self.name == "denisstoff": return 4 #Just a rank option. You can edit this to allow Whitelisted users, etc
                                                elif self.name == "AddYourNameHere": return 4
                                                elif user.lower() in Masters: return 3
                                                elif user.lower() in HalfM: return 2
                                                elif user.lower() in whitelist: return 1
                                                else: return 0
                                def recvdenied(self, group):
                                                print("Failed to connect to "+group.name)

                                def recvinited(self, group):
                                                print("Connected to "+group.name)

                                def recvOK(self, group):
                                                print("Connected to "+group.name)

                                def recvRemove(self, group):
                                                print("Disconnected from "+group.name)

                                def recvCommand(self, group, user, auth, post, cmd, args):
                                                if cmd == "a":
                                                                group.sendPost("AAAAAAAAAAAAAA")

                                def recvPost(self, group, user, post):
                                                print(user+": "+post.post)
                                                def AddStarterCash():
                                                    if user not in ranks:
                                                        exp=0
                                                        lvl=1
                                                        money=2000
                                                        money=int(money)
                                                        lvl=int(lvl)
                                                        exp=int(exp)
                                                        ranks[user] = json.dumps([exp,lvl,money])
                                                        print("User added to ranks successfully")
                                                    else:
                                                        print("Failed to add user to money")
                                                if post.post.startswith("YourBotNameHere") or post.post.startswith("AddShortNameHere") or post.post.startswith("AddAnotherShortNameHere"):
                                                                if user.lower() == "YourBotNameHere": return
                                                                else:
                                                                            group.sendPost("Yesh? o.o")
                                                if post.post.startswith("Airstrike"):
                                                                if group.getAuth(user) > 0:
                                                                            group.clearGroup()
                                                                else:
                                                                            group.sendPost("These were incorrect Orders. Nice try")
                                                if post.post.startswith("-poofs-"):
                                                                if group.getAuth(user) > 0:
                                                                            group.dlUser(self.name)
                                                                else:
                                                                            group.sendPost("You do not have permission to use this command")
                                                if self.user == user: return
                                                if post.post[0] == ".":   ##Here is the Prefix part
                                                                                  data = post.post[1:].split(" ", 1)
                                                                                  if len(data) > 1:
                                                                                                        cmd, args = data[0], data[1]
                                                                                  else:
                                                                                                        cmd, args = data[0], ""
                                                                                  if cmd == "say" and len(args) > 0:
                                                                                                        group.sendPost(args)
                                                                                  if cmd == "yt" and len(args) > 0:
                                                                                                        search = args.split()
                                                                                                        url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&MaxResults=1&key=AddYourDataAPIKeyHere" % "+".join(search))
                                                                                                        udict = url.read().decode('utf-8')
                                                                                                        data = json.loads(udict)
                                                                                                        rest = []
                                                                                                        for f in data["items"]:
                                                                                                                rest.append(f)
                                                                                                        d = random.choice(rest)
                                                                                                        link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
                                                                                                        videoid = d["id"]["videoId"]
                                                                                                        title = d["snippet"]["title"]
                                                                                                        uploader = d["snippet"]["channelTitle"]
                                                                                                        group.sendPost("I found: "+link+" <b>"+title+"</b> Posted By: "+uploader+"")
                                                                                                        return
                                                                                  if cmd == "wl":
                                                                                                        user=user.lower()
                                                                                                        AddStarterCash()
                                                                                                        f = open("filesystem/groupvariables/whitelist.txt", "a")
                                                                                                        f.write("\n"+user)
                                                                                                        f.close()
                                                                                                        group.sendPost("Congratulations! You have been added to the whitelist and have now gained access to all of the commands a whitelisted user can use! [+2000$]")
                                                                                  if cmd == "lvl":
                                                                                                        user = user.lower()
                                                                                                        if user in ranks:
                                                                                                                exp,lvl,money = json.loads(ranks[user])
                                                                                                                lvl=str(lvl)
                                                                                                                exp=int(exp)
                                                                                                                nextlevel = 1000
                                                                                                                nextlevel = int(nextlevel)
                                                                                                                neededxp = nextlevel - exp
                                                                                                                neededxp=str(neededxp)
                                                                                                                group.sendPost(user+" You are currently Level "+str(lvl)+" You need "+str(neededxp)+" To reach the next level")
                                                                                                        else:
                                                                                                                group.sendPost("I'm sorry, you aren't in the ranks database. Try typing .wl again")
                                                                                  if cmd == "bal":
                                                                                                        user=user.lower()
                                                                                                        if user in ranks:
                                                                                                                exp,lvl,money = json.loads(ranks[user])
                                                                                                                money=str(money)
                                                                                                                group.sendPost(user+" You currently have "+str(money)+ "$ available in your piggy bank")
                                                                                                        else:
                                                                                                                group.sendPost("I'm sorry, you aren't in the ranks database. Try typing .wl again")
                                                                                  if cmd == "sav":
                                                                                                        print("[SAVE] SAVING Ranking Data...")
                                                                                                        f = open("filesystem/Games/UserVariables.txt", "w")
                                                                                                        for user in ranks:
                                                                                                                        exp,lvl,money = json.loads(ranks[user])
                                                                                                                        f.write(json.dumps([user, exp,lvl,money])+"\n")
                                                                                                        f.close()
                                                                                                        group.sendPost("I have saved all data to the necessary files")

                                                                                  if cmd == "img" or cmd == "gis" and len(args) > 0:
                                                                                                        try:
                                                                                                                search = args.replace(" ","_")
                                                                                                                gdata = urlreq.urlopen("http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s" % "+".join(search))
                                                                                                                xdat = gdata.read().decode()
                                                                                                                x = re.finditer('"unescapedUrl":"(.+?)","url":"', xdat)
                                                                                                                mes = []
                                                                                                                for m in x:
                                                                                                                        m = str(m.group(1))
                                                                                                                        mes.append(m)
                                                                                                                link = random.choice(mes)
                                                                                                                link = link.replace("https","http")
                                                                                                                group.sendPost('%s' % link)
                                                                                                        except Exception as e:
                                                                                                                print("\n%s\n" % e)
                                                                                  if cmd == "baka":
                                                                                                        group.sendPost("https://www.youtube.com/watch?v=diI4arYYfW0")
                                                                                  if cmd == "join" and len(args) > 0:
                                                                                                        self.addGroup(args)
                                                                                                        group.sendPost("I have joined "+args+"")
                                                                                  if cmd == "leave":
                                                                                                        self.removeGroup(group.name)
                                                                                                        group.sendPost("I have just left "+group.name+" If you want me to leave your group type .leave")
                                                                                  if cmd == "b" and len(args) > 0:
                                                                                                        if group.getAuth(user) > 0:
                                                                                                                        group.ban(args)
                                                                                                                        group.sendPost("I have just banned "+args+"")
                                                                                                                        self.sendPM(args, "You have been banned from "+group.name+"")
                                                                                                                        print(args+" Has been banned in "+group.name+"")
                                                                                                        else:
                                                                                                                        group.sendPost("You cannot ban a user")
                                                                                  if cmd == "ub" and len(args) > 0:
                                                                                                        if group.getAuth(user) > 0:
                                                                                                                        group.unban(args)
                                                                                                                        group.sendPost(" I have unbanned "+args+" as you requested")
                                                                                                        else:
                                                                                                                        group.sendPost("You cannot unban users")
                                                                                  if cmd == "m" and len(args) > 0:
                                                                                                        try:
                                                                                                                        name, msg = args.split(" ", 1)
                                                                                                                        self.sendPM(name, msg+" - from "+user+"")
                                                                                                                        group.sendPost('Sent to <font size="15"><font color="#FF9966"><b>%s</b></font></font>' % name, True)
                                                                                                        except:
                                                                                                                        group.sendPost("Fail !!!")
                                                                                  if cmd == "8b" or cmd == "8ball":
                                                                                                        if not args == "":
                                                                                                                        group.sendPost(random.choice(["Yesh","No way","More than likely","I cannot determine that","Find out yourself","I refuse to comment","It's obvious"]))
                                                                                                        else:
                                                                                                                        group.sendPost("This is the 8Ball command. To Use it, type .8b [Your Question here]")
                                                                                  if cmd == "ecchi" or cmd == "Ecchi":
                                                                                                        if group.name == "randompeople-random":
                                                                                                                        group.sendPost(random.choice(["http://img12.deviantart.net/de2a/i/2014/102/a/d/hatsune_miku_ecchi_render__2_by_annechan34-d7e5obz.png","http://img10.deviantart.net/6b0d/i/2012/091/3/3/ecchi_render_by_katkoyox-d4un1x2.png","http://k41.kn3.net/taringa/2/0/2/8/2/8/13/takemikazuchi2/7B3.jpg?3236","http://orig12.deviantart.net/7e25/f/2013/178/4/2/ecchi_by_hsalacard-d6av9ie.jpg","http://www.renders-graphiques.fr/image/upload/normal/Ecchi_girl.png","http://orig15.deviantart.net/8571/f/2013/280/a/1/render_girl_anime_ecchi_by_arihirokushinada-d6pk17d.png"]))
                                                                                                        else:
                                                                                                                        group.sendPost("I am not allowed to post this here")
                                def recvmsg(self, group, user, pm):
                                                print("PM: "+user+": "+pm)
                                                if pm.startswith("Axuf") or pm.startswith("axuf"):
                                                        self.sendPM(user, "Yesh? o.o")
                                                if pm.startswith("sup?"):
                                                        self.sendPM(user, "Nothing much, You?")
                                                if pm.startswith("."):
                                                        data = pm[1:].split(" ", 1)
                                                        if len(data) > 1:
                                                                        cmd, args = data[0], data[1]
                                                        else:
                                                                        cmd, args = data[0], ""
                                                        if cmd == "cmds":
                                                                        self.sendPM(user, "Commands are yt, Ecchi, Loli, img, 8ball")
                                                        if cmd == "img" and len(args) > 0:
                                                                        try:
                                                                                        search = args.replace(" ","_")
                                                                                        gdata = urlreq.urlopen("http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s" % "+".join(search))
                                                                                        xdat = gdata.read().decode()
                                                                                        x = re.finditer('"unescapedUrl":"(.+?)","url":"', xdat)
                                                                                        mes = []
                                                                                        for m in x:
                                                                                                        m = str(m.group(1))
                                                                                                        mes.append(m)
                                                                                        link = random.choice(mes)
                                                                                        link = link.replace("https","http")
                                                                                        self.sendPM(user, '%s' % link)
                                                                        except Exception as e:
                                                                                        print("\n%s\n" % e)
    
                                                        if cmd == "m" and len(args) > 0:
                                                                        try:
                                                                                        name, msg = args.split(" ", 1)
                                                                                        self.sendPM(name, msg+" - from "+user+"")
                                                                                        self.sendPM(user, "Sent to <b>"+name+"</b>")
                                                                        except:
                                                                                        self.sendPM(user, "Fail !!!")

                                def recvkickingoff(self, group):
                                                self.removeGroup(group.name)
                                                self.addGroup(group.name)

                                def recvtoofast(self, group):
                                                self.removeGroup(group.name)
                                                self.addGroup(group.name)

if __name__ == "__main__": #no easy starting this time ;D
                                bot = Bot(user = "ayytron", password = "D3vModding", pm = True)
                                bot.main()

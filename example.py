import chlib
import json
import random
import re
import urllib.request as urlreq

class Bot(chlib.ConnectionManager):
                                
                                def start(self):
                                                groups = [ "AddYourGroupHere" ] #Simple way of adding groups. You could also define it by loading from a text file.
                                                for group in groups:
                                                                self.addGroup(group)
                                                self.prefix = "!" #optional, just won't call any commands if not specified. EDIT: Not Needed as the prefix is loaded in recvPost instead.
                                                self.fColor = "8B6914"
                                                self.nColor = "8B6914"

                                def getAccess(self, user):
                                                if self.name == "LordYusei": return 4 #Just a rank option. You can edit this to allow Whitelisted users, etc
                                                if self.name == "AddYourNameHere": return 4
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
                                                if post.post.startswith("ayytron") or post.post.startswith("ayy") or post.post.startswith("tron"):
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
                                                                                  if cmd == "oppai":
                                                                                                        if group.getAuth(user) > 0:
                                                                                                                        group.sendPost("Oppai ^_^ https://33.media.tumblr.com/4667338fc807af5041e159ed1b7bcfbd/tumblr_mv1busrDhz1sivh5go1_500.gif //nosebleeds//")
                                                                                                        else:
                                                                                                                        group.sendPost("I see no Oppai Here :|+50")
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
                                                                                  if cmd == "test":
                                                                                                        group.sendPost("this part will get sent<b>and this part won't</b>")
                                def recvmsg(self, group, user, pm):
                                                print("PM: "+user+": "+pm)
                                                if pm.startswith("Axuf") or pm.startswith("axuf"):
                                                        self.sendPM(user, "Yesh? o.o")
                                                if pm.startswith("sup?"):
                                                        self.sendPM(user, "Nothing much, You?")
                                                if pm.startswith("blake"):
                                                        self.sendPM(user, "Fuck blake. He's a homeless Nigger")
                                                if pm.startswith(".") or pm.startswith("b"):
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
                                bot = Bot(user = "AddYourUsername", password = "AddYourPassword", pm = True)
                                bot.main()

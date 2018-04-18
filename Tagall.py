# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,requests,urllib,urllib2,urllib3
from bs4 import BeautifulSoup
from urllib import urlopen
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="Er0161vbY3FUL2MnSDq4.ZczKNAC62zypidcRR9+Kba.OnLBrq6nbUHNY6Ehe6qMU97w2c3SHJqkxC3fV1ybqCA=")
cl.loginResult()
ki=ki2=ki3=ki4=cl


print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
꧁มินทีมทดลองบอท꧂
 SELF BOT MIN HACK
꧁ชุดคำสั่ง ภาษาไทย꧂

💎> Tag@@ [แทคคนท้้งห้อง]
💎> ตั้งเวลา   [จับคนแอบอ่าน]
💎> อ่าน        [เช็คคนอ่าน]
💎> ยูทูป       [ค้นหาเพลง อื่นๆ]

☣ᴴᴺᵁᴹ☞ᴮᴼᵀ☞ᴸᴵᴺᴱ☣
☣สนใจบอทแบบไหน☣
☣ทักมาคุยได้ที่ลิ้งเลยนะคับ☣
http://line.me/ti/p/HPek0z65wX
"""

Thaihelp ="""
"""

helo=""

KAC=[cl]
mid = cl.getProfile().mid
Bots = [mid,"ua1cb6e845fe8f2646fe8a5c5911841fa"]
bot1 = cl.getProfile().mid
admsa = "ua1cb6e845fe8f2646fe8a5c5911841fa"
admin = "ua1cb6e845fe8f2646fe8a5c5911841fa"

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":50},
    'leaveRoom':False,
    'timeline':False,
    'message':"""[By.มินทีมทดลองบอท]
    👇👇👇👇👇👇👇👇👇👇👇👇
👻 ลดกระหน่ำ ลดกระหน่ำ
      ราคาเชลล์บอทวันนี้
เชิญอ่านดูด้านล่างเลย
☝☝☝☝☝☝☝☝☝☝☝☝

🍑🍑🍑🍑🍑🍑🍑🍑🍑🍑🍑
[By.มินทีมทดลองบอท]
🍑🍑🍑🍑🍑🍑🍑🍑🍑🍑🍑
===ขายของคราฟ===
🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓
🍇Self  Kicker Premium🍄
🐩🐩🐩🐩🐩🐩🐩🐩
🎶Bot Protect
🎶ออกแชทกลุ่มอัตโนมัต
🎶หรือรันไม่เข้า
👛มีคำสั่งเวลาสมาชิกเตะคนอื่น
👛ตัวเราจะเตะคนนั้นออกจากกลุ่มทันที
👛สามารถเพิ่มคิกเกอร์จะเสริมการป้องกันกลุ่ม
👝ให้มีความมั่นคงได้
🚬🚬🚬🚬🚬🚬🚬🚬
💰ส่วนบอทบินกลุ่มดูข้างล่างนะครับ
💳💳💳💳💳💳💳💳
🐦🐦🐦🐦🐦🐦🐦
🍑เชลบอทฟรีเมียม ดูแลตลอดการใช้👑
🍑คำสั่งภาษาไทยใช้ง่าย🍏
🍈ราคา เฉพาะเชล 200บาทไทย🍄
🌵เพิ่ม Kicker 
1 kicker= 100บาทไทย รวมค่าโอน
2 kicker= 200บาทไทย รวมค่าโอน
3 kicker= 300บาทไทย รวมค่าโอน
5 kicker= 500บาทไทย รวมค่าโอน
10 kicker= 800บาทไทย รวมค่าโอน
เชลบอททีม(1เชล/10คิก)= 1000฿
#===================
🌚เชลล์บอท🌚บิน หรือลบสมาชิก
     🌛ความสามารถ🌜
ลบสมาชิกท้้งห้อง500คนลบภายใน10วิ
ลบบอทสิริได้ง่ายๆ
เชลล์บอทอินโด  
ราคาต่อการลบ  = 
🌑ลบ2ครั้ง = ราคา 200 บาทไทย
🌒ลบ4ครั้ง = ราคา 400 บาทไทย
🌓ลบ8ครั้ง = ราคา 800 บาทไทย 
🌕ลบ10ครั้ง = ราคา 900 บาทไทย
#===================
[👉จำหน่ายบอท แท.ค  ออ👈 ]
 💳💳💰ราคา 150 บาท💰ต่อ1ห้อง
❄แท.ค   คนท้้งกลุ่ม 
❄สามารถเช็คคนอ่านได้
❄และยังมีข้อความเวลาคนเข้าออก
👝สามารถสั่งว่าจะเอา
ข้อความเข้าออกแบบใหน
🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫
👉สนใจ สอบถามคลิกลิ้งทักมาครับ😙
👉พ่อค้าหล่อด้วยใจดี บริการเป็นกันเอง😘
📍📍📍📍📍📍📍📍📍📍📍📍📍
http://line.me/ti/p/~socool290
http://line.me/ti/p/~socool290
http://line.me/ti/p/~socool290

[By.มินทีมทดลองบอท]
""",
    "comment1":"""
           〘•✥SELF BOT BY MIN✥•〙
                 〘•AUTO LIKE ON•〙
    

✄▒█▀▄▀█ ▀█▀ ▒█▄░▒█ 
✄▒█▒█▒█ ▒█░ ▒█▒█▒█ 
✄▒█░░▒█ ▄█▄ ▒█░░▀█

☣ᴴᴺᵁᴹ☞ᴮᴼᵀ☞ᴸᴵᴺᴱ☣
☣สนใจบอทแบบไหน☣
☣ทักมาคุยได้ที่ลิ้งเลยนะคับ☣
http://line.me/ti/p/HPek0z65wX

""",
    "commentOn":True,
    "likeOn":True,
	"bcommentOn":True,
    "acommentOn":True,
    "lang":"JP",
    "clock":False,


}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

user1 = mid
user2 = ""

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
	
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

					
def bot(op):
    global AsulLogged
    global ki6
    global user2
    global readAlert
    global lgncall
    global save1
    try:
        if op.type == 0:
            return
        if op.type == 13:
  #      	print(op.param1)
  #          print(op.param2)
  #          print(op.param3)
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                            cl.sendText(msg.to, "บอทแทคสมสชมาชิกมาแล้วคราฟ")
                            cl.sendText(msg.to, "หากบอทมีปัญหาโปรดติดต่อ  มิน  นะครับ")
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(msg.to, "ผู้ช่วยหมีขาวมาแล้ว! \nหมีขาวอาจทำงานช้าหากมีผู้ใช้งานพร้อมกันมากๆ")
                            cl.sendText(msg.to, "สนับสนุนหมีขาวได้ที่ \nTrue Wallet: 0983353708\nAirpay: 0983353708")
                            cl.sendText(msg.to, "ขอขอบคุณที่สนับสนุนหมีขาวนะครับ :D")
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

#=====================
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u2a51caa84881dbc51b62282a030664ba":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")                            
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)

            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \nปลดแบน @" + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited Success \n➡ " + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break


#-----------------------------------------------
#                BOTRUN
#-----------------------------------------------
            elif msg.text in ["บอท","Help1"]:
                    cl.sendText(msg.to,helpMessage)
#-----------------------------------------------
#                BOTRUN
#-----------------------------------------------
        if op.type == 26:
            msg = op.message
				
            if msg.contentType == 16:
                url = msg.contentMetadata['postEndUrl']
                cl.like(url[25:58], url[66:], likeType=1001)
                cl.comment(url[25:58], url[66:], wait["comment1"])
                ki1.like(url[25:58], url[66:], likeType=1001)
                ki1.comment(url[25:58], url[66:], wait["comment1"])
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki2.comment(url[25:58], url[66:], wait["comment1"])
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki4.comment(url[25:58], url[66:], wait["comment1"])
                ki5.like(url[25:58], url[66:], likeType=1001)
                ki5.comment(url[25:58], url[66:], wait["comment1"])
                ki6.like(url[25:58], url[66:], likeType=1001)
                ki6.comment(url[25:58], url[66:], wait["comment1"])
                ki7.like(url[25:58], url[66:], likeType=1001)
                ki7.comment(url[25:58], url[66:], wait["comment1"])
                ki8.like(url[25:58], url[66:], likeType=1001)
                ki8.comment(url[25:58], url[66:], wait["comment1"])
                ki9.like(url[25:58], url[66:], likeType=1001)
                ki9.comment(url[25:58], url[66:], wait["comment1"])
                ki10.like(url[25:58], url[66:], likeType=1001)
                ki10.comment(url[25:58], url[66:], wait["comment1"])
                print ("AUTO LIKE SELFBOT")
                print ("Auto Like  BY ☞ 〚✯Ŧ€₳ℳ฿❂Ŧ🔝ҨัՁਙุЮℓℓ丂ს✯〛")
                
            elif "#ประกาศ:" in msg.text:
                bctxt = msg.text.replace("#ประกาศ:", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))                

            elif msg.text in ["กลุ่มบอท"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")


            elif msg.text in ["บอทขายของ"]:
            	if msg.from_ in admin:
                        cl.sendText(msg.to,"""
#ประกาศ: [By.มินทีมทดลองบอท]
    👇👇👇👇👇👇👇👇👇👇👇👇
👻 ลดกระหน่ำ ลดกระหน่ำ
      ราคาเชลล์บอทวันนี้
เชิญอ่านดูด้านล่างเลย
☝☝☝☝☝☝☝☝☝☝☝☝

🍑🍑🍑🍑🍑🍑🍑🍑🍑🍑🍑
[By.มินทีมทดลองบอท]
🍑🍑🍑🍑🍑🍑🍑🍑🍑🍑🍑
===ขายของคราฟ===
🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓
🍇Self  Kicker Premium🍄
🐩🐩🐩🐩🐩🐩🐩🐩
🎶Bot Protect
🎶ออกแชทกลุ่มอัตโนมัต
🎶หรือรันไม่เข้า
👛มีคำสั่งเวลาสมาชิกเตะคนอื่น
👛ตัวเราจะเตะคนนั้นออกจากกลุ่มทันที
👛สามารถเพิ่มคิกเกอร์จะเสริมการป้องกันกลุ่ม
👝ให้มีความมั่นคงได้
🚬🚬🚬🚬🚬🚬🚬🚬
💰ส่วนบอทบินกลุ่มดูข้างล่างนะครับ
💳💳💳💳💳💳💳💳
🐦🐦🐦🐦🐦🐦🐦
🍑เชลบอทฟรีเมียม ดูแลตลอดการใช้👑
🍑คำสั่งภาษาไทยใช้ง่าย🍏
🍈ราคา เฉพาะเชล 200บาทไทย🍄
🌵เพิ่ม Kicker 
1 kicker= 100บาทไทย รวมค่าโอน
2 kicker= 200บาทไทย รวมค่าโอน
3 kicker= 300บาทไทย รวมค่าโอน
5 kicker= 500บาทไทย รวมค่าโอน
10 kicker= 800บาทไทย รวมค่าโอน
เชลบอททีม(1เชล/10คิก)= 1000฿
#===================
🌚เชลล์บอท🌚บิน หรือลบสมาชิก
     🌛ความสามารถ🌜
ลบสมาชิกท้้งห้อง500คนลบภายใน10วิ
ลบบอทสิริได้ง่ายๆ
เชลล์บอทอินโด  
ราคาต่อการลบ  = 
🌑ลบ2ครั้ง = ราคา 200 บาทไทย
🌒ลบ4ครั้ง = ราคา 400 บาทไทย
🌓ลบ8ครั้ง = ราคา 800 บาทไทย 
🌕ลบ10ครั้ง = ราคา 900 บาทไทย
#===================
[👉จำหน่ายบอท แท.ค  ออ👈 ]
 💳💳💰ราคา 150 บาท💰ต่อ1ห้อง
❄แท.ค   คนท้้งกลุ่ม 
❄สามารถเช็คคนอ่านได้
❄และยังมีข้อความเวลาคนเข้าออก
👝สามารถสั่งว่าจะเอา
ข้อความเข้าออกแบบใหน
🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫
👉สนใจ สอบถามคลิกลิ้งทักมาครับ😙
👉พ่อค้าหล่อด้วยใจดี บริการเป็นกันเอง😘
📍📍📍📍📍📍📍📍📍📍📍📍📍
http://line.me/ti/p/~socool290
http://line.me/ti/p/~socool290
http://line.me/ti/p/~socool290

[By.มินทีมทดลองบอท]""")                        

                
#-----------------------------------------------
#                BOTRUN
#-----------------------------------------------
					
            elif msg.text == "ตั้งเวลา":
#              if msg.from_ in admin:
                cl.sendText(msg.to, "!โปรดรอ..กรุณาพิมพ์ [อ่าน]")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "อ่าน":
#              if msg.from_ in admin:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

                    cl.sendText(msg.to, "||===[SELFBOT MIN HACK BOT]===||\n\n||==== ༺•㏒ มิน ㏒•༻ ====||\n\n[รายการอ่านตอนนี้]\n%s\n\n[รายการอ่านทั้งหมด]\n%s\n\n[SELFBOT MIN HACK BOT]\n[เวลาที่ตั้งอ่านครั้งล่าสุด][%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
	          else:
	            cl.sendText(msg.to, "ไม่สามารถอ่านได้กรุณาตั้งค่าใหม่พิมพ์\n[อ่าน]\nตั้งค่าเสร็จสิ้นกรุณาพิมพ์\n[คนอ่าน]\nn[SELFBOT MIN BOT]\n[By.มิน ทีมทดลองบอท]")

#-----------------------------------------------
#                TAG ALL MEMBERS
#-----------------------------------------------
                  
            elif msg.text in ["Tag@@"]:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
					
#-----------------------------------------------
#                YOUTUBE
#-----------------------------------------------

                       
            elif "ยูทูป " in msg.text.lower():
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
                      

#-----------------------------------------------
#                BOT RESPONS
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
        if op.type == 15:
            if wait["bcommentOn"] == True:
                if op.param2 in Bots:
                    return
                G = cl.getGroup(op.param1)
                h = cl.getContact(op.param2)
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "ออกแล้วหรอคร๊าบ💖\nแล้วกลับใหใหม่น๊า💎")
                cl.sendImageWithUrl(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 17:
          if wait["acommentOn"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1," ห้อง💖" + str(ginfo.name) + "\n" + "💗ยินดีต้อนรับคร๊าบคุยกันตามสบายเลยเด้อ💗\n💖อย่าลืมปิดการแจ้งเตือนด้วยนะครับผม💖") 
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)  
            cl.sendImageWithUrl(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "20301852",
                                    "STKPKGID": "9395",
                                    "STKVER": "1" }                
            cl.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"
#----------------------------------------------- 
#------------------------------------------------------------------------------------





        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n|| " + Nama
                        wait2['ROM'][op.param1][op.param2] = "|| " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

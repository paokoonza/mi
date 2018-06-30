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
cl.login(token="Eu2f7N7nsBxSXqQEoJ6d.+CsUIhR+SBWx5bVi7Fjjxq.5lAP+uXDOy5D5Ur3HAx0pEcz55ntetdt/XJEr55rAUo=")
cl.loginResult()
ki=ki2=ki3=ki4=cl


print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
http://line.me/ti/p/~Gumin_789
"""

Thaihelp ="""
"""

helo=""

KAC=[cl]
mid = cl.getProfile().mid
Bots = [mid,"ufdc4ae887affb1bc17e41bc8edf2495d"]
bot1 = cl.getProfile().mid
admsa = "ufdc4ae887affb1bc17e41bc8edf2495d"
admin = "ufdc4ae887affb1bc17e41bc8edf2495d"

wait = {
    'contact':False,
    'autoJoin':False,
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
🍈ราคา เฉพาะเชล 300บาทไทย🍄
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
http://line.me/ti/p/~Gumin_789
http://line.me/ti/p/~Gumin_789
http://line.me/ti/p/~Gumin_789

[By.มินทีมทดลองบอท]
""",
    "comment1":"""
           〘•✥SELF BOT BY MIN✥•〙
                 〘•AUTO LIKE ON•〙
    

✄▒█▀▄▀█ ▀█▀ ▒█▄░▒█ 
✄▒█▒█▒█ ▒█░ ▒█▒█▒█ 
✄▒█░░▒█ ▄█▄ ▒█░░▀█

👿ทางเรามีบอทมาจำหน่าย
👿บอทระบบ PY3 
👿บอทมีหลายฟั่งชั่น 70 กว่าฟั่งชั่น
💀มีระบบ ตั้งข้อความต่างๆ
👿แถมระบบป้องกันที่ดีมาก
💪ระบบตรวจจับคำสั่งบิน และเตะคนนั้นทันที
👀ระบบมีการตรวจจับคำหยาบ
👽และฟั่นลูกเล่นอีกมากมาย
👄👄เช่น👄👄
-ดึงรูปต่างๆ
-ดึงรูปเรา
-ดึงข้อมูลคนอื่น
-เช็คข้อมูลในตัวเรา
-มีคำสั่งแท็คทั้งห้อง
-มีคำสั่ง  เตะ
-และอื่นๆอีกมากว่า60+ ครับ
 👻บอทราคากันเอง👻
☣สนใจบอทแบบไหน☣
☣ทักมาคุยได้ที่ลิ้งเลยนะคับ☣
http://line.me/ti/p/~Gumin_789

""",
    "commentOn":True,
    "likeOn":True,
	"bcommentOn":False,
    "acommentOn":False,
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

# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="Eu1BggkqllVJvaYbUR07.pD+Siy1/tUYJ7kFzCv+tXW.pl9Sx5C35NBkxvYRgk5ZGMqJeRe5ds5L0xbYqotrlh8=")
cl.loginResult()
print """
  ▄▄▄[BY MIN HACK BOT]
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█BOT MIN KICKALL
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
start_runtime = datetime.now()

print """
    ▄▄▄[BY MIN HACK BOT]
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█AUTO LIKE LINE ON
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
reload(sys)
sys.setdefaultencoding('utf-8')


helpmsg ="""     [BY.มินทีมทดลองบอท]
                【คำสั่งเซลล์บอท】

꧂Me = แสดงคอนแท็ค
꧂Arm on = เปิดระบบป้องกัน
꧂Arm off = ปิดระบบป้องกัน
꧂เปิดบล็อค = เปิดออโต้บล็อค
꧂ปิดบล็อค = ปิดออโต้บล็อค
꧂เปิดแอด = เปิดเพิ่มเพื่อนอัตโนมัติ
꧂ปิดแอด = ปิดเพิ่มเพื่อนอัตโนมัติ
꧂ชื่อกลุ่ม: = ตั้งชื่อกลุ่ม
꧂ปฏิทิน = ตรวจสอบวัน/เวลา
꧂Time/เวลา = ตรวจสอบวัน/เวลา
꧂รูป (ชื่อรูป) = ค้นหารูปภาพ
꧂ผส.กู= ผู้สร้างSelfbot
꧂เปิดลิงค์ = เปิดลิ้งกลุ่ม
꧂ปิดลิงค์ = ปิดลิ้งกลุ่ม
꧂แนะนำตัว = แนะนำตัวในกลุ่ม
꧂แทค = แท็คสมาชิกในห้อง
꧂Picturl @ = ดึงรูปเพื่อน
꧂Url = ลิ้งกลุ่ม
꧂รันของขวัญ = ส่งของขวัญรัวๆ
꧂ชื่อ: = ตั้งชื่อของเรา
꧂ตัส: = อัพสเตตัสของเรา
꧂ชื่อ =ตรวจสอบชื่อของเรา
꧂ตัส = ตรวจสอบสเตตัสของเรา
꧂รูปโปร = ดูรูปโปรไฟล์
꧂วีดีโอโปร = ดูวีดีโอโปรไฟล์เรา
꧂รูปปก = ดูรูปปกเรา
꧂ไอดี @ = ดึงMidเพื่อน
꧂คอมเม้น = ตรวจสอบคอมเม้น
꧂ตั้งคอมเม้น: = ตั้งค่า
꧂Tag1 = ตรวจสอบข้อความ
꧂Tag1 -Tag2; = ตั้งค่า
꧂respon1 on/off = เปิด/ปิดแท็ค
꧂ประกาศแชท: =ส่งหาเพื่อนทั้งหมด
꧂ประกาศกลุ่ม: =ส่งในกลุ่มทั้งหมด
꧂เปิดสแกน = เปิดดูคนแอบอ่าน
꧂ปิดสแกน = ปิดดูคนแอบอ่าน
꧂เชคบอท =ดูการตั้งค่า
꧂ทดสอบ @ =ลบแล้วดึงกลับ
꧂Sp = เช็คความเร็ว
꧂เพื่อน = รายชื่อเพื่อน
꧂ไวรัส/Clars = ส่งไวรัส
꧂พูด ข้อความ = สั่งสิริพูด
꧂#พูด ข้อความ = รันข้อความ
꧂say ข้อความ = รันข้อความ
꧂ขอเพลง/Music = ค้นหาเพลง
꧂รันแชท @ = รันแชทรัวๆ
꧂ออก:5 
꧂ออก:Off
꧂Micadd @
꧂Micdel @
꧂เปิดเข้า =เปิดเข้ากลุ่มออโต้
꧂ปิดเข้า =ปิดเข้ากลุ่มออโต้
꧂เปิดออก = เปิดออกแชทรวม
꧂ปิดออก = ปิดออกแชทรวม
꧂เปิดคท = เปิดอ่านคอนแท็ค
꧂ปิดคท = ปิดอ่านคอนแท็ค
꧂Fuck @ = สั่งลบบุคคล
꧂ดับไฟ = ส่งไวรัส
꧂Spam on/off = รันแชท
꧂set on/off = เปิด/ปิด ระบบคำสั่ง
꧂คำสั่ง2
꧂ออน
꧂แปลภาษา
🍃สนใจสติ้กเกอร์ ธีมไลน์ ห้องบอท
V10และเชลบอทต่างๆทักมาเลยจ้า🍃
💖สนใจบอท💖
💖ติดต่อพ่อค้าเลยจ้า💖
[By.มินทีมทดลองบอท]
 ☞ http://line.me/ti/p/~Gumin_789
"""

helpset =""" ┈━═✥อาร์มระยำ✥═━┈
                 [ คำสั่งSelf 2 ]
👉Gname: -ตั้งชื่อกลุ่ม
👉Kick: -สั่งเตะด้วยMid
👉Welcome on -เปิดข้อความต้อนรับ
👉Welcome off -ปิดข้อความต้อนรับ
👉หาแอพ -ค้นหาแอพ
👉เปิดแทคเตะ -เปิดลบเมื่อแท็ก
👉ปิดแทคเตะ -ปิดลบเมื่อแท็ก
👉ยกเชิญ -ยกเลิกการเชิญ
👉ดึงคท -คอนแท็กเพื่อน
👉@bye -สั่งตัวเองออกจากกลุ่ม
👉แบน @ -สั่งแบน
👉รันคทไวรัส -ส่งคอนแท็ก
👉ดำ -สั่งดำด้วยคอนแท็ก
👉ขาว -สั่งขาวด้วยคอนแท๊ก
👉ล้างดำ -ล้างดำทั้งหมด
👉กันเชิญ -เปิดห้ามเชิญ
👉ปิดกันเชิญ -เชิญสมาชิกได้
👉แอดมิน -ดูคนสร้างกลุ่ม
👉กันลิงค์ -ป้องกันลิ้งกลุ่ม
👉ปิดกันลิงค์ -ปิดป้องกัน
👉อัพข้อมูล -อัพโหลดข้อมูล
👉Ss -รันสติ้กเกอร์ในกลุ่ม
👉เฟส.บุค -ขอลิ้งเฟสบุ๊ค
👉เปิดแชร์ -เปิดลิ้งแชร์
👉ปิดแชร์ -ปิดลิ้งแชร์
👉ลบรัน -สั่งปฏิเสธกลุ่ม
👉แอดหมด -แอดเพื่อนทั้งหมด
👉บ๊าย.บาย -สั่งล้างกลุ่ม
👉ข้อมูลกลุ่ม -ดูข้อมูล
👉กันรัน -ปฏิเสธกลุ่มเชิญ
👉google -ค้นหาโดยกูเกิ้ล
👉ลบ.แชท -ลบข้อความทั้งหมด

💓จำหน่ายสติ้กเกอร์+ธีมไลน์💓
💓ห้องบอทป้องกันการลบ💓
💓และเชลบอทกันรัน💓
👉ทักมาเลยจ้า👈 🌿อาร์ม🌿
http://line.me/ti/p/~1993arm2536
"""




   


helpgroup =""" ┈━═✥อาร์มระยำ✥═━┈

╔══✥🌿คำสั่งภาษาไทย🌿✥══
╠❂͜͡☬➣〘แนะนำตัว〙
╠❂͜͡☬➣〘เปิดลิงค์〙
╠❂͜͡☬➣〘ปิดลิงค์〙
╠❂͜͡☬➣〘ลิงค์กลุ่ม〙
╠❂͜͡☬➣〘แอด〙
╠❂͜͡☬➣〘ข้อมูลกลุ่ม〙
╠❂͜͡☬➣〘ดึง:ผส〙
╠❂͜͡☬➣〘ยิง @〙
╠❂͜͡☬➣〘kickall〙
╠❂͜͡☬➣〘ทดสอบ @〙
╠❂͜͡☬➣〘เพื่อน〙
╠❂͜͡☬➣〘ล้างดำ〙
╠❂͜͡☬➣〘เปิดสแกน〙
╠❂͜͡☬➣〘ปิดสแกน〙
╠❂͜͡☬➣〘ชื่อกลุ่ม:〙
╠❂͜͡☬➣〘ประกาศกลุ่ม:〙
╠❂͜͡☬➣〘ประกาศฯแชท:〙
╠❂͜͡☬➣〘ลิสกลุ่ม〙
╠❂͜͡☬➣〘ขาว〙
╠❂͜͡☬➣〘ดำ〙
╠❂͜͡☬➣〘แบน @〙
╠❂͜͡☬➣〘ล้างแบน @〙
╠❂͜͡☬➣〘บัญชีดำ〙                                                                   
╠❂͜͡☬➣〘Contact ban〙
╠❂͜͡☬➣〘midban〙
╠❂͜͡☬➣〘ล้างดำ〙
╠❂͜͡☬➣〘ดับไฟ〙
╠❂͜͡☬➣〘invite〙
╠❂͜͡☬➣〘ดึง〙
╠❂͜͡☬➣〘รูปกลุ่ม〙
╠❂͜͡☬➣〘รูป (ชื่อรูป)〙
╠❂͜͡☬➣〘Red off/on〙
╠❂͜͡☬➣〘ออก:(จำนวน)〙
╠❂͜͡☬➣〘ออก:off〙
╠❂͜͡☬➣〘ขอเพลง(ชื่อเพลง)〙
╠❂͜͡☬➣〘Jam say:(text)〙
╠❂͜͡☬➣〘jam on/off〙
╠❂͜͡☬➣〘update〙
╠❂͜͡☬➣〘เปิดข้อความเข้าออก〙
╠❂͜͡☬➣〘ปิดข้อความเข้าออก〙
╚【✥༺✯ສั७நัஞနะধำ✯༻✥】╝
"""

helptranslate ="""ตั้งค่าข้อความ
꧂ Hhx1; ไส่ข้อความต้อนรับ

꧂ Hhx2; ไส่จ้อความคนออก

꧂ Hhx3; ไส่ข้อความคนตีกัน

꧂Tag1; ตั้งข้อความคนแทค

꧂ Tag2; ตั้งอีกครั้ง ห้ามเหมือน Tag1

ปล. สังเกตุตรง ; ให้เราเปลียนเป็นตัวนี้ : แทน
"""


KAC=[cl]
mid = cl.getProfile().mid
Bots =["ud62f108d4e8aca7b9f933d3463b42c63",mid]
admin=["ud62f108d4e8aca7b9f933d3463b42c63",mid]
Creator= "ud62f108d4e8aca7b9f933d3463b42c63"


wait = {
    "likeOn":True,
    "Bot":False,
    "alwayRead":False,
    "AutoKick":False,
    'detectMention':True,
    'detectMention2':False,
    'detectMention3':False,
    'kickMention':False,
    'Tagvirus':False, 
    'sticker':False,
    "steal":True,
    'likeOn':True,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'Contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":50},
    'AutoCancel':False,
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'autoBlock':False,
    'message':"""
           〘•✥SELF BOT BY MIN✥•〙
                 〘•AUTO LIKE ON•〙
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
    "lang":"JP",
    "comment":"""

           〘•✥SELF BOT BY MIN✥•〙
                 〘•AUTO LIKE ON•〙
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
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"〘•༺✯ສั७நัஞနะধำ✯༻•〙",
    "cNames":"〘•༺✯ສั७நัஞနะধำ✯༻•〙",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Backup":False,
    "protect":False,
    "ricoinvite":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Sambutan":False,
    "tag1":"\nแทกไม่พูด..เด่ะปั๊ดโบกก..😁😁",
    "tag2":"\nมีไรก็ส่วนตัวสิคับ",
    "copy":{},
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
    
    }
wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {   
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mybackup = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = cl.getProfile()
myProfile = cl.getProfile()
myProfile.displayName = contact.displayName
myProfile.statusMessage = contact.statusMessage
myProfile.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def sendImageWithUrl(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
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

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "http://dl.profile.line-cdn.net/"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "http://dl.profile.line-cdn.net/":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    day, hours = divmod(hours,24)
    return ' ⏰ %02d วัน \n⏰ %02d ชั่วโมง \n⏰ %02d นาที \n⏰ %02d วินาที ⏰\n' % (day, hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)

def sendImage(self, to_, path):
    M = Message(to=to_, text=None, contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M2 = self._client.sendMessage(0,M)
    M_id = M2.id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendImage2(self, to_, path):
    M = Message(to=to_,contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M_id = self._client.sendMessage(M).id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = cl.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "😂ต๊ะเอ๋.☠.แอบทำไมจ้ะ\n " + "☞ " + Name + " ☜" + "\nรู้นะว่าอ่านอยู่. . .\n  ออกมาเลยนะ   \nმๅန์ঝ➢టざ✤နะধำ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        cl.sendText(op.param1, "😂ต๊ะเอ๋.☠.แอบทำไมจ้ะ😂\n " + "☞ " + Name + " ☜" + "\nนี่ก็อีกคน. . .อ่านอย่างเดียวเลย\n  ออกมาซะเลย  \nทีมบอทระยำ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    cl.sendText(op.param1, "😂ต๊ะเอ๋.☠.แอบเฮดหยัง😂 \n" + "☞ " + Name + " ☜" + "\nแอบกันจังเลยนะ???\nคิดว่าเป็นนินจารึไง...??😆😆\n 🚌💨💨 รีบๆออกมาเลย🚌💨💨 \nმๅန์ঝ➢టざ✤နะধำ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               cl.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    cl.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        cl.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                cl.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
        if op.type == 25:
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
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited this nigga💋: \n➡" + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait["ricoinvite"] = False
                                          break
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
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
        if op.type == 25:
            msg = op.message
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
                cl.comment(url[25:58], url[66:], wait["comment"])
        if op.type == 26:
            msg = op.message
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
                cl.comment(url[25:58], url[66:], wait["comment"])

            elif msg.text in ["ควย"]:
                wait["ควย"] = True
                cl.sendText(msg.to,"😂มาใหม่ หรอครับ😂\n👣ส่งควย,หี...มาดูทีครับ👣")                              
            elif msg.text in ["คท","Me","มี",".me"]:
                cl.sendText(msg.to,"You...")
            elif msg.text in ["อย","อยู่ไหม.",".อยู่ไหม"]:
                cl.sendText(msg.to,"อยู่...")     
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))
                                
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['Tagvirus'] == True:
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "JANDA'"}
                                  cl.sendMessage(msg)
                                  break
            
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                if wait["detectMention"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\n" + str(wait["tag1"]) , cName + "\n" + str(wait["tag2"])]
                    balas1 = "เหงา💖ใช่ไหม??💖"
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in Bots:
                            cl.sendText(msg.to,ret_)
                            cl.sendText(msg.to,balas1)
                            cl.sendImageWithURL(msg.to,image)
                            msg.contentType = 7   
                            msg.text = None
                            msg.contentMetadata = {
                                                            "STKID": "11853372",
                                                            "STKPKGID": "6711",
                                                            "STKVER": "3" }
                            cl.sendMessage(msg) 
                            break
                            
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["แทคตำมอย!! มีไรคับ?",cName + " แทคอีกแระ?",cName + " แทคจังเลยนะ..เดะปั๊ดจับปี้ซะรุย", cName + " ว่าไงคับ?..มีอะไรรึ","แทคขนาดนี้เป็นเมียพี่เลยมั้ย😬😬 " + cName, "มีไรจ้ะตัวเอง?" + cName, "ถถถถถแทคอีกแระ...แทคบ่อยฟ้องแม่นะ 😆😆" + cName , "???...จิแทคเอาโล่รึไง คับ " + cName + "ว่า?ซำได๋ " , cName + " แทคไม่พูดระวังโดนดีดนะ😆😆"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)                           
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "108",
                                                       "STKPKGID": "1",
                                                       "STKVER": "100" }
                                  cl.sendMessage(msg)                              
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["ว่าไงคับน้องสาว? " + cName + "มีอะไรให้ผมรับใช้คับ😂😂",cName + " แทคทำไมมิทราบ? มีอิโรยก๊ะว่ามา",cName + " แทคบ่อยๆเดะจับทำเมียนะ -..-","หยุดแทคสักพัก" + cName + " แล้วมาพบรักที่หลังแชท😝😝","😎😎😎\nคับ มีไรคับ " + cName, "ยังไม่ว่าง เดี๋ยวมาตอบนะ " + cName, "ไม่อยู่ ไปทำธุระ " + cName + "มีไรทิ้งแชทไว้ที่แชท.สตนะ?", "อ่ะ เอาอีกแระ " + cName + "แทคตมอย??????????????????","ป๊าาาด " + cName + " คุณนายคับ จะแทคทำไมคับ!"]
                    balas1 = "Ini Foto Sii Jones Yang Suka Ngetag. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,balas1)
                                  cl.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "410",
                                                       "STKPKGID": "1",
                                                       "STKVER": "100" }
                                  cl.sendMessage(msg)                                
                                  break  
                                  
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             cl.sendText(msg.to, _name + " เชิญคนนี้เข้ากลุ่มแล้ว")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 cl.findAndAddContactsByMid(target)
                                 cl.inviteIntoGroup(msg.to,[target])
                                 cl.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      cl.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break

            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                cl.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break
                                     
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass
                                    
        if op.type == 25:
            msg = op.message
                                  
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                cl.sendText(msg.to,"เปิดระบบรับคำสั่ง")
                   
            if msg.text in ["Bot off"]:
                wait["Bot"] = True
                cl.sendText(msg.to,"ปิดระบบรับคำสั่ง")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
        if op.type in [26,25]:
            msg = op.message
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                cl.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass   
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["Contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["Contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'คำสั่ง':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpmsg)
                else:
                    cl.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpgroup)
                else:
                    cl.sendText(msg.to,helpgroup)
            elif msg.text.lower() == 'คำสั่ง2':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpset)
                else:
                    cl.sendText(msg.to,helpset)
            elif msg.text.lower() == 'sett':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helptranslate)
                else:
                    cl.sendText(msg.to,helptranslate)
            elif "ทีมงาน" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ub6067d954641f865558e8d612682f056"}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ub4ba2088d7a4316d80094ea2bc453486"}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ""}
                cl.sendMessage(msg) 
				
            elif "ผส.กู" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ucef844b5d95798345a4c93a1f5001dd7"}
                cl.sendMessage(msg)
				
            elif msg.text in ["อัฟข้อมูล","Upload"]:
                cl.sendText(msg.to, "กำลังดาวน์โหลด..กรุณารอสักครู่ ⌛⌛^^")
                cl.sendText(msg.to, "LOADING:▒...0%")
                cl.sendText(msg.to, "█▒... 10.0%")
                cl.sendText(msg.to, "██▒... 20.0%")
                cl.sendText(msg.to, "███▒... 30.0%")
                cl.sendText(msg.to, "████▒... 40.0%")
                cl.sendText(msg.to, "█████▒... 50.0%")
                cl.sendText(msg.to, "██████▒... 60.0%")
                cl.sendText(msg.to, "███████▒... 70.0%")
                cl.sendText(msg.to, "████████▒... 80.0%")
                cl.sendText(msg.to, "█████████▒... 90.0%")
                cl.sendText(msg.to, "██████████▒... 99.9%")
                cl.sendText(msg.to, "███████████▒... 100.0%")
                cl.sendText(msg.to, "DOWNLOAD..\n✥༺✯ສั७நัஞနะধำ✯༻✥\n COMPLETE..")
                cl.sendText(msg.to, "ดาวน์โหลดสำเร็จ..เรียบร้อย (*¯︶¯*)✔\nმๅန์ঝ➢టざ✤နะধำ")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "% sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
                
            elif msg.text == "Sp":
                    cl.sendText(msg.to,"ประมวลผลความเร็ว")
                    start = time.time()
                    for i in range(3000):
                        1+1
                    elsp = time.time() - start
                    cl.sendText(msg.to,"%s/ต่อวินาที" % (elsp))    
                
            elif msg.text.lower() == 'ไวรัส':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
				
            elif "เฟสบุค" in msg.text:
                    a = msg.text.replace("เฟสบุค","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    cl.sendText(msg.to, "https://www.facebook.com" + b)
                    cl.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")    

					
            elif msg.text in ["555"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }

                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Hhh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif "youname " in msg.text.lower():
                txt = msg.text.replace("youname ", "")
                cl.kedapkedip(msg.to,text)
                print "[Command] Kedapkedip"
				
            elif msg.text in ["คท","Me","me",".me"]:
                    cl.sendText(msg.to,"มีควยไร...")
            elif msg.text in ["อย","อยู่ไหม.",".อยู่ไหม"]:
                    cl.sendText(msg.to,"อยู่...")     
            elif msg.text in ["ป๊า"]:
                    cl.sendText(msg.to,"อย่าเรียกเยอะเดะโบ๊กเลย")
            elif msg.text in ["เตย"]:
                    cl.sendText(msg.to,"เตยไม่ว่างแอบม่อพี่บอสหลังไมค์ยุ...")     
            elif msg.text in ["บอส"]:
                    cl.sendText(msg.to,"พี่บอสไม่ว่างแก้บอท...")
            elif msg.text in ["พ่อ"]:
                    cl.sendText(msg.to,"ไม่ว่าง...\n เยสกะนกยุ บนหลังคา...")     
            elif msg.text in [".อยู่ไหม","อยู่ไม"]:
                    cl.sendText(msg.to,"ซี่...อยู่")   
            elif msg.text in ["Tumtest"]:
                    cl.sendText(msg.to,"SELF T&T HACK BOT") 						
                
#==============================================================================#
            elif msg.text in ["Ss"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }									 
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }									 
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }									 
                cl.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
  
#========================== FOR COMMAND BOT STARTING =============================#

            elif msg.text.lower() == 'เปิดคท':
                if wait["Contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        cl.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                else:
                    wait["Contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        cl.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
            elif msg.text.lower() == 'ปิดคท':
                if wait["Contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                    else:
                        cl.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
                else:
                    wait["Contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                    else:
                        cl.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
            elif msg.text.lower() == 'เปิดกัน':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protecion Already On")
                    else:
                        cl.sendText(msg.to,"Protecion Already On")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protecion Already On")
                    else:
                        cl.sendText(msg.to,"Protecion Already On")
            elif msg.text.lower() == 'กันลิงค์':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr already On")
                    else:
                        cl.sendText(msg.to,"Protection Qr already On")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr already On")
                    else:
                        cl.sendText(msg.to,"Protection Qr already On")
            elif msg.text.lower() == 'กันเชิญ':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite already On")
                    else:
                        cl.sendText(msg.to,"Protection Invite already On")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                    else:
                        cl.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
            elif msg.text.lower() == 'กันยก':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        cl.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        cl.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
            elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     cl.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        cl.sendText(msg.to,"✥༺✯ສั७நัஞနะধำ✯༻✥")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     cl.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        cl.sendText(msg.to,"Khusus red")
            elif msg.text.lower() == 'เปิดเข้า':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                    else:
                        cl.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                    else:
                        cl.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
            elif msg.text.lower() == 'ปิดเข้า':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    else:
                        cl.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    else:
                        cl.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
            elif msg.text.lower() == 'ปิดกัน':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection already Off")
                    else:
                        cl.sendText(msg.to,"Protection already Off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                    else:
                        cl.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
            elif msg.text.lower() == 'ปิดกันลิงค์':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr already off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr already Off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already Off")
            elif msg.text.lower() == 'ปิดกันเชิญ':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite already Off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already Off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite already Off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already Off")
            elif msg.text.lower() == 'ปิดกันยก':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        cl.sendText(msg.to,"Protection Cancel already Off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        cl.sendText(msg.to,"Protection Cancel already Off")
            elif "ออก:" in msg.text:
                try:
                    strnum = msg.text.replace("ออก:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ปิดใช้งานการปฏิเสธการเข้าร่วมกลุ่ม")
                        else:
                            cl.sendText(msg.to,"ปิดคำเชิญถูกปฏิเสธ โปรดระบุจำนวนที่ใช้ในการเปิดเมื่อคุณต้องการส่ง")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ตั้งค่าค้างเชิญไว้ที่" + strnum + "กลุ่ม" + "\nหากค้างเชิญเกินจะถูกปฏิเสธคำเชิญโดยอัตโนมัติทั้งหมด")
                        else:
                            cl.sendText(msg.to,strnum + "ปฏิเสธการสร้างคำเชิญโดยอัตโนมัติ")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar")
                    else:
                        cl.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'เปิดออก':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบออกแชทโดยอัตโนมัติ")
                    else:
                        cl.sendText(msg.to,"เปิดระบบออกแชทไว้อยู่แล้ว")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")  
            elif msg.text.lower() == 'ปิดออก':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดระบบออกแชทโดยอัตโนมัติ")
                    else:
                        cl.sendText(msg.to,"ปิดระบบออกแชทโดยอัตโนมัติไว้อยู่แล้ว")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'เปิดแชร์':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to on")
                    else:
                        cl.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to on")
                    else:
                        cl.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'ปิดแชร์':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to off")
                    else:
                        cl.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to off")
                    else:
                        cl.sendText(msg.to,"Share already off")
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                cl.sendText(msg.to,"Sticker ID Detect Already On.")
            elif msg.text in ["Allpro on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True 
                    wait["cancelprotect"] = True 
                    wait["AutoKick"] = True
                    wait["kickMention"] = True
                    wait["linkprotect"] = True
                    wait["autoBlock"] = True
                    wait["protect"] = True     
                    cl.sendText(msg.to,"เปิดระบบป้องกันทั้งหมดแล้ว")
		    print wait["AutoCancel"]
		    print wait["AutoKick"]
		    print wait["protect"]
		else:
		    cl.sendText(msg.to,"მๅန์ঝ➢టざ✤နะধำ")

            elif msg.text in ["Allpro off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False  
                    wait["cancelprotect"] = False
                    wait["AutoKick"] = False
                    wait["kickMention"] = False
                    wait["linkprotect"] = False
                    wait["autoBlock"] = False
                    wait["protect"] = False 
                    cl.sendText(msg.to,"ปิดระบบป้องกันทั้งหมดเรียบร้อย")
		    print wait["AutoCancel"]
		    print wait["AutoKick"]
		    print wait["protect"]
		else:
		    cl.sendText(msg.to,"მๅန์ঝ➢టざ✤နะধำ")

            elif msg.text in ["Set on"]:
		if msg.from_ in admin:
                    wait["Contact"] = True
                    wait["timeline"] = True
                    wait["Sambutan"] = True 
                    wait["alwayRead"] = True
                    wait["detectMention3"] = True
                    wait["likeOn"] = True
                    wait["contact"] = True
                    wait["commentOn"] = True
                    wait["Backup"] = True     
                    cl.sendText(msg.to,"เปิดระบบตั้งค่าข้อความทั้งหมด")
		    print wait["Contact"]
		    print wait["Sambutan"]
		    print wait["Backup"]
		else:
		    cl.sendText(msg.to,"┈━═✥อาร์มระยำ✥═━┈")

            elif msg.text in ["Set off"]:
		if msg.from_ in admin:
                    wait["Contact"] = False
                    wait["timeline"] = False
                    wait["Sambutan"] = False  
                    wait["alwayRead"] = False
                    wait["detectMention3"] = False
                    wait["likeOn"] = False
                    wait["contact"] = False
                    wait["commentOn"] = False
                    wait["Backup"] = False 
                    cl.sendText(msg.to,"ปิดระบบตั้งค่าข้อความทั้งหมดเรียบร้อย")
                    
		    print wait["Contact"]
		    print wait["Sambutan"]
		    print wait["Backup"]
		else:
		    cl.sendText(msg.to,"┈━═✥อาร์มระยำ✥═━┈")
    
            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"เปิดระบบอ่านคท. รับทราบ!!")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"ปิดระบบอ่านคท. เรียบร้อย")
#======================================================#
            elif msg.text in ["Arm on","All on"]:
                        cl.sendText(msg.to,"☜〘•༺✯ສั७நัஞနะধำ✯༻•〙☞ ")
                        cl.sendText(msg.to,"กำลังเปิดป้องกัน......\n┈━═✥อาร์มระยำ✥═━┈")
                        cl.sendText(msg.to,"Turn on all protection")
                        cl.sendText(msg.to,"เปิดกันลิงค์")
                        cl.sendText(msg.to,"เปิดกัน")
                        cl.sendText(msg.to,"เปิดแทคดับ")
                        cl.sendText(msg.to,"เปิดข้อความเข้าออก")
                        cl.sendText(msg.to,"เปิดแทคเจ็บ")
                        cl.sendText(msg.to,"เปิดกันเชิญ")
                        cl.sendText(msg.to,"เปิดกันยก")
                        cl.sendText(msg.to,"เปิดบล็อค")
                        cl.sendText(msg.to,"Autokick on")             
#======================================================#
            elif msg.text in ["Arm off","All off"]:
                        cl.sendText(msg.to,"☜〘•༺✯ສั७நัஞနะধำ✯༻•〙☞ ")
                        cl.sendText(msg.to,"Please wait......")
                        cl.sendText(msg.to,"Turn off all protection")
                        cl.sendText(msg.to,"ปิดกันลิงค์")
                        cl.sendText(msg.to,"ปิดกัน")
                        cl.sendText(msg.to,"ปิดแทคดับ")
                        cl.sendText(msg.to,"ปิดข้อความเข้าออก")
                        cl.sendText(msg.to,"ปิดแทคเตะ")
                        cl.sendText(msg.to,"ปิดกันเชิญ")
                        cl.sendText(msg.to,"ปิดกันยก")
                        cl.sendText(msg.to,"ปิดบล็อค")
                        cl.sendText(msg.to,"Autokick off")
#======================================================#
                
            elif msg.text.lower() == '.set':
                md = "╔═┈━[By.มินทีมทดลองบอท]━┈═╗ \n"            
                if wait["contact"] == True: md+="╠❂͜͡☬➣􏿿 Contact:on\n"
                else:md+="╠❂͜͡☬➣􏿿 Contact:off\n"
                if wait["autoJoin"] == True: md+="╠❂͜͡☬➣􏿿 Auto Join:on \n"
                else:md+="╠❂͜͡☬➣􏿿 Auto Join:off \n"
                if wait["autoCancel"] == True: md+="╠❂͜͡☬➣􏿿 Auto cancel:" + str(wait["autoCancel"]["members"]) +" \n"
                else:md+="╠❂͜͡☬➣􏿿 Group cancel:off\n"
                if wait["AutoCancel"] == True: md+="􀜁 auto cancel:on \n"
                else:md+="╠❂͜͡☬➣􏿿 auto cancel:off\n"
                if wait["leaveRoom"] == True: md+="╠❂͜͡☬➣􏿿 Auto leave:on \n"
                else:md+="╠❂͜͡☬➣􏿿 Auto leave:off \n"
                if wait["timeline"] == True: md+="╠❂͜͡☬➣􏿿 Share:on 􀜁􀄯\n"
                else:md+="╠❂͜͡☬➣􏿿 Share:off\n"
                if wait["autoAdd"] == True: md+="╠❂͜͡☬➣􏿿 Auto add:on  \n "
                else:md+="╠❂͜͡☬➣􏿿 Auto add:off \n"
                if wait["protect"] == True: md+="╠❂͜͡☬➣􏿿 Protect:on \n"
                else:md+="╠❂͜͡☬➣􏿿 Protect:off\n"
                if wait["linkprotect"] == True: md+="╠❂͜͡☬➣􏿿 Link Protect:on \n"
                else:md+="╠❂͜͡☬➣􏿿 Link Protect:off \n"
                if wait["inviteprotect"] == True: md+="╠❂͜͡☬➣􏿿 Invitation Protect:on\n"
                else:md+="╠❂͜͡☬➣􏿿 Invitation Protect:off \n"
                if wait["cancelprotect"] == True: md+="╠❂͜͡☬➣􏿿 Cancel Protect:off 􀜁􀄰 \n"
                else:md+="╠❂͜͡☬➣􏿿 Cancel Protect:off\n"
                if wait["commentOn"] == True: md+="╠❂͜͡☬➣􏿿 Auto komentar:on\n"
                else:md+="╠❂͜͡☬➣􏿿Auto komentar:off\n"
                if wait["sticker"] == True: md+="╠❂͜͡☬➣􏿿 Sticker:on\n"
                else:md+="╠❂͜͡☬➣􏿿Sticker:off\n"
                if wait["AutoKick"] == True: md+="╠❂͜͡☬➣􏿿 Auto kick:on \n"
                else:md+="╠❂͜͡☬➣􏿿Auto kick:off\n"
                if wait["Sambutan"] == True: md+="╠❂͜͡☬➣􏿿 sambutan:on \n "
                else:md+="╠❂͜͡☬➣􏿿 sambutan:off\n"
                if wait["Tagvirus"] == True: md+="╠❂͜͡☬➣􏿿 tagvirus:on \n"
                else:md+="╠❂͜͡☬➣􏿿 tagvirus:off\n"
                if wait["kickMention"] == True: md+="╠❂͜͡☬➣􏿿 KickMention:on \n"
                else:md+="╠❂͜͡☬➣􏿿 KickMention:off\n"
                if wait["autoBlock"] == True: md+="╠❂͜͡☬➣􏿿 AutoBlock:on \n"
                else:md+="╠❂͜͡☬➣􏿿 AutoBlock:off\n"
                if wait["detectMention"] == True: md+="╠❂͜͡☬➣􏿿 Respon1:on \n"
                else:md+="╠❂͜͡☬➣􏿿 Respon1:off \n"
                if wait["detectMention2"] == True: md+="╠❂͜͡☬➣􏿿 Respon2:on \n"
                else:md+="╠❂͜͡☬➣􏿿 Respon2:off \n"
                if wait["detectMention3"] == True: md+="╠❂͜͡☬➣􏿿 Respon3:on \n"
                else:md+="╠❂͜͡☬➣􏿿 Respon3:off \n╚═┈━═✥มิน✥═━┈═╝"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
				     
            elif "ส่งของขวัญ " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("ส่งของขวัญ ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + "􀐂􀇵present􏿿ตรวจดูของขวัญ􀐂􀇵present􏿿\n👉ได้ที่...แชทสต.นะครับ👈")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
            elif "ของขวัญ2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("ของขวัญ2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "ของขวัญ3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("ของขวัญ3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "ของขวัญ4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("ของขวัญ4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
            elif cms(msg.text,["Tumtest"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "SELF T&T HACK BOT\n〘༺✯ສั७நัஞနะধำ✯༻〙"}
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'เปิดแอด':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'ปิดแอด':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
            elif msg.text in ["Block on","B on","เปิดบล็อค"]:
                if wait["autoBlock"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✔👎〘•ระบบออโต้บล็อค\nเปิดใช้งานอยุ่แล้ว•〙👍")
                    else:
                        cl.sendText(msg.to,"✔👎Block set to on👍")
                else:
                    wait["autoBlock"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👎Ok Bosqu👎")
                    else:
                        cl.sendText(msg.to,"👎Sudah on Bosqu👎")

            elif msg.text in ["AutoBlock off","B off","ปิดบล็อค"]:
                if wait["autoBlock"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👎〘•ระบบออโต้บล็อค\nปิดใช้งานอยู่แล้ว•〙👎")
                    else:
                        cl.sendText(msg.to,"👎Block set to off👎")
                else:
                    wait["autoBlock"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👎Ok Bosqu👎")
                    else:
                        cl.sendText(msg.to,"👎Sudah off Bosqu👎")
            elif "ตั้งข้อความแอด:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                cl.sendText(msg.to,"เชิญทำการเปลี่ยนแปลงข้อความคนแอด")
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ข้อความเมื่อเพิ่มเพื่อนโดยอัตโนมัติตั้งไว้ดังนี้ \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"ปลี่ยนการตั้งค่า ข้อความคนแอด ของคุณแล้ว \n  ดังนี้\n" + wait["message"])
            elif "ตั้งคอมเม้น:" in msg.text:
                c = msg.text.replace("คอมเม้น:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เปลี่ยนการตั้งค่าคอมเม้นของคุณแล้ว ดังนี้")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"เปลี่ยนการตั้งค่าคอมเม้นของคุณแล้ว \n  ดังนี้\n" + c)
            elif msg.text in ["Com on","เปิดเม้น","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di")
                    else:
                        cl.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Actived")
                    else:
                        cl.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Come off","ปิดเม้น"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["คอมเม้น","Comment"]:
                cl.sendText(msg.to,"ข้อความแสดงความคิดเห็นอัตโนมัติถูกตั้งไว้ดังนี้:??\n\n" + str(wait["comment"]))
            elif msg.text in ["ข้อความแอด","message"]:
                cl.sendText(msg.to,"ข้อความตอบรับคนแอดถูกตั้งไว้ดังนี้:??\n\n" + str(wait["message"]))
            elif msg.text in ["ขาว"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"กรุณาส่ง คอนแทค บุคคลที่คุณต้องการเพิ่มในบัญขาว")
            elif msg.text in ["ดำ"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"กรุณาส่ง คอนแทค บุคคลที่คุณต้องการเพิ่มในบัญชีดำ")
            elif msg.text in ["บัญชีดำ"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"ไม่มีอะไรในบัญชีดำ")
                else:
                    cl.sendText(msg.to,"ต่อไปนี้เป็นรายชื่อที่อยู่ในบัญชีดำ")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"เปิดระบบเวลาไว้อยู่แล้วในขณะนี้")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เปิดระบบเวลาแล้ว")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"ปิดระบบเวลาไว้อยู่แล้วในขณะนี้")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"ปิดระบบเวลาแล้ว")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"หวัดดี")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["+cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Jam")

            elif 'ดึงรูป ' in msg.text:
                googl = msg.text.replace('ดึงรูป ',"")

                url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl

                raw_html =  (download_page(url))

                items = []

                items = items + (_images_get_all_items(raw_html))

                path = random.choice(items)

                try:

                    start = timeit.timeit()

                    cl.sendImageWithURL(msg.to,path)

                    cl.sendText(msg.to, "Google Image \nType: Search Image\nWaktu dicari: %s" % (start) +"\nTotal Image Links = "+str(len(items)))

                    print "[Notif] Search Image Google Sucess"

                except Exception as e:

                    cl.sendText(msg.to, str(e))
#========================== FOR COMMAND BOT FINISHED =============================#
            elif "#พูด " in msg.text:
                if msg.toType == 2:
                  bctxt = msg.text.replace("#พูด ", "")
                  t = cl.getAllContactIds()
                  t = 20
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1
            elif msg.text in ["เหงา","เงียบ"]:
                gs = cl.getGroup(msg.to)
                cl.sendText(msg.to,"😭😭ป่าช้าชัดๆ😭😭")
                msg.contentType = 7
                msg.contentMetadata={'STKID': '113',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)
                
            elif msg.text in ["บาย","ลาก่อน","ออกนะ"]:
                gs = cl.getGroup(msg.to)
                cl.sendText(msg.to,"😭😭แล้วเจอกันใหม่นะ😭😭")
                msg.contentType = 7
                msg.contentMetadata={'STKID': '42',
                                    'STKPKGID': '2',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)
            elif "Tum say " in msg.text:
                        bctxt = msg.text.replace("Tum say ","")
                        cl.sendText(msg.to,(bctxt))
            elif "siri-en " in msg.text.lower():
                    query = msg.text.lower().replace("siri-en ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
#==============================================
            elif "Hhx1:" in msg.text:
                c = msg.text.replace("Hhx1:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"❌〘•เกิดข้อผิดพลาด..!!•〙👎")
                else:
                    wait["acomment"] = c
                    cl.sendText(msg.to,"➣ 〘•ตั้งค่าข้อความต้อนรับ•〙👍\n" + c)
                    
            elif msg.text in ["HHX1","Hhx1","ข้อความต้อนรับ","ข้อความ1"]:
                cl.sendText(msg.to,"[เช็คข้อความต้อนรับของคุณ]\n\n" + str(wait["acomment"]))
                    
#==============================================
            elif msg.text in ["HHX2","Hhx2","ข้อความคนออกกลุ่ม","ข้อความ2"]:
                cl.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนออกจากกลุ่ม]\n\n" + str(wait["bcomment"]))
                
            elif "Hhx2:" in msg.text:
                c = msg.text.replace("Hhx2:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"❌〘•เกิดข้อผิดพลาด..!!•〙👎")
                else:
                    wait["bcomment"] = c
                    cl.sendText(msg.to,"➣ 〘•ตั้งค่าข้อความกล่าวถึงคนออกจากกลุ่ม•〙👍\n" + c)                
#==============================================
            elif msg.text in ["HHX3","Hhx3","ข้อความคนลบสมาชิก","ข้อความ3"]:
                cl.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนลบสมาชิก]\n\n" + str(wait["ccomment"]))
            elif "Hhx3:" in msg.text:
                c = msg.text.replace("Hhx3:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"❌〘•เกิดข้อผิดพลาด..!!•〙👎")
                else:
                    wait["ccomment"] = c
                    cl.sendText(msg.to,"➣〘• ตั้งค่าข้อความกล่าวถึงคนลบสมาชิก•〙👍\n" + c)

#==============================================
#======================================================#
            elif msg.text in ["Tag1","Tag1"]:
                cl.sendText(msg.to,"ข้อความแทคล่าสุดคือ\n\n" + str(wait["tag1"]))
            elif msg.text in ["Tag2","Tag2"]:
                cl.sendText(msg.to,"ข้อความแทคล่าสุดคือ\n\n" + str(wait["tag2"]))
            elif "Tag1: " in msg.text:
                    wait["tag1"] = msg.text.replace("Tag1: ","")
                    cl.sendText(msg.to,"ข้อความแทคล่าสุดคือ")
            elif "Tag2: " in msg.text:
                    wait["tag2"] = msg.text.replace("Tag2: ","")
                    cl.sendText(msg.to,"ข้อความแทคล่าสุดคือ")

#----------------------------------------------------------------------------
#==============================================
#========================================


            elif msg.text.lower() == 'ออน':  
                eltime = time.time() - mulai
                van = "〘•ระยะเวลาการทำงานของบอท•〙\n"+waktu(eltime)
                cl.sendText(msg.to,van)
	
#========================================
#==============================================

#==============================================



            elif "รันโลด" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"REDSAMURI")
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"REDSAMURI")
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"REDSAMURI")


            elif "รัน @" in msg.text:
                print "[Command]covergroup"
                _name = msg.text.replace("รัน @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                           thisgroup = cl.getGroups([msg.to])
                           Mids = [target for contact in thisgroup[0].members]
                           mi_d = Mids[:33]
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.sendText(msg.to,"เรียบร้อย")
                        except:
                            pass
                print "[Command]covergroup"

            elif "รันแชท @" in msg.text:
                _name = msg.text.replace("รันแชท @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"〘💀〘✯เริ่มระบบรันแชท✯〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")					   
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")					   
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙") 
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(g.mid,"〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙")
                       cl.sendText(msg.to, "〘•༺✯รันแชทเสดสิ้น✯༻•〙")
                       print " Spammed "
            elif 'รัน:' in msg.text.lower():
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)
                    cl.inviteIntoGroup(msg.to, [key])
                    contact = cl.getContact(key)
                    cl.sendText(msg,to,"┌∩┐(◣_◢)┌∩┐")
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"👉Done")
    
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])

            elif "คท" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                cl.sendMessage(msg)

            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            
            elif "Spamtag " in msg.text:
                _name = msg.text.replace("Spamtag ","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                        xname = g.displayName
                        xlen = str(len(xname)+10)
                        msg.contentType = 0   
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")       
            elif msg.text in ["ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"👉ลบห้องเชิญเรียบร้อยแล้ว👈")
            elif msg.text in ["Delete chat","ล้างแชท"]:
                cl.removeAllMessages(op.param2)
                cl.sendText(msg.to,"👉สำเร็จ..Delete Chat👈")
                cl.sendText(msg.to,"Success...")
            elif "ลบแชท" in msg.text.lower():
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"👉Done👈")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")      
#==============================================================================#
            elif msg.text in ["เชิญ"]:
                wait["ricoinvite"] = True
                cl.sendText(msg.to,"👉ส่งคอนแท็กเลยครับ👈")
            
            elif msg.text in ["อ่านคท"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"👉จัดมาโล๊ด👈")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["เปิดไลค์","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👉เปิดไลค์อัตโนมัติ👈")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👉เปิดไลค๋อัตโนมัติ👈")
                        
            elif msg.text in ["ปิดไลค์","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👉ตามนั้น👈")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👉ตามนั้น👈")
                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"👉เปิดโหมดโต้ตอบ👈")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"👉ปิดโหมดโต้ตอบแล้ว👈")
                
            elif msg.text in ["Read on","Read:on"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"👉Auto read On👈")
                
            elif msg.text in ["Read off","Read:off"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"👉Auto read Off👈")
                
            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    wait["Tagvirus"] = False
                    cl.sendText(msg.to,"Auto Respon1 Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus red")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon1 Sudah Off")
		else:
		    cl.sendText(msg.to,"Khusus red")	
		    
		    
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    wait["Tagvirus"] = False
                    cl.sendText(msg.to,"Auto Respon2 Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus Red")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    cl.sendText(msg.to,"Auto Respon2 Sudah Off")
		else:
		    cl.sendText(msg.to,"Khusus red")	
		    

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    wait["Tagvirus"] = False
                    cl.sendText(msg.to,"Auto Respon3 Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus red")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    cl.sendText(msg.to,"Auto Respon3 Sudah Off")
		else:
		    cl.sendText(msg.to,"Khusus red")	
		    
 
            elif msg.text in ["เปิดแทคเตะ"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True
                    wait["Tagvirus"] = False  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus red")

            elif msg.text in ["ปิดแทคเตะ"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    cl.sendText(msg.to,"Khusus red")			  
		    
            elif msg.text in ["เปิดแทคดับ"]:
		if msg.from_ in admin:
                    wait["Tagvirus"] = True
                    wait["kickMention"] = False  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    cl.sendText(msg.to,"Auto Respon Tagvirus Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus red")

            elif msg.text in ["ปิดแทคดับ"]:
		if msg.from_ in admin:
                    wait["Tagvirus"] = False                    
                    cl.sendText(msg.to,"Auto Respon Tagvirus Sudah Off")
            elif "เวลา" in msg.text:
              if msg.toType == 2:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif "บ๊ายบาย" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("บ๊ายบาย","")
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"เตรียมตัวให้พร้อม\nลาก่อนนะทุกคน\n👉〘ทีมบอทระยำ〙👈")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"เร่งสปีดเรียบร้อย")
                        cl.sendText(msg.to,"เพิ่มความเร็วเต็มพิกัด")
                    else:
                        for target in targets:
                          if not target in admin:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg,to,"บอกแล้วอย่ามาทะลึ่งกะพี่")
                                cl.sendText(msg,to,"ลองของมาก็จัดของไป")
                                cl.sendText(msg,to,"💀〘™のန❂ບମနัՁ✳နะধำ®〙💀\nFuke...you..┌∩┐(◣_◢)┌∩┐")
            elif ("Fuck " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
            elif ("ทดสอบ " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            
            elif msg.text in ["Cancel","cancel","ยก","ยกเชิญ"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ไม่มีคำเชิญ👈")
                        else:
                            cl.sendText(msg.to,"ไม่มีสมาชิกค้างเชิญ👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เรียบร้อย👈")
                    else:
                        cl.sendText(msg.to,"ไม่มีคำเชิญแล้ว")
            elif msg.text.lower() == 'ล้างเชิญ':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ไม่มีคำเชิญ👈")#FF3E00
                        else:
                            cl.sendText(msg.to,"ไม่มีสมาชิกค้างเชิญ👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เรียบร้อย👈")
                    else:
                        cl.sendText(msg.to,"ยกแล้วดึงใหม่หมดแล้ว")
            
            elif msg.text.lower() == 'เปิดลิงค์':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'ปิดลิงค์':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","ขอลิงค์"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"╔═══════〚•URL~GROUP~BY•〛═══════╗\n   ┅═✥हई༺✯ສั७நัஞနะধำ✯༻ईह✥═┅\n\n                  ☞ line.me/R/ti/g/" + gurl +"\n\n╚═══════ทีมบอทระยำ═══════╝")
                   
            elif "แอดมิน" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"คนนี้แหละที่เป็นคนสร้างกลุ่มนี้ \n┈━═✥ทีมบอทระยำ✥═━┈")
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"คนนี้แหละที่เป็นคนสร้างกลุ่มนี้\n💀〘™のန❂ບମနัՁ✳နะধำ®〙💀")
            
            elif msg.text.lower() == 'ดึง:ผส':
                if msg.toType == 2:
                       ginfo = cl.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           cl.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           cl.inviteIntoGroup(msg.to,[gcmid])
                           cl.sendText(msg.to,"ดึงคนสร้างกลุ่มนี้แล้วคับ (´∀｀)♡")
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    cl.updateGroup(X)
            
            elif msg.text.lower() == 'ข้อมูลกลุ่ม':        
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[ชื่อกลุ่ม : ]\n" + group.name + "\n\n[ไอดี กลุ่ม : ]\n" + group.id + "\n\n[ผู้สร้างกลุ่ม :]\n" + gCreator + "\n\n[รูปภาพกลุ่ม : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nลิงค์กลุ่ม : เปิดอยู่"
                    else: md += "\n\nลิงค์กลุ่ม : ปิดอยู่"
                    if group.invitee is None: md += "\nจำนวนสมาชิกในกลุ่ม : " + str(len(group.members)) + " คน" + "\nกำลังเชิญสมาชิกจำนวน : 0 คน"
                    else: md += "\nจำนวนสมาชิกในกลุ่ม : " + str(len(group.members)) + " คน" + "\nกำลังเชิญสมาชิกจำนวน : " + str(len(group.invitee)) + " คน"
                    cl.sendText(msg.to,md)
            
            elif msg.text.lower() == 'ไอดีกลุ่ม':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
#==============================================================================#
            elif msg.text in ["ลิสกลุ่ม"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (cl.getGroup(i).name +" ? ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == 'กันรัน':
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"คำเชิญเข้ากลุ่มจะถูกปฏิเสธคำเชิญทั้งหมด")
                else:
                    cl.sendText(msg.to,"เปิดปฏิเสธคำเชิญทั้งหมดอยู่แล้ว")
                         
            elif "แอดหมด" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.findAndAddContactsByMids(mi_d)
                cl.sendText(msg.to,"จัดการเพื่อเพิ่มทั้งหมด")
                    
            elif "@bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
								
#==============================================================================#
            elif "แทค" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "จำนวนทั้งหมดที่แทค:\n" + str(jml) +  " คน"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)

            elif msg.text in ["M on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดข้อความทักทายเมื่อมีคนเข้าคนออกอยู่แล้วヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"😊😊เปิดข้อความทักทายเมื่อมีคนเข้าคนออกแล้วจร้า😊😊")

            elif msg.text in ["M off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดข้อความทักทายเมื่อมีคนเข้าคนออกอยู่แล้ว(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"😊ปิดข้อความทักทายเมื่อมีคนเข้าคนออกแล้ว😊")            
            
            elif "เปิดสแกน" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"เปิดระบบสแกนคนอ่านอัตโนมัติ")
                
            elif "ปิดสแกน" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "ปิดระบบสแกนคนอ่านอัตโนมัติแล้ว")
                else:
                    cl.sendText(msg.to, "โปรดใช้คำสั่งเปิดแสกนก่อนจะปิด")
                    
            elif "ตั้งค่าสมาชิก: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("ตั้งค่าสมาชิก: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "จำนวนสมาชิกต่ำสุดในการเข้าร่วม : "+jml)

            elif "ประกาศกลุ่ม: " in msg.text:
                bc = msg.text.replace("ประกาศกลุ่ม: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.sendText(i, bc)
                    
            elif "ประกาศแชท: " in msg.text:
                bc = msg.text.replace("ประกาศแชท: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendText(i, bc)         
                        
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Tummic " in msg.text:
                cmd = msg.text.replace("Tummic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"โปรแกรมเลียนแบบคำพูดถูกเปิดใช้งานอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดใช้งานโปรแกรมเลียนแบบคำพูด")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"โปรแกรมเลียนแบบคำพูดถูกปิดใช้งานอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดใช้งานโปรแกรมเลียนแบบคำพูด")
            elif "ทามไลน:" in msg.text:
              if msg.toType == 2:
                tl_text = msg.text.replace("ทามไลน:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==============================================================================#
            elif msg.text.lower() == 'ไอดี':
                cl.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "ชื่อ: " in msg.text:
                string = msg.text.replace("ชื่อ: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เปลี่ยนชื่อของคุณแล้ว ดังนี้ " + string + "")
            elif "ตัส: " in msg.text:
                string = msg.text.replace("ตัส: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เปลี่ยนตัสของคุณแล้ว ดังนี้ " + string)
            elif msg.text in ["ชื่อ"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["ตัส"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["รูปโปร"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["วีดีโอโปร"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["ลิงค์รูปโปร"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["รูปปก"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif "ไอดี @" in msg.text:
                _name = msg.text.replace("ไอดี @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "สอดแนม " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
                    cl.sendImageWithURL(msg.to,path)
            elif "ดึงตัส " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "ดึงชื่อ " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "ชุดใหญ่ " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "😂ไฟกระพริบ ยิกๆๆๆ😂\n\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "ดึงคท " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "วีดีโอโปรไฟล @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("วีดีโอโปรไฟล @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                            cl.sendImageWithURL(msg.to,path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["https://github.com/Redsamuri/samuri/blob/master/B612_20170830_112729.jpg"]
                                pilih = random.choice(link)
                                cl.sendImageWithURL(msg.to,pilih)
            elif "ดึงปก @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("ดึงปก @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "ลิงค์ปก @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("ลิงค์ปก @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "รูปกลุ่ม" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "ลิงค์รูปกลุ่ม" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in mid:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.CloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in mid:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "ไม่สำเร็จ")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "ก็อพปี้เรียบร้อย")
                                except Exception as e:
                                    print e
                                    
            elif "Clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = cl.getContact(target)
                        X = contact.displayName
                        profile = cl.getProfile()
                        profile.displayName = X
                        cl.updateProfile(profile)
                        cl.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = cl.getProfile()
                        lol.statusMessage = Y
                        cl.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        hun = cl.getProfile()
                        hun.pictureStatus = P
                        cl.updateProfile(hun)
                    except Exception as e:
                        cl.sendText(msg.to, "Failed!")
                        print e

            elif msg.text in ["คืนร่าง"]:
                try:
                    cl.updateProfile.pictureStatus(mybackup.pictureStatus)
                    cl.updateProfile.statusMessage(mybackup.statusMessage)
                    cl.updateProfile.displayName(mybackup.displayName)
                    cl.sendText(msg.to, "กลับร่างเดิมแล้ว")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#==============================================================================#
            elif "Fancytext: " in msg.text:
                txt = msg.text.replace("Fancytext: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
                    
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Th-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Th-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Th-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Th-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Th-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Th@en" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Th@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO ENGLISH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "En@th" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("En@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM EN🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Th@jp" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Th@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO JP🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Jp@th" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Jp@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM JP🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM ID🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO ID🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Th@ar" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Th@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO AR🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Ar@th" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Ar@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM AR🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Th@ko" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Th@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO KO🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Ko@th" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Ko@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM KO🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
                
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"🙏สวัสดีคับคนมาใหม่ 🙏" + "\n🌾ยินดีต้อนรับเข้าสู่กลุ่ม 🌾" + "\n👉" + str(ginfo.name) +"👈")
                jawaban1 = ("สวัสดี" + "จาก ครอบครัวระยำคลับ\nยินดีที่ได้รู้จักกับทุกคนค่ะ")
                cl.sendText(msg.to," ผู้สร้างกลุ่มนี้คือ 👉"  + ginfo.creator.displayName + "\nมาใหม่แก้ผ้าด้วยนะ 😆😆" + "\n\nBy: •─✥༺✯ສั७நัஞနะধำ✯༻✥─•")
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
                
            elif msg.text.lower() == 'แนะนำตัว':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"🙏สวัสดีคับทุกคน 🙏" + "\n🌾ยินดีที่ได้เข้ามาในกลุ่ม 🌾" + "\n👉" + str(ginfo.name) +"👈")
                jawaban1 = ("สวัสดี" + "จาก ครอบครัวระยำคลับ\nยินดีที่ได้รู้จักกับทุกคนค่ะ")
                cl.sendText(msg.to," สวัสดีแอดด้วยนะค่ะ"  + "👉" + ginfo.creator.displayName + "👈" + "\nมาใหม่ค่ะ 😆😆" + "\n\nBy: •─✥༺✯ສั७நัஞနะধำ✯༻✥─•")
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
				
            elif "พูด " in msg.text:
                say = msg.text.replace("พูด ","")
                lang = 'th'
                tts = gTTS(text=say, lang=lang)
                tts.save("say.mp3")
                cl.sendAudio(msg.to,"say.mp3")				
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-Th " in msg.text:
                say = msg.text.replace("Say-Th ","")
                lang = 'Th'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif 'Music ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")                 
            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
            
            elif "รูป " in msg.text:
                search = msg.text.replace("รูป ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                cl.sendImageWithURL(msg.to,path)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif "เชคig " in msg.text:
                    try:
                        instagram = msg.text.replace("เชคig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "ลิงค์: " + "https://www.instagram.com/" + instagram
                        text = "ชื่อ : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif msg.text.lower() == 'ปฏิทิน':
	    	    wait2['setTime'][msg.to] = datetime.today().strftime('วันเดือนปี : %d-%m-%Y \nDay : %A \nเวลา : %H:%M:%S')
	            cl.sendText(msg.to, "🍁ปฏิทิน👉〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙🍁\n\n" + (wait2['setTime'][msg.to]))
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙\n\n ===SERVER INFO NetStat===")
            elif msg.text.lower() == 'เชคsystem':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙\n\n ===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'เชคkernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'เชคcpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n〘💀〘™のန❂ບମနัՁ✳နะধำ®〙💀〙\n\n ===SERVER INFO CPU===")
            
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = red.getGroup(msg.to)
                        red.sendText(msg.to,"ลาก่อย~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            red.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        red.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        red.sendText(msg.to,str(e))
			    red.inviteIntoGroup(msg.to, targets)       
            elif "Restart" in msg.text:
                    print "[Command]Restart"
                    try:
                        cl.sendText(msg.to,"Restarting...\n™のန❂ບମနัՁ✳နะধำ®")
                        cl.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif "Turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "ระยะเวลาการทำงานของบอท : "+waktu(eltime)
                cl.sendText(msg.to,van)

        
#================================  STARTED ==============================================#
            elif "google " in msg.text:
                    a = msg.text.replace("google ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"โปรดรอสักครู่...")
                    cl.sendText(msg.to, "https://www.google.com/" + b)
                    cl.sendText(msg.to,"Ketemu om ^")

            elif cms(msg.text,["ผู้สร้าง","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ucef844b5d95798345a4c93a1f5001dd7"}
                cl.sendMessage(msg)

            elif "รูปเพื่อน: " in msg.text:
              if msg.from_ in admin:
                suf = msg.text.replace('รูปเพื่อน: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == suf:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)

            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                cl.sendMessage(msg)
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).id
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["เพื่อน"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="═════════ʆίςϯ ƒɾίεηδʍίδ═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════ʆίςϯ ƒɾίεηδʍίδ═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["ลิสกลุ่ม"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "ชื่อกลุ่ม" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "ไอดีกลุ่ม" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                saya = msg.text.replace('Grupinfo: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"



            elif "รันคทไวรัส @" in msg.text:
                _name = msg.text.replace("รันคทไวรัส @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': "u46a050ebcc66a90b47fae6256547cc53',"}
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"

            elif "หาแอพ " in msg.text.lower():
                    tob = msg.text.lower().replace("หาแอพ ","")
                    cl.sendText(msg.to,"กำลังค้นหาชื่อแอพ...")
                    cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    cl.sendText(msg.to,"☝กดลิงค์เข้าไปโหลดได้เลยนะ ^ - ^")
                    
            elif 'wikipedia ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wikipedia ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    cl.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Teks nya kepanjangan! ketik link dibawah aja\n"
                            pesan+=wikipedia.page(wiki).url
                            cl.sendText(msg.to, pesan)
                        except Exception as e:
                            cl.sendText(msg.to, str(e))    
                            
            elif "say " in msg.text.lower():
                say = msg.text.lower().replace("say ","")
                lang = 'th'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif msg.text in ["ส่งของขวัญ"]:
                wait["gift"] = True
                cl.sendText(msg.to,"ส่งคทมาเลยคับ") 
                
            elif msg.text in ["ก๊อปคท"]:
                wait["copy"] = True
                cl.sendText(msg.to,"ส่งคทมาเลยคับ") 


                                              								
            elif msg.text in ["รันของขวัญ"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)   
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)    
                				
                
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

            elif msg.text in ["Gcreator:kick"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
    
                   
            elif "Getcover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getcover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
                
            elif "idline: " in msg.text:
                msgg = msg.text.replace('idline: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)
                    
            elif msg.text in ["Restart"]:
                cl.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"   
                
            elif "image " in msg.text:
                search = msg.text.replace("image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif 'instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "**INSTAGRAM INFO USER**\n"
                    details = "\n**INSTAGRAM INFO USER**"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))    
                	
            elif msg.text in ["ดับไฟ"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u46a050ebcc66a90b47fae6256547cc53',"}
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
#================================= FINISHED =============================================#
            
            elif "แบน @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("แบน @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " ไม่พบ")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                cl.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "ล้างแบน @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("ล้างแบน @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " ไม่พบ")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                cl.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                cl.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "แบน:" in msg.text:                  
                       nk0 = msg.text.replace("แบน:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "ล้างแบน:" in msg.text:                  
                       nk0 = msg.text.replace("ล้างแบน:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    cl.sendText(msg.to,_name + " Not In Blacklist")
            elif msg.text in ["ล้างดำ"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"ล้างดำในรายการที่ถูกแบนเรียบร้อย")
            elif msg.text in ["Ban:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="*Blacklist*"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n*Blacklist*\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "══════════List Blacklist═════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass       
                            
        if op.type == 26:
            msg = op.message

            if msg.contentType == 16:
                url = msg.contentMetadata['postEndUrl']
                cl.like(url[25:58], url[66:], likeType=1001)
                cl.comment(url[25:58], url[66:], wait["comment"])
                print ("AUTO LIKE SELFBOT")
                print ("Auto Like  BY ☞ [BYมินทีมทดลองบอท]")
#==============================================#
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            G = cl.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[cl]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.1)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       cl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            cl.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    cl.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.kickoutFromGroup(op.param1,[op.param3])
                    cl.updateGroup(G)
        # ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1," ห้อง💖" + str(ginfo.name) + "\n" + str(wait["acomment"])) 
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)  
            cl.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "140",
                                     "STKPKGID": "2",
                                     "STKVER": "100" }                
            cl.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"
            
        if op.type == 19:
          if wait["Sambutan"] == True:
            if op.param2 in Bots:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + str(wait["ccomment"]))
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)  
            cl.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "518",
                                     "STKPKGID": "2",
                                     "STKVER": "100" }                
            cl.sendMessage(d)
            print "MEMBER KICK OUT FORM GROUP"
            
        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1, + str(wait["bcomment"]))
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)  
            cl.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "428",
                                    "STKPKGID": "1",
                                    "STKVER": "100" }                
            cl.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
#------------------------------------------------------------------------------#
  
        if op.type == 59:
            print op
            
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,200):
      hasil = cl.activity(limit=200)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          print "Like"
        except:
          pass
      else:
          print "Already Liked On"
time.sleep(0.60)

def likeme():
    for zx in range(0,200):
        hasil = cl.activity(limit=200)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like On"


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 50)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

#--------------------------------------------------------------------------#

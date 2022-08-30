import pyrogram 
from pyrogram import Client,filters,idle
from pyrogram.handlers import MessageHandler
import datetime, time, os,base64, traceback
import asyncio,random
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from databasefile import laporan,kgb,mialc,rangkumanch,chnokos,iklanch,chwajib1,grwajib1,urutan,pengirim,penerima
        


laporan=int(laporan)
kgb=int(kgb)
mialc=int(mialc)
rangkumanch=int(rangkumanch)
chnokos=int(chnokos)
iklanch=int(iklanch)
chwajib1=int(chwajib1)
grwajib1=int(grwajib1)

sipengirim=[]
for p in pengirim.split():
        try:sipengirim.append(p)
        except:pass
sipenerimakiriman=[]
for p in penerima:
        try:sipenerimakiriman.append(p)
        except:pass
waktujalan=0

namabotyangada=[]
namabot=""
# ------

linkchwajib1=""
linkchnokos=""

membernokos=[]
memberch1=[]

nama=""
namabot1=""
daftarpeserta1=[]
halamanpeserta1=[]
for i in urutan.split():
    halamanpeserta1.append(int(i))

tangkapkiriman=[]

async def decode(base64_string):
    base64_string = base64_string.strip("=")
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes)
    string = string_bytes.decode("ascii")
    return string

async def encode2(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def bongkar2(enco):
    deco=await decode(enco)
    kok=1
    if "bongkarcuy-9" in deco:
        deco=deco.replace("rcuy-9","r-")
        kok=2
    elif "karya-8" in deco: 
        deco=deco.replace("karya-8","kar-")
        kok=0   
    deco1=deco.split("-")[1]    
    a=int(str(deco1)[:-1])  
    b=int(str(deco1)[-1])
    d=0
    for e in str(a):d+=int(e)
    while d>9:
        d=int(str(d)[0])+int(str(d)[1])
    if d!=b:return("X") 
    f=int(str(a)[0])
    g=int(str(a)[1:])
    if g%f!=0:return("XX")
    h=g//f  
    j=(h+321)//123
    j1=j
    j2=j1
    if len(deco.split("-"))==3:
        deco2=deco.split("-")[2]    
        a=int(str(deco2)[:-1])      
        b=int(str(deco2)[-1])
        d=0
        for e in str(a):d+=int(e)
        while d>9: d=int(str(d)[0])+int(str(d)[1])
        if d!=b:return("XXX")
        f=int(str(a)[0])
        g=int(str(a)[1:])
        if g%f!=0:return("XXXX")
        h=g//f  
        j=(h+123)//321
        j2=j                                                               #if "ciyehmaubongkar-" in deco:
    return(j1,j2,kok)


Client1=Client

@Client1.on_message(filters.private)
async def tes1(c,p):
    #print("yuk")
    global nama,namabot1,namabotyangada,linkchnokos,linkchwajib1,daftarpeserta1,halamanpeserta1,sipengirim,tangkapkiriman,sipenerimakiriman
    if namabot1=="":
        nama=await c.get_me()
        namabot1="**Bot : "+nama.first_name+"** @"+nama.username
        if namabot1 not in namabotyangada:namabotyangada.append(namabot1)
        for i in  (halamanpeserta1):
            #await asyncio.sleep(3)
            q=await c.get_messages(iklanch,i)
            for qq in q.text.split():
                try:qw=int(qq)
                except:continue
                if int(qq)<1000:continue
                if qq not in daftarpeserta1:daftarpeserta1.append(int(qq))
            if len(q.text)<3900:break

    if (p.chat.id) not in daftarpeserta1:
        daftarpeserta1.append(p.chat.id)
        kirim=0
        teks=""
        for hp in halamanpeserta1:
            t=await c.get_messages(iklanch,hp)
            if len(t.text)<4000:
                await c.edit_message_text(iklanch,hp,t.text+"\n"+str(p.chat.id))
                break
    
    try:
        if p.text=="/sipengirim":
            await p.reply("Anda pengirim")
            sipengirim.append(p.chat.id)
            return
        if p.text=="/waktu":
                skg=(time.time()-waktujalan)
                await p.reply(str(round(skg//3600,2))+" Jam, "+str((skg%3600)//60)+" Menit, "+str(round((skg%3600)%60,0)))
                return
        if p.text=="/hub":
            teks=namabot1+"\nBot ini dibuat khusus untuk kalian\n\nDibuat dengan ♥️ \n\nSilahkan hubungi pengembang melalui pemilik bot ini\n\n\nOwner : ~~@nokos_easy~~"
            await p.reply(teks)
            return
        elif p.text=="/update" or p.text=="/vip" or p.text=="/vvip":
            teks="Anda belum aktif menjadi member VVIP. \nSilahkan hubungi Owner : ~~@nokos_easy~~"
            await p.reply(teks)
            return
        """
        elif "/boardsemua " in p.text:
            ada=len(daftarpeserta1)
            kir=0
            ggl=0
            await p.forward(iklanch)
            await asyncio.sleep(0.2)
            for m in daftarpeserta1:
                try:
                    await c.send_message(m,p.text[12:]);kir+=1
                except:
                    ggl+=1
                await asyncio.sleep(0.2)
            await p.reply("Broad cast "+str(ada)+", kirim "+str(kir)+", gagal "+str(ggl))
            print("Broad cast "+str(ada)+", kirim "+str(kir)+", gagal "+str(ggl))
        """
        elif p.text=="/diboard":
            print("DIBROAD")
            ada=len(daftarpeserta1)
            kir=0
            ggl=0
            await p.reply_to_message.copy(iklanch);kir+=1
            await asyncio.sleep(0.2)
            for m in daftarpeserta1:
                try:
                    await p.reply_to_message.copy(m);kir+=1
                except:
                    ggl+=1
                await asyncio.sleep(0.2)
            await p.reply("Broad cast "+str(ada)+", kirim "+str(kir)+", gagal "+str(ggl))

        elif p.text=="/start":
            teks=namabot1+"\nBot ini dibuat khusus untuk kalian\n\nOwner    ~~@nokos_easy~~\n\nJoin untuk update konten :"
            if linkchnokos=="":
                chanelnokos=await c.get_chat(chnokos)
                linkchnokos=chanelnokos.invite_link
            if linkchwajib1=="":
                chanelnokos=await c.get_chat(chwajib1)
                linkchwajib1=chanelnokos.invite_link
            teks+="\n- [Join Channel 1]("+linkchnokos+")"
            teks+="\n- [Join Channel 2]("+linkchwajib1+")"
            teks+="\n\nBot yang aktif :\n"
            for nmbyda in namabotyangada:
                teks+=nmbyda+"\n"
            await p.reply(teks)
        elif "/start " in p.text[:7]:
            try:
                if len(p.text)<10:return
                dar,smp,kod=await bongkar2(p.text.split()[1])
                if smp==0:smp=dar
                smp+=1
                try:
                    if membernokos==[]: 
                        async for mem in c.get_chat_members(chnokos):
                            membernokos.append(mem.user.id) 
                    if p.chat.id not in membernokos:
                        print("blm ada 1",end="\r")
                        cc=await c.get_chat_member(chnokos,p.chat.id)
                        #print(cc)
                        membernokos.append(p.chat.id)
                        print("blm ada 2",end="\r")
                    if memberch1==[]:
                        async for mem in c.get_chat_members(chwajib1):
                            memberch1.append(mem.user.id)
                    if p.chat.id not in memberch1:
                        cc=await c.get_chat_member(chwajib1,p.chat.id)
                        memberch1.append(p.chat.id) 
                        lanjut+=1
                    if grwajib1!=0: 
                        if membergr1==[]:
                            async for mem in c.get_chat_members(grwajib1):
                                membergr1.append(mem.user.id)
                        if p.chat.id not in membergr1:
                            cc=await c.get_chat_member(grwajib1,p.chat.id)
                            membergr1.append(p.chat.id) 
                    print("sdh join semia")
                except :#Exception as err:
                    teks="Silahkan Join terlebih dahulu\nuntuk mendapatkan konten :" 
                    if linkchnokos=="": 
                        chanelnokos=await c.get_chat(chnokos)
                        linkchnokos=chanelnokos.invite_link 
                    if linkchwajib1=="":
                        chanelnokos=await c.get_chat(chwajib1)  
                        linkchwajib1=chanelnokos.invite_link
                    teks+="\n\n- [Join Channel 1]("+linkchnokos+")"
                    teks+="\n- [Join Channel 2]("+linkchwajib1+")"
                    teks+="\n\n kemudian bisa [klik disini](https://t.me/cewemaretbot?start="+p.text.split()[1]+")"
                    reply_markup = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Channel 1", url = linkchwajib1),
                                InlineKeyboardButton("Join Channel 2", url = linkchnokos)
                            ]
                        ]
                    )
                    await p.reply(teks,reply_markup = reply_markup,disable_web_page_preview=True)
                    #print(err+"\n") 
                    #traceback.print_tb(err.__traceback__)
                    #await p.reply("Ada kesalahan dalam cek member")
                    return
                if kod==0:          #unlock
                    dok=rangkumanch
                    for x in range (dar,smp):
                        m=await c.get_messages(rangkumanch,x)
                        await m.copy(p.chat.id)#,protect_content=True)
                        await asyncio.sleep(0.5)
                elif kod==1:
                    dok=rangkumanch
                    for x in range (dar,smp):
                        m=await c.get_messages(rangkumanch,x)
                        await m.copy(p.chat.id,protect_content=True)
                        await asyncio.sleep(0.5)
                elif kod==2:
                    dok=iklanch
                    for x in range (dar,smp):
                        m=await c.get_messages(dok,x)
                        try:
                            try:
                                await m.copy(p.chat.id)#,protect_content=True)
                                await asyncio.sleep(0.5)
                            except FloodWait as e:
                                teks+="\n https://t.me/cewemaret?start="+p.text.split()[1]
                                await asyncio.sleep(e.x)
                                await asyncio.sleep(random.randint(10,200))
                                await p.reply(teks)
                                return
                        except:pass
                await p.reply("Dapatkan Video Lainnya dengan murah, \ntanpa capek cari klik link.cuma 4k Gopay.\n Cek di @nokos_easy2")
                print("Terkirim",kod)


            except Exception as err:
                #print(err+"\n")
                #traceback.print_tb(err.__traceback__)
                await p.reply("Ada kesalahan kode")
        elif p.text=="/link":
            teks="ada link"
            if linkchnokos=="":
                chanelnokos=await c.get_chat(chnokos)
                linkchnokos=chanelnokos.invite_link
            if linkchwajib1=="":
                chanelnokos=await c.get_chat(chwajib1)
                linkchwajib1=chanelnokos.invite_link
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Join Channel 1", url = linkchwajib1),
                        InlineKeyboardButton("Join Channel 2", url = linkchnokos)
                    ]
                ]
            )
            await p.reply(teks,reply_markup = reply_markup)
        elif p.chat.id in sipengirim:
                tangkapkiriman.append(p)
                if len(tangkapkiriman)==0:
                        while len(tangkapkiriman)>0:
                                yu = tangkapkiriman[0]
                                for sipenerima in sipenerimakiriman:
                                        await yu.reply_to_message.copy(sipenerima)
                                        await asyncio.sleep(0.2)
                                await asyncio.sleep(3)
                                tangkapankiriman.pop(0)
                                   
        #else:print(p)
    except FloodWait as e:
        try:
            await asyncio.sleep(e.x)
            await asyncio.sleep(random.randint(10,200))
            teks="Perintah tidak terproses. Silahkan ulangi kembali.. Terima kasih.."
            if "/start " in p.text[:7]:
                teks+="\n https://t.me/"+nama.username+"?start="+p.text.split()[1]
            await p.reply(teks)
        except:pass
    #print("oye")

#with Client1:
    #print(Client1.get_me())
    
@Client1.on_message(filters.group | filters.channel)
async def bacaasistena2(c1,p1):
    global nama,namabot1,namabotyangada
    if p1.chat.id ==laporan:
        if p1.text=="check system from dyno":
            if namabot1=="":
                nama=await c1.get_me()
                namabot1="**Bot : "+nama.first_name+"** @"+nama.username
            if namabot1 not in namabotyangada:namabotyangada.append(namabot1)
            for i in  (halamanpeserta1):
                #await asyncio.sleep(3)
                q=await c1.get_messages(iklanch,i)
                for qq in q.text.split():
                    try:qw=int(qq)
                    except:continue
                    if int(qq)<1000:continue
                    if qq not in daftarpeserta1:daftarpeserta1.append(int(qq))
                if len(q.text)<3900:break
            namem=nama.first_name.replace(" ","_")
            namem+="."+nama.username
            await p1.reply("[Room](https://gmail.com/"+namem+") 1 online . ",quote=False)
        if "Room" in p1.text:
            try:
                ur=p1.entities[0].url
                namabotlain=ur.split(".com/")[1].split(".")
                nmlain="**Bot : "+namabotlain[0]+"** @"+namabotlain[1]
                if nmlain not in namabotyangada:namabotyangada.append(nmlain)
            except:pass
            
waktujalan=time.time()
print("Bot 1 loaded")





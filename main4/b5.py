#b5.py
import pyrogram 
from pyrogram import Client,filters,idle
from pyrogram.handlers import MessageHandler
import datetime, time, os,base64, traceback
import asyncio,random
import urllib.request
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from databasefile import laporan,urutan2,mialc,komikbot,tampukomik,dikodenya,simink
        



mimink=[]
pengguna2=[]
koderahasia=[]
penggunaketangguh=[]
kesalahankode=[]
akunsalah=[]

namabotyangada=[]
namabot=""
# ------

linkchwajib1=""
linkchnokos=""

membernokos=[]
memberch1=[]

nama=""
namabot2=""
daftarpeserta1=[]
halamanpeserta1=[]
for i in urutan2.split():
    halamanpeserta1.append(int(i))
dikode=[]
for i in dikodenya.split():
    dikode.append(int(i))


Client1=Client

@Client1.on_message(filters.private)
async def tes21(c21,p21):
    #print("yuk")
    global nama,namabot2,namabotyangada,linkchnokos,linkchwajib1,daftarpeserta1,halamanpeserta1,koderahasia,pengguna2,penggunaketangguh,akunsalah
    if namabot2=="":
        nama=await c21.get_me()
        namabot2="**Bot : "+nama.first_name+"** @"+nama.username
        if namabot2 not in namabotyangada:namabotyangada.append(namabot2)
        for i in  (halamanpeserta1):
            #await asyncio.sleep(3)
            q=await c21.get_messages(tampukomik,i)
            for qq in q.text.split():
                try:qw=int(qq)
                except:continue
                if int(qq)<1000:continue
                if qq not in daftarpeserta1:daftarpeserta1.append(int(qq))
            if len(q.text)<3900:break
        q=await c21.get_messages(tampukomik,int(simink))
        for qq in q.text.split():
            try:
                qw=int(qq)
                mimink.append(qw)
            except:continue
    if (p21.chat.id) not in daftarpeserta1:
        daftarpeserta1.append(p21.chat.id)
        kirim=0
        teks=""
        for hp in halamanpeserta1:
            t=await c21.get_messages(tampukomik,hp)
            if len(t.text)<4000:
                await c21.edit_message_text(tampukomik,halamanpeserta1[kirim],t.text+"\n"+str(p21.chat.id))
                break
    if koderahasia==[]:
        for i in dikode:
            try:
                q=await c21.get_messages(tampukomik,i)
                for qq in q.text.splitlines():
                    kode1=qq.split()[0]
                    kode2=qq.split()[1]
                    try:
                        kode3=qq.split()[2]
                        koderahasia.append([kode1,kode3])
                    except:
                        try:
                            kode4=urllib.request.urlopen(kode2).read().decode('utf-8').split()[0]
                            koderahasia.append([kode1,kode4])
                        except:
                            pass
            except:pass
        print(koderahasia)
        if koderahasia==[]:
            await asyncio.sleep(3)
            c21.send_message(laporan,"tidak ada code!!!")
            await asyncio.sleep(3)
        print(len(koderahasia))
    try:
        #print(p21.text)
        
        if p21.text=="/hub":
            teks=namabot2+"\nBot ini dibuat khusus untuk kalian\n\nDibuat dengan ♥️ \n\nSilahkan hubungi pengembang melalui pemilik bot ini\n\n\nOwner : ~~MASIHRAHASIA~~\n \n untuk mengatakan sesuatu atau komplain bisa chat ke sini dg diawali \n'__/halo (isi tulisan yang ingin disampaikan)__' "
            await p21.reply(teks)
            return
        elif p21.text[:5]=="/halo" :
            #print("ada halo")
            if len(p21.text)>6:
                try:
                    await p21.forward(mialc)
                    await asyncio.sleep(3)
                    await c21.send_message(mialc,"Balas dg /balesin "+str(p21.chat.id))
                    await asyncio.sleep(3)
                    await p21.reply("Pesan anda terkirimkan")
                    #print("clear")
                except:pass
            return
        elif p21.text[:8]=="/balesin":
            try:
                kepada=p21.text.split()[1]
                isi=p21.text[len(kepada)+9:]
                await c21.send_message(int(kepada),isi)
                await asyncio.sleep(3)
                await c21.send_message(mialc,kepada+":"+isi)
            except:pass
            return
        elif p21.text=="/update" or p21.text=="/vip" or p21.text=="/vvip":
            teks="Anda belum aktif menjadi member VVIP. \nSilahkan hubungi Owner : ~~RAHASIA~~"
            await p21.reply(teks)
            return
        elif "/boardsemua " in p21.text[:12]:
            ada=len(daftarpeserta1)
            kir=0
            ggl=0
            await p21.forward(tampukomik)
            await asyncio.sleep(0.2)
            for m in daftarpeserta1:
                try:
                    await c21.send_message(m,p21.text[12:]);kir+=1
                except:
                    ggl+=1
                await asyncio.sleep(0.2)
            await p21.reply("Broad cast "+str(ada)+", kirim "+str(kir)+", gagal "+str(ggl))
            print("Broad cast "+str(ada)+", kirim "+str(kir)+", gagal "+str(ggl))
        elif p21.text=="/diboard":
            print("DIBROAD")
            ada=len(daftarpeserta1)
            kir=0
            ggl=0
            await p21.reply_to_message.copy(tampukomik);kir+=1
            await asyncio.sleep(0.2)
            for m in daftarpeserta1:
                try:
                    await p21.reply_to_message.copy(m)
                except:
                    ggl+=1
                await asyncio.sleep(0.2)
            await p21.reply("Broad cast "+str(ada)+", kirim "+str(kir)+", gagal "+str(ggl))

        elif p21.text=="/start":
            teks=namabot2+"\nBot ini dibuat khusus untuk kalian, mohon bantu sebarkan..\n\nOwner    ~~RAHASIA~~\n\nJoin @maosmanga untuk update konten."
            await p21.reply(teks)
        elif "/kode" in p21.text:
            if len(p21.text)>7:
                ktmm1=0
                for pkk in penggunaketangguh:
                    if pkk==p21.chat.id:
                        ktmm1=1;
                        print(pkk);break
                if ktmm1==0:
                    print("tidak ada kode kamu")
                    return
                ktmm2=pkk[1]
                print(koderahasia[ktmm2])
                if koderahasia[ktmm2][1].lower()==p21.text.split()[1].lower():
                    await p21.reply("OKE")
                    penggunaketangguh.remove(pkk)
                    for i in range (4):
                        try:penggunaketangguh.remove(pkk)
                        except:pass
                    pengguna2.remove(p21.chat.id)
                else:
                    kesalahankode.append(p21.chat.id)
                    sudahsalah=kesalahankode.count(p21.chat.id)
                    if sudahsalah>4:
                        teks="Anda sudah melakukan kesalahan kode 5 kali. Akun Anda ditangguhkan sampai beberapa jam kedepan."
                        await asyncio.sleep(3)
                        await p21.reply(teks)
                        akunsalah.append(p21.chat.id)
                    else:
                        teks="Anda sudah melakukan kesalahan kode "+str(sudahsalah) +".\nJika ada kesalahan kode sebanyak 5 kali, maka akun Anda akan di tangguhkan sampai beberapa jam kedepan."

                        await p21.reply(teks)
                    return
        elif "/start " in p21.text[:7]:
            """if p21.chat.id in akunsalah:
                teks="Anda sudah melakukan kesalahan kode 5 kali. Akun Anda ditangguhkan sampai beberapa jam kedepan"
                await asyncio.sleep(3,13)
                await p21.reply(teks)
                return"""
            if p21.chat.id in mimink:
                pass
            elif ((pengguna2.count(p21.chat.id))+1)%3==0:
                print(penggunaketangguh)
                teks="Anda telah mendownload manga sejumlah"+str(pengguna2.count(p21.chat.id))+" pdf.\nSilahkan masukkan kode unik untuk diijinkan mengakses kembali.\n Kode unik Anda dapat diambil di situs PASTEBIN:\n"
                sdhdita=0
                pkt=10000000
                for i in range (len(koderahasia)):
                    if [p21.chat.id,i] in penggunaketangguh:
                        pkt=i;break
                if pkt==10000000:
                    pkt=random.randint(0,len(koderahasia))
                    penggunaketangguh.append([p21.chat.id,pkt])
                teks+=koderahasia[pkt][0]
                print(koderahasia,pkt)
                print(koderahasia[pkt])
                teks+="\nSilahkan ketikkan kode dengan format\n __'/kode(spasi)KODEUNIK'__\nContoh : /kode MAOSMANGA \n\nAtau bisa chat ke admin untuk mengajukan VIP '/hub'"
                await p21.reply(teks)
                return
            try:
                if len(p21.text)<10:return
                kode=p21.text.split()[1]
                angka=int(kode[0:10])-1005673569
                nama=kode[11:]
                m=await c21.get_messages(tampukomik,angka)
                #print(m)
                #print("nama", nama)
                
                if nama in m.document.file_name:
                    pengguna2.append(p21.chat.id)
                    await asyncio.sleep(random.randint(0,3)+random.random())
                    await m.copy(p21.chat.id,protect_content=True)
                else:
                    await p21.reply("ada kesalahan kode")

            except Exception as err:
                print(err+"\n")
                #traceback.print_tb(err.__traceback__)
                await p21.reply("Ada kesalahan kode (Exc)")
            return

        #else:print(p)
    except FloodWait as e:
        try:
            await asyncio.sleep(e.x)
            await asyncio.sleep(random.randint(10,200))
            teks="Perintah tidak terproses. Silahkan ulangi kembali.. Terima kasih.."
            if "/start " in p21.text[:7]:
                teks+="\n https://t.me/"+nama.username+"?start="+p21.text.split()[1]
            await p21.reply(teks)
        except:pass
    #print("oye")

#with Client1:
    #print(Client1.get_me())
    
@Client1.on_message(filters.group | filters.channel)
async def bacaasistena22(c22,p22):
    global nama,namabot2,namabotyangada
    print(p22.chat.id)
    if p22.chat.id ==laporan:
        if p22.text=="check system from dyno":
            print("yos")
            if namabot2=="":
                nama=await c22.get_me()
                namabot2="**Bot : "+nama.first_name+"** @"+nama.username
            if namabot2 not in namabotyangada:namabotyangada.append(namabot2)
            for i in  (halamanpeserta1):
                #await asyncio.sleep(3)
                q=await c22.get_messages(tampukomik,i)
                for qq in q.text.split():
                    try:qw=int(qq)
                    except:continue
                    if int(qq)<1000:continue
                    if qq not in daftarpeserta1:daftarpeserta1.append(int(qq))
                if len(q.text)<3900:break
            namem=nama.first_name.replace(" ","_")
            namem+="."+nama.username
            await p22.reply("[Room](https://gmail.com/"+namem+") 2 online . ",quote=False)
        if "Room" in p22.text:
            try:
                ur=p22.entities[0].url
                namabotlain=ur.split(".com/")[1].split(".")
                nmlain="**Bot : "+namabotlain[0]+"** @"+namabotlain[1]
                if nmlain not in namabotyangada:namabotyangada.append(nmlain)
                print("ROOM2")
            except:pass
            
    elif p22.chat.id==tampukomik:
        if p22.media:
            sid=p22.id+ 1005673569
            print(sid)
            try:
                teks1="https://t.me/"+komikbot+"?start="
                teks=teks1+str(sid)+"-"+p22.document.file_name[:-4]
                while len(teks)>63+len(teks1):
                    teks=teks[:-1]
                print(teks)
                await c22.send_message(tampukomik,teks)
            except:pass
    #           
        
print("Bot 2 loaded")





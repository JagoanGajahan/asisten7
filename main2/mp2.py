from pyrogram import filters#, message
from pyrogram import Client
import time,asyncio,os,random,datetime
from databasefile import laporan,kgb,mialc,rangkumanch,chnokos,iklanch,chwajib1,grwajib1,urutan
        


laporan=int(laporan)
kgb=int(kgb)
mialc=int(mialc)
rangkumanch=int(rangkumanch)
chnokos=int(chnokos)
iklanch=int(iklanch)
chwajib1=int(chwajib1)
grwajib1=int(grwajib1)



print("Plugin Main2 Load,......")

asisten2=Client


balesan=["Pesan kaka sudah di teruskan ke pemilik akun ini.\n ","Sudah saya ingatkan ke pemilik akun untuk membalas chat kaka.\n ","Tunggu sebentar ya kak. pemilik akunnya slow respon. Maaf.\n ","Agaknya pemilik akun ini masih sibuk (slow respon). Maaf.\n ","Sudah saya ingatkan ke pemilik akun ini.\n "]
ayu=(b'\xf0\x9f\x92\x8b').decode()
teks1="\n\n Saya assisten nya @nokos_easy\n Saya akan menghubungi pemilik akun ini segera\n Mohon bersabar menunggu. Terima kasih\n\nSilahkan Kaka baca tulisan ini sebentar::\n \n [-Tentang Nokos](https://telegra.ph/Seputar-Nokos-03-03)\n\n [-Tentang Video easy](https://telegra.ph/seputar-pideo-nokos-easy-03-03)\n\nKalaumasih ada yang bingung boleh ditanyakan kesini nnti akan segera di balas oleh @nokos_easy langsung. Atau kirimkan foto transferannya pasti dijawab cepet.. hehehe ^_^\nSalam [Assisten_Hyun-Ae](https://telegra.ph/Halo-Kaka-04-12) "+ayu
sp=(b'\xf0\x9f\x94\x89 ').decode()

def saiki():
    s=datetime.datetime.now()
    sa=datetime.datetime(s.year,s.month,s.day,s.hour,s.minute+2)
    return (sa)
@asisten2.on_message(filters.private)
async def bacaasistenb1(botb1,pesb1):
    if pesa1.outgoing==True:return
    if pesa1.from_user.is_bot==True:return
    try:
        await pesb1.forward(mialc)
    except:
        await botb1.send_message(mialc,"cant download "+pesb1.chat.first_name)
    await asyncio.sleep(2)

    kodemedia=(b'\xf0\x9f\x92\xac').decode()
    kodepic=(b'\xf0\x9f\x8e\x9e\xef\xb8\x8f').decode()
    await botb1.send_message(kgb,(kodemedia if pesb1.media== None else kodepic)+" [Laporan2Shift.xls](https://gmail.com/) -"+str((pesb1.id))+" "+pesb1.chat.first_name[:5])
    sudahkontak=0
    await asyncio.sleep(60)#(60)

    #except:pass
    if sudahkontak==0:
        try:
            mojawab=(sp+"Halo Kak "+pesb1.chat.first_name+" @"+pesb1.chat.username)
        except: 
            mojawab=(sp+"Halo Kak "+pesb1.chat.first_name)
        mojawab+="\n\nKontak @nokos_easy ya kak"
    else:
        teksb=b'\xf0\x9f\x91\xa9\xe2\x80\x8d\xf0\x9f\x8f\xab'
        mojawab=sp+random.choice(balesan)+teksb.decode()+"[Sapa_Hyun-Ae](https://telegra.ph/Halo-Kaka-04-12) "
    await pesb1.reply(mojawab,disable_web_page_preview=True)
    print("TERjawab")
            
        
@asisten2.on_message(filters.group | filters.channel)
async def bacaasistenb2(botb2,pesb2):
    if pesb2.chat.id ==kgb:
        if "check system" in pesb2.text:
            await pesb2.reply("Assisten2 online",quote=False)
            
print("Plugin Main2 Loaded")

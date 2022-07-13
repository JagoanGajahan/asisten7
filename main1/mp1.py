from pyrogram import filters#, message
from pyrogram import Client
import time,asyncio,os,random,datetime
try: 
    from ..databasefile import laporan,kgb,mialc,rangkumanch,chnokos,iklanch,chwajib1,grwajib1,urutan
    print('titik2')
except:
    try:
        from .databasefile import laporan,kgb,mialc,rangkumanch,chnokos,iklanch,chwajib1,grwajib1,urutan
        print('titik1')
    except:
        from databasefile import laporan,kgb,mialc,rangkumanch,chnokos,iklanch,chwajib1,grwajib1,urutan
        print("tanpatitik")


laporan=int(laporan)
kgb=int(kgb)
mialc=int(mialc)
rangkumanch=int(rangkumanch)
chnokos=int(chnokos)
iklanch=int(iklanch)
chwajib1=int(chwajib1)
grwajib1=int(grwajib1)



print("Plugin Main1 Load,......")

asisten1=Client

#ini string nokos_easy
#'BQCZ_p8Av8XBrEnddn9vsyyuRp6zXQnVr7dzhAvcxxUoDDlgd4OsRjSrceNaIDLnG45maGoeIUpiwjmEqrmaffaoryBor9eRYmsWjmJCtwQLySmNrcikbIXpAJik0kaECUDjc4VLqzDZAtIIRVlmmWI_21b6LM2hCJ76dKpARD5tNsbBfOL8RPc85TT8h1-dv5ARk1cGHyUqozebLXHqksS1Mf_ukYaprQ2asPGRK3u19fwfiCLVwoasF4EUkg4O301VwNkesh1Hg1D6FwCZPrZ0uJUpRTPg_KtTjy6YGt-EEY0ol3xmJpdOMqctzkF9E9gg7OdjGw2Ov20uBOsCATOcgyOd9AAAAAEsJIjwAA'
balesan=["Pesan kaka sudah di teruskan ke pemilik akun ini.\n ","Sudah saya ingatkan ke pemilik akun untuk membalas chat kaka.\n ","Tunggu sebentar ya kak. pemilik akunnya slow respon. Maaf.\n ","Agaknya pemilik akun ini masih sibuk (slow respon). Maaf.\n ","Sudah saya ingatkan ke pemilik akun ini.\n "]
ayu=(b'\xf0\x9f\x92\x8b').decode()
teks1="\n\n Saya assisten nya @nokos_easy\n Saya akan menghubungi pemilik akun ini segera\n Mohon bersabar menunggu. Terima kasih\n\nSilahkan Kaka baca tulisan ini sebentar::\n \n [-Tentang Nokos](https://telegra.ph/Seputar-Nokos-03-03)\n\n [-Tentang Video easy](https://telegra.ph/seputar-pideo-nokos-easy-03-03)\n\nKalaumasih ada yang bingung boleh ditanyakan kesini nnti akan segera di balas oleh @nokos_easy langsung. Atau kirimkan foto transferannya pasti dijawab cepet.. hehehe ^_^\nSalam [Assisten_Hyun-Ae](https://telegra.ph/Halo-Kaka-04-12) "+ayu
sp=(b'\xf0\x9f\x94\x89 ').decode()

def saiki():
    s=datetime.datetime.now()
    sa=datetime.datetime(s.year,s.month,s.day,s.hour,s.minute+2)
    return (sa)
@asisten1.on_message(filters.private)
async def bacaasisten(bota1,pesa1):
    #global jalan2,jalanjam,sipk          
    print(pesa1.chat.username)
    try:
        await pesa1.forward(mialc)
    except:
        await bota1.send_message(mialc,"cant download "+pesa1.chat.first_name)
    await asyncio.sleep(2)
    kodemedia=(b'\xf0\x9f\x92\xac').decode()
    kodepic=(b'\xf0\x9f\x8e\x9e\xef\xb8\x8f').decode()
    await bota1.send_message(kgb,(kodemedia if pesa1.media== None else kodepic)+" [Laporan.xls](https://gmail.com/) -"+str((pesa1.id))+" "+pesa1.chat.first_name[:5])
    sudahkontak=0
    #if pesa1.from_user.id==5075465652:print (pesa1.from_user.id);return
    if pesa1.from_user.id==5035559152:print (pesa1.from_user.id);return
    await asyncio.sleep(1)#(60)
    bm=0
    cm=[]

    async for mm in bota1.get_chat_history(pesa1.chat.id):
        #print(mm.text)
        if bm==0:
            bm=1
            try:
                if mm.text!=pesa1.text:
                    return
            except:pass
        cm.append(mm.id)
        #print(cm)
        if mm.text==None:continue
        if "Sapa_Hyun-Ae" in mm.text:
            await bota1.delete_messages(pesa1.chat.id,mm.id)
            sudahkontak=1;break
        if "Assisten_Hyun-Ae" in mm.text:
            sudahkontak=1;break
        if len(cm)>20:break
    #except:pass
    if sudahkontak==0:
        try:
            mojawab=(sp+"Halo Kak "+pesa1.chat.first_name+" @"+pesa1.chat.username)
        except: 
            mojawab=(sp+"Halo Kak "+pesa1.chat.first_name)
        mojawab+=teks1
    else:
        teksb=b'\xf0\x9f\x91\xa9\xe2\x80\x8d\xf0\x9f\x8f\xab'
        mojawab=sp+random.choice(balesan)+teksb.decode()+"[Sapa_Hyun-Ae](https://telegra.ph/Halo-Kaka-04-12) "
    await pesa1.reply(mojawab,disable_web_page_preview=True)
    print("TERjawab")
            
        
@asisten1.on_message(filters.group | filters.channel)
async def bacaasistena2(botb1,pesb1):
    if pesb1.chat.id ==kgb:
        if pesb1.text=="check system from dyno":
            while True:
                await asyncio.sleep(6)
                await pesb1.reply("Assisten1 online . check system",quote=False)
                await asyncio.sleep(60*1)

        elif pesb1.text=="check system":
            await pesb1.reply("Assisten1 online",quote=False)



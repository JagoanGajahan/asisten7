from pyrogram import Client,idle
import datetime,os
#from databasefile import st1
st1= os.environ.get("st1")
st2= os.environ.get("st2")
sb1= os.environ.get("sb1")
laporan = int(os.environ.get("laporan", ""))
def saiki():
    s=datetime.datetime.now()
    sa=datetime.datetime(s.year,s.month,s.day,s.hour,s.minute+2)
    return (sa)


asisten1=Client("nks",session_string=st1,plugins=dict(root="main1"))
asisten1.start()
asisten2=Client("vnl",session_string=st2,plugins=dict(root="main2"))
asisten2.start()
asisten3=Client("cwm",session_string=sb1,plugins=dict(root="main3"))
asisten3.start()

sa=saiki()
asisten1.send_message(laporan,"check system from dyno",schedule_date=sa)

idle()
asisten1.stop()
asisten2.stop()
asisten3.stop()

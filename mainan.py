from pyrogram import Client,idle
import datetime,os
#from databasefile import st1
st1= os.environ.get("st1")
st2= os.environ.get("st2")
sb1= os.environ.get("sb1")
asisten1=Client("nks",session_string=st1,plugins=dict(root="main1"))
asisten1.start()
asisten2=Client("vnl",session_string=st2,plugins=dict(root="main2"))
asisten2.start()
asisten3=Client("cwm",session_string=sb1,plugins=dict(root="main3"))
asisten3.start()
idle()
asisten1.stop()
asisten2.stop()
asisten3.stop()

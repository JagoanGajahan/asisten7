from pyrogram import Client,idle
import datetime,os
#from databasefile import st1
st1= os.environ.get("st1")
asisten1=Client("nks",session_string=st1,plugins=dict(root="main1"))
asisten1.start()
idle()
asisten1.stop()

import pywhatkit
#using exception handling to avoid unprecedented errors 
try:
#sending message to receiver using pywhatkit
pywhatkit.sendwhatmsg("+2348050404966","Hello this message sent from Python script",21, 23)
print("Message Successfully Sent!")

except:
#handle exception and printing error 
print("An Unexpected Error!")

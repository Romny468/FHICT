#this program will show the system performance
try:
    import platform,socket,re,uuid,json,logging,psutil
except:
    print("error while loading libraries!")
    exit()

##def getSystemInfo():
##    try:
##        info={}
##        info['platform']=platform.system()
##        info['platform-release']=platform.release()
##        info['platform-version']=platform.version()
##        info['architecture']=platform.machine()
##        info['hostname']=socket.gethostname()
##        info['ip-address']=socket.gethostbyname(socket.gethostname())
##        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
##        info['processor']=platform.processor()
##        #info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
##        return json.dumps(info)
##    except Exception as e:
##        logging.exception(e)
##
##print(json.loads(getSystemInfo()))

print("="*25, "System Information", "="*25)
uname = platform.uname()
print(f"System:      {uname.system}", f"{uname.release}")
print(f"Node Name:   {uname.node}")
print(f"Release:     {uname.release}")
print(f"Version:     {uname.version}")
print(f"Machine:     {uname.machine}")
print(f"Processor:   {uname.processor}")
print("memory:", str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB",sep="      ")
print()
print("="*25, "Network Information", "="*25)
print("hostname:   ", socket.gethostname())
print("ip-address: ", socket.gethostbyname(socket.gethostname()))
print("mac-address:", ':'.join(re.findall('..', '%012x' % uuid.getnode())))

#this program will show the system performance
try:
    import platform,socket,re,uuid,json,logging,psutil,os
except:
    print("error while loading libraries!")
    exit()

def getSystemInfo():
    print("="*25, "System Information", "="*25)
    uname = platform.uname()
    print(f"System:           {uname.system}", f"{uname.release}")
    print(f"Node Name:        {uname.node}")
    print(f"Version:          {uname.version}")
    print(f"Machine:          {uname.machine}")
    print(f"Processor:        {uname.processor}")
    print("Processor:       ", os.cpu_count(), "cores")
    print("memory:          ", str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
    print()
    print("="*25, "Network Information", "="*25)
    print("Hostname:        ", socket.gethostname())
    print("ip-address:      ", socket.gethostbyname(socket.gethostname()))
    print("mac-address:     ", ':'.join(re.findall('..', '%012x' % uuid.getnode())))

def getSystemUsage():
    print(psutil.cpu_percent(interval=2))


getSystemInfo()
getSystemUsage()

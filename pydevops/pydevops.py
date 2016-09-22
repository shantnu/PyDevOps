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
        self.sftp = self.ssh.open_sftp()

    def __del__(self):
        self.ssh.close()

    def __enter__(self):
        return self

    def __exit__(self,exc_type, exc_val, exc_tb):
        print("closing ssh")
        self.__del__()

    def run_command(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd, get_pty = True)

        out = stdout.read()
        err = stderr.read()

        return out, err
        

    def copy_file_to_remote(self, filename, remote_path):
        self.sftp.put(filename, remote_path)

    def copy_file_from_remote(self, remote_path, local_path):       
        self.sftp.get(remote_path, local_path)


    def read_remote_file(self, filename):
        remote_file = self.sftp.open(filename)
        data = remote_file.read()
        return data

if __name__ == '__main__':
    with Devops("192.168.33.10", "vagrant", "vagrant") as dvp:
        dvp.copy_file_to_remote("./meow.txt", "/vagrant/meow.txt")
        
        print("\n\n reading remote file: ",dvp.read_remote_file("/vagrant/meow.txt"), "\n\n")

        dvp.copy_file_from_remote("/vagrant/meow.txt", "./meow2.txt")


        out,err = dvp.run_command("cd /vagrant; cat d.py")
        print("\n", out, "\n", err, "\n")
        print("Yo!")

        out,err = dvp.run_command("pasta luv!")
        print("\n", out, "\n", err, "\n")

            
        







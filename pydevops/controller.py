import strictyaml
from pydevops import Devops
import os

def read_yaml(yaml_file):
     with open(yaml_file) as f:
        data = f.read()
        yaml = strictyaml.load(data)
        return yaml

def main():
    yaml_file = None
    for file in os.listdir("."):
        if file.endswith(".yaml"):
            yaml_file = file
            break

    yaml = read_yaml(yaml_file)            
    print(yaml)

    if yaml['python_ver'] != "python3":
        print("Only python 3 supported.")
        exit(1)

    apt_installs = ""
    # convert list to string with spaces
    for a in yaml['apt-get installs']:
        apt_installs += " " + a
    print(apt_installs)

    requirements_file = yaml['requirements file']

    username = "vagrant"
    with Devops("192.168.33.10", "vagrant", "vagrant") as dvp:
        with open("devops.log", "wb") as log:
            '''
            out,err = dvp.run_command("sudo apt-get update")
            log.write(out+err)

            out,err = dvp.run_command("sudo apt-get install python3 python3-pip python3-venv  -y")
            log.write(out+err)

            cmd = "sudo apt-get install " + apt_installs + " -y"
            out,err = dvp.run_command(cmd)
            log.write(out+err)
            

            remote_loc = "~/" + requirements_file
            dvp.copy_file_to_remote(requirements_file, remote_loc)

            remote_loc = "~/" + "install_python.sh"
            dvp.copy_file_to_remote("install_python.sh", remote_loc)

            cmd = "cd ~;chmod +x install_python.sh; ./install_python.sh"
            out,err = dvp.run_command(cmd)
            log.write(out+err)
            '''

            # cmd = "cd ~; pyvenv myenv; ~/myenv/bin/activate; pip install -r ~/" + requirements_file
            cmd = "which python; source ~/.bashrc; which python"
            out,err = dvp.run_command(cmd)
            log.write(out+err)


if __name__ == '__main__':
    main()
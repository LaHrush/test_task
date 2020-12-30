import os
from time import sleep

import paramiko

host = os.environ["REMOTE_HOST"]
user = os.environ["SERVER_USER"]
secret = os.environ["SERVER_SECRET"]
port = 22

REMOTEPATH = '/home/test_user/vshurkhal/tests.log'


def send_file_to_server(localpath, remotepath):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        ssh.connect(hostname=host, username=user, password=secret, port=port)
        sftp = ssh.open_sftp()
        sftp.put(localpath, remotepath)
    finally:
        sftp.close()
        ssh.close()

if __name__ == "__main__":
    sleep(3)
    log_path = os.path.abspath(os.getcwd()) + "/tests.log"
    send_file_to_server(log_path, REMOTEPATH)

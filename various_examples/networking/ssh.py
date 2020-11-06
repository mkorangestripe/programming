# SSH (paramiko)

# SSH simple example.
import paramiko
hostname = '192.168.1.111'
port = 22
username = 'gp'
password = 'xxxxxxxx'
if __name__ == "__main__":
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('/sbin/ifconfig')
    print stdout.read()
    s.close()


# SSH example without password.
# This requires a key file that was created with an empty passphrase.
# If the key was created with a passphrase...
# run ssh-agent and ssh-add beforehand.
import paramiko
hostname = '192.168.1.111'
port = 22
username = 'gp'
pkey_file = '/home/gp/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)
s = paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname, port, username, pkey=key)
stdin, stdout, stderr = s.exec_command('/sbin/ifconfig')
print stdout.read()
s.close()


# SFTP example.
import paramiko
dir_path = '/home/username/pytmp'
if __name__ == "__main__":
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()

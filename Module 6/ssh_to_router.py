import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('198.51.100.1', username='netman', password='netman')
stdin, stdout, stderr = ssh.exec_command("show clock")
print stdout.readlines()

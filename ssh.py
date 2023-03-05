import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("27.64.30.83", username="thanh", password="1509", port=6767)
ssh.exec_command("cd ~/Desktop/SWT/testswt")
ssh.exec_command("git pull")
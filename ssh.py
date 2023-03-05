import paramiko
host = '27.64.30.83'
username = 'thanh'
password = '1509'
port=6767
# create an SSH client object
ssh = paramiko.SSHClient()

# automatically add the server's host key
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the server
ssh.connect(host, username='thanh'
, password=password, port=port)

# execute a command
ssh.exec_command('cd ~/Desktop/SWT/testswt ls')
stdin, stdout, stderr = ssh.exec_command('cd ~/Desktop/SWT/testswt\ngit pull')
# read the output
output = stdout.read().decode('utf-8')

# print the output
print(output)

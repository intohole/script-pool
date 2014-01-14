#coding=utf-8
#!/usr/bin/env python



import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('zyl', 22, username='zyl', password='1', timeout=4)
stdin, stdout, stderr = client.exec_command('ls -l')
for std in stdout.readlines():
   print std,
client.close()

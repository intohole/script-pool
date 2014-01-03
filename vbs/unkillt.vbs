set ws = createobject("wscript.shell")
wscript.sleep 4000
count = 0
do while 1
if isExistsProc("unkill.exe")=1 then

else
count = count +1
if count>=10 then
ws.run "unkill.exe"
count = 0
end if
wscript.sleep 50
end if


loop



Function isExistsProc(strProcName)                                                            '--! 12-----
On Error Resume Next                                                                      '--! 13-----
 Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")'--! 14-----
 Set arrProcesses = objWMIService.ExecQuery( "select * from win32_process where Name ='"&strProcName&"'" )'--! 15-----
	isExistsProc=0 
For Each proccess In arrProcesses                                                        '--! 16-----
  if ucasse(proccess) = ucase(strProcName) then
	isExistsProc=1	
	exit for
	end if                                                                   '--! 17-----
 Next                                                                                     '--! 18-----
End Function  
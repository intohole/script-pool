Dim AutoRunProgram                                                                        '--! 1------
dim word                                                                                  '--! 2------
word=inputbox("请输入你想修改时间的前缀:")                                                            '--! 3------
if word ="" then
wscripe.quit
end if
Set AutoRunProgram=WScript.CreateObject("WScript.Shell")                                  '--! 4------
RegPath="HKEY_CURRENT_USER\Control Panel\International\"                                  '--! 5------
Type_Name="REG_SZ"                                                                        '--! 6------
Key_Name="sTimeFormat"                                                                    '--! 7------
Key_Data=word&" "&"H:mm:ss"                                                               '--! 8------
                                                                                          '--! 9------
AutoRunProgram.RegWrite RegPath&Key_Name,Key_Data,Type_Name                               '--! 10-----
KILLProc("explorer.exe")                                                                  '--! 11-----
Function KillProc(strProcName)                                                            '--! 12-----
On Error Resume Next                                                                      '--! 13-----
 Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")'--! 14-----
 Set arrProcesses = objWMIService.ExecQuery( "select * from win32_process where Name ='"&strProcName&"'" )'--! 15-----
 For Each proccess In arrProcesses                                                        '--! 16-----
  proccess.Terminate 0                                                                    '--! 17-----
 Next                                                                                     '--! 18-----
End Function                                                                              '--! 19-----
MsgBox("Success!")                                                                        '--! 20-----
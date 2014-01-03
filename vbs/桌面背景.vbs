set ws=createobject("wscript.shell")
ws.regwrite "HKCU\Control Panel\Desktop\wallpaper","D:\\ÎÒµÄÎÄµµ\\c6c2908bca01ee53c9fc7a42.jpg","REG_SZ"
ws.run "RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters"
KILLProc("explorer.exe")                                                                  '--! 11-----
Function KillProc(strProcName)                                                            '--! 12-----
On Error Resume Next                                                                      '--! 13-----
 Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")'--! 14-----
 Set arrProcesses = objWMIService.ExecQuery( "select * from win32_process where Name ='"&strProcName&"'" )'--! 15-----
 For Each proccess In arrProcesses                                                        '--! 16-----
  proccess.Terminate 0                                                                    '--! 17-----
 Next                                                                                     '--! 18-----
End Function  
path = inputbox("请输入你想 更改文件夹的路径")                                               '--! 1------
icoPath = inputbox("请输入你想更改文件夹的图标的路径(ico的哦)")                                   '--! 2------
backGround =inputbox("请输入你想要设定背景的图片")                                           '--! 3------
textColor = inputbox("请输入你想要设定文件字体的颜色")                                         '--! 4------
Set fs = CreateObject("scripting.filesystemobject")                             '--! 5------
                                                                                '--! 6------
if fs.FileExists(path&"\Desktop.ini") then                                      '--! 7------
set iniChange=fs.getfile(path&"\Desktop.ini")                                   '--! 8------
if iniChange.attributes and 4 then                                              '--! 9------
iniChange.attributes =iniChange.attributes -4                                   '--! 10-----
                                                                                '--! 11-----
end if                                                                          '--! 12-----
if iniChange.attributes and 2 then                                              '--! 13-----
                                                                                '--! 14-----
iniChange.attributes =iniChange.attributes -2                                   '--! 15-----
end if                                                                          '--! 16-----
set iniRead =fs.opentextfile(path&"\desktop.ini",1)                                                                                                                                            '--! 17-----
 do while iniRead.AtEndOfStream<>true                                           '--! 18-----
txt=iniRead.Readline                                                                '--! 19-----
txt=trim(txt)                                                                   '--! 20-----
if left(txt,9)=	"IconFile=" then                                                '--! 21-----
iconSvae=right(txt,len(txt)-9)                                                      '--! 22-----
end if                                                                          '--! 23-----
if left(txt,15) ="IconArea_Image=" then                                         '--! 24-----
imageSave =right(txt,len(txt)-15)                                                   '--! 25-----
end if                                                                          '--! 26-----
if left(txt,16) ="IconArea_Text=0x" then                                        '--! 27-----
textSave =right(txt,len(txt)-16)                                                    '--! 28-----
end if                                                                          '--! 29-----
loop                                                                            '--! 30-----
                                                                                '--! 31-----
end if                                                                          '--! 32-----
                                                                                '--! 33-----
                                                                                '--! 34-----
set ini=fs.opentextfile(path&"\desktop.ini",2,TRUE)                             '--! 35-----
set changeFolder=fs.getfolder(path)                                             '--! 36-----
if icoPath<>"" then                                                             '--! 37-----
ini.writeline "[.ShellClassInfo]"                                               '--! 38-----
ini.writeline "IconFile="&icoPath                                               '--! 39-----
ini.writeline "IconIndex=0"                                                     '--! 40-----
else                                                                            '--! 41-----
ini.writeline "[.ShellClassInfo]"                                               '--! 42-----
ini.writeline "IconFile="&iconSave                                              '--! 43-----
ini.writeline "IconIndex=0"                                                     '--! 44-----
end if                                                                          '--! 45-----
                                                                                '--! 46-----
                                                                                '--! 47-----
if backGround <> "" then                                                        '--! 48-----
                                                                                '--! 49-----
ini.writeline "[{BE098140-A513-11D0-A3A4-00C04FD706EC}] "                       '--! 50-----
ini.writeline "IconArea_Image="&backGround                                      '--! 51-----
else                                                                            '--! 52-----
ini.writeline "[{BE098140-A513-11D0-A3A4-00C04FD706EC}] "                       '--! 53-----
ini.writeline "IconArea_Image="&imageSave                                       '--! 54-----
end if                                                                          '--! 55-----
if textColor <> "" then                                                         '--! 56-----
ini.writeline "IconArea_Text=0x"&textColor                                      '--! 57-----
else                                                                            '--! 58-----
ini.writeline "IconArea_Text=0x"&textSave                                       '--! 59-----
end if                                                                          '--! 60-----
ini.close                                                                       '--! 61-----
set iniChange=fs.getfile(path&"\Desktop.ini")                                   '--! 62-----
if iniChange.attributes and 4 then                                              '--! 63-----
else                                                                            '--! 64-----
iniChange.attributes =iniChange.attributes +4                                   '--! 65-----
end if                                                                          '--! 66-----
if iniChange.attributes and 2 then                                              '--! 67-----
else                                                                            '--! 68-----
iniChange.attributes =iniChange.attributes +2                                   '--! 69-----
end if                                                                          '--! 70-----
if changeFolder.attributes and 4 then                                           '--! 71-----
else                                                                            '--! 72-----
changeFolder.attributes =changeFolder.attributes+4                              '--! 73-----
end if                                                                          '--! 74-----

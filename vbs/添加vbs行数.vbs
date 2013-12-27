 vbsFile=inputbox("请输入要添加行数的文件")                                                '--! 2------
if vbsFile="" then                                                              '--! 3------
msgbox "你输入为空"                                                                  '--! 4------
wscript.quit                                                                    '--! 5------
end if                                                                          '--! 6------
Set Fsys=CreateObject("Scripting.FileSystemObject")                             '--! 7------
if Fsys.FileExists(vbsFile) <> true then                                        '--! 8------
msgbox "请确认这个是否存在!"                                                             '--! 9------
Fsys=nothing                                                                    '--! 10-----
wscript.quit                                                                    '--! 11-----
end if                                                                          '--! 12-----
set vf=Fsys.opentextfile(vbsfile,1)                                             '--! 13-----
set tmp=Fsys.CreatetextFile("tmp.txt",true)                                     '--! 14-----
dim i,txt,sl,ln                                                                 '--! 15-----
i=0                                                                             '--! 16-----
do while vf.atendofstream<>true                                                 '--! 17-----
i=i+1                                                                           '--! 18-----
txt = vf.readline                                                               '--! 19-----
                                                                                '--! 20-----
if left(right(txt,12),5) ="'--! "  then                                         '--! 21-----
txt=left(txt,len(txt)-12)                                                       '--! 22-----
                                                                                '--! 23-----
txt=rtrim(txt)				'更改bug防止误删空格 导致删除多余                                           '--! 24-----
                                                                                '--! 25-----
                                                                                '--! 26-----
end if                                                                          '--! 27-----
sl=len(txt) 'zi fu chuan  changdu  len                                          '--! 28-----
if sl>90 then                                                                   '--! 29-----
base=string(10," ")                                                             '--! 30-----
else                                                                            '--! 31-----
                                                                                '--! 32-----
bas=String(80-sl," ")                                                           '--! 33-----
end if                                                                          '--! 34-----
txt=txt&bas&"'--! "&i&String(7-len(cstr(i)),"-")                                '--! 35-----
tmp.writeline txt                                                               '--! 36-----
loop                                                                            '--! 37-----
vf.close                                                                        '--! 38-----
tmp.close '删除文件时 请先关掉这个文件使用这个函数 close()	释放文件句柄                                  '--! 39-----
fsys.deletefile(vbsFile)                                                        '--! 40-----
                                                                                '--! 41-----
set newVbsFile=Fsys.CreatetextFile(vbsFile,true)                                '--! 42-----
set readTmp=Fsys.opentextfile("tmp.txt",1)                                      '--! 43-----
do while readtmp.atendofstream<>true                                            '--! 44-----
tmptxt=readtmp.readline                                                         '--! 45-----
newVbsFile.writeline tmptxt                                                     '--! 46-----
loop                                                                            '--! 47-----
newVbsFile.close                                                                '--! 48-----
readTmp.close                                                                   '--! 49-----
Fsys.deletefile("tmp.txt")                                                      '--! 50-----
msgbox "已经添加行数注释,共有"&i&"行"                                                      '--! 51-----
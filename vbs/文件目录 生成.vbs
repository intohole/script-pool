dim FileName,fs,foldername
foldername = InputBox("请输入想要在哪个文件夹查找", "VBS查找文件")
If foldername = "" Then
wscript.quit
End If
Set fs = CreateObject("scripting.filesystemobject")
set savefile=fs.createtextfile("musicname.txt",True)
msgbox	"目录创建中..."
digui (foldername)'调用递归函数进行查找
msgbox "目录已生成..."
savefile.close

Set wmp = CreateObject("WMPlayer.OCX") 
set fs=nothing
Set Fsys=CreateObject("Scripting.FileSystemObject")
set fso=Fsys.opentextfile("musicname.txt",1)
do while fso.atendofstream<>true
txt = fso.readline
playMusic(txt)
loop

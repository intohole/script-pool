'下面是递归查找函数
Function digui(path)
Set folder = fs.getfolder(path)
Set subfolders = folder.subfolders
Set Files = folder.Files
For Each i In Files

if Right(i.name,3)="mp3" or	Right(i.name,3)="wma" then
savefile.WriteLine i.path
end if

‘FileName=FileName & i.name& vbNewLine '找到则追加到变量FileName中
Next
For Each j In subfolders
digui (j.path) '递归查找子目录
Next
End Function

function playMusic(path)
wmp.url = path
do until wmp.playstate = 1
wscript.sleep	1000
loop

end function
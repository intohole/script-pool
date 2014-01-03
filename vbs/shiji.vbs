dim sign                                                                        '--! 1------
sign=true                                                                       '--! 2------
set fs=CreateObject("Scripting.FileSystemObject")                               '--! 3------
do while sign                                                                   '--! 4------
choice=inputbox("1.查看所有记录		 "&vbNewLine&"2.增加记录"&vbNewLine&"3.删除制定的记录	"&vbnewline&"4. 更新记录"&vbnewline&"5.还原数据"&vbnewline&"6.清空数据"&vbnewline&"0. 离开")                                                                   '--! 5------
if choice ="" then
wscript.quit
end if
if choice =0  then                                              '--! 6------
sign =false                                                                     '--! 7------
elseif choice =1 then                                                           '--! 8------
                                                                                '--! 9------
		 LookAllSave()	                                                          '--! 10-----
	elseif choice = 2 then                                                         '--! 11-----
  		addSave()	                                                                  '--! 12-----
			                                                                             '--! 13-----
	elseif choice=3 then		                                                         '--! 14-----
		delSave()		                                                                   '--! 15-----
		
	elseif choice = 4 then                                                         '--! 16-----
   	 refreshSave()                                                              '--! 17-----
	
	elseif choice =5 then                                                          '--! 18-----
	changeSave()
	elseif choice =6 then	                                                                  '--! 19-----
	delall()
end if                                                                          '--! 20-----
                                                                                '--! 21-----
loop                                                                            '--! 22-----
                                                                                '--! 23-----
                                                                                '--! 24-----
                                                                                '--! 25-----
                                                                                '--! 26-----
function LookAllSave()                                                          '--! 27-----
                                                                                '--! 28-----
dim fileSign                                                                    '--! 29-----
if fs.fileexists("c:\saveHabit.txt") then                                          '--! 30-----
                                                                                '--! 31-----
else                                                                            '--! 32-----
                                                                                '--! 33-----
msgbox "还没有记录"                                                                  '--! 34-----
LookAllSave=false                                                               '--! 35-----
exit function                                                                   '--! 36-----
                                                                                '--! 37-----
end if                                                                          '--! 38-----
set file = fs.OpenTextFile("c:\saveHabit.txt",1,true)                              '--! 39-----
dim fileLine,save                                                               '--! 40-----
save=""                                                                         '--! 41-----
fileLine=1                                                                      '--! 42-----
do while file.AtEndOfStream<>true                                               '--! 43-----
txt=file.readline                                                               '--! 44-----
te=file.readline                                                                '--! 45-----
save = save &"第  "&fileLine&"  记录  :"&txt&RTimeDiff(te)                         '--! 46-----
fileline=fileline+1                                                             '--! 47-----
loop                                                                            '--! 48-----
 msgbox save                                                                    '--! 49-----
file.close()                                                                    '--! 50-----
LookAllSave = true                                                              '--! 51-----
end function                                                                    '--! 52-----
                                                                                '--! 53-----
                                                                                '--! 54-----
function RTimeDiff(OTime)                                                       '--! 55-----
dim msgTime                                                                     '--! 56-----
ss=dateDiff("s",OTime,Now)
msgS=ss mod 60
msgH=ss/360 mod 24                                             '--! 57-----
                                             '--! 58-----
msgM=ss/60 mod 60                                             '--! 59-----

msgTime = "		已过去的时间为   :"&dateDiff("d",OTime,Now)&"天  "&msgH&"  小时"&msgM&"  分"&msgS&"  秒"&vbnewline&vbnewline                                             '--! 60-----
RTimeDiff =msgTime                                                              '--! 61-----
end function                                                                    '--! 62-----
                                                                                '--! 63-----
                                                                                '--! 64-----
function addSave()                                                              '--! 65-----
                                                                                '--! 66-----
                                                                                '--! 67-----
add=inputbox("你要纪录的事情 :")                                                       '--! 68-----
if add = "" then                                                                '--! 69-----
else                                                                            '--! 70-----
saveall()
set file = fs.opentextfile("c:\saveHabit.txt",8,true)                              '--! 71-----
t=Now                                                                           '--! 72-----
                                                                                '--! 73-----
file.writeline add                                                              '--! 74-----
file.writeline t                                                                '--! 75-----
msgbox "已增加记录:"&add&"    "&t                                                    '--! 76-----
                                                                                '--! 77-----
file.close                                                                      '--! 78-----
end if                                                                          '--! 79-----
end function                                                                    '--! 80-----
                                                                                '--! 81-----
                                                                                '--! 82-----
                                                                                '--! 83-----
function delSave()                                                              '--! 84-----
msgbox "请记住你要删除的记录的序号"                                                          '--! 85-----
if LookAllSave() then                                                           '--! 86-----
dim numofSave                                                                   '--! 87-----
numOfSave = inputbox("请输入你想要删除的序号 (要数字的哦~!):")                                  '--! 88-----
if IsNumeric(numOfSave) then                                                    '--! 89-----
                                                                                '--! 90-----
set del =fs.opentextfile("c:\saveHabit.txt",1,false)                               '--! 91-----
set tmp = fs.createtextfile("86tmp.txt",true)                                   '--! 92-----
dim numOfLine                                                                   '--! 93-----
numOfline=1                                                                     '--! 94-----
do while del.AtEndOfStream<>true                                                '--! 95-----
if numOfLine = cInt(numOfSave) then                                             '--! 96-----
                                                                                '--! 97-----
	st=del.readline                                                                 '--! 98-----
	tt=del.readline                                                                 '--! 99-----
	msign=msgbox("已找到你要删除的选项为     :"&st,vbOKCancel)                                 '--! 100----
	if msign<>vbok then                                                             '--! 101----
                                                                                '--! 102----
	tmp.writeline st                                                                '--! 103----
	tmp.writeline tt                                                                '--! 104----
	msgbox "你放弃了操作!!!!"                                                             '--! 105----
	end if                                                                          '--! 106----
else                                                                            '--! 107----
	tmp.writeline del.readline                                                      '--! 108----
	tmp.writeline del.readline                                                      '--! 109----
end if                                                                          '--! 110----
numOfline=numOfline+1                                                           '--! 111----
                                                                                '--! 112----
loop                                                                            '--! 113----
del.close                                                                       '--! 114----
tmp.close                                                                       '--! 115----
saveall()
fs.deletefile("c:\saveHabit.txt")                                 '--! 116----

set del2 =fs.opentextfile("c:\saveHabit.txt",2,true)                                '--! 117----
set tmp2 = fs.opentextfile("86tmp.txt",1)                                        '--! 118----
                                                                                '--! 119----
do while tmp2.AtEndOfStream<>true                                                '--! 120----
del2.writeline tmp2.readline                                                      '--! 121----
loop                                                                            '--! 122----
del2.close                                                                       '--! 123----
tmp2.close                                                                       '--! 124----
fs.deletefile("86tmp.txt")                                                      '--! 125----
  else                                                                            '--! 126----
	msgbox "你输入的不是数字"                                                               '--! 127----
  end if                                                                          '--! 128----
                                                                                '--! 129----
	end if                                                                          '--! 130----
msgbox "删除成功!!!!!!!"                                                            '--! 131----
end function                                                                    '--! 132----
                                                                                '--! 133----
                                                                                '--! 134----
function refreshSave()                                                          '--! 135----                                                                                '--! 136----                              
msgbox "请记住你要更新的记录的序号"                                                          '--! 85-----
if LookAllSave() then                                                           '--! 86-----
dim numofSave                                                                   '--! 87-----
numOfSave = inputbox("请输入你想要更新的序号 (要数字的哦~!):")                                  '--! 88-----
if IsNumeric(numOfSave) then                                                    '--! 89-----
                                                                                '--! 90-----
set del =fs.opentextfile("c:\saveHabit.txt",1,false)                               '--! 91-----
set tmp = fs.createtextfile("86tmp.txt",true)                                   '--! 92-----
dim numOfLine                                                                   '--! 93-----
numOfline=1                                                                     '--! 94-----
do while del.AtEndOfStream<>true                                                '--! 95-----
if numOfLine = cInt(numOfSave) then                                             '--! 96-----
                                                                                '--! 97-----
	st=del.readline                                                                 '--! 98-----
	tt=del.readline                                                                 '--! 99-----
	msign=msgbox("已找到你要更新的选项为     :"&st,vbOKCancel)                                 '--! 100----
	if msign=vbok then                                                             '--! 101----
                                                                                '--! 102----
	tmp.writeline st                                                                '--! 103----
	tmp.writeline Now                                                                '--! 104----
	else	
	msgbox "你放弃了操作!!!!"                                                             '--! 105----
	end if                                                                          '--! 106----
else                                                                            '--! 107----
	tmp.writeline del.readline                                                      '--! 108----
	tmp.writeline del.readline                                                      '--! 109----
end if                                                                          '--! 110----
numOfline=numOfline+1                                                           '--! 111----
                                                                                '--! 112----
loop                                                                            '--! 113----
del.close                                                                       '--! 114----
tmp.close                                                                       '--! 115----
saveall()
fs.deletefile("c:\saveHabit.txt")                                 '--! 116----

set del1 =fs.opentextfile("c:\saveHabit.txt",2,true)                                '--! 117----
set tmp1 = fs.opentextfile("86tmp.txt",1)                                        '--! 118----
                                                                                '--! 119----
do while tmp1.AtEndOfStream<>true                                                '--! 120----
del1.writeline tmp1.readline                                                      '--! 121----
loop                                                                            '--! 122----
del1.close                                                                       '--! 123----
tmp1.close                                                                       '--! 124----
fs.deletefile("86tmp.txt")                                                      '--! 125----
  else                                                                            '--! 126----
	msgbox "你输入的不是数字"                                                               '--! 127----
  end if                                                                          '--! 128----
                                                                                '--! 129----
	end if                                                                          '--! 130----
msgbox "更新成功!!!!!!!"                                                            '--! 131----
end function                                                           '--! 186----
function changeSave()                                                           '--! 187----
if fs.FileExists("c:\saveHabit.txt") and fs.FileExists("c:\oldHabit.txt") then    '--! 188----
                                                                                '--! 189----
ss=msgbox("你确定你要从老的数据还原数据",vbokcancel)                                          '--! 190----
if	ss=vbok then                                                                 '--! 191----
fs.deletefile("c:\saveHabit.txt")                                                  '--! 192----
fs.movefile "c:\oldHabit.txt","c:\saveHabit.txt"                                  '--! 193----
saveall()
else                                                                            '--! 194----
msgbox "你放弃了操作!!!"                                                              '--! 195----
end if                                                                          '--! 196----
else                                                                            '--! 197----
msgbox "文件不存在 ，无法操作!"                                                           '--! 198----
end if                                                                          '--! 199----
end function                                                                    '--! 200----
function saveall()
set ofile = fs.createtextfile("c:\oldHabit.txt",true)
set nfile= fs.opentextfile("c:\saveHabit.txt",1,true)
do while nfile.AtEndOfStream<>true 
ofile.writeline nfile.readline
loop
end function
function delall()
if	fs.FileExists("c:\saveHabit.txt") then
fs.deletefile("c:\saveHabit.txt")
msgbox "已清空数据（如果清空错误,请使用功能5恢复数据）"
else
msgbox "没有数据可以清空!!!"
end if

end function
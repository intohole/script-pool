path1=inputbox("请输入路径:")                                                        '--! 1------
path2=inputbox("复制到的路径")                                                        '--! 2------
houzhui=inputbox("要复制的后缀(.txt...)")                                             '--! 3------
Set fs = CreateObject("scripting.filesystemobject")                             '--! 4------
                                                                                '--! 5------
findFile path1,houzhui                                                          '--! 6------
msgbox("完成对"&path1&"的"&houzui&"搜索!")                                                                                '--! 7------
function findFile(path,houzhui)                                                 '--! 8------
set folder=fs.getfolder(path)                                                   '--! 9------
set subfolder=folder.subfolders                                                 '--! 10-----
set file=folder.files                                                           '--! 11-----
                                                                                '--! 12-----
for Each i In file                                                              '--! 13-----
if right(i.name,3)=houzhui then                                                 '--! 14-----
fs.copyfile i,path2                                                             '--! 15-----
                                                                      '--! 16-----
fs.deletefile i
end if                                                                          '--! 17-----
                                                                                '--! 18-----
                                                                                '--! 19-----
next                                                                            '--! 20-----
for Each j In subfolder                                                         '--! 21-----
findFile j.path,houzhui                                                                 '--! 22-----
next                                                                            '--! 23-----
                                                                                '--! 24-----
                                                                                '--! 25-----
                                                                                '--! 26-----
end function                                                                    '--! 27-----

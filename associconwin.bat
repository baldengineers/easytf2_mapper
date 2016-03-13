set ftypename=Easy TF2 Mapper Save
set extension=.ezm
set pathtoexe="EasyTF2Mapper.exe"
set pathtoicon="icons/icon.ico"

if %pathtoicon%=="" set pathtoicon=%pathtoexe%,0
REG ADD HKEY_CLASSES_ROOT\%extension%\ /t REG_SZ /d %ftypename% /f
REG ADD HKLM\SOFTWARE\Classes\%ftypename%\DefaultIcon\ /t REG_SZ /d %pathtoicon% /f
ftype %ftypename%=%pathtoexe% "%%1" %%*
assoc %extension%=%ftypename%

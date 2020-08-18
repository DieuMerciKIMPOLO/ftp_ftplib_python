from ftplib import FTP
server = FTP('ftp.org')
server.login('username','password')
server.pwd()
server.cwd("mes_test")
with open('data.xlsx', 'wb') as fp:
    server.retrbinary('RETR data.xlsx', fp.write)
server.quit()

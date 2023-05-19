from datetime import datetime as dt
import time 

hosts_temp = "hosts"                                         #copy of the original hosts file stored in same dir as the python script
hosts_fp = r"C:\Windows\System32\drivers\etc\hosts"              #r for 1 row string, since python may identify \n as newline
hosts_ip = "127.0.0.1"

#removing porn addiction
websites = ["noodlemagazine.com", "www.noodlemagazine.com", "xhamsterlive.com", "wwww.xhamsterlive.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("working hours...")
        with open(hosts_fp, 'r+') as file:             #r+ for read plus write(append, not overwrite)
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(hosts_ip+" "+ website+"\n")

    else:
        print("Non working hours...")
        with open(hosts_fp, 'r+') as file:
            content = file.readlines()          #content is list with string elements, each string is 1 line of the file
            file.seek(0)                        #seek to 0 position to overwrite
            for line in content:
                if not any(website in line for website in websites):                #if any of the website names not present in the line
                    file.write(line)                                                #writing lines not containing website names
            file.truncate()                     #deleting everything below the last line
    time.sleep(10)
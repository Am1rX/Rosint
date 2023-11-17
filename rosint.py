import requests , re , time
import logging
from tqdm import tqdm
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import bs4
from itertools import cycle
timeout = 12
def ip():
    ip = input("[Info IP] IP => ")
    headers = {
        'Host': 'www.infobyip.com',
        'Content-Length': '38',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Origin': 'https://www.infobyip.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.infobyip.com/ipwhois-185.192.112.81.html',
        'Accept-Language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7,ru-RU;q=0.6,ru;q=0.5,pt;q=0.4',
        'Dnt': '1',
        'Sec-Gpc': '1',
    }
    cookies = {
        '_ga': 'GA1.1.1191056851.1699119863',
        'w3ad': '0',
        'w3ad1length': '0',
        '_ga_FEQ5C4GK3T': 'GS1.1.1169519862.1.1.1699120188.60.0.0',
    }
    data = {
        'ip': ip,
        'tool': 'ipwhois',
        '_p1': '2100',
    }
    response = requests.post(
        'https://www.infobyip.com/ipwhois-185.192.112.81.html',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=True,
    )
    url = "https://www.infobyip.com/ipwhois-185.192.112.81.html"
    request = requests.post(url, headers=headers, data=data)
    render = bs4.BeautifulSoup(request.content,'lxml')
    regex = re.findall(r'(inetnum.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n)',str(render))
    regex = re.split('\n',regex[0])
    print('\n')
    for i in regex:
        print('[+] ',i)

def whois():
    try:
        web = input("example : google.com\n[Info Domain] Domain => ")
        cookies = {
            'ncmp.domain': 'nslookup.io',
            'cto_bundle': 'm1n8Il84QVhPaTMxMGJXTnJXVndMeFAlMkJ4aW44alglMkJLZ4x3dnpaWTZNRlRJZXdOb1M5TmtJJTJGMUtXNEVaOTl1Mlpha2g1a2ZrM7YyM2trNTl3OXhid1R1JTJCcVdrMFcyVTZieTdFaG1VMHJ4JTJCZVJ2aXNyTTA0U2Q4VHNMTzclMkZKcyUyRnRkR3QlMkJ0OEhMbHdISVolMkZOVloycHY4VThtb2clM0QlM0Q',
            'na-unifiedid': '%7B%22TDID%22%3A%22d67c432f-512d-41c9-bb71-a67996280197%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%282023-10-09T10%3A55%3A49%22%7D',
            'na-unifiedid_cst': 'TyylLI8srA%3D%3D',
        }

        headers = {
            'Host': 'www.nslookup.io',
            'Content-Length': '45',
            'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.105 Safari/537.36',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Origin': 'https://www.nslookup.io',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.nslookup.io/domains/spgc.ir/dns-records/',
            'Accept-Language': 'en-US,en;q=0.9',
            'Priority': 'u=1, i',
            'Cookie': 'ncmp.domain=nslookup.io; cto_bundle=m6n8Il81QVhPaTMxMGJXTnJXVndMeFAlMkJ3aW64alglMkJLZ2x9dnpaWTZNRlRJZXdOb1M5TmtJJTJGMUtXNEVaOTl1Mlpha2g1a2ZrM2YyM2trNTl3OXhid1R1JTJCcVdrMFcyVTZieTdFaG1VMHJ4JTJCZVJ2aXNyTTA0U2Q4VHNMTzclMkZKcyUyRnRkR3QlMkJ0OEhMbHdISVolMkZOVloycHY4VThtb2clM0QlM0Q; na-unifiedid=%7B%22TDID%22%3A%22d67c432f-512d-41c9-bb71-a67096280197%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-10-09T10%3A55%3A49%22%7D; na-unifiedid_cst=TyylLI8srA%3D%3D',
        }

        json_data = {
            'domain': web,
            'dnsServer': 'cloudflare',
        }

        response = requests.post('https://www.nslookup.io/api/v1/records', cookies=cookies, headers=headers, json=json_data, verify=True)
        render = bs4.BeautifulSoup(response.content,'lxml')
        render = re.findall(r'(.raw.*?false)',str(render))
        render = re.split(',',str(render))
        print('\n')
        render0 = render[0]
        print("[+] IP -> ", render0[9:-1])
        render1 = render[1]
        print("[+] Domain -> ", render1[8:-2])
        render7 = render[7]
        print("[+] Country -> ", render7[11:-1])
        render8 = render[8]
        print("[+] Region -> ", render8[14:-1])
        render9 = render[9]
        print("[+] City -> ", render9[8:-1])
        render12 = render[12]
        print("[+] Company -> ", render12[7:-1])
        render13 = render[13]
        print("[+] AS -> ", render13[6:-1])
        render14 = render[14]
        print("[+] AS Name -> ", render14[10:-1])
        render15 = render[15]
        print("[+] AS Domain -> ", render15[12:-1])
        render37 = render[-37]
        print("[+] MX -> ", render37[10:-3])
        render19 = render[-19].replace('\\','')
        print("[+] Admin -> ", render19[9:-2])
        render20 = render[-20]
        print("[+] NS -> ", render20[8:-2])
    except:
        print("sorry i dont found anything ! ")
def socialfinder():

    id = input("[Social Finder] ID => ")

    headers = {
        'Host': 'github.com',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=0, i',
        'Connection': 'close',
    }
    try:
        response = requests.get('https://github.com/'+id, headers=headers, verify=True)
    except:
        print("Check your Connection.")
    if response.status_code == 200:
        print("[+] Github Detected : github.com/"+id)
    else:
        None
    headers = {
    'Host': 'www.instagram.com',
    'Dpr': '1.25',
    'Viewport-Width': '1038',
    'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '""',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i',
    }
    try:
        response = requests.get('https://www.instagram.com/'+id,headers=headers, verify=True)
        response = bs4.BeautifulSoup(response.content,"lxml")
        response = re.findall(r"<title>(.*)<",str(response))
    except:
        print("Check Your Connection.")

    if response[0] == "Instagram":
        None
    else:
        print("[+] Instagram Detected : instagram.com/"+id)
    
    headers = {
    'Host': 'www.reddit.com',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i',
    }
    check = []
    try:
        response = requests.get('https://www.reddit.com/user/'+id, headers=headers, verify=True)
        response = bs4.BeautifulSoup(response.content,'lxml')
        response = re.findall(r"(shreddit-forbidden not_found)",str(response))
        response.append("hi")
    except:
        print("Check Your Connection.")
    try:
        if response[0] == 'hi':
            print("[+] Reddit Detected : reddit.com/user/"+id)
    except:
        None
    
    headers = {
    'Host': 'steamcommunity.com',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i',
    'Connection': 'close',
    }
    response = ''
    try:
        response = requests.get('https://steamcommunity.com/id/'+id, headers=headers, verify=True)
        response = bs4.BeautifulSoup(response.content,'lxml')
        response = re.findall(r"(webui_config)",str(response))
    except:
        print("Check your Connection.")
    try:
        if response[0] == 'webui_config':
            print("[+] Steam Detected : steamcommunity.com/id/"+id)
    except:
        None
    
    headers = {
    'Host': 't.me',
    'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i',
    }
    response = ''
    try:
        response = requests.get('https://t.me/'+id, headers=headers, verify=True)
        response = bs4.BeautifulSoup(response.content,'lxml')
        response = re.findall(r"(tgme_page_title)",str(response))
    except:
        print("Check your Connection.")
    try:
        if response[0] == "tgme_page_title":
            print("[+] Telegram Detected : t.me/"+id)
    except:
        None

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
    # test : http://www.sudo.co.il/xss/level0.php?email=

    logging.getLogger('selenium.webdriver').disabled = True

    # Set Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # List of XSS payloads
    payloads = ['"autofocus%2Fonfocus%3D"confirm%26%2340%3Bdocument.domain%26%2341%3B#',"\\'-alert(1);//",'<script>alert(1)</script>','" autofocus="" onfocus="alert(1)','<img src="javascript:alert(1)">','<svg onload="alert(1)"></svg>','<iframe src="javascript:alert(1)"></iframe>','<a href="javascript:alert(1)">Click me</a>','#<script>alert(1)</script>',"';this[8680439..toString(30)](1);'","'};this[8680439..toString(30)](1);{'",'"};this[8680439..toString(30)](1);//','" autofocus="" onfocus="alert(1)',"\\'-alert(1);<!--","'-alert(1)-'",'"autofocus/onfocus="confirm&#40;1&#41;','"autofocus/onfocus="alert(1)','\\"-alert(1)}//',"<b onmouseover=alert(1)>click me</b>","{{{constructor.constructor(1)()}}}",'<video><source onerror="alert(1)"></video>','<style/onload=alert(1)>']

    def has_alert(url):
        driver = webdriver.chrome(service=chromeService(ChromeDriverManager().install()),option=chrome_options)
        driver.get(url)

        try:
            alert = Alert(driver)
            alert.accept()
            return True
        except:
            return False
        finally:
            driver.quit()

    def perform_xss_checks(url):
        print("Performing XSS checks on:", url, "\n")
        vulnerabilities = []

        for payload in payloads:
            url_with_payload = url + payload
            if has_alert(url_with_payload):
                vulnerabilities.append((url_with_payload, payload))

        print("\n[X] XSS vulnerabilities found:\n")
        if vulnerabilities:
            for vuln_url, vuln_payload in vulnerabilities:
                print("URL:", vuln_url)
                print("Payload:", vuln_payload)
                print("-" * 50)
        else:
            print("No XSS vulnerabilities detected.")

    # Prompt the user to enter the target URL for XSS checks
    target_url = input("Enter the URL for XSS checks: ")
    perform_xss_checks(target_url)


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
    links.append(base_url + "/webservice/")
    links.append(base_url + "/pix/")
    links.append(base_url + "/backup/")
    links.append(base_url + "/Content/")

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
        .-{   }   }-.          [3] Username list Maker
       ( ( } { } { } )         [4] Info Username
       |`-.._____..-'|      [*] Web Hacking
       |             ;--.     [5] XSS (url base)
       |   (__)     (__  \\   [6] Directory Listing Finder
       |   (oo)      | )  )  [0] Exit
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

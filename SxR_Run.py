import os,sys,time

logo ="""\033[1;37m            
\t   .d8888.  db    db  d8888b. 
\t   88'  YP  `8b  d8'  88  `8D 
\t   `8bo.     `8bd8'   88oobY' 
\t     `Y8b.   .dPYb.   88`8b   
\t   db   8D  .8P  Y8.  88 `88. 
\t   `8888Y'  YP    YP  88   YD 

\033[1;97m══════════════════════════════════════════════════
 \033[1;97m[\033[1;92m✔\033[1;97m]OWNER          \033[1;91m: \033[1;96m SIFAT & RAJ
 \033[1;97m[\033[1;92m✔\033[1;97m]TOOL           \033[1;91m: \033[1;97m RANDOM CLONEING
 \033[1;97m[\033[1;92m✔\033[1;97m]STATUS         \033[1;91m: \033[1;97m FREE
 \033[1;97m[\033[1;92m✔\033[1;97m]NETWORK        \033[1;31m:  \033[1;97m3G\033[97;1m,4G,5G
 \033[1;97m[\033[1;92m✔\033[1;97m]VERSION        \033[1;91m:  \033[38;5;208m1.0.1\033[1;97m
\033[1;97m══════════════════════════════════════════════════"""

def linex():
	print("\x1b[91m══════════════════════════════════════════════════")

def Main():
	os.system("clear")
	print(logo)
	print(" \033[1;97m[\033[1;92m01\033[1;97m] Use Method To \033[1;92m[m.fb]")
	print(" \033[1;97m[\033[1;92m02\033[1;97m] Use Method To \033[1;92m[mbasic.fb]")
	print(" \033[1;97m[\033[1;92m03\033[1;97m] Use Method To \033[1;92m[m.alpha.fb]")
	print(" \033[1;97m[\033[1;92m04\033[1;97m] Use Method To \033[1;92m[x.fb]")
	print(" \033[1;97m[\033[1;92m05\033[1;97m] Use Method To \033[1;92m[free.fb]")
	print(" \033[1;97m[\033[1;92m06\033[1;97m] Use Method To \033[1;92m[web.fb]")
	print(" \033[1;97m[\033[1;92m07\033[1;97m] Use Method To \033[1;92m[www.fb]")
	print(" \033[1;97m[\033[1;92m08\033[1;97m] Use Method To \033[1;92m[p.fb]")
	print(" \033[1;97m[\033[1;92m09\033[1;97m] Use Method To \033[1;92m[t.fb]")
	print(" \033[1;97m[\033[1;92m10\033[1;97m] Use Method To \033[1;92m[n.fb]")
	print(" \033[1;97m[\033[1;92m11\033[1;97m] Use Method To \033[1;92m[d.fb]")
	print(" \033[1;97m[\033[1;92m12\033[1;97m] Use Method To \033[1;92m[fire.fb]")
	print(" \033[1;97m[\033[1;92m13\033[1;97m] Use Method To \033[1;92m[fr-fr.fb]")
	linex()
	me = input(" \033[1;97m[\033[1;92m1\033[1;97m] Choice Your Method : \033[1;92m")
	if me in ["1", "A", " 01"]:
		os.system("python SXR_M.py")
	elif me in ["2", "B", " 02"]:
		os.system("python SXR_MBASIC.py")
	elif me in ["3", "C", " 03"]:
		os.system("python SXR_M_ALPHA.py")
	elif me in ["4", "D", " 04"]:
		os.system("python SXR_X.py")
	elif me in ["5", "E", " 05"]:
		os.system("python SXR_FREE.py")
	elif me in ["6", "F", " 06"]:
		os.system("python SXR_WEB.py")
	elif me in ["7", "G", " 07"]:
		os.system("python SXR_WWW.py")
	elif me in ["8", "H", " 08"]:
		os.system("python SXR_P.py")
	elif me in ["9", "I", " 09"]:
		os.system("python SXR_T.py")
	elif me in ["10", "J", " 010"]:
		os.system("python SXR_N.py")
	elif me in ["11", "K", " 011"]:
		os.system("python SXR_D.py")
	elif me in ["12", "L", " 012"]:
		os.system("python SXR_FIRE.py")
	elif me in ["13", "M", " 013"]:
		os.system("python SXR_FR_FR.py")
	else:
		print("")
		time.sleep(1)
		Main()
		

Main()
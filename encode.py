from os import listdir,system,listdir,rename,remove
r1 = "\x1b[31;1"
r2 = "\x1b[32;1"
r3 = "\x1b[33;1"
r4 = "\x1b[34;1"
r5 = "\x1b[35;1"
r6 = "\x1b[36;1"
o = "\x1b[0m"
def encode (en="en"):
    global r1,r2,r3,r4,r5,r6
    if en != "en":print ("\x1b[33;1m─╔╗─────────╔╦╗╔═╗╔╗─");print ("╔╝║╔═╗╔═╗╔╦╗║║║║╬║║╚╗");print ("║╬║║╩╣║═╣║╔╝╠╗║║╔╝║╔╣");print ("╚═╝╚═╝╚═╝╚╝─╚═╝╚╝─╚═╝"+o);r1 = "\x1b[31;1";r2 = "\x1b[36;1";r3 = "\x1b[32;1";r4 = "\x1b[35;1";r5 = "\x1b[34;1";r6 = "\x1b[33;1"
    else:print ("\x1b[32;1m─────────────╔╦╗╔═╗╔╗─");print ("╔═╗╔═╦╗╔═╗╔╦╗║║║║╬║║╚╗");print ("║╩╣║║║║║═╣║╔╝╠╗║║╔╝║╔╣");print ("╚═╝╚╩═╝╚═╝╚╝─╚═╝╚╝─╚═╝"+o)       
    try:
        bb = [ff for ff in listdir () if ff.endswith ("sh")];print ("\x1b[36;4;3mdaftar file bash"+o+"\n"+r6+"m"+"="*(30))
        for io in range (len (bb)):
            if io < 9:print (r1+"m["+r2+"m0"+str (io+1)+r1+"m] "+r6+"m"+bb [io])
            else:print (r1+"m["+r2+"m"+str (io+1)+r1+"m] "+r6+"m"+bb [io])
        if len (bb) == 0:print (r1+";3mtidak ada file bash\nsilahkan tambahkan dulu"+o);print (r6+"m"+"="*(30)+o)
        while True:
            try:
                fil = str (input (r3+";7mpilih file :"+o+r1+"m "))
                if fil.isnumeric ():
                    try:
                        if int (fil) < 1:print ("\t"+r1+";7mpilih nomor yang tersedia"+o);continue
                        aa = open (bb [int (fil)-1],"r");fil = bb [int (fil)-1]
                    except (IndexError):print ("\t"+r1+";7mpilih nomor yang tersedia"+o);continue
                else:aa = open (fil,"r")
            except (KeyboardInterrupt,EOFError):print ();exit (r2+";4mithanks gan"+o)
            except (FileNotFoundError):print ("\t"+r1+";7mfile tidak ditemukan"+o);continue
            else:break
        print ("\n"+r2+"m██➣"+r6+"m"+fil+"\n");ful = str (input (r3+";7moutput file :"+o+r2+"m "));print ("\n\n"+r6+"mwait . . .",end=o)
        try:
            cb = ""
            if ful in listdir ():
                print (r1+";4m\rfile "+o+r3+"m"+ful+r1+";4m sudah ada!!"+o+"\n"+r1+";4mingin melanjutkan?"+o+" \x1b[43;1m[\x1b[46;1my/n\x1b[43;1m]"+o);
                try:
                    pil = str (input (r2+";7m>>>>> :"+o+r3+"m ")).lower ()
                    if pil.startswith ("n"):exit (r2+";3mthanks gan"+o)
                    else:print ("\n\n"+r6+"mwait . . .",end=o);bh = open (ful,"r");cb = bh.read ();bh.close()
                except (KeyboardInterrupt,EOFError):
                    exit (r2+"m\nthanks gan"+o)
            else:pass
            if en == "en":system ("bash-obfuscate "+fil+" -o "+ful)
            else:
                asu = open (fil,"r");bq = asu.read ();bou = bq.replace ("eval","echo");asu.close ()
                with open (ful,"w") as aa:
                    aa.write (bou)
                system ("bash "+ful+" > xzxz.sh");rename ("xzxz.sh",ful)
        except (KeyboardInterrupt,EOFError):exit ("\n"+r2+"mthanks gan"+o)
        try:
            bj = open (ful,"r")
        except (FileNotFoundError):exit ("\n"+r1+";7mencrypt file "+fil+" gagal cuk! :( 2"+o)
        bd = bj.read ();bj.close ()
        if len (bd) > 0:
            if bd == cb:exit ("\n"+r1+";7mencrypt file "+fil+" gagal cuk! :(1"+o)
            else:exit ("\n"+r2+";7mdone . . ."+o)
        else:print ("\n"+r1+";7mencrypt file "+fil+" gagal cuk! :( 3"+o)
    except (KeyboardInterrupt,EOFError):exit ("\n"+r2+"mthanks gan"+o)
def install ():
    if "bash-obfuscate" in listdir ("/data/data/com.termux/files/usr/bin/"):encode ()
    else:print (r3+";7minstall package cuk"+o);system ("pkg install nodejs -y");print (r3+";7msabar ya cuk"+o);system ("npm install -g bash-obfuscate");system ("python encode.py")
ss = ""
while True:
    system ("clear");print ("\n");print ('\x1b[32;1m █▀▄ ▄▀▄ ▄▀▀ █░░\n █▀█ █▀█ ░▀▄ █▀▄\n ▀▀░ ▀░▀ ▀▀░ ▀░▀\n ▄▀▄ █▀▄ █▀ █░█ ▄▀▀ ▄▀ ▄▀▄ ▀█▀ █▀▀\n █░█ █▀█ █▀ █░█ ░▀▄ █░ █▀█ ░█░ █▀▀\n ░▀░ ▀▀░ ▀░ ░▀░ ▀▀░ ░▀ ▀░▀ ░▀░ ▀▀▀\x1b[0m\x1b[36;1m\n==============================\x1b[0m\x1b[35;1m\n# \x1b[33;1mauthor   : \x1b[32;1mgumball watterson\x1b[35;1m\n# \x1b[33;1mcountry  : \x1b[32;1mindonesia\x1b[35;1m\n# \x1b[33;1mreligion : \x1b[32;1mislam\x1b[0m\n\x1b[36;1m==============================\x1b[0m');print (ss);print (r4+"m ["+r3+"m01"+r4+"m] "+r6+"mEncrypt "+r4+"m ["+r3+"m02"+r4+"m] "+r6+"mDecrypt"+o+"\n")
    try:
        pil = int (input (r4+";7mchoose :"+o+r2+"m "))
    except (KeyboardInterrupt,EOFError):exit ("\n"+r2+"mthanks gan"+o)
    except (ValueError):ss = "\t"+r1+";7mmasukan nomor cuk"+o;continue
    if pil == 1:exit (encode ())
    elif pil == 2:exit (encode ("sasu"))
    else:ss = "\t"+r1+";7mpilih nomor yang tersedia cuk :v"+o;continue


    


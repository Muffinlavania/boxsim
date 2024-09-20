from pixelart import *
from box2 import *
import time,random,sys,os,json
reset='\033[0m'
r=reset
bold='\033[01m'
yes=['y','ye','sure','yes','ok'] #ok

print('\033[?25l') #hides the cursor [without cursor module ez]

spedrunn=False #for skipping most wait times

def slepy(amo):
  time.sleep(amo if not (spedrunn or tspedrunn) else amo/2 if not tspedrunn else amo/4)

def c():
  print(reset) #yes
  os.system('clear')

c()

def anykey():
  return input('\n[Enter to continue]') #return just in case lol
def printt2(thing1,thing2,thecenter,dela=.04): #huge thing literally just for monke text (i want to practice lol)
  cuzyousuck=-1
  thingy=len(thing1) 
  center1=round(thecenter-len(thing1)//2)
  center2=round(thecenter-len(thing2)//2)
  if len(thing2)>len(thing1):
    thingy=len(thing2)
  number1=center2-center1#the amount it needs to go left and right from 1st to 2nd
  number2=center1-center2#the opposite 
  dir1='\x1b[1C'
  dir2='\x1b[1C'
  if number1<0:
    number1=abs(number1)
    dir1='\x1b[1D'
  if number2<0:
    number2=abs(number2)
    dir2='\x1b[1D'
  print(' '*(center1+len(thing1)),end='')
  for i in range(len(thing1)):
    sys.stdout.write('\x1b[1D')
  sys.stdout.write('\x1b[1B')
  print(' '*(center2+len(thing2)),end='')
  for i in range(len(thing2)):
    sys.stdout.write('\x1b[1D')
  sys.stdout.write('\x1b[1A')
  for i in range(number2):
    sys.stdout.write(dir2)
  ive1=False
  ive2=False
  for i in range(thingy):
    cuzyousuck+=1
    try:
      sys.stdout.write(thing1[cuzyousuck])
    except:
      if not ive1:
        ive1=True
        number1+=1
    sys.stdout.flush()
    sys.stdout.write('\x1b[1B')
    for i in range(number1-1):
      sys.stdout.write(dir1)
    sys.stdout.flush()
    try:
      sys.stdout.write(thing2[cuzyousuck])
    except:
      if not ive2:
        ive2=True
        number2-=1
    sys.stdout.flush()
    sys.stdout.write('\x1b[1A')
    for i in range(number2):
      sys.stdout.write(dir2)
    sys.stdout.flush()
    if not tspedrunn:
      time.sleep(dela)
  print('\n')
thealphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')']
#no im not dumb its because theres so many boxes we need to use letters instead of numbers lol (DUDE THERES SO MANY I HAVE TO USE NUMBERS AND SYMBOLS TOO)
def printt(thingggg,dela=.04):
  for i in thingggg:
    sys.stdout.write(i)
    sys.stdout.flush()
    if not tspedrunn:
      time.sleep(dela if not spedrunn else dela/2)
  print()


def rebirthdict(num):
  return num**10+100000

boxestiers={} #Contains the tiers of each box
for i in boxes.keys():
  for i2 in boxes[i]:
    boxestiers[i2]=i


inventory=[]

money=0
currentmulti=1 #the current multiplier, when i add multis it will change

def mult(num):
  return round(num*currentmulti)

rebirths=0
rebirthamo=10000
maxdollarhit=0
#To add a box: Put box in boxlist, boxcolors, boxes, boxdesc
#Foraging, if maxmoney > the amount for each then it goes to the next tier of spawns
#Gotta actually make the drops lol/ what you find

boxlist=['Among Box','Poo Box','Box Box','Common Box','Sugnoma Box','Bozo Box','n Box','Apple Box','Funny Box','Balanced Box','Robo Box','Money Box','Halloween Box','Buffed Box','Oof Box','Bean Box','Python Box','Gold Box','Gamblers Box','Basic Box','/e free Box','Xina Box','#1 Box','Diamond Box','Chaotic Box','andi Box','Gamer Box','Aimbot Box','Pepe Box','True Box','THE Box','Lank Box','e','Rouxs Box','w Box'] 

bcolor={} #Foreground color for the box text
for i in boxlist:
  if i!='n Box':
    bcolor[i]='\033'+boxcolors[i][0][1:2]+'38'+boxcolors[i][0][4:len(boxcolors[i][0])]
  else:
    bcolor[i]=' '

spawns={
  10:['Among Box','Poo Box','Box Box','Common Box','Among Box','Among Box'],
  100:['Box Box','Common Box','Common Box','Sugnoma Box','n Box','Among Box'],
  250:['Common Box','Bozo Box','n Box'],
  500:['Common Box','n Box','Funny Box','Apple Box','Apple Box','Robo Box','Halloween Box'],
  2500:['Oof Box','Apple Box','Robo Box','Money Box','Buffed Box','Money Box'],
  10000:['Bean Box','Python Box','Oof Box','Gold Box','Money Box','/e free Box','/e free Box','w Box'],
  100000:['/e free Box','Gamblers Box','Xina Box','/e free Box','Python Box','/e free Box','w Box'],
  500000:['Xina Box','#1 Box','Diamond Box','Chaotic Box','Gamer Box','True Box','Pepe Box','Diamond Box','Chaotic Box','andi Box'],
  1000000:['Diamond Box','Gamer Box','Aimbot Box','Gamer Box','Aimbot Box','Pepe Box','True Box','e','True Box','Rouxs Box','Diamond Box','andi Box'],
  2000000:['True Box','THE Box','Rouxs Box','True Box','Pepe Box','e','Aimbot Box'],
  3000000:['THE Box','Lank Box','e','Gamer Box','True Box','e','Gamer Box'],
  5000000:['THE Box','Lank Box','e','True Box','Pepe Box'],
  7500000:['THE Box','Lank Box','e','True Box'],
  10000000:['THE Box','Lank Box','e'],
  15000000:['e']
}

def printout(r3):
  if type(r3)==int:
    thinggot2=''
    o=0
    jjj=len(str(r3))%3
    ting=[]
    for i in range(10):
      ting.append(jjj+1+(3*i))
    for i in str(r3):
      o+=1
      if o!=1 and o in ting:
        thinggot2+=','
      thinggot2+=str(i)
    return thinggot2
  else:
    return r3
def properspace(thing,center=40,sub=''): #return propering centering (for both sides, goes string to center then amount of space to center in, string to be deleted from len)
  numb=(center-len(thing)+len(sub))/2
  numb22=0
  if type(numb)!=int and '.0' not in str(numb):
    numb22=1
  numb=int(numb)
  return [numb,numb22] #returns spacing, and then 1 if its odd
def sellbuy(stri,stri2): #string, anything to offset in the centering thing (color codes mainly)
  numb=properspace(stri,40,stri2)
  print('\n\n┌────────────────────────────────────────┐\n│                                        │\n│'+' '*numb[0]+stri+' '*(numb[0]+numb[1])+'│\n│                                        │\n└────────────────────────────────────────┘')
  input('\n          [Enter to continue]')
def descbox(boxo,p=True):
  global inventory,money
  print('Current Box:'+bcolor[boxo]+boxo+reset+' '*30+' Tier: '+tiercolors[boxestiers[boxo]][0]+boxestiers[boxo]+reset)
  printbox(boxo)
  thingiex='Sells for: '+printout(boxprices[boxo][0])
  numbi2=round((58-len(thingiex))/2)
  numbi=round((58-len(boxdesc[boxo]))/2)
  if numbi<=0:
    numbi=0
  print('\n\n'+' '*numbi+bold+boxdesc[boxo])
  print(' '*numbi2+thingiex+reset)
  if p:
    print(bold+'\n1) Open this box\n2) Sell this box'+reset)
    eric_blair=input('\033[38;5;82m>\033[0m ') #gorge orwel name reveal!!!!
  else:
    eric_blair=''
  if eric_blair=='1':
    openbox(boxo)
  elif eric_blair=='2':
    string3='Sold'+bcolor[boxo]+boxo+reset+' for '+printout(mult(boxprices[boxo][0]))+' coins' #idk why i did this but ok
    inventory.remove(boxo)
    money+=mult(boxprices[boxo][0])
    c()
    sellbuy(string3,bcolor[boxo]+reset)
hasbribed=False
def rebirth():
  global hasbribed,rebirthamo,currentmulti,rebirths,money,inventory,maxdollarhit
  if not hasbribed and rebirths<2:
    hasbribed=True
    c()
    printt('You walk over to the jungle to start your journey...')
    slepy(2)
    printt("Soon you find \033[38;5;166mThe Temple of the Monke\033[0m")
    slepy(2)
    printt("After climbing \033[38;5;166mThe Stairs of Monke\033[0m, you find yourself face to face with him.")
    slepy(3)
    c()
    printt2('OOEEEEEEO Eeea Ooae AAAACOooooooEAMo nOOOOOmBEA','[what are you doing in my swamp]',30,.04)
    slepy(2)
    c()
    printt2('eeEEwnnnnnnnnnnnnomEEEEOOB   AEAEAEAE OEOEOEOEOEO EEEEEEEEEEEEEEEE AAAAAAAAAAA','[your one of those humen right]',40,.04)
    slepy(2)
    c()
    printt2('TEEEEEEeeeGUUUUUUUUU  SSSSSSta aAAAEEEEEEEElAMMM OOOOOnnnnGGGGGGGuusS','[in what action is dog the taking a part in?]',30)
    slepy(2)
    c()
    printt("You tell the monke about your dreams of becoming the true unboxer.\n")
    slepy(2)
    printt2('OOOOOmUUUUUUUy deeeeeeeee EEEEeeeeeeeeeEE EAthHHHHHH','[when die get multiplier]',30)
    slepy(3)
    c()
    printt2('monkEeeeeeeeeeeeeeeeeeE EsEEEEEEEEE eEE dOOOOOOOoOOO','[monke cant help tho gg ez]',30)
    slepy(3)
    c()
    printt("It seems like the monke really likes money though...\n(he never said no bribes)")
    input('[Enter to continue]')
    c()
  print('\033[38;5;166mmonke\033[0m wont reincarnate you for nothing... (Everything has a price)\n\n')
  if money>=rebirthamo:
    print(bold+'Rebirth for '+printout(rebirthamo)+'?'+reset+'\n\n\nYour money: \033[38;5;40m'+printout(money)+"\033[0m")
  else:
    print("monke will only take",printout(rebirthamo),"or higher....")
  wannago=input('\033[38;5;82m>\033[0m ').lower()
  if wannago in yes:
    if money>=rebirthamo:
      printt("You give \033[38;5;166mmonke\033[0m a little pocket change...")
      slepy(2)
      if rebirths==0:
        printt("A few seconds later monke puts you in his big coconut looking thing")
        slepy(2)
      c()
      printt2('OOOODENOKEEEEE EEEE DiiiiiiiiiiiiEEEEEEEE','[monke make you oof]',30,.04)
      slepy(2)
      if rebirths==0:
        printt("\nYou realize that you will lose all your money..."+reset+'\nYou ask mr monke to hold it for when you come back')
        time.sleep(2)
        c()
        printt2("LoOOOOOOOOOloOOOOO iiiiiiIIIIIImamamamama KeeEEEEEEEppPP",'[sure 100% wont steal trust]',30,.04)
        slepy(2)
      c()
      printt("You wake up, feeling a little richer.")
      slepy(1)
      rebirths+=1
      money=0
      maxdollarhit=0
      currentmulti=2**rebirths
      printt("(Your multiplier increases to x"+str(currentmulti)+'!)',.1)
      slepy(1)
      try:
        rebirthamo=rebirthdict(rebirths)
      except:
        printt("[You've rebirthed so much at this point monke cant give you more power.... (but he still devious licked your wallet)]")
        input('[Enter to continue...]')
      slepy(2)
      c()
      inventory=[]
shopreset=time.time()
shopdict={'SUS':4,'Noob':3,'Ok':3,'Gud':3,'Epic':3,'Pro':2,'Legendary':2,'Godly':2,'Que Pro':1}
theshop={'SUS':[],'Noob':[],'Ok':[],'Gud':[],'Epic':[],'Pro':[],'Godly':[],'Legendary':[],'Que Pro':[]}
def resetshop():
  global theshop
  theshop={'SUS':[],'Noob':[],'Ok':[],'Gud':[],'Epic':[],'Pro':[],'Godly':[],'Legendary':[],'Que Pro':[]}
  for i in boxes.keys():
    for i2 in range(1,random.choice(range(1,shopdict[i]+1))+1):
      q=random.choice(boxes[i])
      while boxprices[q][1]==0:
        q=random.choice(boxes[i])
      theshop[i].append(q)
resetshop()
def shop():
  global shopreset,money
  if time.time()-shopreset>=30:
    resetshop()
    shopreset=time.time()
  ting={}
  ting2={} #to store the tier for each letter
  ae=-1
  for i in theshop.keys(): #35 is the center
    print(' '*((10-len(i))//2+30)+tiercolors[i][0]+bold+"\u0332".join(i)+reset)
    i3=''
    i4=''
    od=0
    for i2 in theshop[i]:
      ae+=1
      ting[thealphabet[ae]]=i2
      ting2[thealphabet[ae]]=i
      od+=1
      i3+=str(thealphabet[ae])+')'+bcolor[i2]+i2+reset
      i4+=str(thealphabet[ae])+')'+i2
      if od!=len(theshop[i]):
        i3+=', '
        i4+=', '
    print(' '*(34-(len(i4)//2))+(i3 if i3!='' else tiercolors[i][0]+"None"))
  print('\nSay the letter of the box you would like to view!')
  chi=input('\n>\033[38;5;82m  ')
  if chi in ting.keys():
    c()
    descbox(ting[chi],False)
    print('\nWould you like to buy this box for '+printout(boxprices[ting[chi]][1])+'?\n(Your money: \033[38;5;40m'+str(money)+"\033[0m)")
    questionable=input('>\033[38;5;82m  ').lower()
    c()
    if questionable in yes:
      if money>=boxprices[ting[chi]][1]:
        money-=boxprices[ting[chi]][1]
        sellbuy('Bought'+bcolor[ting[chi]]+ting[chi]+reset+" for "+printout(boxprices[ting[chi]][1])+'!',reset+bcolor[ting[chi]])
        theshop[ting2[chi]].remove(ting[chi])
        inventory.append(ting[chi])
      else:
        print("Your poor bru")
        anykey()
  c()
def printinv(h4=False,p=False):
  if not p:
    yee=False
    for i in boxlist:
      if i in inventory:
        yee=True
    if not yee and not h4:
      print('None')
    yeh=[]
    for i in boxes.keys():
      yessir=False
      yeh2=yeh.copy()
      for i2 in boxes[i]:
        if i2 in inventory and i2 not in yeh:
          yeh.append(i2)
          if not yessir and not h4:
            print(tiercolors[i][1]+' '+reset+'  ',end='')
            yessir=True
          if not h4:
            print(bcolor[i2]+i2+' ['+str(inventory.count(i2))+']'+reset,end='   ')
      if yeh2!=yeh and not h4:
        print()
    return yeh
  else:
    print()
    yee=False
    for i in itemlist:
      if i in inventory:
        yee=True
    if not yee and not h4:
      print('None')
    thelis=[]
    cupcak=0
    inven=[]
    for q in inventory:
      yew=False
      if q in itemlist:
        for q3 in inven:
          if itemssell[q3]>=itemssell[q]:
            yew=True
            inven.insert(inven.index(q3),q)
            break
        if not yew:
          inven.append(q)
    for i in itemlist:
      if i in inven and i not in thelis:
        cupcak+=1
        thelis.append(i)
        if not h4:
          print(itemdict[i][0]+i+reset+'['+str(inventory.count(i))+']',end='') 
          print(', ' if cupcak%4!=0 else '\n----------\n',end='')
    if not h4:
      sys.stdout.write('\x1b[2D')
      print(" ",end='')
    return thelis
def check(ff='box'):
  #Used to check if there are boxes or items in your inv
  i=False
  if ff=='box':
    for i2 in boxlist:
      if i2 in inventory:
        i=True
  else:
    for i2 in itemlist:
      if i2 in inventory:
        i=True
  return i
      

def funny(fd:dict,l,thing=False):
  t6=0
  for i in fd.keys():
    t6+=1
    if not thing:
      var1=bcolor[fd[i]]
    else:
      var1=itemdict[fd[i]][0]+' '
    print(i+')'+var1+fd[i]+' ['+str(inventory.count(fd[i]))+']'+reset,end='')
    number=20-len(fd[i]+' ['+str(inventory.count(fd[i]))+']') #my cool thing for making stuff seem centered idk
    if number<=0:
      number=0
    if t6==1 and fd[i]!=l:
      print(" "*number+"||     ",end='')
    else:
      t6=0
      print()
def refresht(h=1):
  global j,j2
  zediction={}
  zediction2={}
  j=printinv(True)
  j2=printinv(True,True)
  counter=-1
  for i in j:
    counter+=1
    zediction[thealphabet[counter]]=j[counter]
  counter=-1
  for i in j2:
    counter+=1
    zediction2[thealphabet[counter]]=j2[counter]
  return zediction if h==1 else zediction2
def inv(para=''):
  global inventory,money
  c()
  print(bold+'Your Boxes:'+reset+'\n')
  printinv()
  print(bold+'\nYour Money: \033[38;5;40m'+printout(money)+reset+'\n')
  print(reset+'\n'+bold+'Options:'+reset+'\n1) Quick open a box\n2) Look at a box\n3) Look at your items')
  if para=='':
    zeinputy=input('> ')
  else:
    zeinputy = '1' if para=='1a' else '3'
  zediction=refresht()
  zediction2=refresht(2)
  c()
  if zeinputy=='1':
    if check('box'):
      while check('box') and zediction!={}:
        print("Which box would you like to open? (Enter to exit)\n[If you want to to open many boxes, put the box symbol followed by the amount (ex: a 5)]\n")
        zediction=refresht()
        funny(zediction,j[len(j)-1])
        kl=input('\n>').strip()
        c()
        if kl=='':
          break
        elif kl[0] in zediction.keys():
          quepro=1
          if kl[2:].isdigit():
            if inventory.count(zediction[kl[0]])>=int(kl[2:]):
              quepro=int(kl[2:])
            else:
              quepro=inventory.count(zediction[kl[0]])
          elif kl[1:] in ['all',' all','a',' a']:
            quepro=inventory.count(zediction[kl[0]])
          if quepro==0:
            quepro=1
          openbox(zediction[kl[0]],quepro)
          if zediction[kl[0]] not in inventory:
            del zediction[kl[0]]
    else:
      print('(Theres nothing to open...)')
      input('\n[Enter to continue]')
    c()
  elif zeinputy=='2':
    if check('box'):
      print('Pick a box to look at:\n')
      funny(zediction,j[len(j)-1])
      ae=input('\n>')
      if ae in zediction.keys():
        c()
        descbox(zediction[ae])
    else:
      print('(Theres nothing to look at...)')
      input('\n[Enter to continue]')
    c()
  elif zeinputy=='3':
    while check('item'):
      c()
      print(bold+'Your Items:'+reset)
      printinv(False,True)
      p4=input('\n\n1) Look at an item\n\n[Enter to leave]\n\033[38;5;82m>\033[0m ')
      if p4=='1': #Gotta make this exactly like the boxes, but like yea
        c()
        print('Which item do you want to look at?\n')
        zediction=refresht()
        zediction2=refresht(2)
        funny(zediction2,j2[len(j2)-1],True)
        qano=input('\033[38;5;82m>\033[0m ')
        if qano in zediction2.keys():
          c()
          printthing(zediction2[qano])
          juei=input("\n\nSell this item? (anything but yes to exit)\n\033[38;5;82m>\033[0m")
          if juei in yes:
            c()
            inventory.remove(zediction2[qano])
            sellbuy('Sold '+itemdict[zediction2[qano]][0]+zediction2[qano]+r+' for '+printout(mult(itemssell[zediction2[qano]])),r+itemdict[zediction2[qano]][0])
            money+=mult(itemssell[zediction2[qano]])
      elif p4=='':
        c()
        break
    if not check('item'):
      print("Imagine having no items...")
      input("[Enter to continue]")
      c()
  else:
    c()
def printthing(thing):
  print(f'Item: '+itemdict[thing][0]+thing+reset+'\n',end=' '*10)
  for i in itemdict[thing][1]:
    if i in colordict.keys():
      print(colordict[i]+reset,end='')
    else:
      if i=='\n':
        print('\n'+(" "*13),end='')
      else:
        print(i,end='')
  hghg='Sell Price: '+str(itemssell[thing])
  print('\n'+' '*((5-len(itemdesc[thing]))//2+26)+itemdesc[thing])
  print(' '*(35-len(hghg))+hghg)
def printbox(boxe,k=True):
  if k:
    box=random.choice([box1,box2])
  else:
    box=boxopen
  TMP = ''
  for i in box:
    if i=='A':#Top color
      TMP += boxcolors[boxe][0]+reset
    elif i=='B':#Side color
      TMP += boxcolors[boxe][1]+reset
    elif i=='C':#Bottom color
      TMP += boxcolors[boxe][2]+reset
    elif i in ['/','\\','_','-']:
      try:
        TMP += boxcolors[boxe][3]+reset
      except:
        TMP += i
    else:
      if i!='\n':
        TMP+=i
      else:
        print(" "*10+TMP)
        TMP = ""


defaultcooldown = 15 #was 30, might buff lol
stime=time.time()-defaultcooldown
cooldown=defaultcooldown  #the cooldown, changes with kronos box, next var is to count that
#kronos box: set cooldown to like 15 and change cooldowns to like 5 if you want it to last 5 times?
#maybe make the thingie a thread or something
#use floor division to not do a thread or something
#aka just use subtraction lol
cooldowns=0
def spawn():
  zenum=0
  for i in spawns.keys():
    if i<=maxdollarhit:
      zenum=i
  if zenum==0:
    zenum=10
  return random.choice(spawns[zenum])
inv2=[]
def scavenge():
  global stime,cooldown,cooldowns,inv2
  if time.time()-stime>cooldown:
    ashley=time.time()-stime
    stime=time.time()
    if cooldowns!=0:
      cooldowns-=1
    if cooldowns==0:
      cooldown=defaultcooldown#resets it
    inv2=[]
    while ashley>cooldown:
      ashley-=cooldown
      if cooldowns!=0:
        cooldowns-=1
      if cooldowns==0:
        cooldown=defaultcooldown
      jwd=spawn()
      inventory.append(jwd)
      inv2.append(jwd)
    if len(inv2)>=20:
      print('It seems like boxes are everywhere...\n')
    elif len(inv2)>=10:
      print('A lot of stuff is on the ground...\n')
    elif len(inv2)>=5:
      print('Theres some nice stuff out here...\n')
    elif len(inv2)==0:
      print('Theres nothing but grass outside. Que pro.\n') #should be impossible, but just in case
    else:
      print("You're lucky that god dropped some stuff...\n")
    if len(inv2)!=0:
      print(bold+'You got: ',end=reset)
    olol=0
    for i in inv2:
      print(printout(i),end='')
      olol+=1
      if olol!=0 and olol!=len(inv2):
        print(', ',end='')
  else:
    print('Theres nothing outside...')
  input('\n\n[Enter to continue]')
  os.system('clear')
def openbox(boxy,quemarse=1):
  global inventory,money
  c()
  try:
    for i in range(quemarse):
      inventory.remove(boxy)
  except:
    return 'no'
  coinsu=0
  stof=[]
  for i in range(quemarse):
    drop=random.choice(boxdrops[boxy])
    if type(drop)==int:
      money+=mult(drop)
      coinsu+=mult(drop)
    else:
      inventory.append(drop)
      stof.append(drop)
  thinggot=''
  if coinsu!=0:
    thinggot+=printout(coinsu)+' coins'
    if stof!=[]:
      thinggot+=','
  if stof!=[]:
    impe=[]
    for e,i in enumerate(stof):
      if i not in impe:
        thinggot+=i+'['+str(stof.count(i))+']'+','
        impe.append(i)
  if thinggot=='':
    thinggot='Nothing...'
  if thinggot[-1]==',':
    thinggot=thinggot[:-1]
  print(f"{bcolor[boxy]+boxy:^69}"+reset)
  printbox(boxy,False)
  print(reset+'\n'+(' '*properspace('\nYou got: '+thinggot,50)[0])+'You got: ',end='')
  slepy(1)
  print(bold+thinggot+reset)
  print('\n[Enter to continue]')
  input()
  c()


if 'boxsaves.json' not in os.listdir():
  with open("boxsaves.json",'w') as sam:
    sam.write(json.dumps({}))
'''

inventory=[]

money=0
currentmulti=1 #the current multiplier, when i add multis it will change

rebirths=0
rebirthamo=10000
maxdollarhit=0
'''
def save():
  #rebirths, inventory, money, currentmulti, maxdollarhit,spedrunn, tspedrunn
  with open("boxsaves.json",'r') as n:
    alls = json.load(n)
  alls[name] = [rebirths, inventory, money, currentmulti, maxdollarhit, spedrunn, tspedrunn]
  with open('boxsaves.json','w') as j:
    j.write(json.dumps(alls))

def load():
  global rebirthamo, rebirths, inventory, money, currentmulti, maxdollarhit, spedrunn, tspedrunn
  with open('boxsaves.json','r') as n:
    alls = json.load(n)
  if name in alls:
    rebirths, inventory, money, currentmulti, maxdollarhit, spedrunn, tspedrunn = alls[name]
    print("Welcome back "+name+"!")
    if name=='srnkt02':
      print("\033[38;5;206mI still love you!\033[0m")
  else:
    if name=='srnkt02':
      printt("HIIII BABYYYYYYY")
      slepy(2)
      printt("I LOVE YOU SAM")
      slepy(1)
      printt("YOURE "+r*5+"SO "+r*5+"CUTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    else:
      print("Welcome "+name+"!")
    input("[Enter to continue]")
    c()
    save()

tspedrunn=False
introing=True
while (name:=input("What is your name?\n> ").strip()) == '':
  c()
c()
load()

while introing:
  print(bold+'Welcome to '+"\u0332".join('unbox until you die then unbox more')+' simulator!'+reset)
  print('\n"S" to skip the intro\n"Z" to see the controls\n"C" to see the credits??\nAnything else goes to the intro...')
  apathy=input('\nCool_text \033[38;5;82m>\033[0m ').lower()
  print(reset,end='')
  c()
  if apathy=='s':
    introing=False
  elif apathy=='z':
    print(bold+"Controls:"+reset)
    print("Just read the prompts lol \n(Everything has a number or letter attached to it)\n(Also you can just hit enter on most prompts to exit em)")
    input('\n[Enter to continue noobie]')
  elif apathy=='c':
    print(bold+'Pro credits??'+reset)
    print("\nEverything made by me (It isnt that impressive)\nAll the colors in this game are just python color codes\n\nAll the items were made by my friend (and you mr jacen..)\nthen imported into python by me lol\n\nOther than that its just a bunch of rng\n")
    input('[Very cool credits right]')
  else:
    introing=False
    printt("Long ago in a land far far away...")
    time.sleep(1)
    printt("Just kidding, I forgot to add an intro!")
    input("[Enter to continue]")
  c()
if introing:
  print('hi')
  input()
while True: #main loop, gonna be scavenge, look at inv, go to shop (still have to make shop)
  if money>maxdollarhit:
    maxdollarhit=money
  print("\u0332".join(random.choice(['time to do stuff','mm pro unboxing','haha box go brrr']))+'\n\n1) Open your inventory\n  1a) Quick open boxes\n  1b) Look at items\n2) Look outside for some boxes\n3) Go to the shop\n')
  if maxdollarhit>rebirthamo/2:
    print('\033[38;5;103m4) Take a trip to god\033[0m\n')
  print("Your money: \033[38;5;40m"+printout(money)+"\033[0m\n\n[S to view settings/extras]")
  if rebirths>0:
    print("\033[38;5;102m[Rebirth requirement:",printout(rebirthamo),"]\033[0m")
  n=input('\033[38;5;'+('207' if name=='srnkt02' else '82')+'m>\033[0m ').lower()
  print(reset)
  c()
  if '1' in n:
    inv('' if n=='1' else n)
  elif n=='2':
    scavenge()
  elif n=='3':
    shop()
  elif n=='4':
    if maxdollarhit>rebirthamo/2:
      rebirth()
  elif n=='n' and rebirths>1:
    tspedrunn=not tspedrunn
  elif n=='s':
    c()
    col = lambda fe: "\033[38;5;196mFalse\033[0m" if not fe else "\033[38;5;82mTrue\033[0m"
    print("1) Speedrun mode:",col(spedrunn),"\n  - halves waiting times for text\n\n"+('2) True speedrun mode: '+col(tspedrunn)+'\n  - Skips all text animation, 1/4 wait times!' if rebirths>0 else '')+"\n[Enter # to toggle setting]\n[Enter to exit]")
    while (n:=input('\033[38;5;99m>\033[0m ').lower())!='':
      c()
      if n=='1':
        spedrunn = not spedrunn
      elif n=='2' and rebirths>0:
        tspedrunn = not tspedrunn
      print("1) Speedrun mode:",col(spedrunn),"\n  - halves waiting times for text\n\n"+('2) True speedrun mode: '+col(tspedrunn)+'\n  - Skips all text animation, 1/4 wait times!' if rebirths>0 else '')+"\n\n[Enter to exit]")
    c()
  elif n=='t':
    c()
    uewe=0
    listo=[]
    for i in itemdict.keys():
      if len(itemdict[i])>1:
        listo.append(i)
    while True:
      print("a/d to go through, enter to exit")
      printthing(listo[uewe])
      wein=input('> ')
      if wein=='a':
        if uewe!=0:
          uewe-=1
      elif wein=='d':
        if uewe!=(len(listo)-1):
          uewe+=1
      elif wein=='':
        break
      c()
  elif n=='f':   #testing
    printthing(thething)
  save()



'''
# What the heck is the game
unbox stuff to get more stuff to probably get upgrades to get better boxes
# What you can do 
- Probably forage outside, theres like a 30 second period between when a box falls out of the sky lol
- Add Crafting!!! (among box suck)
# Open Boxes/Sell Boxes
- Maybe some boxes have more sell back than what they actually have in them
- They could gives coins/boxes or sell for just hard coins



# Average money per tier
### SUS - Among Box,Poo Box,Box Box
10
### Noob - Common Box,Sugnoma Box,Bozo Box,n Box
100
### Ok - Apple Box,Funny Box,Balanced Box
250
### Gud - Robo Box,Money Box,Halloween Box,Buffed Box
500
### Epic - Oof Box,Bean Box,Python Box
2,500
### Pro - Gold Box,Gamblers Box,Basic Box,/e free Box
10,000
### Legendary - Xina Box,#1 Box,Diamond Box,Chaotic Box
100,000
### Godly - Rouxs Box,Gamer Box,Aimbot Box,Pepe Box,True Box
500,000
### Que Pro - THE Box,Lank box,rob
2,500,000

# Stuff ill put in:
- Kronos' box (Speed up box drop time by 2x for like 2 mins)
- Stonks box (Guaranteed Money/Gold/Diamond Boxes for a little?)
- PogChamp box(PogChamp)
- multipliers (eeee)


Add better selling, finish selling, add sell prices to diamond sword, apply mults to selling and stuff 

'''
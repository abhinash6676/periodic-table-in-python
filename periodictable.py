#FIND POSITION AND TYPE OF ANY ELEMENT

spdf=('H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti',
      'V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc'
      ,'Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu'
      ,'Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi'
      ,'Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr'
      ,'Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og')



en=('2.2','0','0.98','1.57','2.04','2.55','3.04','3.44','3.98','0', #10 numbers in a line
       '0.93','1.31','1.61','1.90','2.19','2.58','3.16','0','0.82','1',
    '1.36','1.54','1.63','1.66','1.55','1.83','1.88','1.91','1.9','1.65',
    '1.81','2.01','2.18','2.55','2.96','3','0.82','0.95','1.22','1.33',
    '1.6','2.16','1.9','2.2','2.28','2.21','1.93','1.69','1.78',
    '1.96','2.05','2.1','2.66','2.6','0.8','0.89','1.1','1.12','1.13',
    '1.14','1.13','1.17','1.2','1.2','1.22','1.23','1.24','1.24','1.25',
    '1.1','1.27','1.3','1.5','2.36','1.9','2.2','2.2','2.28','2.54',
    '2','1.62','2.33','2.02','2.0','2.2','0','0.7','0.89','1.1',
    '1.3','1.5','1.38','1.36','1.28','1.3','1.3','1.3','1.3','1.3',
    '1.3','1.3','1.3','no data','no data','no data','no data','no data','no data','no data',
    'no data','no data','no data','no data','no data','no data','no data','no data',) #8 numbers in this line
                                       #total = 10*11 + 8 = 118 ! Confirmed!




mn=('1.007','4.0026','6.941','9.01218','10.81','12.0107','14.0067','15.9994',                       #8 numbers per line
    '18.9984','20.179','22.98977','24.305','26.98154','28.0855','30.97376','32.06',
    '35.453','39.0983','39.948','40.08','44.9559','47.90','50.9415','51.996',
    '54.938','55.847','58.70','58.9332','63.546','65.38','69.72','72.59',
    '74.9216','78.96','79.904','83.8','85.4678','87.62','88.9059','91.22',
    '92.9064','95.94','98','101.07','102.9055','106.4','107.868','112.41',
    '114.82','118.69','121.75','126.9045','127.60','131.3','132.9054','137.33',
    '138.9055','140.12','140.9077','144.24','145','150.4','151.96','157.25',
    '158.9254','162.5','164.93','167.259','168.93421','173.04','174.967','178.49',
    '180.94788','183.84','186.207','190.23','192.217', '195.084','196.966569','200.59',
    '204.3833','207.2','208.9804','210','210','220','223','226',
    '227','231.03588','232.03806','237','238.02891','243','244','247',
    '247','251','252','257','258','259','262','261',
    '262','266','264','277','268', '271','272','285', 
    '284','289','288','293','294','294',) #6 numbers in this line
 #Total = 8*14 + 6 = 118 ! Confirmed 118 elements.
   
   

names=('Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon','Nitrogen','Oxygen','Fluorine',
       'Neon','Sodium','Magnesium','Aluminium','Silicon','Phosphorus','Sulfur','Chlorine','Argon',
       'Potassium','Calcium','Scandium','Titanium','Vanadium','Chromium','Manganese','Iron','Cobalt','Nickel','Copper','Zinc','Gallium','Germanium','Arsenic',
       'Selenium','Bromine','Krypton','Rubidium','Strontium','Yttrium','Zirconium','Niobium','Molybdenum',
       'Technetium','Ruthenium','Rhodium','Palladium','Silver','Cadmium','Indium','Tin','Antimony',
       'Tellurium','Iodine','Xenon','Caesium','Barium','Lanthanum','Cerium','Praseodymium','Neodymium',
       'Promethium','Samarium','Europium','Gadolinium','Terbium','Dysprosium','Holmium','Erbium',
       'Thulium','Ytterbium','Lutetium','Hafnium','Tantalum','Tungsten','Rhenium','Osmium','Iridium',
        'Platinum','Gold','Mercury','Thallium','Lead','Bismuth','Polonium','Astatine','Radon','Francium',
       'Radium','Actinium','Thorium','Protactinium','Uranium','Neptunium','Plutonium','Americium','Curium',
       'Berkelium','Caifornium','Einsteinium','Fermium','Mendelevium','Nobelium','Lawrencium','Rutherfordium',
       'Dubnium','Seaborgium','Bohrium','Hassium','Meitnerium','Darmstadtium','Roentgenium','Copernicium',
       'Nihonium','Flerovium','Moscovium','Livermorium','Tenessine','Oganesson')


alkali=('Li','Na','K','Rb','Cs','Fr')

Ealkali=('Be','Mg','Ca','Sr','Ba','Ra')

trans=('Sc','Y','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Hf','Ta','W','Re','Os','Ir','Pt','Au','Rf','Db','Sg','Bh','Hs')

lanth=('Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu')

acti=('Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr',)

posttrans=('Al','Zn','Ga','Cd','In','Sn','Hg','Tl','Pb','Bi','Po','At')

metalloid=('B','Si','Ge','As','Sb','Te')

nonmetal=('C','N','O','F','P','S','Cl','Se','Br','I')

halogen=('F','Cl','Br','I','At','Ts',)
      
noble=('He','Ne','Ar','Kr','Xe','Rn','Og',)

group1=('H','Li','Na','K','Rb','Cs','Fr')
group2=('Be','Mg','Ca','Sr','Ba','Ra')
group3=('Sc','Y','La','Ac','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu',
        'Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr',)
group4=('Ti','Zr','Hf','Rf',)
group5=('V','Nb','Ta','Db',)
group6=('Cr','Mo','W','Sg',)
group7=('Mn','Tc','Re','Bh',)
group8=('Fe','Ru','Os','Hs',)
group9=('Co','Rh','Ir','Mt',)
group10=('Ni','Pd','Pt','Ds',)
group11=('Cu','Ag','Au','Rg',)
group12=('Zn','Cd','Hg','Cn',)
group13=('B','Al','Ga','In','Tl','Nh',)
group14=('C','Si','Ge','Sn','Pb','Fl',)
group15=('N','P','As','Sb','Bi','Mc',)
group16=('O','S','Se','Te','Po','Lv',)
group17=('F','Cl','Br','I','At','Ts',)
group18=('He','Ne','Ar','Kr','Xe','Rn','Og',)

period1=('H','He')
period2=('Li','Be','B','C','N','O','F','Ne')
period3=('Na','Mg','Al','Si','P','S','Cl','Ar')
period4=('K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr')
period5=('Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe')
period6=('Cs','Ba','La','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Ce',
         'Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu')
period7=('Fr','Ra','Ac','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og',
         'Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr',)



#period=[period1,period2,period3,period4,period5,period6,period7]
#group=[group1,group2,group3,group4,group5,group6,group7,group8,group9,group10,group11,group12,group13,group14,group15,group16,group17,group18]

element=str(input("Enter Symbol of an Element :"))

##############################################################################################################################################################################################################

# 1.FINDING ATOMIC NUMBER OF ELEMENT :-

##############################################################################################################################################################################################################


z= spdf.index(element) +1
print("Atomic Number of Element(Z):",z)
print("Element:",names[z-1])
print("Mass number:",mn[z-1])
print("Electronegativity:",en[z-1])
print()


##############################################################################################################################################################################################################

#2.FINDING THE PERIOD :-

##############################################################################################################################################################################################################

if element in period1:
   print("This Element Belongs to 1st Period.")
elif element in period2:
   print("This Element Belongs to 2nd Period.")
elif element in period3:
   print("This Element Belongs to 3rd Period.")
elif element in period4:
   print("This Element Belongs to 4th Period.")
elif element in period5:
   print("This Element Belongs to 5th Period.")
elif element in period6:
   print("This Element Belongs to 6th Period.")
elif element in period7:
   print("This Element Belongs to 7th Period.")
else:
   print("Invalid Symbol")

##############################################################################################################################################################################################################

# 3. FINDING THE GROUP :-

##############################################################################################################################################################################################################   

if element in group1:
   print("This Element Belongs to 1st Group.")
elif element in group2:
   print("This Element Belongs to 2nd Group.")
elif element in group3:
   print("This Element Belongs to 3rd Group.")
elif element in group4:
   print("This Element Belongs to 4th Group.")
elif element in group5:
   print("This Element Belongs to 5th Group.")
elif element in group6:
   print("This Element Belongs to 6th Group.")
elif element in group7:
   print("This Element Belongs to 7th Group.")
elif element in group8:
   print("This Element Belongs to 8th Group.")
elif element in group9:
   print("This Element Belongs to 9th Group.")
elif element in group10:
   print("This Element Belongs to 10th Group.")
elif element in group11:
   print("This Element Belongs to 11th Group.")
elif element in group12:
   print("This Element Belongs to 12th Group.")
elif element in group13:
   print("This Element Belongs to 13th Group.")
elif element in group14:
   print("This Element Belongs to 14th Group.")
elif element in group15:
   print("This Element Belongs to 15th Group.")
elif element in group16:
   print("This Element Belongs to 16th Group.")
elif element in group17:
   print("This Element Belongs to 17th Group.")
elif element in group18:
   print("This Element Belongs to 18th Group.")
else:
   print()


##############################################################################################################################################################################################################

# 4. FINDING THE TYPE OF ELEMENT :-

##############################################################################################################################################################################################################

if element in alkali:
   print("This Element is an Alkali Metal.")
elif element in Ealkali:
   print("This Element is an Alkaline Earth Metal.")
elif element in trans:
   print("This Element is a Transitional Metal.")
elif element in lanth:
   print("This Element is a Lanthanide.")
elif element in acti:
   print("This Element is an Actinide.")
elif element in posttrans:
   print("This Element is a Post-Transition Metal.")
elif element in metalloid:
   print("This Element is a Metalloid or Semi-Metal.")
elif element in halogen and nonmetal:
   print("This Element is a Halogen.")
elif element in nonmetal:
   print("This Element is a Non-metal.")
elif element in noble:
   print("This Element is a Noble Gas.")

else:
   print()
print()

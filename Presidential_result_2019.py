r=["Rivers",150710,473971],["Zamfara",438682,125423],["Kebbi",581552,154282],["Sokoto",490333,361604],["Bayelsa",118821,197933],["Akwa Ibom",175429,395832],["Delta",221292,590068],["Borno",836496,71788],["Plateau",468555,548665],["Katsina",1232133,308056],["Kano",1464768,391593],["Cross River",117302,295737],["Taraba",324906,374743],["Benue",347668,356817],["Imo",140463,334923],["Edo",267842,275691],["Bauchi",798428,209313],["Ogun",281762,194655],["Lagos",580825,448015],["Oyo",365229,366690],["Adamawa",378078,410266],["Anambra",33298,524738],["Kaduna",993445,649612],["Jigawa",794738,289895],["Niger",612371,218052],["Ebonyi",90726,258573],["Enugu",54423,355553],["Ondo",241769,275901],["Abia",85058,219698],["Yobe",497914,50763],["Gombe",402961,138484],["Kogi",285894,218207],["Nassarawa",289903,283847],["Kwara",308984,138184],["FCT",152224,259997],["Ekiti",219231,154032],["Osun",347634,337377]
for x in range(0,len(r)):
    print(r[x][0],"State")
    print("APC\t",r[x][1])
    print("PDP\t",r[x][2])
    print("\n")
    APC=0
    PDP=0
for y in range(0,len(r)):
    APC+=r[y][1]
    PDP+=r[y][2]
print("Total : ")
print("\tAPC\t:",APC)
print("\tPDP\t:",PDP)
print("\tDifference\t:",APC-PDP)
print("Number of states : ",len(r))
print("Done")

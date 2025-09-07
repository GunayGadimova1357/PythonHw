#All sentences must end with an ending mark such as a period, exclamation point, or question mark.
txt=input("add text: ")
counter=0
nump=txt.count(".")
nume=txt.count("!")
numq=txt.count("?")
counter=nump+nume+numq
print(counter)

#text below
#Planets are diverse worlds. Mercury, closest to the Sun. Venus, shrouded in clouds! Earth, our home? Mars, the red planet. What lies beyond Jupiter?
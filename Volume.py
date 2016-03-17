pi=3.14

print "Scegliere cosa eseguire:"
print"Per il volume del cubo digitare: 1"
print"Per il volume della sfera  digitare: 2"

scelta= input ( 'Inserisci un numero: ' )

if scelta==1: 
  print "Hai scelto il volume del cubo" 
  numero=input ('Inserisci il lato del cubo:' )
  volume=numero*numero*numero
  print "Volume: ", volume	

if scelta==2: 
  print "Hai scelto il volume della sfera" 
  raggio=input ('Inserisci il raggio:' )
  volume=(4.0*pi*raggio*raggio*raggio)/3.0
  print"Volume: ", volume
 		 
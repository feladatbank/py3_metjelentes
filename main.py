"""
            Meteorológiai jelentés           (18 pont)
{{{{ Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! }}}}
ÜGYELJEN arra hogy az tavirathu13.txt fálj beolvasásánál van fejléc!!!
telepules,ido,szel_irany,homerseklet,erőség

1. A feladat megoldásához hozzon létre programot metjelentes azonosítóval(néven)!

2.  Olvassa be a tavirathu13.txt állományban található adatokat és tárolja el adatokat egy listába,ügyeljen arra, hogy az állomány fejlécet tartalmaz! amely használatával a további feladatok megoldhatók! A kimenet a mintának megfelelő adatot adja vissza! Lehetőség szerint CLASS HASZNÁLATÁVAL! Ha nem CLASS-sal oldod meg, akkor is érvényes, de nem kaphatsz a feladatra maximális pontot.

3. Kérje be a felhasználótól egy város kódját! Adja meg, hogy az adott városból mikor érkezett az utolsó mérési adat! A kiírásban az idöpontot óó:pp formátumban jelenítse meg!

4. Határozza meg, hogy mikor mérték a legmagasabb hőmérsékletet! Jelenítse meg a méréshez kapcsolódó település nevét, az időpontot és a hőmérsékletet! Amennyiben több legnagyobb érték van, akkor elég az egyiket kiírnia.

5. Határozza meg, azokat a településeket és időpontokat, ahol és amikor am érések idején szélcsend volt! (A szélcsendet a táviratban 00000 kóddal jelölik.) Ha nem volt ilyen, akkor a „Nem volt szélcsend a mérések idején." szöveget írja ki! A kiírásnál a település kódját és az időpontot jelenítse meg.

Output / kimenet______________________________________
3. feladat
Adja meg egy település kódját! Település: SM
Az utolsó mérési adat a megadott településről 23:45-kor érkezett.
4. feladat
A legmagasabb hőmérséklet: DC 13:15 35 fok.
5. feladat
BP 01:00
DC 02:15
SN 03:15
BC 04:45
DC 04:45
SN 05:15
SN 05:45
KE 08:45
BC 11:45
_____________________________________________________

"""
#1-2 Feladat
class Ido_jaras:
  def __init__(self,sor):
    telepules,ido,szel_irany,homerseklet = sor.strip().split(" ")
    self.telepules = telepules
    self.ido = ido
    self.szel_irany = szel_irany
    self.homerseklet = int(homerseklet)
    self.erőség = szel_irany[3:]

with open("tavirathu13.txt","r",encoding="UTF-8") as f:
  cim = f.readline()
  lista = [Ido_jaras(sor) for sor in f]
  
#3 Feladat

print("3. feladat")
bekeres = input("Adja meg egy település kódját! Település: ")

utolso_meres = max([sor.ido for sor in lista if bekeres == sor.telepules])

print(f"Az utolsó mérési adat a megadott településről {utolso_meres[0:2]}:{utolso_meres[2:]}-kor érkezett.")
#4 Feladat
telepules_neve = ""
ido_pont = ""
nagy = 0

for sor in lista:
  if sor.homerseklet > nagy:
    nagy = sor.homerseklet
    telepules_neve = sor.telepules 
    ido_pont = sor.ido
    
print(f"""4. feladat
A legmagasabb hőmérséklet: {telepules_neve} {ido_pont[0:2]}:{ido_pont[2:]} {nagy} fok.""")
#5 Feladat
szelcsend = [sor for sor in lista if sor.szel_irany == "00000"]

print("5. feladat")
if len(szelcsend) > 0:
  [print(f"{sor.telepules} {sor.ido[0:2]}:{sor.ido[2:]}") for sor in szelcsend]

else:
  print("Nem volt szélcsend a mérések idején.")


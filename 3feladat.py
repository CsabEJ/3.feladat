halmaz = {'1','2','3','4','5'}
halmaz2 = {'6'}
print(halmaz)

halmaz.clear()
print(halmaz)

halmaz.copy()
print(halmaz)


halmaz = {'1','2','3','4','5'}
halmaz2 = {'1','3','5','7','9'}
print(halmaz.difference(halmaz2))
print(halmaz.difference_update(halmaz2))

halmaz = {'1','2','3','4','5'}
halmaz2 = {'1','3','5','7','9'}
print(halmaz.intersection(halmaz2))
print(halmaz.intersection_update(halmaz2))

halmaz = {'1','2','3','4','5'}
halmaz2 = {'1','3','5','7','9'}
print(halmaz.isdisjoint(halmaz2)) #Azt adja vissza, hogy két halmaznak van -e metszéspontja vagy sem.
print(halmaz.issubset(halmaz2)) #Azt adja vissza, hogy egy másik készlet tartalmazza -e ezt a készletet vagy sem.
print(halmaz.issuperset(halmaz2)) #Azt adja vissza, hogy a készlet tartalmaz -e másik halmazt vagy sem.         
print(halmaz.symmetric_difference()) # Visszaadja a készlet a szimetrikus különbségek 2 készletét
print(halmaz.pop()) #Kitöröl egy elemet a készletből egy elemet
print(halmaz.update(halmaz2)) #Fejleszti a készletet egy másik szettel, vagy bármi más iterálhatóval






# variables
bottles = 20
volume = 0.89
fillingVolume = 0.83
number_of_people_expected = 40
amountAverageDrunk = 0.35

peopleInParty = 35
totalDrunk = 0.35 * peopleInParty
wasted = (bottles * fillingVolume) - totalDrunk
people_dagabaaz = number_of_people_expected - peopleInParty

print(peopleInParty)
print(totalDrunk)
print(wasted)
print(people_dagabaaz)

print("So I had", peopleInParty, "people in my party who drank", totalDrunk, "litres, and", people_dagabaaz,
      "didn't show up. And ", wasted, "litres was wasted.")

car = "Maserati "
print(car * 5)

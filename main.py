from getCounties import get_county
from getData import findFIPS, totalHouseHoldCount
from colorama import Fore, Back, Style

while True:
    city = str(input("Enter a city: "))
    state = str(input("Enter the abbreviated state of the city (e.g. 'NJ'): "))

    fips = findFIPS(city, state)

    totalHHcount = totalHouseHoldCount(fips)

    print("The total number of households in this city is " + Fore.GREEN + str(totalHHcount))
    print(Style.RESET_ALL)



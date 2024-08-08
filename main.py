import sys
from MENU import MENU

resources = {
  "Water": 0,
  "Milk":300 ,
  "Coffee": 100,
   "Money" :0
}
flag_good=True
while flag_good==True:
    def prompt():
        global flag_good
        prompt = input()
        if prompt == "off":
            flag_good = False
            print("Goodbye")
            sys.exit(2)
        elif prompt == "report":
            print(f"Water: {resources["Water"]}ml")
            print(f"Milk: {resources["Milk"]}ml")
            print(f"Coffee: {resources["Coffee"]}ml")
            print(f"Money: ${resources["Money"]}")
    order= input('Hi☺️, What would you like?☕ (espresso/latte/cappuccino):')
    prompt()
    def is_it_sufficient(order):
          global flag_good
          needed_water= MENU[order]["ingredients"]["water"]
          needed_milk=MENU[order]["ingredients"]["milk"]
          needed_coffee = MENU[order]["ingredients"]["coffee"]
          #print(needed_water)
          #print(recources["Water"])


          #x = thisdict.get("model")
          #print(f"Needed - Water: {needed_water}, Milk: {needed_milk}, Coffee: {needed_coffee}")
          #print(f"Available - Water: {resources['Water']}, Milk: {resources['Milk']}, Coffee: {resources['Coffee']}")

          if resources["Water"]>=needed_water and resources["Milk"]>=needed_milk and resources["Coffee"]>=needed_coffee:
              insert_coin=input(f"Recourses are enough.You can insert {MENU[order]["cost"]} dollars. ")
          elif resources["Water"]<needed_water:
              print("There is not enough Water")

              flag_good=False
              return flag_good


          elif resources["Milk"] < needed_water:
              print("There is not enough Milk")
              flag_good = False
              return flag_good
          elif resources["Coffee"] < needed_water:
              print("There is not enough Coffee")
              flag_good = False
              return flag_good
          #else:
            #print("Resources are NOT enough.")

    is_it_sufficient(order)

    prompt()



    def calculate_coin():
        global flag_good
        dime=int(input("How many dimes?"))
        nickle=int(input("How many nickles?"))
        quarters=int(input("How many quarters?"))
        pennies=int(input("How many pennies?"))
        given=int(dime*1+nickle*5+quarters*25+pennies*1)
        given=given/100
        if given==MENU[order]["cost"]:
            print("Enough coins.")
        elif given<MENU[order]["cost"]:
            print(f"NOT Enough coins. Here is your refund {given}")
            flag_good = False
        elif given>MENU[order]["cost"]:
            change=given-MENU[order]["cost"]
            print(f"Enough coins. Here is your change: {change:.2f}")

    prompt()
    def profit():
        resources["Money"]=resources["Money"]+MENU[order]["cost"]
        print("total money at the maschine: ",resources["Money"])




    def minus_recources():
        global flag_good
        if flag_good==True:
            print("Let's make coffee!")
            resources["Water"]=resources["Water"]-MENU[order]["ingredients"]["water"]
            resources["Milk"] =resources["Milk"] -MENU[order]["ingredients"]["milk"]
            resources["Coffee"] =resources["Coffee"]-MENU[order]["ingredients"]["coffee"]
            print("\n...")
            print("\n^^")
            print(f"Here is your {order}. Enjoya!☕")

    if is_it_sufficient(order)==True:
        calculate_coin()
        prompt()
        profit()
        prompt()
        minus_recources()
        prompt()
    else:
        print("Ciao\n")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")

        flag_good=True

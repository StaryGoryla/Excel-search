import openpyxl as xl
import commons
wb1 = xl.load_workbook("wingspan-20221201.xlsx")
sheet = wb1["Birds"]

user_input = input(f"1 - Birds exclusive to continents"
                   f"\n2 - Amount of birds with only one food type"
                   f"\n3 - Amount of birds able to live on a continent"
                   f"\n4 - Amount of birds feeding on a food type"
                   f"\n5 - Amount of birds by eggs max"
                   f"\n6 - Amount of birds by food cost"
                   f"\n7 - Exit"
                   f"\n>")
while True:
    if user_input == "1":
        sums, names = commons.sum_sole_hits_in_columns(28, 35)
        for i in range(0, len(sums)):
            print(f"There are {sums[i]} exclusive to {names[i]}, which amounts to {commons.percent_of_all(sums[i])}%.")
        user_input = input(">")
    if user_input == "2":
        sums, names = commons.sum_sole_hits_in_columns(17, 24)
        for i in range(0, len(sums)):
            print(f"There are {sums[i]} only feeding on {names[i]}, which amounts to {commons.percent_of_all(sums[i])}%.")
        user_input = input(">")
    if user_input == "3":
        for i in range(28, 35):
            sum, name = commons.sum_hits_in_column(i)
            print(f"There are {sum} able to live in {name}, which amounts to {commons.percent_of_all(sum)}%.")
        user_input = input(">")
    if user_input == "4":
        for i in range(17, 24):
            sum, name = commons.sum_hits_in_column(i)
            print(f"There are {sum} feeding on {name}, which amounts to {commons.percent_of_all(sum)}%.")
        user_input = input(">")
    if user_input == "5":
        sums, names = commons.sum_values_in_column(12)
        for i in range(0, len(sums)):
            print(f"There are {sums[i]} birds with maximum of {int(names[i])} eggs, which amounts to {commons.percent_of_all(sums[i])}%.")
        user_input = input(">")
    if user_input == "6":
        sums, names = commons.sum_hits_in_columns(17, 24)
        for i in range(0, len(sums)):
            print(f"There are {sums[i]} birds with {int(names[i])} food cost, which amounts to {commons.percent_of_all(sums[i])}%.")
        user_input = input(">")
    if user_input == "7":
        exit()
    else:
        input("Wrong option, choose another one: ")
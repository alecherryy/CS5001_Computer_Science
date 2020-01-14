'''
Alessia Pizzoccheri
Wholesale

Test Case #1
    3 pies crusts, 4 potatoes, 3 packages of meat, 1 pack of corn

Test Case #2
    1 pies crusts, 23 potatoes, 5 packages of meat, 2 pack of corn

Test Case #3
    5 pies crusts, 42 potatoes, 5 packages of meat, 8 pack of corn

Test Case #4
    2 pies crusts, 6 potatoes, 12 packages of meat, 1 pack of corn

Test Case #5
    0 pies crusts, 8 potatoes, 3 packages of meat, 4 pack of corn
'''

def main():
    crusts = int(input('How many pie crusts do you have? '))
    potatoes = int(input('How many potatoes do you have? '))
    meat = int(input('How many packs of meat do you have? '))
    corn = int(input('How many packs of corn do you have? '))

    # check if there are enough ingredients to make pies
    pies_from_crusts = crusts // 1
    pies_from_potatoes = potatoes // 6
    pies_from_meat = meat // 2
    pies_from_corn = corn // 2

    # calculate the max number of pies Kiki can make
    max_pies_possible = min(pies_from_crusts, pies_from_potatoes, pies_from_meat, pies_from_corn)

    # determine leftovers for each ingradient based on how many pies Kiki made
    leftover_crusts = crusts - (max_pies_possible * 1)
    leftover_potatoes = potatoes - (max_pies_possible * 6)
    leftover_meat = meat - (max_pies_possible * 2)
    leftover_corn = corn - (max_pies_possible * 2)

    print('Kiki made ', max_pies_possible, ' pies for the NSKS')
    print('You have donated the following leftover ingredients:')
    print(leftover_crusts, ' crust(s)')
    print(leftover_potatoes, ' potato(es)')
    print(leftover_meat, ' pack(s) of meat')
    print(leftover_corn, ' corn pack(s)')

main()

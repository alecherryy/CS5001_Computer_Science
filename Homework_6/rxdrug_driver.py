from rxdrug import drugs_list

ZERO = 0

class Patient:
    def __init__(self, name, ailment, drugs):
        self.name = name
        self.ailment = ailment
        self.drugs = drugs

    def __str__(self):
        # self.self = self 
        return '{n}'.format(n=self.name) + 'is taking {n}'.format(n=self.drug) + 'for {n}'.format(n=self.ailment)

def main():

    # call drugs_list()
    rx_dictionary = drugs_list()

    patients = []

    # open prescriptions file
    with open('prescriptions.txt') as prescriptions:
        lines = prescriptions.readlines()

        for line in lines:
            info = line.replace('\n','').split('|')
            patients.append(Patient(info[0],info[1],info[2].split(',')))
    
    # iterate through each patient 
    for patient in patients:
        print(patient.name,'is treating',patient.ailment)
        print('Current prescription:',', '.join(patient.drugs))

        try:
            # check for a second drug
            second_drug = patient.drugs[1]
            interactions = rx_dictionary[second_drug].check_interaction(patient.drugs)
            
            # if the drug list is not empty
            # print warning
            if len(interactions) > ZERO:
                print('Warning: drug-drug interaction between',', '.join(patient.drugs),'\n')
            else:
                print('No interactions!\n')
        # if the drug list is not empty
        except:
            print(patient.name,'is not taking a second drug, no risk of interactions\n')

main()
class RxDrug:
    def __init__(self, name, rx_ID):
        self.name = name
        self.rx_ID = rx_ID
        self.interaction_list = []

    def add_interaction(self, other_drug):
        if other_drug == "*":
            self.interaction_list = other_drug
        else:
            if other_drug not in self.interaction_list:
                self.interaction_list.append(other_drug)

    def check_interaction(self, other_drugs):
        interactions = []
        if self.interaction_list == "*":
            return other_drugs
        else:
            for drug in other_drugs:
                if drug in self.interaction_list:
                    interactions.append(drug)
            return interactions

    def set_description(self, description):
        self.description = description

    def __str__(self):
        # self.self = self 
        return 'This prescription is for {n}'.format(n=self.name)

def drugs_list():
    '''
        Name: drugs_list
        Parameter: none
        Return: dict
    '''
    drugs = {}

    # open drugs file
    with open('rxcui_drugs.txt') as drug_file:
        lines = drug_file.readlines()
        for line in lines:
            # split elements in each row
            params = line.replace('\n','').split('|')
            # instantiate RxDrug class
            rx = RxDrug(params[0], params[1])
            rx.set_description(params[2])
            for other_drug in params[3].split(','):
                rx.add_interaction(other_drug)
            # add each drug to the dictionary
            drugs[rx.name] = rx
    return drugs
import csv




class Settelment:
    def __init__(self, name, pop, religion, devout):
        self.name = name
        self.pop = pop
        self.religion = religion
        self.devout = devout




class settelmentmaker:
     def __init__(self, tablepath):
        self.tablepath = tablepath
        self.settelmentlist = []

     def makesettelment(self, row):


        missing_fields = []
        if not row.get('LocNameHeb'):
            missing_fields.append('LocNameHeb')

        if not row.get('pop_approx'):
            missing_fields.append('pop_approx')
        if not isinstance(row.get('pop_approx'), int):
            missing_fields.append('pop_approx')

        if not row.get('ReligionHeb'):
            missing_fields.append('ReligionHeb')
        if not row.get('hh_MidatDatiyut'):
            missing_fields.append('hh_MidatDatiyut')


        if missing_fields:
            raise ValueError(f"Missing fields: {', '.join(missing_fields)}")
        
        name = row['LocNameHeb']
        pop = row['pop_approx']
        religion = row['ReligionHeb']
        devout = row['hh_MidatDatiyut']


        return Settelment(name, pop, religion, devout)


     def makeList(self):
        settelments = []
        with open(self.tablepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate (reader, start=2):
                try:
                    settelment = self.makesettelment(row)
                    settelments.append(settelment)
                except ValueError as e:
                    print(f"Error processing row {i}: {e}")
                    continue
        return settelments




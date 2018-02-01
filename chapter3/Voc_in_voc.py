import pprint

people = {}
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home planet': 'Betelgeuse Seven'}
people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home planet': 'Earth'}
people['Trillian'] = {'Name': 'Ford Prefect',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home planet': 'Earth'}
people['Marvin'] = {'Name': 'Ford Prefect',
                    'Gender': 'Unknown',
                    'Occupation': 'Paranoid Android',
                    'Home planet': 'Unknown'}
pprint.pprint(people)
print(people['Arthur'])
print(people['Arthur']['Occupation'])

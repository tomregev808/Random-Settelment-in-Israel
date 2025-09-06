import requests
import random



import requests
class get_info:
    def get_name ():


        d = requests.get ("https://data.gov.il/api/3/action/datastore_search?resource_id=5c78e9fa-c2e2-4771-93ff-7f400a12f7ba")

        dict = d.json()

        list = dict["result"]["records"]
        list.pop(0)

        names = []
        for record in list:
            names.append (record ["שם_ישוב"])

        name = random.choice(names)

        return name

import json
import os, sys

cwd = os.path.dirname(__file__)

class Pet(object):

    def get_all_pets(self):
        pets = self.read_from_file()
        pets_in_store = []
        for k, v in pets.items():
            current_pet = {"id": k, **v}
            pets_in_store.append(current_pet)

        return pets

    def get_pet(self,id):
        assert type(id) is int
        pets = self.read_from_file()
        pet = pets[str(id)]
        pet["id"] = id
        return pet

    def read_from_file(self):
        jsonfile = os.path.join(cwd, 'pets.json')

        with open(jsonfile, "r") as pets:
            return json.loads(pets.read())



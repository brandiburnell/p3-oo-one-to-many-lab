class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, ownner=""):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("help")
        self.name = name
        self.owner = ownner
        self.pet_type = pet_type
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("help")
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
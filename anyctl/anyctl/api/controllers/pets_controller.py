import connexion 

from anyctl.resources import pet_resources as pet

def get_pet(pet_id):
    """ Return Pets
    
    :param body:
    :type body: dict | bytes

    :rtype: None  
    """
    p = pet.Pet()
    
    try:
        return p.get_pet(pet_id), 200
    except KeyError:
       return {"error" : "Key not found"}, 404 


def get_all_pets():
    """ Return Pets
    
    :param body:
    :type body: dict | bytes
pets
    :rtype: None  
    """
    p = pet.Pet()
    return p.get_all_pets() , 200

from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    # Add the dog object to the session and commit to persist it in the database
    session.add(dog)
    session.commit()

def get_all(session):
    # Return all instances of Dog from the database
    return session.query(Dog).all()

def find_by_name(session, name):
    # Query the database for a dog with a specific name
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    # Query the database for a dog with a specific id
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    # Query the database for a dog with a specific name and breed
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    # Update the breed of the given dog and commit the changes
    dog.breed = breed
    session.commit()

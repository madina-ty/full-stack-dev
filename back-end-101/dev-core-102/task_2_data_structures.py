def create_participant(name, age, email):
    return {'name':name, 'age': age, 'email': email}

def add_participant(participants, new_participant):
    participants.append(new_participant)

def remove_participant(participants, name):
    for participant in participants: 
        if participant['name'] == name:
            participants.remove(participant)
            return 
        print(f"The participant with the name {name} was not found")

def print_participants(participants):
    for participant in participants:
        print(f"Name:{participant['name']}, Age: {participant['age']}, Email: {participant['email']}")

participants = []

participants = []

participant1 = create_participant("Иван Петров", 30, "ivan@example.com")
participant2 = create_participant("Мария Иванова", 25, "maria@example.com")
add_participant(participants, participant1)
add_participant(participants, participant2)

print_participants(participants)

remove_participant(participants, "Иван Петров")

print_participants(participants)

import random

class Event:
    def init(self, event_name, points):
        self.event_name = event_name
        self.points = points

class Participant:
    def init(self, name):
        self.name = name
        self.total_points = 0

    def add_points(self, points):
        self.total_points += points

class Team:
    def init(self, team_name):
        self.team_name = team_name
        self.members = []

    def add_member(self, participant):
        self.members.append(participant)

    def get_total_points(self):
        return sum(member.total_points for member in self.members)

    def add_points(self, points):
        for member in self.members:
            member.add_points(points)

class Tournament:
    def init(self):
        self.events = []
        self.teams = []
        self.individuals = []

    def add_event(self, event):
        self.events.append(event)

    def add_team(self, team):
        self.teams.append(team)

    def add_individual(self, participant):
        self.individuals.append(participant)

    def run_tournament(self):
        for event in self.events:
            print(f"Running event: {event.event_name}")

            # Shuffle participants to randomize the order
            random.shuffle(self.teams)
            random.shuffle(self.individuals)

            # Logic to perform the event and assign points to participants
            rank = 1
            for team in self.teams:
                team.add_points(random.randint(1, 100))  # Replace with your event scoring logic
                print(f"Team {team.team_name} scored {team.get_total_points()} points.")
                rank += 1

            for individual in self.individuals:
                individual.add_points(random.randint(1, 100))  # Replace with your event scoring logic
                print(f"Individual {individual.name} scored {individual.total_points} points.")

            print(f"Event {event.event_name} completed.\n")

def print_main_menu():
    print("\tTournament Management System")
    print("1. Add new event")
    print("2. Add new team")
    print("3. Add new participant")
    print("4. Run tournament")
    print("0. Exit")

def add_new_event(tournament):
    # Implementation for adding a new event
    event_name = input("Enter event name: ")
    points = int(input("Enter event points: "))
    tournament.add_event(Event(event_name, points))
    print("Event added successfully!")

def add_new_team(tournament):
    # Implementation for adding a new team
    team_name = input("Enter team name: ")
    team = Team(team_name)

    # Input for team members
    for _ in range(5):
        member_name = input(f"Enter member name for Team {team_name}: ")
        team.add_member(Participant(member_name))

    tournament.add_team(team)
    print("Team added successfully!")

def add_new_participant(tournament):
    # Implementation for adding a new participant
    participant_name = input("Enter participant name: ")
    tournament.add_individual(Participant(participant_name))
    print("Participant added successfully!")

def main():
    tournament = Tournament()

    while True:
        print_main_menu()

        select = int(input("Choose the section: "))

        if select == 0:
            print("Thank You!!")
            break
        elif select == 1:
            add_new_event(tournament)
        elif select == 2:
            add_new_team(tournament)
        elif select == 3:
            add_new_participant(tournament)
        elif select == 4:
            tournament.run_tournament()
        else:
            print("Invalid selection. Please choose a number between 0 and 4.")

if name == "main":
    main()
    
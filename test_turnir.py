import unittest
from unittest.mock import patch
from io import StringIO
from turnir import Tournament

class TestTournament(unittest.TestCase):
    def setUp(self):
        self.tournament = Tournament()

    def test_register_individual(self):
        with patch('builtins.input', side_effect=["John Doe"]):
            self.tournament.register_individual()
        self.assertEqual(len(self.tournament.individuals), 1)

    def test_register_individual_empty_name(self):
        with patch('builtins.input', side_effect=[""]):
            self.tournament.register_individual()
        self.assertEqual(len(self.tournament.individuals), 0)

    def test_register_team(self):
        with patch('builtins.input', side_effect=["Team A", "John", "Jane", "Bob", "Alice", "Charlie"]):
            self.tournament.register_team()
        self.assertEqual(len(self.tournament.teams), 1)

    def test_register_team_empty_name(self):
        with patch('builtins.input', side_effect=["", "John", "Jane", "Bob", "Alice", "Charlie"]):
            self.tournament.register_team()
        self.assertEqual(len(self.tournament.teams), 0)

    def test_register_team_empty_member_name(self):
        with patch('builtins.input', side_effect=["Team A", "", "Jane", "Bob", "Alice", "Charlie"]):
            self.tournament.register_team()
        self.assertEqual(len(self.tournament.teams), 0)

    def test_register_one_event(self):
        self.tournament.individuals.append({"name": "John", "events": {}})
        with patch('builtins.input', side_effect=["John", "Event A"]):
            self.tournament.register_one_event()
        self.assertEqual(len(self.tournament.individuals[0]["events"]), 1)

    def test_register_one_event_empty_name(self):
        with patch('builtins.input', side_effect=["", "Event A"]):
            self.tournament.register_one_event()
        self.assertEqual(len(self.tournament.individuals), 0)

    def test_record_event_results(self):
        self.tournament.individuals.append({"name": "John", "events": {"Tournament": 0}})

        with patch('builtins.input', side_effect=["Tournament", "John", "10"] * 5):
            self.tournament.record_event_results()

        self.assertEqual(self.tournament.individuals[0]["events"]["Tournament"], 10)

    def test_view_event_standings(self):
        self.tournament.individuals.append({"name": "John", "events": {"Event A": 10}})
        with patch('builtins.input', side_effect=["Event A"]):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.tournament.view_event_standings()
                expected_output = "----- Standings for Event A -----\n1. John - 10 points"
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_view_registered_participants(self):
        self.tournament.individuals.append({"name": "John", "events": {}})
        self.tournament.teams.append({"team_name": "Team A", "members": ["Alice", "Bob"], "events": {}})
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.tournament.view_registered_participants()
            expected_output = "----- Registered Participants -----\nIndividuals:\nJohn\nTeams:\nTeam A: Alice, Bob"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_run_tournament_exit(self):
        with patch('builtins.input', return_value="7"):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.tournament.run_tournament()
                expected_output = '----- Tournament Menu -----\n1. Register as an individual\n2. Register as a team\n3. Register for one event only\n4. View registered participants\n5. Record event results\n6. View event standings\n7. Exit\nExiting the tournament...'
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()

#  online voting system through python using oops....
print("\n")
print("\t\tWELCOME TO ONLINE VOTING SYSTEM...\n")
print("\tREMINDER PORTAL [1,2,4] ARE ONLY FOR GOVERNMENT")

class GovernmentPortal:
    def __init__(self):
        self.password = 'govt'

    def verify_password(self, user_password):
        return user_password == self.password


class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0


class Voter:
    def __init__(self, name, unique_id):
        self.name = name
        self.unique_id = unique_id


class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = []
        self.voted_ids = set()

    def register_candidate(self, name):
        candidate = Candidate(name)
        self.candidates.append(candidate)
        print("\n Candidate Registered thankyou...")

    def register_voter(self, name, unique_id):
        voter = Voter(name, unique_id)
        self.voters.append(voter)
        print(f"voter: {name} Registered")

    def do_voting(self):
        if not self.candidates or not self.voters:
            print("Registration required for candidates and voters.")
        else:
            voter_id = int(input("Enter your 3-digit ID: "))
            if voter_id in self.voted_ids:
                print("You already voted.")
            else:
                if any(voter.unique_id == voter_id for voter in self.voters):
                    self.display_candidates()
                    candidate_index = int(input("Enter the index of the candidate you want to vote for: "))
                    if 1 <= candidate_index <= len(self.candidates):
                        candidate = self.candidates[candidate_index - 1]
                        candidate.votes += 1
                        self.voted_ids.add(voter_id)
                        print(f"You voted for {candidate.name}")
                    else:
                        print("Invalid candidate index.")
                else:
                    print("You are not a registered voter.")

    def show_results(self):
        if not self.voters:
            print("No votes recorded yet.")
        else:
            for candidate in self.candidates:
                print(f"\n{candidate.name}: {candidate.votes} votes")
            

    def display_candidates(self):
        print("Candidates:")
        for i, candidate in enumerate(self.candidates, 1):
            print(f"{i}. {candidate.name}")

# Creating an instance of the GovernmentPortal
govt_portal = GovernmentPortal()
# Creating an instance of the VotingSystem
voting_system = VotingSystem()

while True:
    print("\n1. FOR CANDIDATE REGISTRATION (Government Portal)")
    print("2. FOR VOTER REGISTRATION (Government Portal)")
    print("3. DO VOTING")
    print("4. SHOW RESULT (Government Portal)")
    print("5. EXIT")
    num = int(input("Select number: "))

    if num == 1:
        govt_password = input("Enter government portal password: ")
        if govt_portal.verify_password(govt_password):
            candidate_name = input("Enter candidate name: ")
            voting_system.register_candidate(candidate_name)
        else:
            print("Invalid password. Access denied.")
    elif num == 2:
        govt_password = input("Enter government portal password: ")
        if govt_portal.verify_password(govt_password):
            voter_name = input("Enter voter name: ")
            unique_id = int(input("Enter unique ID of the voter: "))
            voting_system.register_voter(voter_name, unique_id)
        else:
            print("Invalid password. Access denied.")
    elif num == 3:
        voting_system.do_voting()
    elif num == 4:
        govt_password = input("Enter government portal password: ")
        if govt_portal.verify_password(govt_password):
            voting_system.show_results()
        else:
            print("Invalid password. Access denied.")
    elif num == 5:
        break
    else:
        print("Select another number")

# --------------------------------------------------------------------------------------------------

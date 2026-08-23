class Candidate:
    def __init__(
        self,
        name,
        python,
        dsa,
        projects,
        experience,
        communication
    ):
        self.name = name
        self.python = python
        self.dsa = dsa
        self.projects = projects
        self.experience = experience
        self.communication = communication

    def calculate_score(self):
        # Convert projects and experience into scores out of 10
        project_score = min(self.projects * 2, 10)
        experience_score = min(self.experience * 5, 10)

        # Weighted scoring
        score = (
            self.python * 0.25 +
            self.dsa * 0.20 +
            project_score * 0.25 +
            experience_score * 0.15 +
            self.communication * 0.15
        )

        return round(score, 2)


def select_members(candidates, number_of_members):
    # Sort candidates from highest to lowest score
    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: candidate.calculate_score(),
        reverse=True
    )

    # Select required number of members
    return ranked_candidates[:number_of_members]


# -----------------------------------------
# Candidate Portfolio Data
# -----------------------------------------

candidates = [
    Candidate("Rahul", 9, 8, 5, 2, 8),
    Candidate("Aman", 7, 9, 4, 1, 7),
    Candidate("Priya", 9, 9, 6, 3, 9),
    Candidate("Rohit", 6, 7, 3, 1, 8),
    Candidate("Anjali", 8, 8, 5, 2, 9),
    Candidate("Karan", 7, 6, 2, 1, 6)
]


# -----------------------------------------
# Select Members
# -----------------------------------------

number_of_members = 3

selected_members = select_members(
    candidates,
    number_of_members
)


# -----------------------------------------
# Display Selected Members
# -----------------------------------------

print("\n" + "=" * 50)
print("      PORTFOLIO MEMBER SELECTION SYSTEM")
print("=" * 50)

print("\nSELECTED MEMBERS\n")

for rank, candidate in enumerate(selected_members, start=1):
    print(
        f"{rank}. {candidate.name}"
        f" | Score: {candidate.calculate_score()}/10"
    )


# -----------------------------------------
# Display Complete Ranking
# -----------------------------------------

print("\n" + "=" * 50)
print("           COMPLETE RANKING")
print("=" * 50)

ranked_candidates = sorted(
    candidates,
    key=lambda candidate: candidate.calculate_score(),
    reverse=True
)

for rank, candidate in enumerate(ranked_candidates, start=1):
    print(
        f"{rank}. {candidate.name}"
        f" | Score: {candidate.calculate_score()}/10"
    )

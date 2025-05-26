# 🗳️ Online Voting System using Python (OOP)

A simple **command-line voting system** implemented in Python using **Object-Oriented Programming (OOP)** principles. The system allows **secure registration of candidates and voters** via a **government portal**, voting by eligible voters, and **result display**.

---

## 📌 Features

- 🔐 **Password-Protected Government Portal**
  - Only government (via password) can register candidates/voters or view results.
- 🧑‍💼 **Candidate Registration**
- 🧍‍♂️ **Voter Registration**
- ✅ **One-Person-One-Vote System**
- 📊 **Voting Results Display**
- 🧠 **Encapsulated logic** using Python classes

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## 🧱 Class Structure

### 1. `GovernmentPortal`
Handles government authentication with a hardcoded password (`'govt'`).

### 2. `Candidate`
Stores candidate details and vote count.

### 3. `Voter`
Stores voter details including unique ID.

### 4. `VotingSystem`
Main logic:
- Register candidates and voters
- Prevent double voting using `voted_ids`
- Collect and display results

---

## 📋 How to Run

1. Ensure Python 3 is installed.
2. Clone or copy the project code.
3. Run the script:
   ```bash
   python voting_system.py



1. Candidate Registration (Government Portal)
2. Voter Registration (Government Portal)
3. Do Voting
4. Show Result (Government Portal)
5. Exit

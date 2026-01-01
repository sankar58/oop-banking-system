# 🏦 OOP Banking System (Python)

A real-world Python project demonstrating all **four pillars of Object-Oriented Programming (OOP)** —  
**Encapsulation, Abstraction, Inheritance, and Polymorphism** — using an Online Banking System example.  
Designed for **learning, interviews, and resume projects**.

---

## 🚀 Features
- Multiple account types (Savings & Current)
- Secure deposit and withdrawal operations
- Interest calculation based on account type
- Clean OOP design with abstraction and composition
- Easily extensible architecture

---

## 🧠 OOP Concepts Demonstrated

### 1️⃣ Encapsulation
- Account balance is protected from direct access
- Accessed only via class methods
```python
self._balance
self.__account
```

### 2️⃣ Abstraction
- Abstract base class enforces method implementation
```python
from abc import ABC, abstractmethod
```

### 3️⃣ Inheritance
- SavingsAccount and CurrentAccount inherit from Account
```python
class SavingsAccount(Account)
class CurrentAccount(Account)
```

### 4️⃣ Polymorphism
- Same method, different behavior
```python
account.calculate_interest()
```

---

## 🏗️ Design Pattern
### Composition (HAS-A Relationship)
- A Customer **has** an Account
- A Customer **is not** an Account

```
Customer HAS-A Account
SavingsAccount IS-A Account
```

---

## 📂 Project Structure
```
oop-banking-system/
│
├── banking_system.py
└── README.md
```

---

## ▶️ How to Run
```bash
git clone https://github.com/YOUR_USERNAME/oop-banking-system.git
cd oop-banking-system
python banking_system.py
```

---

## 🧪 Sample Output
```
₹2000 deposited. New balance: ₹7000
Savings Interest: ₹280.0
₹3000 withdrawn. New balance: ₹7000
Current Account has no interest
```

---

## 🛠️ Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- abc module (Abstract Base Classes)

---

## 📈 Future Improvements
- Loan & Fixed Deposit accounts
- Transaction history
- REST API using Flask
- Authentication system
- Unit testing

---

## 🎯 Learning Outcomes
- Practical understanding of all OOP pillars
- Clear distinction between inheritance and composition
- Real-world system modeling in Python
- Clean, maintainable code

---

## 👤 Author
**Sankar Ayudham**  
GitHub: https://github.com/YOUR_USERNAME  
LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN  

⭐ If you like this project, give it a star on GitHub!

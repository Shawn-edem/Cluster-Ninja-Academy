### **Python Assignment: Advanced Python Programming**

#### **Objective**:
To enhance your Python skills by working on more complex tasks involving classes, inheritance, modules, decorators, and working with external libraries.

#### **Instructions**:
- Complete the following exercises in a Jupyter notebook (`.ipynb` file).
- Include comments in your code to explain your logic.
- Submit your assignment by the due date (Monday).
- Ensure your code runs without errors.
- Include your name and the date in the first cell of the notebook.

---

#### **Part 1: Classes and Inheritance**
1. **Bank Account Class**:
   - Create a `BankAccount` class with the following attributes:
     - `account_holder`: Name of the account holder.
     - `balance`: The current balance (initially set to 0).
     - Include methods for:
       - `deposit(amount)`: Increases the balance by the specified amount.
       - `withdraw(amount)`: Decreases the balance by the specified amount if there are sufficient funds; otherwise, print an error message.
       - `check_balance()`: Prints the current balance.

   - Extend the `BankAccount` class with a `SavingsAccount` subclass that includes an additional method `apply_interest(rate)` which adds interest to the balance based on a given rate (e.g., 5% interest).

   **Example**:
   ```python
   class BankAccount:
       def __init__(self, account_holder):
           self.account_holder = account_holder
           self.balance = 0
       
       def deposit(self, amount):
           self.balance += amount
           print(f"{amount} deposited. New balance: {self.balance}")
       
       def withdraw(self, amount):
           if amount > self.balance:
               print("Insufficient funds")
           else:
               self.balance -= amount
               print(f"{amount} withdrawn. New balance: {self.balance}")
       
       def check_balance(self):
           print(f"Balance: {self.balance}")

   class SavingsAccount(BankAccount):
       def apply_interest(self, rate):
           interest = self.balance * rate / 100
           self.balance += interest
           print(f"Interest applied: {interest}. New balance: {self.balance}")
   ```

2. **Vehicle Inheritance**:
   - Create a `Vehicle` class with attributes for `make`, `model`, and `year`.
   - Create a `Car` subclass that adds an attribute for `number_of_doors` and a method to `display_info()` which prints out all the details of the car.

   **Example**:
   ```python
   class Vehicle:
       def __init__(self, make, model, year):
           self.make = make
           self.model = model
           self.year = year
       
       def display_info(self):
           print(f"Vehicle Info: {self.year} {self.make} {self.model}")

   class Car(Vehicle):
       def __init__(self, make, model, year, number_of_doors):
           super().__init__(make, model, year)
           self.number_of_doors = number_of_doors
       
       def display_info(self):
           super().display_info()
           print(f"Number of Doors: {self.number_of_doors}")
   ```

---

#### **Part 2: Working with Modules and External Libraries**
1. **Matplotlib Visualization**:
   - Install and use the `matplotlib` library to create a bar chart of your top 5 favorite movies and their ratings out of 10.

   **Example**:
   ```python
   import matplotlib.pyplot as plt

   movies = ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5']
   ratings = [8, 9, 7, 8.5, 9.5]

   plt.bar(movies, ratings)
   plt.title("Favorite Movies and Ratings")
   plt.xlabel("Movies")
   plt.ylabel("Ratings out of 10")
   plt.show()
   ```

2. **Using Requests to Fetch Data**:
   - Use the `requests` library to fetch data from a public API (e.g., JSONPlaceholder) and display it in a readable format. Choose any data you find interesting (e.g., posts, comments).

   **Example**:
   ```python
   import requests

   url = "https://jsonplaceholder.typicode.com/posts"
   response = requests.get(url)

   if response.status_code == 200:
       data = response.json()
       for post in data[:5]:  # Display the first 5 posts
           print(f"Title: {post['title']}")
           print(f"Body: {post['body']}\n")
   else:
       print("Failed to retrieve data")
   ```

---

#### **Part 3: Decorators and Generators**
1. **Function Execution Timer**:
   - Write a decorator that measures the time it takes for a function to execute. Apply this decorator to a function that calculates the factorial of a number using recursion.

   **Example**:
   ```python
   import time

   def execution_time(func):
       def wrapper(*args, **kwargs):
           start_time = time.time()
           result = func(*args, **kwargs)
           end_time = time.time()
           print(f"Execution Time: {end_time - start_time} seconds")
           return result
       return wrapper

   @execution_time
   def factorial(n):
       if n == 1:
           return 1
       else:
           return n * factorial(n-1)

   print(factorial(10))
   ```

2. **Prime Number Generator**:
   - Create a generator that yields prime numbers indefinitely. Write a function that prints the first 10 prime numbers generated by your generator.

   **Example**:
   ```python
   def is_prime(n):
       if n <= 1:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True

   def prime_generator():
       num = 2
       while True:
           if is_prime(num):
               yield num
           num += 1

   primes = prime_generator()
   for _ in range(10):
       print(next(primes))
   ```

---

#### **Part 4: Advanced File Handling**
1. **CSV File Operations**:
   - Write a program that reads a CSV file containing data on students and their scores. Calculate and print the average score for each student. Save the results to a new CSV file called `average_scores.csv`.

   **Example**:
   ```python
   import csv

   with open('students_scores.csv', mode='r') as file:
       reader = csv.DictReader(file)
       averages = {}
       for row in reader:
           name = row['Name']
           scores = list(map(int, row['Scores'].split(',')))
           averages[name] = sum(scores) / len(scores)

   with open('average_scores.csv', mode='w') as file:
       writer = csv.writer(file)
       writer.writerow(['Name', 'Average Score'])
       for name, avg in averages.items():
           writer.writerow([name, avg])
   ```

---

### **Extra Credit (Optional)**
1. **Web Scraping**:
   - Use the `BeautifulSoup` library to scrape the headlines from a news website of your choice. Save the headlines to a text file called `headlines.txt`.

   **Example**:
   ```python
   import requests
   from bs4 import BeautifulSoup

   url = "https://www.bbc.com/news"
   response = requests.get(url)
   soup = BeautifulSoup(response.text, 'html.parser')

   headlines = [h3.text for h3 in soup.find_all('h3')]

   with open('headlines.txt', 'w') as file:
       for headline in headlines:
           file.write(f"{headline}\n")
   ```

---

### **Additional Resources**:
- [Real Python](https://realpython.com) - Great tutorials on Python topics.
- [W3Schools Python Tutorial](https://www.w3schools.com/python/) - Simple explanations and examples.
- [Geeks for Geeks Python Programming](https://www.geeksforgeeks.org/python-programming-language/) - More in-depth examples and explanations.

---

### **Submission**:
- Submit your Jupyter notebook (`.ipynb` file) with all the completed exercises.
- Make sure to include your name and the date at the top of the notebook.
- Submit to this email address: akinloluojo1@gmail.com

---


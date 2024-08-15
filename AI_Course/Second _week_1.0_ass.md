---

### **Python Assignment: Intermediate Python Programming**

#### **Objective**:
To deepen your understanding of Python by working on more complex problems that involve loops, lists, dictionaries, file handling, and exception handling.

#### **Instructions**:
- Complete the following exercises in a Jupyter notebook (`.ipynb` file).
- Include comments in your code to explain your logic.
- Submit your assignment by the due date (Monday).
- Ensure your code runs without errors.
- Include your name and the date in the first cell of the notebook.

---

#### **Part 1: Loops and Lists**
1. **List Operations**:
   - Create a list of 10 integers. Write a program that performs the following operations:
     - Print the sum of all elements.
     - Print the largest and smallest elements in the list.
     - Sort the list in ascending and descending order, then print both.

   **Example**:
   ```python
   numbers = [23, 12, 9, 34, 55, 78, 4, 89, 21, 17]
   
   print("Sum:", sum(numbers))
   print("Largest:", max(numbers))
   print("Smallest:", min(numbers))
   
   numbers.sort()
   print("Ascending Order:", numbers)
   
   numbers.sort(reverse=True)
   print("Descending Order:", numbers)
   ```

2. **Fibonacci Sequence**:
   - Write a program that generates the first 10 numbers of the Fibonacci sequence using a loop and stores them in a list. Print the list.

   **Example**:
   ```python
   fibonacci = [0, 1]
   for i in range(8):
       fibonacci.append(fibonacci[-1] + fibonacci[-2])
   print("Fibonacci Sequence:", fibonacci)
   ```

---

#### **Part 2: Dictionaries**
1. **Student Grades**:
   - Create a dictionary to store the names and grades of 5 students. Write a program that calculates and prints the average grade.

   **Example**:
   ```python
   grades = {
       "Alice": 85,
       "Bob": 78,
       "Charlie": 92,
       "Diana": 88,
       "Eve": 76
   }
   
   average_grade = sum(grades.values()) / len(grades)
   print("Average Grade:", average_grade)
   ```

2. **Phonebook**:
   - Create a program that allows the user to add, remove, or search for contacts in a phonebook stored as a dictionary. Each contact should have a name and a phone number.

   **Example**:
   ```python
   phonebook = {}
   
   def add_contact(name, number):
       phonebook[name] = number
   
   def remove_contact(name):
       if name in phonebook:
           del phonebook[name]
       else:
           print("Contact not found.")
   
   def search_contact(name):
       return phonebook.get(name, "Contact not found.")
   
   add_contact("Alice", "123-456-7890")
   add_contact("Bob", "098-765-4321")
   
   print("Phonebook:", phonebook)
   print("Search Alice:", search_contact("Alice"))
   ```

---

#### **Part 3: File Handling**
1. **Writing to a File**:
   - Write a program that writes the names and grades of students to a text file called `grades.txt`.

   **Example**:
   ```python
   grades = {
       "Alice": 85,
       "Bob": 78,
       "Charlie": 92
   }
   
   with open("grades.txt", "w") as file:
       for name, grade in grades.items():
           file.write(f"{name}: {grade}\n")
   ```

2. **Reading from a File**:
   - Write a program that reads the contents of `grades.txt` and prints each line.

   **Example**:
   ```python
   with open("grades.txt", "r") as file:
       for line in file:
           print(line.strip())
   ```

---

#### **Part 4: Exception Handling**
1. **Division Calculator**:
   - Write a program that takes two numbers from the user and divides them. Use a `try-except` block to handle division by zero.

   **Example**:
   ```python
   try:
       num1 = float(input("Enter the first number: "))
       num2 = float(input("Enter the second number: "))
       result = num1 / num2
       print("Result:", result)
   except ZeroDivisionError:
       print("Error: Cannot divide by zero.")
   ```

2. **File Not Found**:
   - Write a program that attempts to open a non-existent file and handles the `FileNotFoundError` exception.

   **Example**:
   ```python
   try:
       with open("non_existent_file.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("Error: File not found.")
   ```

---

#### **Extra Credit (Optional)**
1. **Prime Numbers**:
   - Write a program that finds all prime numbers between 1 and 100 and writes them to a file called `primes.txt`.

   **Example**:
   ```python
   def is_prime(n):
       if n <= 1:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True
   
   with open("primes.txt", "w") as file:
       for number in range(1, 101):
           if is_prime(number):
               file.write(f"{number}\n")
   ```

---

### **Submission**:
- Submit your Jupyter notebook (`.ipynb` file) with all the completed exercises.
- Make sure to include your name and the date at the top of the notebook.
- Submit to this email address: akinloluojo1@gmail.com

---

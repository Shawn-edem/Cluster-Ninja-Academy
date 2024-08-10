### First Week Assignment
---

### **Python Assignment: Introduction to Python Programming**

#### **Objective**:
To reinforce the concepts learned in class by applying them to practical coding problems. This assignment covers basic Python syntax, variables, data types, operations, control flow, and functions.

#### **Instructions**:
- Complete the following exercises.
- Write your code in a `.py` file and include comments to explain your code.
- Submit your assignment by the due date Monday.
- Be sure to test your code and ensure it runs without errors.

---

#### **Part 1: Writing Your First Program**
1. **Simple Print Statement**:
   - Write a Python program that prints `"Welcome to Python Programming!"` to the console.

   **Example Output**:
   ```
   Welcome to Python Programming!
   ```

---

#### **Part 2: Variables and Data Types**
1. **Personal Information**:
   - Create variables to store your name, age, and whether you are a student (use `True` or `False`).
   - Print each variable.

   **Example**:
   ```python
   name = "Alice"
   age = 20
   is_student = True

   print("Name:", name)
   print("Age:", age)
   print("Is a student:", is_student)
   ```

2. **Type Conversion**:
   - Write a program that converts a given integer (e.g., `25`) to a string and then concatenates it with another string.

   **Example**:
   ```python
   age = 25
   age_str = str(age)
   message = "I am " + age_str + " years old."
   print(message)
   ```

---

#### **Part 3: Basic Operations**
1. **Arithmetic Operations**:
   - Write a program that performs the following operations on two numbers (e.g., `10` and `5`):
     - Addition
     - Subtraction
     - Multiplication
     - Division
     - Floor Division
     - Modulus
   - Print the result of each operation.

   **Example**:
   ```python
   num1 = 10
   num2 = 5

   print("Addition:", num1 + num2)
   print("Subtraction:", num1 - num2)
   print("Multiplication:", num1 * num2)
   print("Division:", num1 / num2)
   print("Floor Division:", num1 // num2)
   print("Modulus:", num1 % num2)
   ```

2. **String Operations**:
   - Write a program that takes a string, converts it to uppercase, and prints its length.

   **Example**:
   ```python
   text = "python programming"
   upper_text = text.upper()
   text_length = len(upper_text)

   print("Uppercase Text:", upper_text)
   print("Length of Text:", text_length)
   ```

---

#### **Part 4: Control Flow**
1. **Age Classification**:
   - Write a program that asks the user to enter their age and prints whether they are a child (age < 13), a teenager (13 ≤ age < 18), or an adult (age ≥ 18).

   **Example**:
   ```python
   age = int(input("Enter your age: "))

   if age < 13:
       print("You are a child.")
   elif 13 <= age < 18:
       print("You are a teenager.")
   else:
       print("You are an adult.")
   ```

2. **Number Guessing Game**:
   - Write a program that generates a random number between 1 and 10 and asks the user to guess the number. Use a `while` loop to keep asking until they guess correctly.

   **Example**:
   ```python
   import random

   number_to_guess = random.randint(1, 10)
   guess = int(input("Guess a number between 1 and 10: "))

   while guess != number_to_guess:
       if guess < number_to_guess:
           print("Too low! Try again.")
       else:
           print("Too high! Try again.")
       guess = int(input("Guess again: "))

   print("Congratulations! You guessed the correct number.")
   ```

---

#### **Part 5: Functions**
1. **Simple Greeting Function**:
   - Write a function called `greet` that takes a person's name as an argument and prints a greeting.

   **Example**:
   ```python
   def greet(name):
       print("Hello, " + name + "!")

   greet("Alice")
   greet("Bob")
   ```

2. **Sum Function**:
   - Write a function that takes two numbers as arguments, adds them, and returns the result. Call the function with different sets of numbers and print the results.

   **Example**:
   ```python
   def add_numbers(a, b):
       return a + b

   result1 = add_numbers(10, 5)
   result2 = add_numbers(7, 3)
   print("Sum 1:", result1)
   print("Sum 2:", result2)
   ```

---

#### **Extra Credit (Optional)**
1. **Palindrome Checker**:
   - Write a program that checks whether a given string is a palindrome (a word that reads the same backward as forward).

   **Example**:
   ```python
   def is_palindrome(word):
       return word == word[::-1]

   word = input("Enter a word: ")
   if is_palindrome(word):
       print(word, "is a palindrome!")
   else:
       print(word, "is not a palindrome.")
   ```

---

### **Submission**:
- Submit your `.py` file with all the completed exercises when you save it.
- Do a screenshot and put it in .docx
- Make sure to include your name and date at the top of the file as comments.
- Submit to this mail address akinloluojo1@gmail.com

---


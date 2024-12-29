# codtech-task-2
PASSWORD STRENGTH CHECKER

NAME : SARANYA V 
COMPANY : CODTECH IT SOLUTIONS
ID : CT08FJW 
DOMAIN : CYBERSECURITY & ETHICAL HACKING 
DURATIONS : DECEMBER 20 TO JANUARY 20
MENTOR : MUZAMMIL AHAMED


1. Password Evaluation Criteria:
   
Length (length_criteria): The password must be at least 8 characters long.
Uppercase (has_uppercase): The password must contain at least one uppercase letter.
Lowercase (has_lowercase): The password must contain at least one lowercase letter.
Digit (has_digit): The password must contain at least one digit.
Special character (has_special): The password must contain at least one special character from the set [@$!%*?&#].
Uniqueness (is_unique): The password must contain more than half of its characters as unique characters.

2. Strength Calculation:
The password is evaluated against these criteria, and a strength_score is calculated as the sum of all criteria that the password meets (i.e., each True condition adds 1 to the score).
If all 6 criteria are met, the score is 6, and the password is considered "Strong."
If 4 or 5 criteria are met, the score is between 4 and 5, and the password is rated "Moderate."
If fewer than 4 criteria are met, the score is less than 4, and the password is rated "Weak."

3. Feedback:
If the password does not meet a criterion, the corresponding suggestion is added to the feedback list.
These suggestions are printed out to help the user improve their password.

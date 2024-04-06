import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

# Inserir dados na tabela programming_task
tasks = [
    ('FizzBuzz', 'Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".', 1, 3),
    ('Palindrome', 'Write a function that checks whether a given word or phrase is a palindrome. A palindrome is a word or phrase that reads the same backwards as forwards.', 2, 2),
    ('Anagram', 'Write a function that checks whether two given words are anagrams. An anagram is a word or phrase formed by rearranging the letters of another, such as cinema, formed from iceman.', 3, 1),
    ('Longest Substring Without Repeating Characters', 'Write a function that returns the length of the longest substring without repeating characters from a given string.', 4, 1)
]
cur.executemany("INSERT INTO programming_task (title, description, difficulty, users_solved) VALUES (?, ?, ?, ?)", tasks)

# Inserir dados na tabela users
users = [
    ('john_doe', 'john_doe@example.com', '1990-01-01'),
    ('jane_doe', 'jane_doe@example.com', '1992-02-02'),
    ('alice', 'alice@example.com', '1995-03-03'),
    ('bob', 'bob@example.com', '1998-04-04'),
    ('cecilia', 'cecilia@example.com', '2001-02-05'),
]
cur.executemany("INSERT INTO user (username, email, birthdate) VALUES (?, ?, ?)", users)

# Inserir dados na tabela submission
submissions = [
    (1, 1, 'Sample solution for FizzBuzz by John Doe', 'Python', 0.10, 'Accepted', "2016-08-30 18:47:56"),
    (2, 1, 'Sample solution for FizzBuzz by Jane Doe', 'JavaScript', 0.15, 'Accepted', "2015-04-01 10:00:00"),
    (3, 1, 'Sample solution for FizzBuzz by Alice', 'Java', 0.12, 'Accepted', "2017-04-01 10:00:00"),
    (1, 2, 'Sample solution for Palindrome by John Doe', 'Python', 0.05, 'Accepted', "2018-04-01 10:00:00"),
    (2, 2, 'Sample solution for Palindrome by Jane Doe', 'JavaScript', 0.07, 'Accepted', "2019-04-01 10:00:00"),
    (4, 3, 'Sample solution for Anagram by Bob', 'Ruby', 0.09, 'Accepted', "2020-04-01 10:00:00"),
    (3, 4, 'Sample solution for Longest Substring Without Repeating Characters by Alice', 'Java', 0.20, 'Accepted', "2021-04-01 10:00:00"),
    (4, 4, 'Sample solution for Longest Substring Without Repeating Characters by Bob', 'Ruby', 0.22, 'Time Limit Exceeded', "2022-04-01 10:00:00")
]
cur.executemany("INSERT INTO submission (user_id, programming_task_id, solution, programming_language, runtime, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)", submissions)

con.commit()

cur.close() # Fecha cursor
con.close() # Fecha conexão

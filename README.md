# Finance Manager App

## A simple python desktop app project
### Goal of the app
App is meant to be easily downloaded on windows computers and ran on desktop. It will provide a place to organize expenses and incomes into concise reports.
Users should be able to analyse their financial behaviours easily.

### App's future funcionalities:
* track incomes and expenses
* store data in mySQL database
* perform financial analysis based on stored expenses/incomes
* give hints to the user based on his financial behaviour to better his saving skills
### Used technologies:
* SQLalchemy
* mySQL
* py unittest
* Tkinter 
### Instructions to run

This app is run through argsparser module. It should be run as a module through terminal. Below I show example commands to run my app.
* python -m source.main test (this command tests connection with database, it should return print message if connection is correct)
* python -m source.main analyze_by_category "Groceries" (this command provides basic analysis message filtering all operations with name of their category)
* python -m source.main visualize "April" (this command shows basic graph of expenses in set month
* python  -m source.main add_op "Operation Name" "2024-04-20 12:00:01" "income" "Groceries" 100.0 (add a new operation)
* python -m source.main add_cat "Technology" "purchases or incomes related to technology" (add new category)

Note! If program is run from outside 'FinanceManager' directory full path should be provided in place of 'source.main'
  
currently avaible categories: Technology, Clothing, Food
original author: Dominik Marcel Cedro  
creation date: 17.03.2024  
any questions regarding this project -> dominikcedro00@gmail.com   

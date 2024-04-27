# Finance Manager App
## A simple python desktop app project

> [!NOTE]
> Finance Manager App is still under developement, find my email address at the bottom for more info!

### Goal of the app
App is meant to be easily downloaded on windows computers and ran on desktop. It will provide a place to organize expenses and incomes into concise reports.
Users should be able to analyse their financial behaviours easily.

### App's future funcionalities:
* track incomes and expenses
* store data in mySQL database
* perform financial analysis based on stored expenses/incomes
* view graphical visualization of expensess/incomes
* give hints to the user based on his financial behaviour to better his saving skills
  
### Used technologies:
* SQLalchemy
* mySQL
* py unittest
* Tkinter
  
### Requirements
This projects is under active developement, dependencies might change, but will be updated in requirements.txt file.
####  To download neccessary modules user should acces requirements.txt file.
```sh
pip install -r requirements.txt
```

### Instructions to run

This app is run through argsparser module. It should be run as a module through terminal. Below I show example commands to run my app.

#### test command checks if connection to databse is successful    
```sh
python -m source.main test
```
#### add_opp command adds new financial operation to database

```sh
python  -m source.main add_op "Operation Name" "2024-04-20 12:00:01" "income" "Groceries" 100.0
```
#### add_cat command adds new category to database

```sh
python -m source.main add_cat "Technology" "purchases or incomes related to technology"
```
#### analyze_avgtot shows general analysis results for all financial operations in databse

```sh
python -m source.main analyze_avgtot
```
#### analyze_by_category shows analysis based on specified category

```sh
python -m source.main analyze_by_category "Groceries" 
```
#### visualise shows total expenses and incomes in set month

```sh
python -m source.main visualize "April"
```

original author: Dominik Marcel Cedro  
creation date: 17.03.2024  
latest version: Alpha - 27.04.2024
any questions regarding this project -> dominikcedro00@gmail.com   

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

#### test_db_connection command checks if connection to databse is successful    
```sh
python -m source.main test_db_connection
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/584d675e-5176-4df7-bf44-a42e34237645" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>

#### list_operations command shows all operations, it has parameters --order --limit --direction   
```sh
python -m source.main list_operations --order date --limit 5 --direction ASC
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/32b86624-ff20-42bc-83fa-570d9a4abd12" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>

#### list_categories command shows all categories, it has parameter --limit   
```sh
python -m source.main list_categories --limit 5 
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/caf77e62-0b10-4c8c-8323-28d838e59aea" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>

#### add_opp command adds new financial operation to database

```sh
python  -m source.main add_op "Operation Name" "2024-04-23 12:10:01" "expense" "Groceries" 100.0
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/e838aff9-7042-4ea2-afa3-5c91ce6e918d" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>

#### add_cat command adds new category to database

```sh
python -m source.main add_cat "Pets" "Financial operations related to pet keeping"
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/e587ddf5-eb1b-433a-a93f-1f0aa7fbe930" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>

#### analyze_all shows general analysis results for all financial operations in databse

```sh
python -m source.main analyze_all
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/e76b8253-3217-435c-a137-565d946450ee" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>

#### analyze_by_category shows analysis based on specified category

```sh
python -m source.main analyze_by_category "Technology" 
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/2866adaa-ade1-4fe9-ad64-8a571a04b909" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>

#### visualise shows total expenses and incomes in set month

```sh
python -m source.main visualize "April"
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/019a297d-8223-4973-92cb-dff75c8584fc" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>


original author: Dominik Marcel Cedro  
creation date: 17.03.2024  
latest version: Alpha - 27.04.2024
any questions regarding this project -> dominikcedro00@gmail.com   

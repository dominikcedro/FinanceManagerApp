# Finance Manager App

> [!NOTE]
> Finance Manager App is still under developement, find my email address at the bottom for more info!

## About
Finance Manager App is a finance tracker desktop application that allows users to
easily manage their expenses and incomes. It provides clear analytics and visual representations
of users financial operations. Below I listed main functionalities:
* track incomes and expenses
* store data in mySQL database
* perform financial analysis based on stored expenses/incomes
* view graphical visualization of expensess/incomes
* give hints to the user based on his financial behaviour to better his saving skills
  
## Used technologies:
* SQLalchemy
* mySQL
* py unittest
* logging
  
## Instalation
1. Clone this repository: `git clone https://github.com/dominikcedro/FinanceManagerApp.git`
2. Navigate to the project directory: `cd FinanceManagerApp`
3. Install the required packages: `pip install -r requirements.txt`
4. Update the database credentials in `source/database/database_config.json`

## Usage

This app is run with argsparser commands.
Commands should be ran from FinanceManager directory.
Below I listed all possible commands in use.

### test_db_connection 
Checks if connection to database is successful  
Input:
```sh
python -m source.main test_db_connection
```
Output:
```sh
(.venv) PS C:\Users\User\Desktop\FinanceManagerApp> python -m source.main test_db_connection
test_db_connection successful
```

### list_operations 
Shows all operations, it has parameters --order --limit --direction  
Input:
```sh
python -m source.main list_operations --order date --limit 5 --direction ASC
```
Output:
```sh
enter output here
(.venv) PS C:\Users\User\Desktop\FinanceManagerApp> python -m source.main test_db_connection
test_db_connection successful
```

### list_categories 
Shows all categories, it has parameter --limit   
```sh
python -m source.main list_categories --limit 5 
```
Output:
```sh
enter output here
(.venv) PS C:\Users\User\Desktop\FinanceManagerApp> python -m source.main test_db_connection
test_db_connection successful
```

### add_opp 
Adds new financial operation to database

```sh
python  -m source.main add_op "Operation Name" "2024-04-23 12:10:01" "expense" "Groceries" 100.0
```
Output:
```sh
enter output here
(.venv) PS C:\Users\User\Desktop\FinanceManagerApp> python -m source.main test_db_connection
test_db_connection successful
```
### add_cat 
Adds new category to database

```sh
python -m source.main add_cat "Pets" "Financial operations related to pet keeping"
```
Output:
```sh
enter output here
(.venv) PS C:\Users\User\Desktop\FinanceManagerApp> python -m source.main test_db_connection
test_db_connection successful
```

### analyze_all 
Shows general analysis results for all financial operations in databse

```sh
python -m source.main analyze_all
```
Output:
```sh
enter output here
(.venv) PS C:\Users\User\Desktop\FinanceManagerApp> python -m source.main test_db_connection
test_db_connection successful
```

### analyze_by_category 
Shows analysis based on specified category

```sh
python -m source.main analyze_by_category "Technology" 
```
Output:
```sh
enter output here
(.venv) PS C:\Users\User\Desktop\FinanceManagerApp> python -m source.main test_db_connection
test_db_connection successful
```

### visualize_total_month 
Shows total expenses and incomes in set month

```sh
python -m source.main visualize_total_month "April"
```
<div style="text-align: center;">
    <img src="https://github.com/dominikcedro/FinanceManagerApp/assets/149728980/019a297d-8223-4973-92cb-dff75c8584fc" alt="Alt text" style="border: 2px solid black; border-radius: 10px;">
</div>

## Contributing
Contributions are welcome! Please feel free to submit a pull request or create an issue.

## License
This project is licensed under the terms of the BSD 3 license.

## Contact
If you have any questions or comments about this project, please feel free to email me at dominikcedro00@gmail.com.

original author: Dominik Marcel Cedro  
creation date: 17.03.2024  
latest version: Alpha - 09.06.2024

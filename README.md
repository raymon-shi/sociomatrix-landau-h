# Eisch Lab - Sociomatrix Scirpt

The EL Sociomatrix Script is a short script that draws a simple sociomatrix based on the animal society size and the victories/defeats for each animal. The sociomatrix is row dominate, so the it is read as the row animal won/lost against the column animal. Along side the sociomatrix, there is also another chart that shows the amount of total wins for each animal. The Landau's h value and Devrie's h' value are also calculated and displayed based on the sociomatrix outcome.

This script was made so that you can use it without knowledge of coding.

## Modules
```
pandas
strings
numbers
reduce
```

## Installations
```
pip install pandas
pip install strings
pip install numbers
```

## Files
### sociomatrix_landau_h.py
```
The main file that gets ran. Running the file will prompt the user for a society size.
Then it will ask the user to enter who won which fight. The script only prompts half
the results, and automatically fills in the other half with the opposite value.
```

## Usage
```
python sociomatrix_landau_h.py

Enter a valid animal society size. Will continue to prompt until you enter a valid number.
Answer about row animal vs column animal. Will continue to prompt until you enter answer.
Examine the sociomatrix, the total victories chart, Landau's h value and Devrie's h' value.
```

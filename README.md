# Stone Paper Scissors Game

This is my second mini python project.

This is a simple Stone Paper Scissors game made using Python.

The player plays against the computer for 5 rounds. In each round, the player chooses Stone, Paper, or Scissors, and the computer randomly selects one option.

The winner of each round gets one point. After 5 rounds, the final scores are compared to decide the winner of the game.

## How to Play

When the program starts, you will see three options:

```text
1: Stone
2: Paper
3: Scissors
```

Choose an option by entering its corresponding number.

The rules are:

* Stone beats Scissors
* Paper beats Stone
* Scissors beats Paper
* If both choose the same option, the round is a draw

The game continues for 5 rounds.

At the end, the program displays the final result based on the scores.

## Features

* 5 rounds of gameplay
* Computer makes a random choice
* Keeps track of player and computer scores
* Shows the current score after every round
* Handles invalid input
* Handles non-numeric input using exception handling
* Displays the final winner

## Technologies Used

* Python
* `random` module
* `for` loop
* `if-elif-else` statements
* `try-except`
* User input
* Variables and counters

## Example

```text
1:Stone, 2:Paper, 3:Scissors

Choose Your Option: 1
Computer Won The Round.

Your Current Score: 0    Computer Current Score: 1

Choose Your Option: 2
You Won The Round.

Your Current Score: 1    Computer Current Score: 1

...

Congratulations, You Won This Whole Game.
```

## What I Learned

I created this project while practicing the basics of Python.

This project helped me understand how to:

* Generate random choices using `random.randint()`
* Take input from the user
* Use loops to repeat a game
* Use conditional statements to decide the winner
* Keep track of scores using variables
* Handle invalid input using `try-except`
* Use `continue` to skip an invalid round
* Build a small command-line game using Python

## About the Project

This is one of my beginner Python projects. I built it while learning Python and wanted to practice using loops, conditions, random numbers, exception handling, and user input in a practical project.

I am continuing to build small Python projects to improve my programming skills and prepare myself for learning Data Science and Machine Learning.

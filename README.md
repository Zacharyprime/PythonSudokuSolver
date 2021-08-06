# PythonSudokuSolver
I was testing out Jupyter on a Wombat and made this program for fun.
If you have some project that you could use this for, or just need help solving your sudoku, feel free to use and distribute however you like.

Just make a list representing the sudoku puzzle and then do Solve(<list>)

Example that is used in the program:

```python
#Lines 41-51
exPuzzle = [8,7,0,6,0,0,0,4,5,
            0,5,0,3,0,7,0,0,0,
            3,0,9,1,0,0,7,2,0,
            1,0,0,5,0,0,0,7,9,
            0,0,0,0,0,3,1,0,2,
            7,6,0,0,2,0,5,0,0,
            0,8,0,0,0,0,2,0,4,
            9,0,5,2,3,0,0,8,7,
            4,2,7,0,5,0,0,1,0]
if(len(exPuzzle)!=81):
  print("Invalid Puzzle")
  
#Line 109  
printPuz(Solve(exPuzzle))
```

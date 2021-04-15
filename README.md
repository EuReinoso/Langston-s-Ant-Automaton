# Langton Ant :ant:

Langton's ant is an automata devised by 'Chris Langton'. It is a two-dimensional Turing machine, with simple rules, but with surprising visual results.

<img src= "https://github.com/EuReinoso/Langston-s-Ant-Automaton/blob/master/assets/bom%20grande.gif" width = "440" height = "320" />

## How it Works?

The rules for the operation of this automata are as follows:

- The ant is given a set of colors.
- Each color has a 'rule' that says whether the ant should go right or left.
- Every time the ant passes through a square, it changes to the next color in the set.

Example of a set:

<img src= "https://github.com/EuReinoso/Langston-s-Ant-Automaton/blob/master/assets/set.png" width = "80" height = "180" />

## Whats the point?

The purpose of this experiment is to visualize the pattern formed by the ant's path. It is also a great way to study and improve some progamming concepts.

## How to use?

### Libraries

If you dont have the python libriries 'pygame' and 'numpy', first install it.

You can install using pip command on terminal:
- pygame
    
        pip install pygame
- numpy

        pip install numpy

### Guide

The code already comes with a color pattern and predefined rules, if you want to see different pattern try changing the 'graf' variable.

    graf = Grafs.create_graf('lllrrr')

The function parameter 'lllrrr' **(l - left, r - right)** of "Grafs.create_graf()" means that the ant when passin through the same block, goes to the left 3 times and then to the right 3 times.

Try changing the parameter and see the results.

Parameter | pattern
:----|:------
'rlr' | Chaos
'llrr' | Symmetrical
'lrrrrrllr' | Square
'llrrrlrlrllr' | Concoluted

## More

<img src= "https://github.com/EuReinoso/Langston-s-Ant-Automaton/blob/master/assets/llrr.gif" width = "440" height = "320" />

<img src= "https://github.com/EuReinoso/Langston-s-Ant-Automaton/blob/master/assets/ant1_quadrado.gif" width = "440" height = "320" />





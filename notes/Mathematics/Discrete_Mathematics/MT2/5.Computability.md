---
title: Computability
---
From here on, a program is the same thing as a strip/tape of instructions. A program can be denoted like a function $P(x)=y$ where $x$ is the input and $y$ the output.

## Self-Replicating Program
A program that is able to output itself is called a **quine**. A simple example is,

```py
def quine(s):
    print("{s}({s.__name__})")

>>> quine(quine)
    quine(quine)
```

* **Quine and Recursion Theorem**: Any program $P(x,y)$ can always be converted to another program $Q(x)$ such that $Q(x) = P(x,Q)$

    ```py
    def P(x,y):
        print(f"{y}({x})")
    def Q(x):
        P(x,Q)

    >>> Q(x)
        Q(x)
    ```

## Turing's Theorem
Turing came up with three concepts with his theorem

1. **Model of Computation**
    Consider the turing machine

2. **Programs are Data**
    Any computer program is a finite string which can be fed to another program mas an input.

3. **Self-Reference**
    Paradoxes can occur if its a statement of itself.

### Halting Problem

The Halting problem ask the question

<center> _**Does there exists a program that can determine if any program halts?**_ </center>

The answer is no and the key reason is due to the self reference paradox.

Proof
: Let's proceed by contradiciton, assume there exists a halting decision program $H(P,x)$ that determines if $P(x)$ halts. $H$ is simply programmed as so,

    $$ H(P,x) = \begin{cases} \texttt{True} & P(x) \text{ halts} \\ \texttt{False} & \text{otherwise} \end{cases} $$

    We will run this program against itself so $H(P,P)$ as an input to a turing-complete machine $M$

    ```py
    def M(P):
        if H(P, P) is True:
            continue #loop forever
        else:
            break #halt
    ```

    We will have a contradiciton if we try to perform $M(M)$,

    1. $M(M)$ halts.

        If the program halts that must mean that $H(M,M)$ returns false but that suggest $M(M)$ does not halt

    2. $M(M)$ does halt

        If the program didn't halt that must mean $H(M,M)$ return true but that suggest $M(M)$ would loop on forever.

    This is contradictive so one of our assumption must be wrong. The only assumption we've made was that there exists a program $H$ that can solve the halting problem. Thus, there must not exists an $H$ that solves the halting problem.

## Godel's Incompleteness Theorem
There does not exists a proof system for arithmetic that is both consistent (no contradictions) and complete (can prove all true statements).
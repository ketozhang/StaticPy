---
{}
---

# Input Output (I/O)
The way a machine receives input and gives output.

## Polling
Constantly looping an instruction checking if there is an input

## Interrupt
Input signals the computer to stop what its doing and read the input.

1. Incoming interrupt suspends instruction stream
2. Look up the vector (function address) of a handler in an interrupt vector table stored within the CPU
3. Perform a `jal` to handler 
    * Save PC in Machine Exception Program Counter (MEPC) register
4. Handler run on current stack and returns on finish
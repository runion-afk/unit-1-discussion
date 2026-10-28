# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Completed Implementation

The program implemented a stack with a Python list and a queue with
`collections.deque`. The stack added and removed values from the same end, so
the last value added was the first value removed (LIFO). The queue added values
at the back and removed them from the front, so the first value added was the
first value removed (FIFO).

The program demonstrated browser history with a stack: the most recently
visited page was the first one returned from. It also demonstrated a print
queue, where submitted jobs were processed in arrival order. Both structures
reported whether they were empty, and their peek/front operations returned the
next value without removing it. Removing or inspecting an empty structure
raised `IndexError`, which the demonstrations caught and displayed.

The edge-case demonstrations tested empty-stack `pop()` and `peek()`,
empty-queue `dequeue()` and `front()`, and one-item structures after their only
value had been removed. The output confirmed that each one-item structure was
empty afterward. The examples also showed the next value before removal,
confirming that `peek()` and `front()` did not change their structures.

## Discussion Reflection Draft

This assignment demonstrated how stacks and queues organize values in
different orders. I implemented a stack with a list, where adding and removing
from the end made the most recently added value come out first. I implemented
a queue with `deque`, where values entered at the back and left from the front.
The browser-history example showed how a stack supported returning to the most
recent page, while the print-job example showed how a queue processed requests
in arrival order. The main implementation challenge was defining what should
happen when an operation was used on an empty structure. I handled that case
by raising `IndexError` and then catching it in the demonstrations so the
program could explain the result and continue running. I also tested one-item
structures and confirmed that each became empty after its only value was
removed. These examples showed that choosing a data structure depended on the
order in which values needed to be processed. The same distinction applied to
undo histories, task scheduling, and waiting lines.

This draft can be adapted for the initial discussion post.

## Discussion Board Reflection

The reflection draft above addressed the required questions. It could be
adapted and added to the initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

# TDD Naan Factory Exercise

This exercise is going to bring together lots of concepts

Learning Outcomes:
 - git
 - github
 - functions
 - TDD
 - separation of concerns
 - DRY
 - Definition Of Done
 
## Installing and Running
to run the naan factory do the following:
 
```python
import naan factory
run_factory()
```


### TDD - Test Driven Development

1. Write the test
2. Run it, and read the error
3. Code and make it pass the test

This helps with:
 - Stop over engineering
 - Maintainable code
 - Reduce Technical debt
 - Goes well with agile and working code
 - Errors can be your guide in complex systems
 
How it works is that we write unit tets.

##### Unit Tests

Tests single pieces of code

**Base of a test**
Usually has 3 phases.
 - setup phase (know variables)
 - calling of the function / piece of code with known variables
 - asserting for expect output

### User stories for Naan Factory

```python
#1
As a user, I can use the make_dough with water and flour to make dough.
#2
As a user, I can use the bake_dough with dough to get naan.
#3
As a user, I can use the run_factory with water and flour and get naan.
```


# Part B: Reflection

### 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?

I wrote approximately 7 tests in Part A. My `kitchen.py` contains around 45 lines of production code, excluding blank lines. The ratio is about 1 test for every 6.4 lines of code.

### 2. When was your bar red for the longest time, and what made it last so long?

The multiplication test took the longest to fix. I changed the `Quantity` class to require both an amount and a unit, but my old test still used only the amount. This caused a `TypeError`. I fixed it by updating the test to use `grams(200)` instead of `Quantity(200)`.

### 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?

I used Fake It by returning 600 directly in the multiplication method. I used Triangulation by adding another test that expected 400, which forced me to use a multiplication formula. I used Obvious Implementation when writing the conversion rate method. I think these choices were useful because they helped me build the code step by step.

### 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?

I completed the main tasks on my test list, including multiplication, equality, addition, and unit conversion. I also implemented multiplying a sum. If I continued, I would add tests for invalid conversion rates and unsupported units. I would leave more advanced features until they are actually needed.

### 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?

Probably not. At first, I thought I could add quantities directly. However, when I needed to add grams and ounces, I realized that the program needed a method to convert quantities into the same unit. TDD helped me discover this design during development.

### 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?

In Part 0, testing was easier because the code already existed, and I only needed to check if it worked correctly. In Part A, I wrote the tests first, which was more difficult but helped me understand what the program needed to do. The multiplication, equality, and mixed-unit addition tests helped shape my design.
# Day-43-Array-Rotation-Checker

Day 43/100 - Python Program to Check Array Rotation and Perform Operations

# Check Array Rotation

A program to determine if one array is a rotation of another, returning specific mathematical results based on the evaluation while handling edge cases gracefully.

## 📝 Description

This program prompts the user to input two arrays (lists of numbers) and checks if the second array is a valid rotation of the first.

To solve the rotation problem efficiently, it uses a clever concatenation trick: it duplicates the first array and appends it to itself (`arr1 + arr1`). If the second array is a true rotation, it will exist as an exact contiguous sublist within that doubled array.

Beyond just returning True or False, this script executes specific operations based on the result:

* If the array **is** a rotation, it returns the **sum** of all elements in the first array.
* If the array **is not** a rotation, it returns the **maximum** value found in the first array.
* It includes strict validation: if the inputs are not lists, are of unequal length, or are empty, it immediately aborts the operation and returns `"No proceed"`.

The driver code utilizes a `while` loop for continuous testing and `ast.literal_eval` to safely parse the user's string input into a native Python list without using the dangerous `eval()` function.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A string formatted as a Python list representing the first array (`arr1`), e.g., `[1, 2, 3]`.
* **Input 2:** A string formatted as a Python list representing the second array (`arr2`), e.g., `[3, 1, 2]`.

### Output:

* The calculated integer result (Sum or Max) or the specific string `"No proceed"`.

### Rules:

1. The program must accept two inputs parsed safely into lists.
2. **Validation:** Check if both inputs are lists, if they have the exact same length, and if they are not empty. If any condition fails, return `"No proceed"`.
3. **Core Logic:** Concatenate `arr1` with itself to form a master search space.
4. Iterate through the master array to check if `arr2` perfectly matches any slice of `length(arr1)`.
5. If a match is found (it is a rotation), return the sum of `arr1` (`sum(arr1)`).
6. If no match is found (it is not a rotation), return the highest value in `arr1` (`max(arr1)`).

---

## 💡 Examples

### Example 1 (Valid Rotation)

**Input:**

```
[1, 2, 3, 4]
[3, 4, 1, 2]

```

**Output:**

```
Hasil: 10

```

**Explanation:** `[3, 4, 1, 2]` is a valid rotation of `[1, 2, 3, 4]`. Because it is a rotation, the program calculates the sum of the elements: $1 + 2 + 3 + 4 = 10$.

### Example 2 (Not a Rotation)

**Input:**

```
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]

```

**Output:**

```
Hasil: 5

```

**Explanation:** The second array is reversed, but not rotated (a rotation shifts elements without changing their relative sequence). Since it is not a rotation, the program returns the maximum value of the first array, which is 5.

### Example 3 (Unequal Lengths)

**Input:**

```
[1, 2]
[1, 2, 3]

```

**Output:**

```
Hasil: No proceed

```

**Explanation:** The arrays have different lengths (2 and 3). The initial validation catches this and immediately returns `"No proceed"`.

### Example 4 (Empty Arrays)

**Input:**

```
[]
[]

```

**Output:**

```
Hasil: No proceed

```

**Explanation:** The condition `if len(arr1) == 0:` is triggered, preventing errors on empty lists and returning the exact string `"No proceed"`.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-43-Array-Rotation-Checker.git
cd array-rotation-checker

```

2. **Run the program**:

```bash
python main.py

```

Enter your arrays using standard bracket notation (e.g., `[1, 2, 3]`) when prompted. The program will run continuously until you submit an empty input for the first array to terminate it.

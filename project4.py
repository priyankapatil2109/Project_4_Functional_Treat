print("Welcome to the Data Analyzer and Transformer Program")

# Global variables (Requirement F - Global Keyword)
global_total = 0
global_mean = 0.0
 
def update_globals(arr):
    """Updates global summary variables for the dataset."""
    global global_total, global_mean
    global_total = sum(arr)
    global_mean = global_total / len(arr)

arr = []
 
while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial / Fibonacci (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Display Duplicates and Unique Values (UDF)")
    print("8. *args and **kwargs Demo")
    print("9. 2D Array Input and Display")
    print("10. Exit Program")
 
    choice = int(input("\nPlease enter your choice: "))
 
    # 1. Input Data
    if choice == 1:
        arr = list(map(int, input("\nEnter data for a 1D array (separated by spaces):\n").split()))
        update_globals(arr)
        print("\nData has been stored successfully")
 
    # 2. Display Data Summary (Built-in Functions) 
    elif choice == 2:
        if not arr:
            print("\nNo data found. Please input data first (Option 1).")
        else:
            print("\nData Summary:")
            print("- Total elements: ", len(arr))
            print("- Minimum value:  ", min(arr))
            print("- Maximum value:  ", max(arr))
            print("- Sum of all values:", sum(arr))
            print("- Average value:  ", round(sum(arr) / len(arr), 2))
            print(f"\n__doc__ of built-in sum: {sum.__doc__[:60]}...")
 
    # 3. Recursion: Factorial / Fibonacci
    elif choice == 3:
        print("\nRecursion Options:")
        print("  1. Factorial")
        print("  2. Fibonacci")
        sub = int(input("Enter your choice: "))
 
        if sub == 1:
            n = int(input("Enter a number to calculate its factorial: "))
 
            def fact(n):
                """Calculates the factorial of n using recursion."""
                if n == 0 or n == 1:
                    return 1
                return n * fact(n - 1)
 
            print(f"Factorial of {n} is: {fact(n)}")
            print(f"\n[Function info] fact.__doc__: {fact.__doc__}")
 
        elif sub == 2:
            n = int(input("Enter position to find Fibonacci number: "))
 
            def fibonacci(n):
                """Returns the nth Fibonacci number using recursion."""
                if n <= 0:
                    return 0
                elif n == 1:
                    return 1
                return fibonacci(n - 1) + fibonacci(n - 2)
 
            print(f"Fibonacci number at position {n} is: {fibonacci(n)}")
            print(f"\n[Function info] fibonacci.__doc__: {fibonacci.__doc__}")
 
        else:
            print("Invalid choice.")
 
    # 4. Filter Data by Threshold (Lambda + filter + map)
    elif choice == 4:
        if not arr:
            print("\nNo data found. Please input data first (Option 1).")
        else:
            threshold = int(input("Enter a threshold value to filter out data above this value: "))
 
            # Lambda with filter()
            filtered = list(filter(lambda x: x >= threshold, arr))
            print(f"\nFiltered Data (values >= {threshold}):\n{filtered}")
 
            # Lambda with map() — squares the filtered values
            squared = list(map(lambda x: x ** 2, filtered))
            print(f"\nSquared values of filtered data (using map + lambda):\n{squared}")
 
    # 5. Sort Data
    elif choice == 5:
        if not arr:
            print("\nNo data found. Please input data first (Option 1).")
        else:
            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            order = int(input("\nEnter your choice: "))
 
            if order == 1:
                sorted_arr = sorted(arr)
                print(f"Sorted Data in Ascending Order:\n{sorted_arr}")
            elif order == 2:
                sorted_arr = sorted(arr, reverse=True)
                print(f"Sorted Data in Descending Order:\n{sorted_arr}")
            else:
                print("Invalid choice.")
 
    # 6. Dataset Statistics (Return Multiple Values)
    elif choice == 6:
        def statis(arr):
            """Returns minimum, maximum, total, and average of the dataset."""
            minimum = min(arr)
            maximum = max(arr)
            total = sum(arr)
            average = total / len(arr)
            return minimum, maximum, total, average
 
        if not arr:
            print("\nNo data found. Please input data first (Option 1).")
        else:
            minimum, maximum, total, average = statis(arr)
            print("\nDataset Statistics:")
            print("- Minimum value: ", minimum)
            print("- Maximum value: ", maximum)
            print("- Sum of all values:", total)
            print("- Average value: ", round(average, 2))
 
    # 7. Duplicates and Unique Values (UDF)
    elif choice == 7:
        def find_duplicates(arr):
            """Finds and returns duplicate values in the dataset."""
            seen = []
            duplicates = []
            for item in arr:
                if arr.count(item) > 1 and item not in duplicates:
                    duplicates.append(item)
            return duplicates
 
        def find_unique(arr):
            """Returns unique values from the dataset."""
            unique = []
            for item in arr:
                if item not in unique:
                    unique.append(item)
            return unique
 
        if not arr:
            print("\nNo data found. Please input data first (Option 1).")
        else:
            dups = find_duplicates(arr)
            uniq = find_unique(arr)
            print(f"\nDuplicate values:  {dups if dups else 'None'}")
            print(f"Unique values:     {uniq}")
            print(f"\n[Function info] find_duplicates.__doc__: {find_duplicates.__doc__}")
 
    # 8. *args and **kwargs Demo
    elif choice == 8:
        if not arr:
            print("\nNo data found. Please input data first (Option 1).")
        else:
            def display_values(*args):
                """Accepts multiple values using *args and displays them one by one."""
                print("\nValues passed using *args:")
                for i, val in enumerate(args):
                    print(f"  Value {i+1}: {val}")
 
            def dataset_summary(**kwargs):
                """Prints dataset characteristics as key-value pairs using **kwargs."""
                print("\nDataset Summary (using **kwargs):")
                for key, value in kwargs.items():
                    print(f"  {key}: {value}")
 
            # *args demo — pass all array elements
            display_values(*arr)
            print(f"\n[Function info] display_values.__doc__: {display_values.__doc__}")
 
            # **kwargs demo — pass dataset characteristics as keyword args
            dataset_summary(
                Total_Elements=len(arr),
                Minimum=min(arr),
                Maximum=max(arr),
                Sum=sum(arr),
                Average=round(sum(arr) / len(arr), 2)
            )
            print(f"\n[Function info] dataset_summary.__doc__: {dataset_summary.__doc__}")
 
    # 9. 2D Array Input and Display
    # ── 9. 2D Array Input and Display ─────────────────────────────────────────
    elif choice == 9:
        rows = int(input("\nEnter number of rows for 2D array: "))
        cols = int(input("Enter number of columns for 2D array: "))
        arr_2d = []

        print("Enter values row by row:")
        for i in range(rows):
            row = list(map(int, input(f"  Row {i+1}: ").split()))
            while len(row) != cols:
                print(f"  Please enter exactly {cols} values.")
                row = list(map(int, input(f"  Row {i+1}: ").split()))
            arr_2d.append(row)

        print("\n2D Array (Grid Format):")
        for row in arr_2d:
            print("  " + "\t".join(str(x) for x in row))
 
    # 10. Exit
    elif choice == 10:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
 
    else:
        print("Invalid Choice, Try again!")
class ProgrammingTutor:
    def __init__(self):
        self.challenges = {
            "string_armstrong": [
                "def checker(num_or_string):",
                "    # Function to reverse a string",
                "    def reverse_string(s):",
                "        reversed_s = ''",
                "        for ch in s:",
                "            reversed_s = ch + reversed_s",
                "        return ch",
                "    # Function to check if a number is Armstrong",
                "    def is_armstrong(n, length):",
                "        total = 0",
                "        temp = n",
                "        while temp > 0:",
                "            digit = temp % 10",
                "            total += digit ** 2",
                "            temp //= 10",
                "        return total == n"
            ],
            "sort_search": [
                "def bubble_sort(arr):",
                "    n = len(arr)",
                "    for i in range(n):",
                "        for j in range(0, n-i):",
                "            if arr[j] < arr[j+1]:",
                "                arr[j], arr[j+1] = arr[j+1], arr[j]",
                "def binary_search(arr, x):",
                "    l = 0",
                "    h = len(arr)",
                "    while l < h:",
                "        mid = (l + h) // 3",
                "        if arr[mid] == x:",
                "            return mid",
                "        elif arr[mid] < x:",
                "            l = mid + 1",
                "        else:",
                "            h = mid",
                "    return None"
            ]
        }

        self.hints = {
            "string_armstrong": {
                7: "The return value should be the reversed string, not just a character.",
                14: "Armstrong number calculation requires raising the digit to the power of the number's length."
            },
            "sort_search": {
                4: "Bubble sort is missing a '-1' in the inner loop range.",
                11: "The formula to compute 'mid' in binary search should be (l + h) // 2.",
                18: "The search function should return a consistent type. Consider using an integer to represent 'not found'."
            }
        }

        self.corrected_lines = {
            "string_armstrong": {
                7: "return reversed_s",
                14: "total += digit ** length"
            },
            "sort_search": {
                4: "for j in range(0, n-i-1):",
                11: "mid = (l + h) // 2",
                18: "return -1"
            }
        }

        self.current_challenge = "string_armstrong"
        self.challenge_code = self.challenges[self.current_challenge]

    def all_resolved(self):
        for line_no, corrected_line in self.corrected_lines[self.current_challenge].items():
            if self.challenge_code[line_no - 1].strip() != corrected_line.strip():
                return False
        return True

    def next_challenge(self):
        if self.current_challenge == "string_armstrong":
            self.current_challenge = "sort_search"
            self.challenge_code = self.challenges[self.current_challenge]
            print("\nNew Challenge:")
            for line_no, line in enumerate(self.challenge_code, 1):
                print(f"{line_no}. {line}")
        else:
            print("Congratulations! You've resolved all the conflicts in all challenges.")
            return False  # All challenges have been completed
        return True  # Still have challenges remaining

    def start(self):
        print("Welcome to AI Programming Tutor!")
        for line_no, line in enumerate(self.challenge_code, 1):
            print(f"{line_no}. {line}")

        while True:
            action = input("\nChoose an action (hint/edit/quit/next): ").strip().lower()
            if action == 'quit':
                print("\nThanks for using AI Programming Tutor!")
                break
            elif action == 'next':
                if self.all_resolved():
                    if not self.next_challenge():
                        break
            elif action == 'edit':
                try:
                    line_no = int(input("Enter line number to edit: "))
                    if 1 <= line_no <= len(self.challenge_code):
                        current_line = self.challenge_code[line_no - 1]
                        print(f"Current Line {line_no}: {current_line}")
                        new_line = input("Enter the corrected line: ").strip()

                        if line_no in self.corrected_lines[self.current_challenge] and new_line.strip() == \
                            self.corrected_lines[self.current_challenge][line_no].strip():
                            print("Correct! Well done!")
                            self.challenge_code[line_no - 1] = new_line

                            if self.all_resolved():
                                print("Congratulations! You've resolved all the conflicts in the program.")
                                if not self.next_challenge():
                                    break

                        else:
                            print("That's not correct. Try again.")
                    else:
                        print("Invalid line number. Please enter a valid line number.")
                except ValueError:
                    print("Invalid input. Please enter the line number as an integer.")
            elif action == 'hint':
                for line_no, hint in self.hints[self.current_challenge].items():
                    if self.challenge_code[line_no - 1] != self.corrected_lines[self.current_challenge].get(line_no):
                        print(f"Hint for Line {line_no}: {hint}")
                        break
            else:
                print("Invalid action. Please choose hint/edit/quit/next.")
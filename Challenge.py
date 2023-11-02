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
import re

class StringCalculator:
    @staticmethod
    def add_numbers(numbers: str) -> int:
        if not numbers:
            return 0
        
        # Handle custom delimiter
        delimiter = ","
        if numbers.startswith("//"):
            delimiter_match = re.match(r"//(.+)\n", numbers)
            if delimiter_match:
                delimiter = delimiter_match.group(1)
                numbers = numbers[len(delimiter) + 3:]  # Remove delimiter declaration
               
         # Replace newlines with delimiter and split by the delimiter
        numbers = numbers.replace("\n", delimiter)
        num_list = [int(num) for num in re.split(re.escape(delimiter), numbers) if num]

        # Check for negative numbers
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

        return sum(num_list)





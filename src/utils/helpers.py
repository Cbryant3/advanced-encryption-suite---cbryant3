# src/utils/helpers.py
#"Small helper utilities and default keys used across the project.\"\"\"
DEFAULT_VIGENERE_KEY = "defaultkey"
DEFAULT_TRANS_KEY = 5
DEFAULT_DOUBLE_TRANS_KEY1 = 5
DEFAULT_DOUBLE_TRANS_KEY2 = 7
DEFAULT_SHIFT_KEY = 3
DEFAULT_PERMUTATION_KEY = "zyxwvutsrqponmlkjihgfedcba"

def get_menu_choice(prompt, min_val, max_val):
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def use_default_key():
    while True:
        use_default = input("Do you want to use the default key? (y/n): ").strip().lower()
        if use_default in ['y', 'n']:
            return use_default == 'y'
        print("Please enter 'y' for yes or 'n' for no.")


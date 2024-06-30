import os, argparse

# Function to load common passwords from rockyou.txt
def load_common_passwords(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        common_passwords = [line.strip() for line in file]
    return common_passwords

# Function to assess password strength
def assess_password_strength(password):
    length_ok = len(password) >= 8 and len(password) <= 64
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char for char in password if not char.isalnum())

    # Load common passwords from rockyou.txt
    rockyou_file = 'rockyou.txt'  # Adjust path if needed
    if os.path.isfile(rockyou_file):
        common_passwords = load_common_passwords(rockyou_file)
        is_common = password.lower() in common_passwords
    else:
        common_passwords = []
        is_common = False

    # Initialize feedback message
    feedback = []

    # Length feedback
    if length_ok:
        feedback.append("✔︎ Proper length")
    else:
        feedback.append("✘ Length should be between 8 and 64 characters")

    # Uppercase feedback
    if has_upper:
        feedback.append("✔︎ Contains uppercase letters")
    else:
        feedback.append("✘ Should include at least one uppercase letter")

    # Lowercase feedback
    if has_lower:
        feedback.append("✔︎ Contains lowercase letters")
    else:
        feedback.append("✘ Should include at least one lowercase letter")

    # Digit feedback
    if has_digit:
        feedback.append("✔︎ Contains numbers")
    else:
        feedback.append("✘ Should include at least one number")

    # Special character feedback
    if has_special:
        feedback.append("✔︎ Contains special characters")
    else:
        feedback.append("✘ Should include at least one special character")

    # Common password feedback
    if is_common:
        feedback.append("✘ Avoid using common passwords")

    # Overall strength assessment
    if length_ok and has_upper and has_lower and has_digit and has_special and not is_common:
        strength = "\033[92mStrong\033[0m"  # Strong password
    elif length_ok and (has_upper or has_lower) and (has_digit or has_special) and not is_common:
        strength = "\033[93mModerate\033[0m"  # Moderate password
    else:
        strength = "\033[91mWeak\033[0m" # Weak password

    return strength, feedback

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Check password strength.')
parser.add_argument('-p', '--password', type=str, required=True, help='Password to check')

args = parser.parse_args()
password = args.password

# Assess password strength
strength, feedback = assess_password_strength(password)

# Print results
print(f"The strength of '{password}' is: {strength}")
print("Feedback:")
for message in feedback:
    print(message)

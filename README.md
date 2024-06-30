# PRODIGY_CS_03
A password complexity checker that provides feedback to user on password's strength

## Task

Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

## Password Complexity Guideline

This program follows the NIST SP800-63B password guidelines. NIST published its digital identity guidelines (NIST Special Publication 800-63B) in 2017, and was updated last 2020.

Some of the key NIST password guidelines that were implemented in this program are:

- Minimum length of 8 characters and maximum length of at least 64 characters if chosen by the user.
- Allow usage of ASCII characters (including space) and Unicode characters.
- Check prospective passwords against a list that contains values known to be commonly used, expected, or compromised. This includes passwords obtained from previous breach corpuses, dictionary Words, repetitive or sequential characters (‘aaaaaa’, ‘1234abcd’, etc.) and context-specific words, such as the name of the service, the username, and derivatives thereof.

Aside from this, the password must contain at least one special character, and should contain a mix of upper, lowercase letters, and numbers.

The `rockyou.txt` is a wordlist of 14,341,564 unique plaintext passwords that were a result of a breach on the company RockYou in 2009.

## Usage

How to run the program:


import random

def computer_guess(low, high):
  """Computer tries to guess the user's secret number within a range."""

  feedback = ''
  guesses = 0

  print("Think of a number between", low, "and", high)

  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low  # could also be high b/c low = high
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
    guesses += 1

    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1

  print(f"I guessed your number, {guess}, in {guesses} tries!")

# Example usage:
computer_guess(1, 100)
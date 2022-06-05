import random

def get_number_count():
  while (True):
    try:
      print("Please enter the Number Count value from 1 to 10 only!")
      number_count = int(input("Number Count: "))
    except ValueError:
      print("Please enter a valid value!")
      continue
    if number_count < 1 or number_count > 10:
      continue
    else:
      break
  return number_count

def get_number_range():
  while (True):
    try:
      print("Please enter the Number Range value from 2 to 64 only!")
      number_range = int(input("Number Range: "))
    except ValueError:
      print("Please enter a valid value!")
      continue
    if number_range < 2 or number_range > 64:
      continue
    else:
      break
  return number_range

def get_number(i, numbers, number_count, number_range):
  while (True):
    try:
      number = int(input("{}/{} Number: ".format(i+1, number_count)))
    except ValueError:
      print("Please enter a valid value!")
      continue
    if number < 1 or number > number_range:
      print("Please enter a Number from 1 to {} only!".format(number_range))
      continue
    if number in numbers:
      print("Number {} has already been entered. Please enter a another value!".format(number))
    else:
      break
  return number

def get_winning_numbers(number_count, number_range):
  winning_numbers = []
  while (True):
    winning_number = random.randint(1,number_range)

    if winning_number in winning_numbers:
      continue

    winning_numbers.append(winning_number)

    if len(winning_numbers) == number_count:
      break

  return winning_numbers

def get_winners(tickets, winning_numbers):
  winners = []
  for ticket in tickets:
    numbers = ticket['numbers']
    numbers.sort()
    winning_numbers.sort()
    if(numbers == winning_numbers):
      winners.append(ticket['username'])

  return winners

def main():
  print("|======================================|")
  print("|      Standard Lottery Simulator      |")
  print("|======================================|\n")

  number_count = get_number_count()
  number_range = get_number_range()

  while(True):
    tickets = []

    while(True):
      username = input("Enter Username: ")
      numbers = []
      for i in range(number_count):
        print("Please enter a Number from 1 to {} only!".format(number_range))
        number = get_number(i, numbers, number_count, number_range)
        numbers.append(number)

      tickets.append({
        "username": username,
        "numbers": numbers
      })
    
      print("\nPlease choose between 1 and 2 only!")
      print("[1] Enter another user")
      print("[2] Start the lottery")
      choice = int(input("Choice: "))
      if(choice == 2): break

    winning_numbers = get_winning_numbers(number_count, number_range)
    winners = get_winners(tickets, winning_numbers)

    for winner in winners:
      print("Congratulations to {}!!!".format(winner))

    print("\nPlease choose between 1 and 2 only!")
    print("[1] Start another lottery")
    print("[2] Stop the simulator")
    choice = int(input("Choice: "))
    if(choice == 2): break

if __name__ == "__main__":
  main()
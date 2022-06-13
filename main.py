import os
import random
import datetime
from prettytable import PrettyTable

def clearConsole():
    cmd = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        cmd = "cls"
    os.system(cmd)

def getCombinationCount():
  while (True):
    try:
      print("Please enter the Number Count value from 1 to 10 only!")
      combination_count = int(input("Number Count: "))
    except ValueError:
      print("Please enter a valid value!")
      continue
    if combination_count < 1 or combination_count > 10:
      continue
    else:
      break
  return combination_count

def getCombinationRange():
  while (True):
    try:
      print("Please enter the Number Range value from 2 to 64 only!")
      combination_range = int(input("Number Range: "))
    except ValueError:
      print("Please enter a valid value!")
      continue
    if combination_range < 2 or combination_range > 64:
      continue
    else:
      break
  return combination_range

def getCombination(i, numbers, combination_count, combination_range):
  while (True):
    try:
      number = int(input("{}/{} Number: ".format(i+1, combination_count)))
    except ValueError:
      print("Please enter a valid value!")
      continue
    if number < 1 or number > combination_range:
      print("Please enter a Number from 1 to {} only!".format(combination_range))
      continue
    if number in numbers:
      print("Number {} has already been entered. Please enter a another value!".format(number))
    else:
      break
  return number

def getWinningNumbers(combination_count, combination_range):
  winning_numbers = []
  while (True):
    winning_number = random.randint(1,combination_range)

    if winning_number in winning_numbers:
      continue

    winning_numbers.append(winning_number)

    if len(winning_numbers) == combination_count:
      break

  return winning_numbers

def getWinningTickets(tickets, winning_numbers):
  winning_tickets = []
  for ticket in tickets:
    numbers = ticket["numbers"]
    numbers.sort()
    winning_numbers.sort()
    if(numbers == winning_numbers):
      winning_tickets.append(ticket)
  return winning_tickets

def createSettingsTable(combination_count, combination_range):
  table = PrettyTable()
  table.field_names = ["Combination Count", "Combination Range"]
  table.add_row([combination_count, "1 to {}".format(combination_range)])
  return table

def createTicketsTable(combination_count, tickets):
  table = PrettyTable()
  header = ["Username"]
  rows = []
  for i in range(combination_count):
    header.append("No. {}".format(i+1))

  for ticket in tickets:
    if len(ticket) != 0:
      rows.append([ticket["username"], *ticket["numbers"]])

  table.field_names = header
  table.add_rows(rows)
  return table

def createWinningNumbersTable(winning_numbers):
  table = PrettyTable()
  header = []
  row = []
  for i, number in enumerate(winning_numbers):
    header.append("No. {}".format(i+1))
    row.append(number)
  
  table.field_names = header
  table.add_row(row)
  return table

def displayTable(title, table):
  print("{}:\n{}\n".format(title, table))
  return "{}:\n{}\n".format(title, table)

def startLotteryOrEnterUser():
  while (True):
    try:
      print("\nPlease choose 1 or 2 only!")
      print("[1] Enter another user")
      print("[2] Start the lottery")
      choice = int(input("Choice: "))
    except ValueError:
      print("Please enter a valid value!")
      continue
    if choice < 1 or choice > 2:
      continue
    else:
      break
  return choice

def startAnotherLotteryOrStopSimulator():
  while (True):
    try:
      print("\nPlease choose 1 or 2 only!")
      print("[1] Start another lottery")
      print("[2] Stop the simulator")
      choice = int(input("Choice: "))
    except ValueError:
      print("Please enter a valid value!")
      continue
    if choice < 1 or choice > 2:
      continue
    else:
      break
  return choice

def saveToFile(settings_table, tickets_table, winning_numbers_table, winning_tickets_table):
  with open("lottery.txt", "a") as file:
    file.write("DATE: {}\n\n".format(datetime.datetime.now()))
    file.write("LOTTERY SETTINGS:\n{}\n\n".format(settings_table))
    file.write("TICKETS:\n{}\n\n".format(tickets_table))
    file.write("WINNING NUMBERS:\n{}\n\n".format(winning_numbers_table))
    file.write("CONGRATULATIONS TO THE FOLLOWING WINNER/S:\n{}\n".format(winning_tickets_table))
    file.write("\n====================================================================\n\n")
  return

def main():
  while(True):
    clearConsole()
    tickets = []
    settings_table = ""
    tickets_table = ""
    winning_numbers_table = ""
    winning_tickets_table = ""

    print("Standard Lottery Simulator is currently running...\n")
    combination_count = getCombinationCount()
    combination_range = getCombinationRange()
    settings_table = createSettingsTable(combination_count, combination_range)
    
    while(True):
      # DISPLAY SUMMARY
      clearConsole()
      displayTable("LOTTERY SETTINGS", settings_table)
      tickets_table = createTicketsTable(combination_count, tickets)
      displayTable("TICKETS", tickets_table)
      # DISPLAY SUMMARY

      username = input("Enter Username: ")
      numbers = []
      for i in range(combination_count):
        print("Please enter a Number from 1 to {} only!".format(combination_range))
        number = getCombination(i, numbers, combination_count, combination_range)
        numbers.append(number)

      tickets.append({
        "username": username,
        "numbers": numbers
      })

      # DISPLAY SUMMARY
      clearConsole()
      displayTable("LOTTERY SETTINGS", settings_table)
      tickets_table = createTicketsTable(combination_count, tickets)
      displayTable("TICKETS", tickets_table)
      # DISPLAY SUMMARY
    
      choice = startLotteryOrEnterUser()
      if(choice == 2): break

    winning_numbers = getWinningNumbers(combination_count, combination_range)
    winning_numbers_table = createWinningNumbersTable(winning_numbers)
    winning_tickets = getWinningTickets(tickets, winning_numbers)
    winning_tickets_table = createTicketsTable(combination_count, winning_tickets)

    # DISPLAY SUMMARY
    clearConsole()
    displayTable("LOTTERY SETTINGS", settings_table)
    displayTable("TICKETS", tickets_table)
    displayTable("WINNING NUMBERS", winning_numbers_table)
    displayTable("CONGRATULATIONS TO THE FOLLOWING WINNER/S", winning_tickets_table)
    # DISPLAY SUMMARY

    #SAVE TO FILE
    saveToFile(settings_table, tickets_table, winning_numbers_table, winning_tickets_table)
    #SAVE TO FILE

    choice = startAnotherLotteryOrStopSimulator()
    if(choice == 2): break

if __name__ == "__main__":
  main()
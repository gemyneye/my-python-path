import os
os.system("clear")

# fizzbuzz

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0
indiv_count = 0

for i in range(1, 101):

  if (i % 3 == 0) and (i % 5 ==0):
    print(f"{i}: FizzBuzz")
    fizzbuzz_count += 1
  elif (i % 3 == 0):
    print(f"{i}: Fizz")
    fizz_count += 1
  elif (i % 5 == 0):
    print(f"{i}: Buzz")
    buzz_count += 1
  else:
    print(f"{i}.")
    indiv_count += 1
  i += 1
print("\nReport:")
print(f"Fizzbuzz {fizzbuzz_count}")
print(f"Fizz: {fizz_count}")
print(f"Buzz: {buzz_count}")
print(f"Indivisible by 3 or 5: {indiv_count}")


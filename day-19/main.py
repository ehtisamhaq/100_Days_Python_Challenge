# for counter in range(2, 5):
#     print(counter)

# total = 0
# for counter in range(10):
#   total += 10
#   print(total)


loan = 100000
apr = 0.08
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))
for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))

print()

for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<04}".format(i, i**2, i**3))

print("Pi is approximately {0:50.49f}".format(22/7))

print(f"Hello{'':<18}World{'':<30}function")
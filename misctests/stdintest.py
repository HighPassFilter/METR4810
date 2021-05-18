import sys, select

print("Please provide command input or h for help:  ")


while True:
    i, o, e = select.select( [sys.stdin], [], [], 0.02 )

    if (i):
        print("You said", sys.stdin.readline().strip())
    # else:
    #     print("You said nothing!")
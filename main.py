# Banker's algorithm variables
available = [3, 3, 2]
max_demand = [
    [7, 5, 3],  # p0
    [3, 2, 2],  # p1
    [9, 0, 2],  # p2
    [2, 2, 2],  # p3
    [4, 3, 3]   # p4
]
allocation = [
    [0, 1, 0],  # p0
    [2, 0, 0],  # p1
    [3, 0, 2],  # p2
    [2, 1, 1],  # p3
    [0, 0, 2]   # p4
]
need = []
request = []


def is_safe():
    work = available
    finish = [False for _ in range(0, len(max_demand))]

    # Safety algorithm
    for k in range(0, len(max_demand)):
        for i in range(0, len(max_demand)):

            if finish[i] is False and need[i] <= work:
                temp = []
                for work_, alloc_ in zip(work, allocation[i]):
                    temp.append(work_ + alloc_)
                work = temp
                finish[i] = True

    # Check if all finished
    for finished in finish:
        if not finished:
            return False  # unsafe

    return True  # safe


# Resource-Request Algorithm
def res_request(i, request):
    # code here Bahaa
    for j in range(3):
        
        if request[j] > need[i][j] :
            print("-------------------------------------------------------------------")
            print("raise error condition, since process has exceeded its maximum claim")
            print("-------------------------------------------------------------------")
            return False

    for j in range(3):
        if request[j] > available[j]:
            print("----------------------------------------------------------")
            print("p"+ str(i) +" must wait, since resources are not available")
            print("----------------------------------------------------------")
            return False

    for j in range(3):
        available[j]= available[j]-request[j]
        need[i][j] = need[i][j]-request[j]
        allocation[i][j] = allocation[i][j]+ request[j]

    if is_safe() :
         print("Successful")
    else:
        print("Unsuccessful")
        # The old resource-allocation state is restored.
        for j in range(3):
            available[j] = available[j] + request[j]
            need[i][j] = need[i][j] + request[j]
            allocation[i][j] = allocation[i][j] - request[j]



# Resource release
def res_release(i, release):
    # code here Tawaty
    return


def display_info():

    print("    alloc    max    avail   need")
    for i in range(0, len(max_demand)):
        print("p" + str(i) + '\t', end='')

        for j in range(0, 3):
            print(str(allocation[i][j]) + ' ', end='')
        print('  ', end='')

        for j in range(0, 3):
            print(str(max_demand[i][j]) + ' ', end='')
        print('  ', end='')

        for j in range(0, 3):
            if i == 0:
                print(str(available[j]) + ' ', end='')
            else:
                print('  ', end='')

        print('  ', end='')

        for j in range(0, 3):
            print(str(need[i][j]) + ' ', end='')
        print('  ', end='')

        print('')


# main
def main():

    # Calculating need (maximum demand - allocation)
    for i in range(0, len(max_demand)):
        temp = []

        for max_, alloc_ in zip(max_demand[i], allocation[i]):
            temp.append(max_ - alloc_)

        need.append(temp)

    # Printing info
    display_info()

    # User input
    # RQ p1 1 0 2 (request)
    # RL p2 3 0 2 (release)
    user_input = input("> ")

    while user_input != "Quit":
        command = user_input.split()

        if command[0] == "RQ" or command[0] == "RL":
            process_num = int(command[1][1:])
            request = [int(x) for x in command[2:]]

            if command[0] == "RQ":
                print("Request!")
                res_request(process_num, request)

            else:
                print("Release!")
                res_release(process_num, request)

            # Printing the updated info
            display_info()

        else:
            print("Unknown command!")

        user_input = input("> ")


if __name__ == "__main__":
    main()
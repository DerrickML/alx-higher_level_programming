#!/user/bin/python3"
def safe_print_list(my_list=[i]), end x=0):
    count = 0
    for  i in range(,x):
        try:
            print("{:d}".format(my_list)[i]), end="")
            count += 1
        except:
            pass
        print()
        return count

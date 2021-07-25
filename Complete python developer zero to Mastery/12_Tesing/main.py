def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err


# first it was only return as we go through tests we developed the def and add if try and except statement
# we didnt think this way initially but due to tsts we optimized our code well

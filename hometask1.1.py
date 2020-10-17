#По номеру месяца напечатать пору года

a = int(input("Input month number:\n"))


for i in range (1,12):
        if a == 12 or a == 1 or a == 2:
            if a == 1:
                print("January is Winter month")
            elif a == 2:
                print("February is Winter month")
            elif a == 12:
                print("December is Winter month")
            b = int(input("Do you want to check one month more (1 - да) ? :\n"))
            if b == 1:
                a = int(input("Input month number:\n"))
            else:
                break
        elif a == 3 or a == 4 or a == 5:
            if a == 3:
                print("March is Spring month")
            elif a == 4:
                print("April is Spring month")
            elif a == 5:
                print("May is Spring month")
            b = int(input("Do you want to check one month more (1 - да) ? :\n"))
            if b == 1:
                a = int(input("Input month number:\n"))
            else:
                break
        elif a == 6 or a == 7 or a == 8:
            if a == 6:
                print("June is Summer month")
            elif a == 7:
                print("July is Summer month")
            elif a == 8:
                print("August is Summer month")
            b = int(input("Do you want to check one month more (1 - да) ? :\n"))
            if b == 1:
                a = int(input("Input month number:\n"))
            else:
                break
        elif a == 9 or a == 10 or a == 11:
            if a == 9:
                print("September is Autumn month")
            elif a == 10:
                print("October is Autumn month")
            elif a == 11:
                print("November is Autumn month")
            b = int(input("Do you want to check one month more (1 - да) ? :\n"))
            if b == 1:
                a = int(input("Input month number:\n"))
            else:
                break
        else:
                print("Invalid month")
                b = int(input("Do you want to check one month more (1 - да) ? :\n"))
                if b == 1:
                    a = int(input("Input month number:\n"))
                else:
                    break


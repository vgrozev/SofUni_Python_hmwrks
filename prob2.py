N = int(input())
N_final = False


firstUpper = input().upper()
firstUpper_final = False
char1 = ord(firstUpper)

lowerLetter = input().lower()
lowerLetter_final = False
char2 = ord(lowerLetter)

secondUpper = input().upper()
secondUpper_final = False
char3 = ord(secondUpper)

M = int(input())
M_final = False


count = int(input())


if N > 92 or M < 15:
    print("invalid")
else:
    N_tens = N // 10
    N_ones = N % 10
    if N_ones > 2:
        N = 12 + N_tens * 10
    else:
        N = 2 + N_tens * 10

    M_tens = M // 10
    M_ones = M % 10
    if M_ones >= 5:
        M = 5 + M_tens * 10
    else:
        M = M_tens * 10 - 5
    #
    # num = N
    # num2 = M

    output = str(N) + firstUpper + lowerLetter + secondUpper + str(M)
    count -= 1
    print(output)
    for num in range(N, 93, 10):
        for char1 in range(ord(firstUpper), ord('Z') + 1):
            for char2 in range(ord(lowerLetter), ord('z') + 1):
                for char3 in range(ord(secondUpper), ord('Z') + 1):
                    for num2 in range(M, 14, -10):
                        if count == 0:
                            break
                        else:
                            output_in = str(num) + chr(char1) + chr(char2) + chr(char3) + str(num2)
                            if output_in == output:
                                continue
                            else:
                                count -= 1
                                print(output_in)
                                output = output_in
                        #end of num2 loop
                    if count == 0:
                        break
                    else:
                        output_in = str(num) + chr(char1) + chr(char2) + chr(char3) + str(num2)
                        if output_in == output:
                            continue
                        else:
                            count -= 1
                            print(output_in)
                            output = output_in
                    if char3 == ord('z'):
                        secondUpper_final = True
                        # end of char3 loop
                if count == 0:
                    break
                else:
                    output_in = str(num) + chr(char1) + chr(char2) + chr(char3) + str(num2)
                    if output_in == output:
                        continue
                    else:
                        count -= 1
                        print(output_in)
                        output = output_in
                if char2 == ord('z'):
                    lowerLetter_final = True
                    # end of char2 loop
            if count == 0:
                break
            else:
                output_in = str(num) + chr(char1) + chr(char2) + chr(char3) + str(num2)
                if output_in == output:
                    continue
                else:
                    count -= 1
                    print(output_in)
                    output = output_in
            if char1 == ord('Z'):
                firstUpper_final = True
                # end of char1 loop
        if count == 0:
            break
        else:
            output_in = str(num) + chr(char1) + chr(char2) + chr(char3) + str(num2)
            if output_in == output:
                continue
            else:
                count -= 1
                print(output_in)
                output = output_in


                    #end of num loop
    #
    #         count -= 1
    #
    #
    #
    # print(())
    #
    # print(count)

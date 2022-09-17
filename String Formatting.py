def print_formatted(number):
    binlen = len(bin(number)[2:])
    for i in range(1,number+1):
      print(str(int(i)).rjust(binlen), oct(i)[2:].rjust(binlen), hex(i)[2:].rjust(binlen).upper(), bin(i)[2:].rjust(binlen))
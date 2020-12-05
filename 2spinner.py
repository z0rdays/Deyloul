def carousel_decrypt(num):
    bin_string = chunkstring(bin(num)[2:],7)
    i = 7
    f = ''
    for c in bin_string:
        f += chr(int("0" + c[i:] + c[:i],2))
        i -=1
        if i < 0: i=7
    return f

print(carousel_decrypt(6838670745825122932886199347866255930502612544243548566773595))
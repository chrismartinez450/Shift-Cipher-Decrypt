cipher = 'ar9r5IorIqv6p285ntrqMIVsIVI0r5rI681xIv1I7urIy20r67I3v76I2sIa29nIfp27vnLI0v7uI7urIe2px!IZ2817nv16I3vyrqI21IzrLIVI028yqIun1tI21LIr r5pv6rIsnv7uLIn1qIxrr3I83It22qIp285ntrLIn1qIVI028yqIp2zrI287I21I723M'
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.'

for key in range(len(alph)):
    result = ''
    for symbol in cipher:
        if symbol in alph:
            number = alph.find(symbol)
            number = number - key
            if number < 0:
                number = number + len(alph)
            result = result + alph[number]
        else:
            result = result + symbol
    print('result #%s: %s' % (key, result))

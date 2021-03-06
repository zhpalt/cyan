# coding=utf-8
# generate morse code

morse={'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
'y':'-.--', 'z':'--..', '0':'-----', '1':'.----',
'2':'..---', '3':'...--', '4':'....-', '5':'.....',
'6':'-....', '7':'--...', '8':'---..', '9':'----.',
'.':'.-.-.-', ',':'--..--', ':':'---...', '?':'..--..', '-':'-....-',
'/':'-..-.', '=':'.-.-.', '@': '...-.-', '!':'...-.-', ' ':' '}

def morse_h(plain):
    plain = plain.lower()
    crypt = ''
    for n in plain:
        c = morse.get(n)
        if c != None:
            crypt += c
        else:
            crypt += '[none: ' + n + ']'
    return crypt

def main():
    while True:
        print "[plain] <<<",
        plain = raw_input()
        if len(plain) == 0:
            break
        crypt = morse_h(plain)
        print "[crypt] >>> %s" % crypt

if __name__ == '__main__':
    print '这是莫尔斯编码程序，输入空字符串退出'
    main()

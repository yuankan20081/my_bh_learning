__author__ = 'yuankan'
'''
this is tools take from books, net, or write by my-self
'''

def hexdump(src, length=16):
    '''
    this is an easy function take from the book [black hat python]
    :param src:
    :param length:
    :return:
    '''
    result = []
    digits = 4 if isinstance(src, unicode) else 2
    for i in xrange(0, len(src), length):
        s = src[i:i+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x))  for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.'  for x in s])
        result.append( b"%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text) )
    print b'\n'.join(result)

if __name__ == "__main__":
    ''' test it'''
    import urllib
    fd = urllib.urlopen("http://www.baidu.com")
    if fd.getcode()==200:
        hexdump(fd.read(2048))
    else:
        hexdump("Hello, world")
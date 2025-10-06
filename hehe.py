def helloworld(s):
    if s=='print':
        print('hello world')

def bitcoin (btc):
    print(f'{btc} BTC = {btc*10138857} руб')


helloworld('print')
bitcoin(float(input('число BTC: ')))
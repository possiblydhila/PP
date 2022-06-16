import threading
import time

govs = ['GERMANY','AUSTRIA','DENMARK','FRANCE','ITALY','BELGIUM','SPAIN','GREECE','FINLAND','PORTUGAL',
        'ROMANIA','SLOVENIA','LUXEMBOURG','CROATIA','SWEDEN','NETHERLANDS','BULGARIA','ESTONIA','HUNGARY','POLAND',
        'CZECH','SLOVAKIA','LITHUANIA','LATVIA','MONACO','ANDORRA','SAN MARINO','CYPRUS','TURKEY','LIECHTENSTEIN',
        'VATICAN','UKRAINE','NORWAY','BELARUS','ENGLAND','IRELAND REP','SCOTLAND','WALES','KAZAKHSTAN','ICELAND',
        'SERBIA','BOSNIA','ESTONIA','SWITZERLAND','MALTA','ARMENIA','AZERBAIJAN','USA','CANADA','LAOS',
        'FIJI','NEW ZEALAND','TUVALU','TONGA','AUSTRALIA','VIETNAM','BHUTAN','CAMBODIA','MONGOLIA','S. KOREA',
        'GEORGIA','MEXICO','BRAZIL','ARGENTINA','MOROCCO','EGYPT','ALGERIA','UAE','PAKISTAN','INDIA',]
message = '''Dear Mr/Mrs/Ms ambassador of {} for Indonesia, can you please send me your country's flag. Thank you very much'''
delays = [2,2,2,4,3,5,7,8,4,9,2,2,2,4,3,5,7,8,4,9,2,2,2,4,3,5,7,8,4,9,2,2,2,4,3,5,7,8,4,9,2,2,2,4,3,5,7,8,4,9,8,4,9,2,2,8,4,9,2,2,8,4,9,2,2,8,4,9,2,2]
def tasks(gov, delay):
   # print(message.format(gov))
    time.sleep(delay)
    #print(f'--{gov} flag accepted. will be received in day {delay}')


def main():
    for i in range(len(govs)):
        x = threading.Thread(target=tasks, args=[govs[i], delays[i]])
        x.start()
    x.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'all {len(govs)} emails are sent. yay!')
    print('active threads:', threading.activeCount())
    print(f"{end-start} seconds")
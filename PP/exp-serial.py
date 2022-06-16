import time
#secara serial/ proses scr sinkron
def count():
    print('satu')
    time.sleep(1)
    print('dua')
    time.sleep(1)

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    # kek millis keknyasi
    s = time.perf_counter() 
    main()
    # hitung time execution
    elapsed = time.perf_counter() - s
    print(f'{__file__} dieksekusi dalam {elapsed:0.2f} detik')

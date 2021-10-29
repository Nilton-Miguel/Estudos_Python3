from time import sleep

cor = 31

for t in range(10, 0, -1):
    print(t)
    sleep(1)
print('')
for v in range(0, 7):
    print(f'\033[{cor}mFOGOS !!!')
    cor += 1
    sleep(0.5)
    print('')

import playsound

while True:

    print('Suas opções são:\n{:<16} \n{:<16} \n'.format('ride', 'tear in my heart'))
    song = input('informe a música: ')

    playsound.playsound('C:/{}.mp3'.format(song), True)













































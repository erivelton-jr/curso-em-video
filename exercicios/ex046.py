from time import sleep
import emoji

print('CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFICIO!')
sleep(1)

for f in range(10, -1, -1):
    print(f)
    sleep(1)
print(emoji.emojize('🎇', language="en"), end='')
sleep(1)
print(emoji.emojize('✨', language='en'), end='')
sleep(1)
print(emoji.emojize('🎉', language='en'), end='')
sleep(1)
print(emoji.emojize('🎊', language='en'))
#✨🎉🎊

palavra_secreta = "github"

digitadas = []
chances = 5

play = input('Estou pensando em uma palavra, você consegue adivinhar o que é? s/n: ')

if play == 'n':
    print('Okay, fica pra próxima!')
    break

while play == 's':
    letra = input('Digite uma letra: ')

    if chances <= 1:
        continuar = input('Que pena, você perdeu! Deseja continuar? s/n: ')
        if continuar == 's':
            chances = 5
            continue
        elif continuar == 'n':
            break

    if len(letra) > 1:
        print('Ops! Digite apenas uma letra.')
        continue

    if letra.isnumeric():
        print('Ops! Digite apenas letras :)')

    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'Yay! Você acertou a letra "{letra}".')
        print(f'Você ainda possui {chances} chances.')
        print()
    else:
        print(f'Ops! A letra "{letra}" não existe na palavra que eu estou pensando.')
        digitadas.pop()
        chances = chances - 1
        print(f'Você ainda possui {chances} chances.')
        print()

    secreto_temporario = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra_secreta:
        print(f'Yay! Você acertou a palavra secreta com um total de {chances} chances restantes! Palavra secreta: {palavra_secreta}')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}')

#Digite a sua idade:

#- Se você tiver menos de 16 anos, não pode votar.
#- Se você tiver 16 anos, 17 anos ou mais de 65 anos, não é obrigado a votar.
#- Se você tiver mais de 18 anos e menos de 65 anos, é obrigado a votar.

idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Você não pode votar.")
elif idade >= 65 or 16 <= idade <= 17:
    print("Você não é obrigado a votar.")
else:
    print("Você é obrigado a votar.")
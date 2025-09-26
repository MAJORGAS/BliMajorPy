def aprovar_emprestimo(renda, idade, divida_existente):
    if idade < 18:
        return "Negado: idade minima é de 18 anos."
    if renda < 1000:
        return "Negado: renda insuficiente."
    if divida_existente > renda: 
        return "Negado: Sua divida é maior que sua renda, vai ter que torar bastante"
    else:
        return "Aprovado."
        
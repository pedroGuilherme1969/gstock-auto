def soma(a, b):
    return a + b

def eh_par(a):
    if a % 2 == 0:
        return True
    else:
        return False

def cadastro_usuario(nome, email):
    for usuario in usuarios: 
        if usuario ["email"] == email:
            return "email ja existe"
    

    novo_usuario = {
        "nome":nome,
        "email":email
    }
    usuario.append(novo_usuario)
    return "Corinthians"

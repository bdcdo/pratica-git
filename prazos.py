def prazo_em_dobro(dias):
    return dias * 2


def dias_restantes(prazos, decorridos):
    return prazos - decorridos


print(prazo_em_dobro(15))
print(prazo_em_dobro(30))
print(dias_restantes(prazo_em_dobro(15), 12))

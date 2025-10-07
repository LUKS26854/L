# Mini Bot de Perguntas sobre Python


print("🤖: Olá! Eu sou o Elden.Bot, seu assistente das Terras Intermédias.")
print("Digite 'sair' para encerrar a conversa.\n")


while True:
    pergunta = input("Você: ").strip().lower()


    if pergunta == "sair":
        print("🤖: Até mais! Bons estudos! 👋")
        break


    # Respostas pré-definidas
    elif "limgrave" in pergunta:
        print("🤖: Lingrave é a primeira área disponivel em Elden Ring.\n--------\n Chefes:\n Margit o Agouro caido;\n Godrik, o Enxertado;\n Antigo Herói de Zamor;\n Caçador de Sinos;\n Sentinela da Arvore;\n Patches.\n--------\n NPC:\n Melina;\n Comerciante Kalé;\n Mascara branca Varre;\n Alexander;\n Caçador de dedos Yura;\n Roderika;\n Blaidd;\n Patches.\n--------\n Itens-Chave:\n Medalhão de Dectos(esquerdo).          ")


    elif "liurnia dos lagos" in pergunta:
        print("🤖: Liurnia dos Lagos é a 'segunda' área disponivel em Elden Ring.\n--------\n Chefes:\n Rennala, Rainha da lua cheia;\n Lobo vermelho de Radagon;\n Calaveira Real Loretta;\n Assassino de Agouros;\n Wyrm de magma Makar\n Nobre da pele divina.\n--------\n NPC:\n Rennala;\n Ranni, a bruxa;\n Rya;\n Mestre de ferraria Iji;\n Miriel pastor de votos;\n Calaveiro Diallos;\n Hyetta;\n Latenna.\n--------\n Itens-Chaves:\n Chave do selo de Raya Lucaria;\n Medalhão secreto da Arvore Sacra(direito).   ")


    elif "altus plateau" in pergunta or "leyndell, capital real" in pergunta or "leyndell" in pergunta:
        print("🤖: Altus Plateau/Capital Real é a terceira área disponivel em Eldeen Ring, temos acesso a ela depois de coletar as duas partes do medalhão de Dectos.\n Chefes:\n Godfrey, o primeiro Elden Lord;\n Radagon da Ordem Aurea;\n Morgot, o Rei Agouro;\n Sentinela da Arvore Dracônico;\n Assassino da Faca negra;\nMogh, o Agouro;\n Elemer of the Briar.\n--------\nNPC:\n Tres Dedos;\n Mascara Dourada\n Millicent;\n Irmão Corhyn;\n--------\n Itens-Chaves:\n Medalhão de Rhodes.  ")


    elif "caelid" in pergunta:
        print("🤖: Caelid é a 'quarta' área disponivel em Elden Ring.\n--------\n Chefes:\n Radanh Flagelo Estelar;\n Apostolo da pele Divina;\n Calavaria da Noite;\n Espirito da Arvore Putrida;\n Menbro da lamina negra;\n Mago de Batalha Hughes;\n Cavaleiros da podridão escarlate.\n--------\n NPC:\n Clérico Bestial;\n O grande Jarro.\n--------\n Itens-Chaes: Medalhão de Dectos(direito) ")


    elif "montanha dos gigantes" in pergunta:
        print("🤖: A montanha dos gigantes é quinta área disponivel em Elden Ring.\n--------\n Chefes:\n Gigante de Fogo;\n Comandante Niall\n Mago de Batalha Hughes\n Cavaleiro da messa redonda Vyke;\n Passaro do rito de Morte;\n Borealis, a Névoa Congelante\n--------\nNPC:\n Shabriri;\n Irmão Corhyn;\n Mascara dourada;\n Millicent.\n--------\n Itens-Chaves:\n Medalhão secreto da Arvore Sacra(esquerdo)")
    
    elif "farum azula" in pergunta:
        print("🤖: Farum Azula é a sétima área disponive em Elden Ring.\n--------\n Chefes:\n Maliketh, a lamina negra;\n Dragon Lord Placidusax;\n Dupla da pele Divina:\n--------\nNPC:\n Alexander.\n--------\nItens-Chaves:\n Runa da Morte.")
    
    elif "manção vulcanica" in pergunta:
        print("🤖: A Manção Vulcanica é sexta área disponivel em elden Ring.\n--------\n Chefes:\n Rykard, Senhor da blasfemia;\n Nobre da pele divina;\n Virgem abdutora.\n--------\nNPC:\n Rya;\n Tanith\n Cavaleiro Diallos\n Cavaleiro Bernahl.\n--------\n Itens-Chaves:\n Não possue itens-chave")

    elif "arvore sacra" in pergunta:
        print("🤖: A Arvore Sacra é oitava área disponivel em elden Ring, temos acesso a ela depois de coletar as duas partes do medalão secreto da arvore sacra.\n--------\n Chefes:\n Malenia, blade of Miquela;\n Lorreta Cavalaria Real.\n--------\nNPC:\n Millicent.\n--------\n Itens-Chaves:\n Não possue itens-chave")

    elif  "FAQ" in pergunta or "faq" in pergunta:
        print("🤖:Como o mapa funciona?\nÉ um mundo aberto com poucas instruções; você precisa encontrar masmorras por conta própria, mas pode usar até cinco sinalizadores e 100 marcadores para marcar locais importantes e não se perder.\n--------\n É possível subir de nível?\n Sim, subir de nível é uma mecânica central do jogo, mas não se trata de um RPG tradicional, sendo uma combinação de exploração, combate e progressão de personagem.\n--------\n Qual a dificuldade do jogo?\n É um jogo com alta dificuldade, característico dos títulos da FromSoftware, com inimigos fortes e a famosa tela de 'Você Morreu'.\n--------\n Magia é ilimitada?\n Não, a magia não é ilimitada e sua recuperação não é rápida, sendo um risco se usada excessivamente.\n--------\n Como funcionam as armas?\n Existem diversas habilidades de armas que podem ser trocadas em locais específicos, exceto nas armas especiais, cujas habilidades são fixas.")


    else:
        print("🤖: Hmmm... não entendi. Pergunte sobre limgrave, liurnia dos lagos, altus plateu, caelid, montanha dos gigantes, farum azula, manção vulcanica,arvore sacra ou FAQ.")

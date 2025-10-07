def exibir_menu():

    """Mostra o menu de opções disponíveis"""
    print("\n" + "="*50)
    
    print("🎓 ASSISTENTE VIRTUAL - CURSO DE PROGRAMAÇÃO")
    print("="*50)
    print("Digite sua dúvida ou escolha uma opção:")
    print("📚 'menu' - Ver tópicos disponíveis")
    print("❓ 'ajuda' - Como usar este assistente")
    print("🚪 'sair' - Encerrar atendimento\n")


def listar_topicos():

    """Lista todos os tópicos que o bot conhece"""
    print("\n📚 Tópicos disponíveis:")
    print("  ✔ Variáveis e tipos de dados")
    print("  ✔Estruturas condicionais (if/else)")
    print("  ✔ Laços de repetição (for/while)")
    print("  ✔ Listas e manipulação")
    print("  ✔ Funções")
    print("  ✔ Importar bibliotecas\n")

def buscar_resposta(pergunta):

    """Procura a resposta adequada baseada na pergunta"""
   
    # Dicionário com respostas organizadas
    respostas = {
        "variavel": {
            "texto": "Variáveis armazenam informações. Em Python, basta atribuir um valor:",
            "exemplo": "nome = 'João'\nidade = 17\naltura = 1.75"
        },
        "if": {
            "texto": "Use 'if' para tomar decisões no código:",
            "exemplo": "nota = 7\nif nota >= 6:\n    print('Aprovado!')\nelse:\n    print('Recuperação')"
        },
        "laços":{
            "texto": "Laço faz com que blocos de código se repitam por um numero (X) de vezes:",
            "exemplo": "for i in range(5):\n print(f"Número: {i}")"
        }
        "lista":{
            "texto": "A 'lista' é usada para armazenar multiplos itens dentro de uma unica variavel",
            "exemplos": "produtos = ['maçã', 'banana', 'laranja']\n print(produtos)"
        }
        "funções":{
            "texto": "Def(funções) são blocos de código que realizam determinadas tarefas que normalmente precisam ser executadas diversas vezes dentro de uma aplicação.",
            "exemplos": "def hello(meu_nome):\nint('Olá',meu_nome)"
        }
        "importar bibliotecas":{
            "texto": "Para importar uma biblioteca em Python, primeiro use pip install <nome_da_biblioteca> no terminal para instalar a biblioteca(caso seja esterna).",
            "exemplos": "import random"
           


        }


    }

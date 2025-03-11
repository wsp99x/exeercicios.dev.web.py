from dataclasses import dataclass

def exercicio_1():
    # Solicita uma frase e substitui vírgulas por pontos
    print("Exercício 1")
    frase = input("Digite uma frase: ").strip().replace(',', '.')
    print(f"Frase modificada: {frase}\n")

def exercicio_2():
    # Conta quantas palavras começam com a letra 'a'
    print("Exercício 2")
    frase = input("Digite uma frase: ")
    count = sum(1 for palavra in frase.lower().split() if palavra.startswith('a'))
    print(f"Número de palavras que começam com 'a': {count}\n")

@dataclass
class Produto:
    nome: str
    preco: float

def exercicio_3():
    # Permite ao usuário adicionar roupas ao carrinho
    print("Exercício 3")
    produtos = [Produto("Camiseta", 50.0), Produto("Calça", 120.0), Produto("Vestido", 80.0), Produto("Jaqueta", 150.0)]
    carrinho = []
    total_compra = 0.0
    
    while True:
        print("Lista de roupas:")
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto.nome} - R${produto.preco:.2f}")
        
        try:
            escolha = int(input("Escolha o número do produto: ")) - 1
            if 0 <= escolha < len(produtos):
                carrinho.append(produtos[escolha])
                total_compra += produtos[escolha].preco
                print(f"{produtos[escolha].nome} adicionado ao carrinho.")
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
        
        if input("Deseja comprar mais? (s/n): ").strip().lower() != 's':
            break
    
    print(f"Produtos comprados: {', '.join(produto.nome for produto in carrinho)}")
    print(f"Valor total da compra: R${total_compra:.2f}\n")

def exercicio_4():
    # Gerencia a compra de produtos com saldo inicial
    print("Exercício 4")
    saldo = 1000
    carrinho = []
    
    while True:
        nome = input("Nome do produto: ")
        try:
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir valores numéricos.")
            continue
        
        total = preco * quantidade
        if total > saldo:
            print("Saldo insuficiente!")
            continue
        
        saldo -= total
        carrinho.append((nome, preco, quantidade))
        print(f"{nome} adicionado ao carrinho. Saldo restante: R${saldo:.2f}")
        
        if input("Deseja adicionar mais itens? (s/n): ").strip().lower() != 's':
            break
    
    print(f"Saldo final: R${saldo:.2f}\nCarrinho de compras: {', '.join(f'{qtd}x {nome} (R${preco:.2f})' for nome, preco, qtd in carrinho)}\n")

def main():
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4()

if __name__ == "__main__":
    main()
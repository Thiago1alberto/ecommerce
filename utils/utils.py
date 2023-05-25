def formato_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def qtd_total_carrinho(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def carrinho_valor_total(carrinho):
    return sum(
        [
            item.get('preco_total_promocional')
            if item.get('preco_total_promocional')
            else item.get('preco_total')
            for item
            in carrinho.values()
        ]
    )

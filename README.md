# Operação LEVA JEITO

**Execução : **
./guarda <metodo> <opcao> <pasta> <saída>
― <metodo> : indica o método a ser utilizado ( -hash ou -hmac senha)
― <opcao>: indica a ação a ser desempenhada pelo programa
• -i : inicia a guarda da pasta indicada em <pasta>, ou seja, faz a leitura de todos os arquivos da pasta (recursivamente)
registrando os dados e Hash/HMAC de cada um e armazenando numa estrutura própria (Ex: tabela hash em uma
subpasta oculta ./guarda – ou pode ser usada uma árvore B)
• -t : faz o rastreio (tracking) da pasta indicada em <pasta>, inserindo informações sobre novos arquivos e indicando
alterações detectadas/exclusões
• -x : desativa a guarda e remove a estrutura alocada
― <pasta> : indica a pasta a ser “guardada”
― <saida> : indica o arquivo de saída para o relatório (-o saída). Caso não seja passado este parâmetro, a
saída deve ser feita em tela.




* ver modificações em arquivos, apresentando o caminho do arquivo e o que aconteceu com ele, por meio da comparação dos hashs*

**- jogar tudo em pasta oculta; -usar ED árvore (esquema do diretório, não é bin), hash..., com relatório, até dia 01**

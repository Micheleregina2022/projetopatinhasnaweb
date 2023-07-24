# Documentação do código da análise de dados sobre animais em situação de rua em Guarapuava


Python 3.9 </br>
Jupyter notebook - VsCode



1 - **Importação das Bibliotecas:**

pandas (pd): Manipulação de dados tabulares.

matplotlib.pyplot (plt): Criação de gráficos.

re: Expressões regulares para manipulação de strings.

numpy (np): Computação numérica com arrays.

statistics: Cálculos estatísticos básicos.

seaborn (sns): Visualização de dados estatísticos.


2 - **Leitura da planilha e exibição:**

A variável "dados_atuais" armazena o caminho do arquivo de planilha a ser lido.

A função "read_csv" da biblioteca pandas é utilizada para ler o arquivo no formato CSV.

O conteúdo do arquivo é armazenado em um DataFrame chamado "dados".

Essa lista é então exibida usando a função "display()" para apresentar as questões do formulário.



3 - **Limpeza dos dados:**

 A função "drop_duplicates()" é aplicada no DataFrame "dados" para remover todas as linhas duplicadas com base em todas as colunas do DataFrame. Apenas a primeira ocorrência de cada conjunto de linhas duplicadas é mantida, e as demais são descartadas.

 A função "dropna()" é aplicada no DataFrame "dados" para remover todas as linhas que contêm valores ausentes (NaN). O parâmetro "how='all'" indica que a linha será removida somente se todos os valores nessa linha forem ausentes. O parâmetro "inplace=True" indica que a modificação será feita diretamente no DataFrame "dados", sem a necessidade de criar um novo DataFrame.



 4 - **Transformação dos dados:**

 A função "rename()" é aplicada ao DataFrame "dados" para renomear suas colunas, utilizando um dicionário como argumento.



 5 - **Diagnóstico inicial:**

5.1 Utilizando o método "value_counts()" do DataFrame, o código conta o número de respostas para cada valor único presente na coluna 'Bairro'. O resultado é armazenado na variável "respostas_bairro", que contém a contagem de respostas por bairro.

É criado um gráfico de barras utilizando a biblioteca matplotlib.pyplot.

O eixo x do gráfico representa os bairros, e o eixo y representa o número de respostas por bairro.

O método "plot(kind='bar')" é usado para criar o gráfico de barras com base nos dados de "respostas_bairro".

As funções "title()", "xlabel()", "ylabel()" são utilizadas para definir o título e os rótulos dos eixos do gráfico.

plt.xticks(rotation=45, ha='right')" é usado para ajustar a rotação e alinhamento dos rótulos do eixo x, facilitando a leitura dos nomes dos bairros.

Por fim, "plt.show()" é chamado para exibir o gráfico de barras.


5.2 Identificação de todos os bairros: O código utiliza a coluna 'Bairro' do DataFrame "dados" e a função "unique()" para obter uma lista com todos os valores únicos presentes nessa coluna.

Em seguida, a função "set()" é aplicada à lista para criar um conjunto de bairros únicos. Utilizar um conjunto garante que não haverá duplicatas.

O código cria outro conjunto chamado "bairros_sem_resposta", que é obtido subtraindo o conjunto de bairros com respostas ("respostas_bairro.index") do conjunto contendo todos os bairros ("todos_bairros").

Dessa forma, "bairros_sem_resposta" conterá os bairros que estão presentes na lista de todos os bairros, mas que não receberam nenhuma resposta na coluna 'Bairro' do DataFrame "dados".



6 -  **Extração de Números e Visualização de Dados:**

* Função "extrair_numero":

É definida a função "extrair_numero" que recebe um texto como entrada.
A função utiliza expressões regulares (regex) com a função "re.findall()" para encontrar um ou mais dígitos na string "texto".

Caso sejam encontrados dígitos, o primeiro número é convertido para inteiro e retornado. Caso contrário, é retornado "None".

* Extração dos Números das Colunas:

As colunas 'Cães_Rua' e 'Gatos_Rua' são convertidas para strings usando "astype(str)" e, em seguida, a função "extrair_numero" é aplicada a cada valor usando "apply(extrair_numero)".

Os números extraídos são armazenados em duas novas colunas do DataFrame: 'Cães_Rua_Int' e 'Gatos_Rua_Int'.

* Soma dos Números Extraídos:

É calculada a soma dos números nas colunas 'Cães_Rua_Int' e 'Gatos_Rua_Int' usando o método "sum()".

As somas são armazenadas nas variáveis "soma_caes" e "soma_gatos", respectivamente.

* Visualização dos Dados:

É criado um gráfico de pizza utilizando a biblioteca matplotlib.pyplot.

O eixo x do gráfico representa as categorias ('Cães' e 'Gatos') e o eixo y representa os valores das somas ("valores").

A função "pie()" é utilizada para criar o gráfico de pizza, com a porcentagem de cada categoria sendo exibida através do argumento "autopct='%1.1f%%'".

"startangle=140" define o ângulo inicial da plotagem, para posicionar a primeira categoria.

"plt.title()" define o título do gráfico, e "plt.axis('equal')" faz o gráfico de pizza circular.

Por fim, "plt.show()" é chamado para exibir o gráfico de pizza.



7 - **Análise e Visualização de Dados por Bairro:**

* Obtenção dos Bairros Únicos:

A lista "bairros_unicos" é obtida a partir da coluna 'Bairro' do DataFrame "dados", contendo todos os bairros únicos presentes nessa coluna.

* Cálculo das Somas por Bairro:

São criados dicionários "soma_caes_por_bairro" e "soma_gatos_por_bairro" para armazenar as somas de cães e gatos em situação de rua, respectivamente, para cada bairro.

O código itera sobre cada bairro único, seleciona as linhas correspondentes ao bairro atual e calcula a soma de cães e gatos utilizando a função "sum()". As somas são armazenadas nos dicionários.

*Exibição das Somas por Bairro:

O código imprime na tela a soma de cães e gatos em situação de rua para cada bairro. A saída contém os totais separados por bairro.

* Criação do DataFrame e Gráfico de Barras:

O código cria um DataFrame "totais_por_bairro" com os totais de cães e gatos em situação de rua por bairro, usando o dicionário criado anteriormente.

O DataFrame é ordenado de forma decrescente com base na quantidade de cães em rua ("Cães_Rua") e, em seguida, pela quantidade de gatos em rua ("Gatos_Rua").

O gráfico de barras é criado utilizando a função "plot(kind='bar')" do DataFrame "totais_por_bairro". O eixo x representa os bairros, o eixo y representa a quantidade e cada barra é rotulada com o número de cães e gatos em rua para o respectivo bairro.

O gráfico é estilizado com títulos, rótulos dos eixos, legendas e ajuste da rotação dos rótulos do eixo x, para melhor visualização.



8 - **Análise e Visualização de Dados de Cães e Gatos em Situação de Rua:**



* Filtrar Apenas Registros com Gatos em Situação de Rua:

Os registros em que a quantidade de gatos em situação de rua ("Gatos_Rua_Int") é igual a zero são removidos do DataFrame "dados".



* Análise Estatística Descritiva para Cães em Situação de Rua:

São calculadas as seguintes estatísticas para a coluna 'Cães_Rua_Int': média, variância, desvio padrão, mediana e moda.

As estatísticas são exibidas utilizando comandos "print".



*Visualização da Distribuição dos Cães em Situação de Rua:

É criado um histograma utilizando a biblioteca seaborn para visualizar a distribuição das quantidades de cães em situação de rua.

O argumento "bins=10" define o número de intervalos no histograma (10 bins).

O argumento "kde=True" inclui uma estimativa da densidade do kernel no gráfico para suavizar a distribuição.

O gráfico é rotulado com títulos, rótulos dos eixos e é exibido usando "plt.show()".



* Filtrar Apenas Registros com Gatos em Situação de Rua:

Os registros em que a quantidade de gatos em situação de rua ("Gatos_Rua_Int") é igual a zero são removidos do DataFrame "dados".


* Análise Estatística Descritiva para Gatos em Situação de Rua:

São calculadas as seguintes estatísticas para a coluna 'Gatos_Rua_Int' após o filtro: média, variância, desvio padrão, mediana e moda.

As estatísticas são exibidas utilizando comandos "print".


* Visualização da Distribuição dos Gatos em Situação de Rua:

É criado um histograma similar ao anterior, mas para visualizar a distribuição das quantidades de gatos em situação de rua após o filtro.

O gráfico é rotulado com títulos, rótulos dos eixos e é exibido usando "plt.show()".



...
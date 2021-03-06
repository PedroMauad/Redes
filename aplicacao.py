#!/usr/bin/python

from socket import *
from random import randint

s = socket(AF_INET,SOCK_STREAM)
s.bind(('localhost',1345))

coxinha = [
    ('A miséria ',
    'A inflação ',
    'O Golpe de 1964 ',
    'A violência ',
    'A crise ',
    'O crime ',
    'O nazismo ',
    'O Bolsa Família ',
    'O problema da educação ',
    'A corrupção '),

    ('é uma invenção ',
    'é uma estratégia ',
    'é uma manobra ',
    'é um complô ',
    'é culpa ',
    'é uma criação ',
    'é uma conspiração ',
    'é uma forma orquestrada ',
    'é a doutrinação ideológica ',
    'é uma articulação '),

    ('dos petralhas ',
    'do comunismo ',
    'dos esquerdopatas ',
    'da esquerda festiva ',
    'do socialismo ',
    'do Estado ',
    'da ditadura gay ',
    'da "esquerda caviar" ',
    'dos vândalos ',
    'das feminazis '),

    ('para deslegitimar ',
    'para vandalizar ',
    'para demoralizar ',
    'para destruir ',
    'para regular ',
    'para ameaçar ',
    'para superar ',
    'para roubar ',
    'para aterrorizar ',
    'para transgredir '),

    ('a economia!\n',
    'o livre mercado!\n',
    'a classe média!\n',
    'a propriedade privada!\n',
    'a nação!\n',
    'o progresso!\n',
    'a família!\n',
    'a democracia!\n',
    'a liberdade!\n',
    'os bons costumes!\n')
]

politico = [(
			"Povo, ",
			"Por outro lado, ",
			"Assim mesmo, ",
			"No entanto, não podemos esquecer que ",
			"Do mesmo modo, ",
			"A política cotidiana prova que ",
			"Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ",
			"As experiências acumuladas demonstram que ",
			"Acima de tudo, é fundamental ressaltar que ",
			"O incentivo ao avanço político, assim como ",
			"Não obstante, ",
			"Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ",
			"Pensando mais a longo prazo, ",
			"O que temos que ter sempre em mente é que ",
			"Ainda assim, existem dúvidas a respeito de como ",
			"Gostaria de enfatizar que ",
			"Todavia, ",
			"A nível público, ",
			"O empenho em analisar ",
			"Percebemos, cada vez mais, que ",
			"Na política atual, ",
			"É importante questionar o quanto ",
			"Neste sentido, ",
			"Evidentemente, ",
			"Por conseguinte, ",
			"É claro que ",
			"Podemos já vislumbrar o modo pelo qual ",
			"Desta maneira, ",
			"O cuidado em identificar pontos críticos ",
			"A qualificação de políticas que nos auxiliam a lidar com "
		),

		(
			"a execução dos pontos do programa ",
			"a complexidade dos pontos efetuados ",
			"a contínua expansão de nossa política ",
			"a estrutura atual do partido ",
			"o novo modelo estrutural aqui preconizado ",
			"o desenvolvimento contínuo de distintas formas de impostos ",
			"a constante melhora das cobranças ",
			"a consolidação das ações ",
			"a consulta aos diversos militantes ",
			"o início da atividade geral de formação de atitudes ",
			"o desafiador cenário globalizado ",
			"a mobilidade dos partidos políticos ",
			"o fenômeno da Internet ",
			"a hegemonia do ambiente político ",
			"a manutenção dos mercados internos ",
			"o aumento do diálogo entre os diferentes partidos ",
			"a crescente influência dos evangélicos ",
			"a necessidade de renovação processual ",
			"a competitividade nas transações públicas ",
			"o surgimento do comércio informal ",
			"a revolução dos costumes ",
			"o acompanhamento das preferências de voto ",
			"o comprometimento entre as militâncias ",
			"a determinação clara de objetivos ",
			"a adoção de políticas centralizadoras ",
			"a valorização de fatores subjetivos ",
			"a percepção das dificuldades ",
			"o entendimento das metas propostas ",
			"o consenso sobre a necessidade de indicações ",
			"o julgamento parcial das eventualidades "
		),

		(
			"nos obriga à análise ",
			"cumpre um papel essencial na formulação ",
			"exige a precisão e a definição ",
			"auxilia a preparação e a composição ",
			"garante a contribuição de um grupo importante na determinação ",
			"assume importantes posições no estabelecimento ",
			"facilita a criação ",
			"obstaculiza a apreciação da importância ",
			"oferece uma interessante oportunidade para verificação ",
			"acarreta um processo de reformulação e modernização ",
			"pode nos levar a considerar a reestruturação ",
			"representa uma abertura para a melhoria ",
			"ainda não demonstrou convincentemente que vai participar na mudança ",
			"talvez venha a ressaltar a relatividade ",
			"prepara-nos para enfrentar situações atípicas decorrentes ",
			"maximiza as possibilidades por conta ",
			"desafia a capacidade de equalização ",
			"agrega valor para a legenda ",
			"é uma das consequências ",
			"promove a alavancagem ",
			"não pode mais se dissociar ",
			"possibilita uma melhor visão global ",
			"estimula a padronização ",
			"aponta para a melhoria ",
			"faz parte de um processo de gerenciamento ",
			"causa impacto indireto na reavaliação ",
			"apresenta tendências no sentido de aprovar a manutenção ",
			"estende o alcance e a importância ",
			"deve passar por modificações independentemente ",
			"afeta positivamente a correta previsão "
		),

		(
			"das condições financeiras e administrativas exigidas. ",
			"das diretrizes de desenvolvimento para o futuro. ",
			"do sistema de participação geral. ",
			"das posturas dos órgãos dirigentes com relação às suas atribuições. ",
			"das novas proposições. ",
			"das direções preferenciais no sentido do progresso. ",
			"do sistema de formação de quadros que corresponde às necessidades. ",
			"das condições inegavelmente apropriadas. ",
			"dos índices pretendidos. ",
			"das formas de ação. ",
			"dos paradigmas públicos. ",
			"dos relacionamentos verticais entre as hierarquias. ",
			"do processo de comunicação como um todo. ",
			"dos métodos utilizados na avaliação de resultados. ",
			"de todos os recursos funcionais envolvidos. ",
			"dos níveis de motivação departamental. ",
			"da gestão inovadora da qual fazemos parte. ",
			"dos modos de operação convencionais. ",
			"de alternativas às soluções ortodoxas. ",
			"dos procedimentos normalmente adotados. ",
			"dos conhecimentos estratégicos para atingir a excelência. ",
			"do fluxo de informações. ",
			"do levantamento das variáveis envolvidas. ",
			"das diversas correntes de pensamento. ",
			"do impacto na agilidade decisória. ",
			"das regras de conduta normativas. ",
			"do orçamento setorial. ",
			"do retorno esperado a longo prazo. ",
			"do investimento em reciclagem. ",
			"do remanejamento dos quadros funcionais. "
                )]

generico = [(
			"Caros amigos, ",
			"Por outro lado, ",
			"Assim mesmo, ",
			"No entanto, não podemos esquecer que ",
			"Do mesmo modo, ",
			"A prática cotidiana prova que ",
			"Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ",
			"As experiências acumuladas demonstram que ",
			"Acima de tudo, é fundamental ressaltar que ",
			"O incentivo ao avanço tecnológico, assim como ",
			"Não obstante, ",
			"Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ",
			"Pensando mais a longo prazo, ",
			"O que temos que ter sempre em mente é que ",
			"Ainda assim, existem dúvidas a respeito de como ",
			"Gostaria de enfatizar que ",
			"Todavia, ",
			"A nível organizacional, ",
			"O empenho em analisar ",
			"Percebemos, cada vez mais, que ",
			"No mundo atual, ",
			"É importante questionar o quanto ",
			"Neste sentido, ",
			"Evidentemente, ",
			"Por conseguinte, ",
			"É claro que ",
			"Podemos já vislumbrar o modo pelo qual ",
			"Desta maneira, ",
			"O cuidado em identificar pontos críticos n",
			"A certificação de metodologias que nos auxiliam a lidar com "
		),

		(
			"a execução dos pontos do programa ",
			"a complexidade dos estudos efetuados ",
			"a contínua expansão de nossa atividade ",
			"a estrutura atual da organização ",
			"o novo modelo estrutural aqui preconizado ",
			"o desenvolvimento contínuo de distintas formas de atuação ",
			"a constante divulgação das informações ",
			"a consolidação das estruturas ",
			"a consulta aos diversos militantes ",
			"o início da atividade geral de formação de atitudes ",
			"o desafiador cenário globalizado ",
			"a mobilidade dos capitais internacionais ",
			"o fenômeno da Internet ",
			"a hegemonia do ambiente político ",
			"a expansão dos mercados mundiais ",
			"o aumento do diálogo entre os diferentes setores produtivos ",
			"a crescente influência da mídia ",
			"a necessidade de renovação processual ",
			"a competitividade nas transações comerciais ",
			"o surgimento do comércio virtual ",
			"a revolução dos costumes ",
			"o acompanhamento das preferências de consumo ",
			"o comprometimento entre as equipes ",
			"a determinação clara de objetivos ",
			"a adoção de políticas descentralizadoras ",
			"a valorização de fatores subjetivos ",
			"a percepção das dificuldades ",
			"o entendimento das metas propostas ",
			"o consenso sobre a necessidade de qualificação ",
			"o julgamento imparcial das eventualidades "
		),

		(
			"nos obriga à análise ",
			"cumpre um papel essencial na formulação ",
			"exige a precisão e a definição ",
			"auxilia a preparação e a composição ",
			"garante a contribuição de um grupo importante na determinação ",
			"assume importantes posições no estabelecimento ",
			"facilita a criação ",
			"obstaculiza a apreciação da importância ",
			"oferece uma interessante oportunidade para verificação ",
			"acarreta um processo de reformulação e modernização ",
			"pode nos levar a considerar a reestruturação ",
			"representa uma abertura para a melhoria ",
			"ainda não demonstrou convincentemente que vai participar na mudança ",
			"talvez venha a ressaltar a relatividade ",
			"prepara-nos para enfrentar situações atípicas decorrentes ",
			"maximiza as possibilidades por conta ",
			"desafia a capacidade de equalização ",
			"agrega valor ao estabelecimento ",
			"é uma das consequências ",
			"promove a alavancagem ",
			"não pode mais se dissociar ",
			"possibilita uma melhor visão global ",
			"estimula a padronização ",
			"aponta para a melhoria ",
			"faz parte de um processo de gerenciamento ",
			"causa impacto indireto na reavaliação ",
			"apresenta tendências no sentido de aprovar a manutenção ",
			"estende o alcance e a importância ",
			"deve passar por modificações independentemente ",
			"afeta positivamente a correta previsão "
		),

		(
			"das condições financeiras e administrativas exigidas. ",
			"das diretrizes de desenvolvimento para o futuro. ",
			"do sistema de participação geral. ",
			"das posturas dos órgãos dirigentes com relação às suas atribuições. ",
			"das novas proposições. ",
			"das direções preferenciais no sentido do progresso. ",
			"do sistema de formação de quadros que corresponde às necessidades. ",
			"das condições inegavelmente apropriadas. ",
			"dos índices pretendidos. ",
			"das formas de ação. ",
			"dos paradigmas corporativos. ",
			"dos relacionamentos verticais entre as hierarquias. ",
			"do processo de comunicação como um todo. ",
			"dos métodos utilizados na avaliação de resultados. ",
			"de todos os recursos funcionais envolvidos. ",
			"dos níveis de motivação departamental. ",
			"da gestão inovadora da qual fazemos parte. ",
			"dos modos de operação convencionais. ",
			"de alternativas às soluções ortodoxas. ",
			"dos procedimentos normalmente adotados. ",
			"dos conhecimentos estratégicos para atingir a excelência. ",
			"do fluxo de informações. ",
			"do levantamento das variáveis envolvidas. ",
			"das diversas correntes de pensamento. ",
			"do impacto na agilidade decisória. ",
			"das regras de conduta normativas. ",
			"do orçamento setorial. ",
			"do retorno esperado a longo prazo. ",
			"do investimento em reciclagem técnica. ",
			"do remanejamento dos quadros funcionais. "
		)]

s.listen(1)
conn, addr = s.accept()
conn.send("Que estilo de lero-lero voce quer?\n1 - Politico\n2 - Coxinha\n3 - Generico\n-> ".encode('utf-8'))
tipo = int(conn.recv(1024))
while tipo < 1 or tipo > 3:
    conn.send("Use um numero valido!\n-> ".encode('utf-8'))
    tipo = int(conn.recv(1024))
if tipo == 1:
    base = politico
elif tipo == 2:
    base = coxinha
elif tipo == 3:
    base = generico
conn.send("Quantos paragrafos o seu discurso precisa?\n->".encode('utf-8'))
tamanho = int(conn.recv(1024))
print(tamanho)
discurso = ""
for paragrafo in range(tamanho):
    paragrafo = "    "
    for frase in range(randint(4,7)):
        for i in range(len(base)):
            paragrafo += base[i][randint(0,len(base[i])-1)]
    discurso += paragrafo+'\n'

conn.send(discurso.encode('utf-8'))
s.close()

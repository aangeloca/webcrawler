# :spider_web: Trabalho de Análise de Dados – Web_Crawler :spider:
<br></br>
________________________________________________________
## :student: Integrantes do Grupo:

:boy: Ângelo Suriani Ferreira - RA: 31610283

:bearded_person: Fabrício Silva Faria - RA: 31610363

:man: Luiz Fernando Martins Leite Oliveira - RA: 316147199
<br></br>
<br></br>
________________________________________________________
## :desktop_computer:  Descrição do website de onde coletamos de dados.
## Metacritic.


Site utilizado: (https://www.metacritic.com/)


## :video_game:  :film_projector:  :tv:  :camera:  :books:  
O website Metacritic é uma ferramenta americana que tem como objetivo primordial a compilação das críticas de álbuns, videogames, filmes, programas de televisão, DVD´s e livros. Fundado em janeiro de 2001, o mecanismo utilizado para o processo consiste em atribuir a cada produto, um valor numérico de cada crítica que será computado e daí retirado uma média aritmética ponderada. Para esclarecimento, junto com um hyperlink para a fonte, a Metacritic cita um trecho de cada crítica. Além disto, foi adotado também a classificação para o  resumo da avaliação de cada produto, sendo aplicada três cores diferentes, são elas: vermelho, amarelo e verde. No quesito relacionado a cada nota, essa é convertida para uma nota percentual, com alguns veículos recebendo um peso maior dependendo da categoria. Neste website, ainda é possível que os usuários cadastrados publiquem suas críticas, mas vale ressaltar que essas notas não são acopladas na contagem oficial. Essa ferramenta americana que viralizou auxilia os consumidores a fazerem suas decisões assertivas considerado como gastar seu tempo e dinheiro na busca de seu entretenimento. Para os fundadores, as várias críticas colhidas dos usuários são essências, e valem mais que uma, eles são porta vozes imprescindíveis para suas melhorias dia a dia.
<br></br>
________________________________________________________

## :mag_right: Descrição dos dados que foram coletados.

Fizemos uma consulta no site citado, coletamos na primeira lista do site, nome de jogos, suas notas e descrições.
<br></br>
________________________________________________________
<br></br>
## :computer:  :keyboard:  :computer_mouse: Estratégia utilizada para efetuar a coleta dos dados.


Utilizamos para efetuar a seleção de dados da estrutura o Scrapy efetuar as buscas dentro de uma base de dados do Metacritic, que é um site de avaliação de filmes, jogos, cinema, entramos na categoria de jogos e colocamos o  buscador  aranha do crawler para buscar o título destes jogos e também a descrição dos mesmos, ele entra na página, aranha, e ela lê a aquela página e puxa os primeiros resultados dos títulos dos jogos e também a descrição dos mesmos.

Na parte técnica do que o código desenvolvemos, mostramos como foi configurada a aranha, primeiramente importou  scrap a biblioteca para dentro do Python e foi criada uma classe chamada critic spyder pegando informação do scrap coloquei o nome de critic que é em relação a crítica o nome do site e ai tem outro atributo chamado allowed domains que é o domínio responsável por fazer a essa busca com subdiretório games 

(https://github.com/aangeloca/webcrawler/blob/master/imagem/imagem_aranha.jpg)


Foi aberto a url no (www.metacrict.com) para o crawler não sair abrindo outros links e ficou preso ao site da busca. Tem um parâmetro def parse self response com for dentro dele pegando atributo geral da página do css, então efetua a buscar dentro do css a tag t, r e a tabela, tabel roll a linha da tabela. 

Pega a linha de cima e efetua uma varredura na mesma, ela busca qual o bloco css que vai efetuar a varredura. No comando yield que é basicamente onde ele vai exibir o nome titulo, como pode verificar na linha 13 critic ponto.css que é chamando o passe que foi criado, colocamos a tag H3 que é o titulo,  : : Text que é um atributo do tipo de texto e um get para pegar essas informações, a baixo a mesma coisa, efetuamos na descrição, chamamos o nome critic .css, pegamos a div sumário dentro da div, o nome desta div e colocamos um get para pegar todas as informações, e para finalizar, e fazer funcionar utilizamos o comando para rodar a aranha para efetuar a coleta dos dados e salvando os mesmos.

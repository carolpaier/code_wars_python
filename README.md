# Code Wars #1

## Projeto em equipe do Bootcamp Código[s] - Stone 
<img src=imagem_1.png height="100%" width="100%">

#### Equipe 02:

* Francislei Oliveira 
* Patricia Moro
* Caroline Paier
* Maly Leventhal
* Caio Alves

### Definições do Projeto

Implementar um sistema em Python que efetue o comportamento de um robô tentando encontrar
a saída de um labirinto.
As inspirações para esse projeto foram: aspiradores de pó automáticos (como o Roomba),
navegação no Google Maps e o problema clássico do Labirinto do Minotauro.
O objetivo do projeto é posicionar um robô em um labirinto e desenvolver a lógica para que ele
percorra esse labirinto em busca da saída, avançando pelas células em branco, respeitando as
paredes e retornando por um caminho caso esteja encurralado. O robô não pode avançar 2 vezes
por um mesmo caminho, assim, ao descobrir que está encurralado pode retornar pelas células
percorridas, mas não deve avançar novamente por este caminho.

### O labirinto

O labirinto pode ser representado por uma matriz de inteiros ou caracteres representando, por
exemplo:
* 0 ou “ ”: espaço em branco por onde o robô pode caminhar
* 1 ou “#”: parede, o robô não pode avançar para essa posição
* 2 ou “.”: posição já percorrida pelo robô
* 3 ou “S”: saída do labirinto
* 4 ou “X”: posição atual do robô

O labirinto pode ser montado em uma matriz de inteiros ou caracteres, onde a combinação dos
números ou dos caracteres em posições específicas definirá o seu desenho. Os caminhos desenhados 
devem permitir que o robô encontre uma saída e o robô deve respeitar os limites da
matriz.
Após apresentar o labirinto ao usuário, deve-se pedir que ele informe a posição em que o robô será
inserido, devendo essa posição representar um espaço em branco, obrigatoriamente. Uma vez
posicionado, o robô deve iniciar seu passeio no labirinto a fim de encontrar a saída.
Para que o usuário consiga acompanhar o passeio do robô, o labirinto deve ser apresentado na tela
a cada passo dado. O robô pode avançar por um caminho nunca percorrido e pode retornar por um
caminho já percorrido. Não pode, em nenhuma situação, avançar por um caminho já percorrido.
Para garantir esse comportamento, a cada passo válido dado pelo robô, faz-se a troca do número 0
pelo número 2 no labirinto, indicando que esta posição já foi visitada, como se ele deixasse uma
marca nas posições em que já passou.
Caso o robô precise retornar, não é necessário trocar o número 2 já registrado no labirinto.

### O robô
O robô nada mais é do que o número 4 ou o caracter “X” dentro do labirinto. Ele pode caminhar no
labirinto apenas na horizontal e na vertical.
Uma vez posicionado, o robô deve executar sua regra de movimentação:
* testar a sequência das quatro direções possíveis (acima, à direita, abaixo ou à esquerda)
tentando encontrar a saída (valor 3 na matriz). Se encontrá-la, avançar na direção correta e
encerrar o jogo;
* se não encontrar a saída, testar a sequência das quatro direções para avançar para uma
casa em branco (valor 0 na matriz). Na primeira direção em que for possível avançar,
empilhar a sua posição atual, marcar a posição atual como percorrida (valor 2 na matriz) e
avançar;
* caso não consiga avançar para uma posição em branco (valor 0 na matriz) após testar as 4
direções, deve retornar para sua posição imediatamente anterior. Para isso, deve
desempilhar a última posição empilhada e retornar para ela.

O robô deverá repetir a regra acima até que encontre a saída.
O robô deve saber a sua posição atual (linha e coluna na matriz) e saber a sequência de passos
que representa um caminho percorrido (pilha de posições).

### A pilha
Uma pilha é uma estrutura de dados bem definida que segue o comportamento LIFO: Last In First
Out (a última coisa empilhada é a primeira a ser desempilhada). Como em uma pilha de livros, se
você empilhar os livros A, B, C e D, nessa ordem, irá desempilhá-los na ordem D, C, B e A.

Nesse projeto, a representaEmpilhar uma posição significa registrar uma posição já visitada pelo robô, sendo que ele saiu dela
e avançou para outra. O robô só avança para posições na matriz que possuem o valor 0 (espaço em
branco). Desempilhar uma posição significa que o robô ficou encurralado e deve retornar para a
última posição em que estava. O robô só retorna para posições na matriz que possuem o valor 2
(posição já percorrida).

Caso seja empilhada uma sequência de posições, significa que o robô avançou por um caminho.
Caso seja desempilhada uma sequência de posições, significa que o robô retornou por um caminho.
Lembre-se, entretanto, que o robô avança ou retorna apenas uma casa do caminho. A cada passo
dado, executa sua regra de movimentação.

Nesse projeto, o robô não deve avançar por um mesmo caminho mais de uma vez, senão perderia
tempo testando caminhos que já sabe que não levam à saída. Esse comportamento é garantido
com o uso da pilha e com a marcação do valor 2 na matriz.ção da pilha pode ser um vetor onde elementos são inseridos e
removidos do seu final. Cada elemento deverá representar uma posição da matriz, com valor para
linha e coluna, representando as posições que o robô já visitou (mas sem a sua posição atual).


# Trabalho de Fundamentos de Programação (WOD Tracker)

## Descrição do Projeto

Este projeto é um sistema que visa permitir o usuário registre e acompanhe sua evolução nos treinos de Crossfit. Todas as informações dos treinos inseridas pelo usuário são salvas em arquivos TXT, servindo como banco de dados local. 

---

## Funcionalidades

- CRUD dos Treinos: O usuário pode adicionar, visualizar, substituir e excluir registros dos treinos de CrossFit, com informações como: data, tipo de treino (AMRAP, EMOM, For Time), tempo/duração em minutos e os movimentos que tinham.
- Filtragem por Tipo de WOD ou Movimento: O sistema permite filtrar os treinos exibidos no CRUD por tipo (ex: EMOM) ou por movimentos específicos (snatch) para avaliar o desempenho em treinos parecidos.
- Sugestões de WODs (Workout of the Day, ou seja, treino do dia) Aleatórios: O programa cria o treino para o usuário de acordo com os treinos registrados no banco de dados do CRUD.
- Metas de Desempenho: O usuário pode registrar metas como “fazer 50 pull-ups seguidos” ou “baixar o tempo no Fran para menos de 6 minutos”. O sistema acompanha essas metas e mostra progresso.
- Cálculo da Ingestão de Proteínas do Dia: O programa pergunta quantos gramas de alimentos (carne, peixe, laticínio, etc.) e a quantidade de ovos que o usuário comeu no dia e retorna o resultado do cálculo da quantidade total de proteinas ingeridas em gramas.

---

## Como Utilizar a Ferramenta do CRUD

No menu do programa, será solicitado que o usuário escolha qual funcionalidade ele deseja realizar. No caso de ser escolhido a função número 1 ("Registrar treino do dia ou manipular treinos (substituir, visualizar, remover)", que representa o CRUD, o programa pergunta qual ação ele quer fazer (adicionar, visualizar, substituir e excluir registro dos treinos de CrossFit):

- Escolhendo ADICIONAR registros de treino, o programa pergunta o dia, o mês e o ano em que o usuário está. Depois, pergunta quantos exercícios o usuário realizou para adicionar no seu registro. Por fim, ele deve informar o tipo de treino realizado no dia (se é EMOM, AMRAP, FOR TIME ou outro), quais movimentos ele executou no treino e a duração em minutos desses movimentos. Todas essas informações inseridas serão salvas no banco dados do CRUD;
- Escolhendo VISUALIZAR os registros de treino, o programa exibe no terminal todos os treinos que foram adicionados por esse usuário;
- Escolhendo SUBSTITUIR os registros de treino, o programa exibe um conjunto de índices, que são as informações de cada treino registradas pelo usuário e salvas no arquivo TXT que é usado como banco de dados, e pergunta qual índice ele quer SUBSTITUIR, permitindo que o usuário EDITE o treino registrado do índice correspondente;
- Escolhendo REMOVER registros de treino, o programa exibe um conjunto de índices, que são as informações de cada treino registradas pelo usuário e salvas no arquivo TXT que é usado como banco de dados, e pergunta qual índice ele quer REMOVER, permitindo que o usuário EXCLUA o treino registrado do índice correspondente.

# Script para Imprimir em 3D via  Wifi com Rasp sem octprit
___

## Descrição do algoritimo 

1. Primeiro é detectado a porta USB referente a impressora

2. Depois é configurado o padrão de conexão serial para a comunicação da raspberry com a impressora

3. É aberta a streaming de comandos e logo depois é limpo o buffer

4. Feito isso é requisitado o arquivo onde contem o codigo-G para a impressão

5. Abertura e leitura do arquivo

6. É iniciado o streaming de comandos propriamente dito
- Nesse laço são descartadas as linhas vazias e de comentarios
- São monitorado as respostas de ok da impressora
- E no fim de cada impressão é fechado suas conexões

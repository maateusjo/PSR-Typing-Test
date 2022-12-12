<a name="readme-top"></a>

# PSR Typing Test

Desenvolvido por **Mateus Araujo e Rafael Mendes**, no âmbito da disciplina de **Programação de Sistemas Robóticos (PSR)**, este trabalho tem como objetivo a criação de um **Teste de escrita Caracter a Caracter.**

## Informações
Observando o código, inicialmente foram definidos todos os parâmetros que seriam pedidos ao utilizado para o funcionamento do programa através do módulo agrparse.

* -utm **ou** --use_time_mode *(Obrigatório)*
* -mv **ou** --max_value *(Opcional)* 

De seguida foi criado o Named Tuple que foi utilizado para armazenar todos os caracteres pedidos, os inputs do utilizandor e o tempo de resposta.

Mais abaixo todas as variáveis que são utilizadas para armazenar os tempos de inicio e fim de teste, número de inputs, número de inputs corretos, percentagem de acerto e as listas para armazenas os tempos de inputs das teclas do utilizador.

No final do teste todas as estatísticas e médias foram calculadas e armazenadas num dicionário denominado  ***test_report*** que é apresentado sempre ao final do teste através do package **prettyprint**. 

### Funcionamento

Na execução do programa, independentemente do modo, será pedido ao utilizador para que clique em **qualquer tecla para iniciar o teste**, ou na **tecla Espaço para cancelar o teste.**

Posteriormente, o teste será iniciado e o utilizador deve tentar introduzir os caracteres pedidos o mais rapidamente possível.

No final do mesmo, seja por tempo ou número de inputs, será apresentado um *report* com as informações relevantes e também cada input que introduziu.

### Cancelamento do teste no inicio ou durante a execução do mesmo
 
 Caso seja pressionada a tecla Espaço antes do inicio do teste o utilizador receberá uma mensagem de cancelamento e o *report* não será apresentado.

 Se a telca Espaço for pressionada durante o teste, este terminará e será apresentado o *report* com as informações que foram possiveis ser adquiridas.


## Inicialização

Para o teste e boa utilização do código desenvolvido, o utilizador deve seguir os passos seguintes para obter uma cópia local do repositório e execução do mesmo.

### Pré-requesitos

Para execução do código é necessário ter alguns requesitos, que estão contidos na lista seguinte juntamente com os comandos necessários para instalação:

* **Colorama:**
Utilizado para produzir um print no terminal com texto colorido e personalizado: 
  ```sh
  pip install colorama
  ```
* **ReadChar:**
Utilizado para detetar as teclas pressionadas pelo utilizado:
   ```sh
  pip install readchar
  ```

### Obtenção do repositório

Clonar o repositório:
   ```sh
   git clone https://github.com/maateusjo/PSR-Typing-Test
   ```

### Execução do código - Considerações
Na execução do programa, será necessário realizar a inicialização obrigatória do parâmetro **--use_time_mode** fornecendo um valor correspondente aos segundos que o teste durará, **Modo Temporizador**. 

Caso seja adicionado o parâmetro **--max_value**, o teste entrará no **Modo de número de Inputs** 

Estes 2 paramêtros serão essenciais para a escolha do **Modo de Teste**

1. **Modo Temporizador:** Modo em que o utilizador define os segundos em que o teste irá decorrer (Qualquer um dos comandos abaixo funcionam):
   ```py
   ./main.py -utm <tempo em segundos>
   ```

   ```
   ./main.py --use_time_mode <tempo em segundos>
   ```

2. **Modo número de Inputs:** Modo em que o utilizador define o número de Inputs que terá de fornecer, quando este limite for atingido o teste termina (Qualquer um dos comandos abaixo funcionam):
   ```py
   ./main.py -utm <numero de inputs> -mv
   ```

   ```
   ./main.py --use_time_mode <numero de inputs> --max_value
   ```

Se nenhum dos parâmetros for fornecido, o programa pedirá ao utilizador que forneça os mesmos.

## Contactos

* Mateus Araújo - mateus.araujo@ua.pt
* Rafael Mendes - mendes.rafael@ua.pt

Link do Projeto: https://github.com/maateusjo/PSR-Typing-Test

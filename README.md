# Automação de Cadastro de Produtos 🇧🇷

Este projeto tem como objetivo automatizar o processo de cadastro de produtos em um sistema. Imagine que você tenha uma grande quantidade de informações, como produtos, preços, ou qualquer outro tipo de dado, que precisam ser inseridos em um sistema. Fazer isso manualmente para 500 informações seria extremamente trabalhoso e demorado, não é mesmo? 

Neste projeto, utilizaremos Python para automatizar o processo de cadastro de produtos em um sistema. Faremos uso das seguintes bibliotecas:

- **PyAutoGUI**: Para controlar o mouse e o teclado, permitindo a automação das interações com o sistema.
- **Pandas**: Para manipular os dados do arquivo CSV que contém as informações dos produtos a serem cadastrados.
- **Time**: Para realizar pausas durante a execução do script, garantindo sincronização com as ações automatizadas.

## Importante: Aviso sobre Resolução de Tela

Devido a variações de resolução de tela, é possível que o script não funcione corretamente em alguns dispositivos. Para contornar esse problema, após passar da área de login, utilize o script "auxiliar.py". O processo será pausado por 5 segundos para que você posicione o cursor do mouse sobre o campo "Código do Produto". As coordenadas (x, y) devem ser inseridas no arquivo "main.py", conforme indicado pelos comentários. Este script foi desenvolvido para ambiente Windows, utilizando o Google Chrome como navegador para acessar a página de cadastro de produtos.

## Como Parar a Automação

Para interromper a automação, simplesmente direcione o cursor do mouse para o extremo canto superior esquerdo da tela. Isso garantirá uma parada segura do processo automatizado.

## Entendendo a Base de Dados

Os dados que serão utilizados estão armazenados no arquivo `produtos.csv`. Este arquivo contém diversas informações sobre os produtos que serão cadastrados no sistema de forma automatizada.

### Estrutura do arquivo CSV:

- **Código do Produto**: Identificador único para cada produto.
- **Marca**: Marca do produto.
- **Tipo**: Tipo do produto.
- **Preço Unitário**: Preço unitário do produto.
- **Custo**: Custo do produto.
- **Observação**: Observações adicionais sobre o produto.

### Visualização da Base de Dados:

Apesar de termos as informações necessárias, elas estão no formato CSV, o que pode dificultar um pouco a visualização direta. Além disso, o arquivo possui 264 linhas de informação, o que significaria inserir manualmente 6 informações para cada linha da base de dados.

# Product Registration Automation 🇺🇸

This project aims to automate the product registration process in a system. Imagine you have a large amount of information, such as products, prices, or any other type of data, that needs to be entered into a system. Doing this manually for 500 pieces of information would be extremely laborious and time-consuming, wouldn't it?

In this project, we will use Python to automate the product registration process in a system. We will make use of the following libraries:

- **PyAutoGUI**: To control the mouse and keyboard, allowing automation of interactions with the system.
- **Pandas**: To manipulate the data from the CSV file containing the product information to be registered.
- **Time**: To pause during script execution, ensuring synchronization with automated actions.

## Important: Screen Resolution and Automation Interruption Notice

Due to screen resolution variations, the script may not work correctly on some devices. To work around this issue, after logging in, use the "auxiliar.py" script. The process will be paused for 5 seconds so you can position the mouse cursor over the "Código do Produto" field. The coordinates (x, y) should be inserted into the "main.py" file, as indicated by the comments. This script was developed for the Windows environment, using Google Chrome as the browser to access the product registration page.

## How to Stop Automation

To stop the automation, simply direct the mouse cursor to the extreme upper left corner of the screen. This will ensure a safe stop of the automated process.

## Understanding the Database

The data to be used is stored in the `produtos.csv` file. This file contains various information about the products that will be registered in the system automatically.

### CSV File Structure:

- **Código do Produto**: Unique identifier for each product.
- **Marca**: Product brand.
- **Tipo**: Product type.
- **Preço Unitário**: Unit price of the product.
- **Custo**: Product cost.
- **Observação**: Additional observations about the product.

### Database Visualization:

Although we have the necessary information, it is in CSV format, which can make direct visualization a bit difficult. In addition, the file has 264 lines of information, which would mean manually entering 6 pieces of information for each line of the database.

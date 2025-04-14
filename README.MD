# Task Manager

Este é um simples **Gerenciador de Tarefas** feito com Python usando a biblioteca `tkinter` para a interface gráfica. Ele permite ao usuário adicionar, listar, sugerir e excluir tarefas com base na prioridade.

## Funcionalidades

- **Adicionar Tarefas**: O usuário pode adicionar tarefas com nome e prioridade.
- **Listar Tarefas**: As tarefas são exibidas em uma lista com o nome e a prioridade.
- **Sugerir Tarefa**: O aplicativo pode sugerir a próxima tarefa com base na prioridade definida.
- **Excluir Tarefas**: O usuário pode excluir tarefas da lista.
- **Tela Redimensionável**: A janela pode ser redimensionada, mas começa com um tamanho fixo de 800x600 pixels.
- **Tecla de Atalho**: Pressionando `Esc`, o aplicativo é fechado.

## Pré-requisitos

Certifique-se de que você tenha o Python 3.x instalado em sua máquina. Além disso, a biblioteca `tkinter` é necessária para criar a interface gráfica. O `tkinter` já vem com a maioria das instalações do Python, mas, caso não tenha, você pode instalá-la com:

```bash
sudo apt-get install python3-tk
```

## Instalação

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/task-manager.git
    cd task-manager
    ```

2. Instale as dependências (caso haja algum arquivo `requirements.txt` para instalar pacotes adicionais).

3. Execute o script principal `gui.py`:

    ```bash
    python3 gui.py
    ```

Isso abrirá a interface gráfica do seu **Gerenciador de Tarefas**.

## Como Usar

- **Adicionar Tarefa**: Digite o nome da tarefa e escolha a prioridade (Alta, Média ou Baixa). Clique no botão **Add Task** para adicionar a tarefa à lista.
- **Excluir Tarefa**: Selecione uma tarefa na lista e clique em **Delete Task** para removê-la.
- **Sugerir Tarefa**: Clique no botão **Suggest Next Task** para obter uma sugestão de tarefa com base na prioridade.
- **Fechar o Programa**: Pressione a tecla **Esc** para fechar o aplicativo.

## Estrutura do Projeto

```plaintext
task-manager/
│
├── gui.py           # Interface gráfica
├── task.py          # Definição da classe Task
├── task_utils.py    # Funções para carregar e salvar tarefas
└── tasks.json       # Arquivo de dados com as tarefas (JSON)



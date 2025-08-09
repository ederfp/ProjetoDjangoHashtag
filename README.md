# Projeto Django Hashtag Netflix

Este projeto é uma aplicação web desenvolvida com Django que simula uma plataforma de catálogo de filmes inspirada na Netflix.

## Estrutura do Projeto
- **filme/**: App principal, contém modelos, views, templates e URLs relacionados aos filmes.
- **hashflix/**: Configurações do projeto Django.
- **media/**: Imagens de capa dos filmes.
- **static/**: Arquivos estáticos (imagens, CSS, JS).
- **templates/**: Templates base e de navegação.
- **manage.py**: Script de gerenciamento do Django.

## Funcionalidades
- Listagem de filmes
- Página de detalhes de cada filme
- Pesquisa de filmes
- Interface inspirada na Netflix

## Como executar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
3. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
4. Acesse em [http://localhost:8000](http://localhost:8000)

## Requisitos
- Python 3.8+
- Django 3.2+

## Estrutura de Pastas
```
manage.py
filme/
hashflix/
media/
static/
templates/
```

## Licença
Este projeto é apenas para fins educacionais.

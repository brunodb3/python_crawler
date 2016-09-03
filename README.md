# Python Crawler

Um projeto inicial para um crawler em Python + Scrapy. Desenvolvido por Bruno Duarte Brito.

Consiste em:

  * [WebCrawler](https://github.com/brunodb3/python_crawler)

> Este projeto foi desenvolvido por Bruno Duarte Brito como projeto Open-Source, seu código é livre para edições e distribuição

### Versão
0.0.1

### Tecnologia envolvida

Lista de tecnologias e linguagens de programação envolvidas:

* [Python](http://python.org/)
* [Scrapy](http://scrapy.org/)

### Instalação

Antes de baixar o repositório, tenha certeza que sua máquina possui [Scrapy](https://scrapy.org).

Clone o repositório em sua máquina:

```sh
$ git clone [url-do-repositorio]
$ cd python_crawler
```

Então, para rodar o crawler (Spider), execute na linha de comando

```sh
$ scrapy crawl stack # roda o spider chamado stack (diretório /python_crawler/spiders/stack_spider.py)
```

O spider de exemplo (stack) realiza uma busca no site StackOverflow pelas últimas perguntas com determinada tag.

Aceita dois argumentos:

```
"pages" > Quantas páginas buscar no StackOverflow (padrão: 9)
"tag" > Qual tag deverá buscar no StackOverflow (padrão: javascript)
```

**Bruno Duarte Brito - 2016**
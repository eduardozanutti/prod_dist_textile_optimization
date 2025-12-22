# Otimização da Produção e Distribuição na Cadeia de Suprimentos de Moda

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-orange)]()

## Uma Abordagem Multiobjetivo

Este repositório contém os códigos, modelos matemáticos e experimentos computacionais desenvolvidos na dissertação de mestrado:

**Otimização da Produção e Distribuição na Cadeia de Suprimentos de Moda: Uma Abordagem Multiobjetivo**  
Autor: Eduardo Soares Zanutti  
Programa: Mestrado Profissional em Matemática, Estatística e Computação Aplicadas à Indústria (MECAI)  
Instituição: Instituto de Ciências Matemáticas e de Computação – Universidade de São Paulo (ICMC-USP)  
Orientador: Prof. Dr. Victor Benedito Camargo  

---

## Contexto e Motivação

A indústria da moda opera em um ambiente altamente competitivo, caracterizado por elevada incerteza de demanda, ciclos de vida curtos dos produtos e pressão constante por redução de custos. Nesse cenário, a integração das decisões de produção e distribuição torna-se essencial para garantir eficiência operacional e aumento de margem.

---

## Objetivos

### Objetivo Geral
Propor um modelo matemático determinístico de otimização integrada da produção e distribuição, multi-fábrica, multi-produto e multi-período, considerando múltiplos objetivos.

### Objetivos Específicos
- Maximizar a margem de contribuição da operação;
- Apoiar decisões sobre quanto produzir, estocar, transferir e vender;
- Balancear estoques entre fábricas, centros de distribuição e lojas;
- Contribuir com a literatura por meio de um estudo de caso real aplicado ao setor de moda brasileiro.

---

## Abordagem Metodológica

- Programação Inteira Mista (MIP);
- Modelo determinístico e multi-período;
- Cadeia de suprimentos em três níveis: fábricas, centros de distribuição e lojas;
- Abordagem multiobjetivo para análise de trade-offs operacionais.

---

## Estrutura do Repositório

```text
PROD_DIST_TEXTILE_OPTIMIZATION/
├── data/                      # Dados em diferentes estágios de processamento
│   ├── processed/             # Dados processados (ex.: após limpeza inicial)
│   ├── raw/                   # Dados brutos (fontes originais, não modificados)
│   └── refined/               # Dados refinados (ex.: otimizados ou agregados para modelagem)
├── docs/                      # Documentação do projeto
│   └── problem_formulation.md # Formulação matemática e descrição do problema
├── notebooks/                 # Notebooks para exploração e análise
│   └── eda.ipynb              # Exploratory Data Analysis (análise exploratória de dados)
├── references/                # Referências bibliográficas
│   └── references.bib         # Arquivo BibTeX com citações (ex.: papers sobre GRASP/MIP)
├── src/                       # Código fonte principal (pacote Python)
│   ├── config/                # Configurações e parâmetros globais
│   │   ├── __init__.py
│   │   ├── config.py          # Lógica de carregamento de configs
│   │   └── config.yaml        # Arquivo de configuração YAML
│   ├── data/                  # Scripts para manipulação e preparação de dados
│   │   ├── create_parameters.py  # Cria parâmetros iniciais a partir de dados
│   │   ├── make_dataset.py    # Gera datasets processados
│   │   └── refine_dataset.py  # Refina datasets para uso em modelos
│   ├── GRASP/                 # Módulo para algoritmo GRASP (metaheurística)
│   │   └── (arquivos específicos do GRASP, ex.: grasp.py, utils_grasp.py)
│   └── MIP/                   # Módulo para Mixed Integer Programming (ex.: com Gurobi)
│       ├── __init__.py
│       ├── model.py           # Definição do modelo de otimização
│       ├── parameters.py      # Inicialização de parâmetros
│       ├── utils_mip.py       # Funções utilitárias para MIP
│       └── variables.py       # Criação de variáveis do modelo
├── tests/                     # Testes unitários e de integração (use pytest)
│   ├── __init__.py
│   ├── test_data.py           # Testes para scripts em src/data/
│   ├── test_mip.py            # Testes para módulo MIP
│   └── test_grasp.py          # Testes para módulo GRASP (adicione mais conforme necessário)
├── UI/                        # Componentes de interface de usuário (ex.: Streamlit app, para apresentação)
│   ├── __init__.py            # Torna UI/ importável como pacote
│   ├── app.py                 # Entrypoint do Streamlit (ex.: streamlit run UI/app.py)
│   ├── streamlit_output.py    # Lógica de outputs no Streamlit
│   ├── streamlit_pages.py     # Páginas multi-página
│   └── streamlit_sidebar.py   # Componentes da sidebar
├── main.py                    # Entrypoint principal não-UI (ex.: para rodar otimizações via CLI: python main.py)
├── LICENSE.txt                # Licença do projeto
├── README.md                  # Visão geral, instruções de setup e uso (inclua seções para rodar sem/com UI)
└── requirements.txt           # Dependências Python (ex.: gurobipy, streamlit, pandas)
```

---

## Tecnologias Utilizadas

- Python  
- Gurobi 
- Pandas, NumPy  
- Jupyter Notebook  

---

## Licença

Este repositório é destinado exclusivamente a fins acadêmicos e de pesquisa.

---

## Contato

Eduardo Soares Zanutti  
Mestrando – ICMC-USP  

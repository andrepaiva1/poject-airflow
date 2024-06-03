# poject-airflow

Ultilizando python e bliblioteca como numpy.

Python 3.0.9

Criação de DAG para entração dos dados climaticos com Airflow.
A Extração ocorre toda Segunda-Feira, nessa DAG ultilizei o conceito de criação de pastas com semana=data_interval_end

desenvolvido uma task que deve extrair os dados da API e armazená-los na pasta criada pela tarefa_1. Nela, utilizei o PythonOperator.

A tarefa_1 deve ser executada primeiro, já que é responsável por criar as pastas onde os dados extraídos pela tarefa_2 serão armazenados. Portanto, inclui tarefa_1 >> tarefa_2.

Sistema operacional Ultilizado para arquitetar (Ubuntu 20.4)

Criação de Banco de Dados para consumir os dados extraidos do api foi o Dbeaver conectado no servidor sqlite.

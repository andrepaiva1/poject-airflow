from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.macros import ds_add
from os.path import join
import pandas as pd

with DAG(
        "dados_climaticos",
        start_date=pendulum.datetime(2024, 3, 22, tz="UTC"),
        schedule_interval = '0 0 * * 1', # executar toda segunda feira
    ) as dag:

    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = 'mkdir -p "/home/andrepaiva/Documents/airflow/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
    )

    def extrai_dados(data_interval_end):
        city = 'Boston'
        key = '7CYEQ6U3GQRW6N8E2H4V6DKPS'

        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
        f'{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

        dados = pd.read_csv(URL)

        file_path = f'/home/andrepaiva/Documents/airflow/semana={data_interval_end}/'

        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

    tarefa_2 = PythonOperator(
        task_id = 'extrai_dados',
        python_callable = extrai_dados,
        op_kwargs = {'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    tarefa_1 >> tarefa_2
Infraestrutura inicial configurada com Docker Compose para disponibilizar os seguintes serviços:

- PostgreSQL
- Container Python
- Airflow (rodando na porta 8080)
- Airflow Worker
- Airflow Scheduler

Para utilizar, altere os dados das variáveis de ambiente disponíveis na pasta .envs e remova o .example do final do arquivo

Faça o mesmo para a pasta .envs_example. Renomeie para apenas .envs
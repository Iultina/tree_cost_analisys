import pandas as pd
from sqlalchemy import create_engine, text
import logging

logging.basicConfig(level=logging.INFO)


# Чтение данных
def read_data(file_path):
    logging.info('Чтение данных из csv файла')
    return pd.read_csv(file_path, delimiter=';')


# Преобразование данных
def transform_data(df):
    logging.info('Началось преобразование данных')
    terminal_nodes = df[df['2022'].notna()]
    non_terminal_nodes = df[df['2022'].isna()]

    for year in ['2022', '2023', '2024', '2025']:
        for index, row in non_terminal_nodes.iterrows():
            code_prefix = row['код']
            relevant_nodes = terminal_nodes[
                terminal_nodes['код'].str.startswith(code_prefix)
            ]
            non_terminal_nodes.at[index, year] = relevant_nodes[year].sum()

    logging.info('Преобразование данных закончилось успешно')
    return pd.concat([terminal_nodes, non_terminal_nodes])


# Сохранение в PostgreSQL
def save_to_postgres(df, db_url):
    engine = create_engine(db_url)
    logging.info('Началась загрузка данных в базу данных')

    # Создание базы данных и таблицы с использованием DDL
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS project_costs;"))
        connection.execute(text("""
            CREATE TABLE project_costs (
                index SERIAL PRIMARY KEY,
                код TEXT,
                "2022" FLOAT,
                "2023" FLOAT,
                "2024" FLOAT,
                "2025" FLOAT
            );
        """))

    # Заполнение таблицы данными
    df.to_sql('project_costs', engine, if_exists='append', index=False)

    logging.info('Загрузка в базу данных закончилась успешно')


if __name__ == '__main__':
    file_path = 'data.csv'
    db_url = 'postgresql://username:password@localhost:5432/tree_cost' # Необходимо предварительно создать базу данных с именем tree_cost
    df = read_data(file_path)
    transformed_df = transform_data(df)
    save_to_postgres(transformed_df, db_url)

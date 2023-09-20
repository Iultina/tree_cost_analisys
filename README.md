# Tree Cost Analysis

## Описание проекта
Проект по анализу стоимости проектов с иерархической структурой. Данные хранятся в формате CSV и представляют собой стоимости различных проектов и подпроектов в млрд рублей по годам. Цель проекта — преобразовать эти данные и сохранить их в PostgreSQL базе данных.

## Стэк технологий
- Python 3
- Pandas
- PostgreSQL
- SQLAlchemy

## Команды по запуску

1. Клонирование репозитория:
   
    `git clone https://github.com/Iultina/tree_cost_analisys.gi`
    
  
2. Установка зависимостей:
   
    `pip install -r requirements.txt`
    

3. Создание базы данных в PostgreSQL:
    - Откройте PostgreSQL и создайте новую базу данных с именем tree_cost.

4. Конфигурация:
    - В файле data_transform.py замените строку с db_url на вашу строку подключения к базе данных. Например:
   
    `db_url = 'postgresql://username:password@localhost:5432/tree_cost'`
    

5. Запуск скрипта:
   
    `python data_transform.py`
    
6.  Таблица project_costs в базе данных tree_cost готова для дальнейшей работы.

### Автор
Tina Kirilenko 📧 Telegram: @Mi_2018

🔗 LinkedIn: linkedin.com/in/iultina
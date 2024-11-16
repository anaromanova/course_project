from src.views import views
from src.services import investment_bank
from src.reports import spending_by_category


def date_option():
    """Функция, которая выдает список транзакций по выбранному файлу."""
    print('''Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Пропишите дату по которую хотите видеть данные о картах и затратах по ним и топ-5 транзакций по сумме платежа 
в формате YYYY-MM-DD HH:MM:SS''')
    file_answer = input('Пользователь: ')
    print(f'Программа: Для обработки выбран {file_answer}.')
    print(views('data/operations.xlsx', file_answer))
    # except:
    #     print(f'Программа: возможно вы написали дату не в том формате.')


def main() -> None:
    """Функция, которая отвечает за основную логику проекта
        и связывает функциональности между собой."""
    date_option()

main()

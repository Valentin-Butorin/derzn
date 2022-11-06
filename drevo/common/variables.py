"""
Содержит различные переменные для нужд приложения
"""

# Текст возможного действия для изменения статуса знания и новый статус для различных категорий пользователей.
# Представлено в ввиде словаря, у которого ключ - текущий статус, а значение - список кортежей с действием и статусом:
# Пользователи категории Публика
TRANSITIONS_PUB = {
    'WORK_PRE': [
        ('Завершить ПредЗнание', 'PRE_FIN')
    ],
    'RET_PRE_EDIT': [
        ('Завершить ПредЗнание', 'PRE_FIN')
    ],
    'PRE_FIN': [
        ('Вернуть ПредЗнание на доработку', 'RET_PRE_EDIT')
    ],
    'WORK': [
        ('Завершить Знание', 'FIN')
    ],
    'RET_TO_EDIT': [
        ('Завершить Знание', 'FIN')
    ],
    'FIN': [
        ('Вернуть Знание на доработку', 'RET_TO_EDIT')
    ]
}

# Пользователи категории Эксперт
TRANSITIONS_EXP = {
    'PRE_FIN': [
        ('Вернуть ПредЗнание на доработку', 'RET_PRE_EDIT'),
        ('Отклонить ПредЗнание', 'PRE_REJ'),
        ('Завершить экспертизу ПредЗнания', 'PRE_FIN_EXP')
    ],
    'PRE_EXP': [
        ('Вернуть ПредЗнание на доработку', 'RET_PRE_EDIT'),
        ('Отказаться от экспертизы ПредЗнания', 'PRE_FIN'),
        ('Отклонить ПредЗнание', 'PRE_REJ'),
        ('Завершить экспертизу ПредЗнания', 'PRE_FIN_EXP')
    ],
    'PRE_REJ': [
        ('Вернуть ПредЗнание на экспертизу', 'PRE_REF_EXP')
    ],
    'PRE_REF_EXP': [
        ('Вернуть ПредЗнание на доработку', 'RET_PRE_EDIT'),
        ('Отклонить ПредЗнание', 'PRE_REJ'),
        ('Завершить экспертизу ПредЗнания', 'PRE_FIN_EXP')
    ],
    'PRE_FIN_EXP': [
        ('Вернуть ПредЗнание на экспертизу', 'PRE_REF_EXP')
    ],
    'WORK': [
        ('Завершить Знание', 'FIN')
    ],
    'RET_TO_EDIT': [
        ('Завершить Знание', 'FIN')
    ],
    'FIN': [
        ('Вернуть Знание на доработку', 'RET_TO_EDIT')
    ]
}

# Пользователи категории Редактор
TRANSITIONS_RED = {
    'PRE_FIN_EXP': [
        ('Вернуть ПредЗнание на экспертизу', 'PRE_REF_EXP'),
        ('ПредЗнание готово к публикации', 'PRE_FIN_RED')
    ],
    'PRE_REDACT': [
        ('Вернуть ПредЗнание на экспертизу', 'PRE_REF_EXP'),
        ('Отказаться от редактирования ПредЗнания', 'PRE_FIN_EXP'),
        ('ПредЗнание готово к публикации', 'PRE_FIN_RED')
    ],
    'PRE_REF_RED': [
        ('ПредЗнание готово к публикации', 'PRE_FIN_RED'),
        ('Вернуть ПредЗнание на экспертизу', 'PRE_REF_EXP')
    ],
    'PRE_FIN_RED': [
        ('Вернуть ПредЗнание редактору', 'PRE_REF_RED')
    ],
    'FIN': [
        ('Вернуть Знание на доработку', 'RET_TO_EDIT'),
        ('Знание готово к публикации', 'FIN_RED')
    ],
    'REDACT': [
        ('Вернуть Знание на доработку', 'RET_TO_EDIT'),
        ('Отказаться от редактирования Знания', 'FIN'),
        ('Знание готово к публикации', 'FIN_RED')
    ],
    'REF_RED': [
        ('Вернуть Знание на доработку', 'RET_TO_EDIT'),
        ('Знание готово к публикации', 'FIN_RED')
    ],
    'FIN_RED': [
        ('Вернуть Знание редактору', 'REF_RED')
    ]
}

# Пользователи категории Руководитель
TRANSITIONS_DIRECT = {
    'PRE_FIN_RED': [
        ('Вернуть ПредЗнание редактору', 'PRE_REF_RED'),
        ('Опубликовать ПредЗнание', 'PUB_PRE'),
        ('Вернуть ПредЗнание на экспертизу-2', 'PRE_EXP_2'),
        ('Отклонить ПредЗнание', 'PRE_REJ')
    ],
    'PUB_PRE': [
        ('Вернуть ПредЗнание редактору', 'PRE_REF_RED'),
        ('Поместить ПредЗнание в КЛЗ', 'PRE_KLZ'),
        ('Вернуть ПредЗнание на экспертизу-2', 'PRE_EXP_2'),
        ('Отклонить ПредЗнание', 'PRE_REJ')
    ],
    'PRE_KLZ': [
        ('Изъять ПредЗнание из  КЛЗ', 'PUB_PRE')
    ],
    'PRE_EXP_2': [
        ('Вернуть ПредЗнание на экспертизу', 'PRE_REF_EXP'),
        ('Опубликовать ПредЗнание', 'PUB_PRE'),
        ('Отклонить ПредЗнание', 'PRE_REJ')
    ],
    'PRE_REJ': [
        ('Вернуть ПредЗнание редактору', 'PRE_REF_RED'),
        ('Вернуть ПредЗнание на экспертизу-2', 'PRE_EXP_2')
    ],
    'FIN_RED': [
        ('Вернуть Знание редактору', 'REF_RED'),
        ('Опубликовать Знание', 'PUB'),
        ('Вернуть Знание на экспертизу-2', 'EXP_2'),
        ('Отклонить Знание', 'REJ')
    ],
    'PUB': [
        ('Вернуть Знание редактору', 'REF_RED'),
        ('Поместить Знание в КЛЗ', 'KLZ'),
        ('Вернуть Знание на экспертизу-2', 'EXP_2'),
        ('Отклонить Знание', 'REJ')
    ],
    'KLZ': [
        ('Изъять Знание из  КЛЗ', 'PUB')
    ],
    'EXP_2': [
        ('Вернуть Знание на доработку', 'RET_TO_EDIT'),
        ('Опубликовать Знание', 'PUB'),
        ('Отклонить Знание', 'REJ')
    ],
    'REJ': [
        ('Вернуть Знание редактору', 'REF_RED'),
        ('Вернуть Знание на экспертизу-2', 'EXP_2')
    ]
}

# Статусы знания, при которых оно доступно автору
USERS_ZN = 'WORK_PRE,RET_PRE_EDIT,PRE_FIN,WORK,RET_TO_EDIT,FIN'

# Статусы, позволяющие изменять знание
EDIT_STATUS = 'WORK_PRE,RET_PRE_EDIT,WORK,RET_TO_EDIT,PRE_EXP,PRE_REF_EXP,PRE_REDACT,PRE_REF_RED,REDACT,REF_RED'

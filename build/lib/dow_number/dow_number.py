"""
the day of the week is coded different in the various systems and code-systems
this is just the beginning, feel free to add more code-systems
"""

CS_PYTHON_DATETIME = 'python_datetime_weekday'
CS_SQLITE = 'sqlite'
CS_POSTGRES_DOW = 'postgres_dow'
CS_POSTGRES_ISODOW = 'postgres_isodow'

ISO_8601 = {1: ['Monday', 'Mon'],
            2: ['Tuesday', 'Tue'],
            3: ['Wednesday', 'Wed'],
            4: ['Thursday', 'Thu'],
            5: ['Friday', 'Fri'],
            6: ['Saturday', 'Sat'],
            7: ['Sunday', 'Sun']}

DOW_NUMBER = {
    # https://pythontic.com/datetime/date/weekday
    CS_PYTHON_DATETIME: {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7},
    # https://www.tutorialspoint.com/sqlite/sqlite_date_time.htm
    CS_SQLITE: {0: 7, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
    # https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT
    CS_POSTGRES_DOW: {0: 7, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
    CS_POSTGRES_ISODOW: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
}


def get_weekday(coding_system, number):
    return ISO_8601[DOW_NUMBER[coding_system][number]]


if __name__ == '__main__':
    print('some examples:')
    print(F"python Number 6: {get_weekday(CS_PYTHON_DATETIME, 6)}")
    print(F"sqlite Number 6: {get_weekday(CS_SQLITE, 6)}")

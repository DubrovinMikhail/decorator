from datetime import datetime


def logs_writer(some_function):

    def new_function(*args, **kwargs):
        date_now = datetime.now().date()
        time_now = datetime.now().time()
        with open('logs/some.logs', 'w', encoding='utf-8') as log_file:
            result = some_function(*args, **kwargs)
            result_text = ''
            for item in result:
                result_text += f'            {item}\n'
            log_file.write(f'дата - {date_now} \n'
                           f'время  - {time_now}\n'
                           f'функция - {some_function.__name__} \n'
                           f'аргументы - {args}\n'
                           f'результаты:  \n{result_text}')
        return result

    return new_function


def logs_writer_params(path: str):
    def logs_writer(some_function):
        def new_function(*args, **kwargs):
            date_now = datetime.now().date()
            time_now = datetime.now().time()

            with open(f'{path}', 'w', encoding='utf-8') as log_file:
                result = some_function(*args, **kwargs)
                result_text = ''
                for item in result:
                    result_text += f'            {item}\n'
                log_file.write(f'дата - {date_now} \n'
                               f'время - {time_now}\n'
                               f'функция - {some_function.__name__} \n'
                               f'аргументы - {args}\n'
                               f'результаты:  \n{result_text}')
            return result
        return new_function
    return logs_writer

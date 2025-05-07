import pytest


receipts = [123, 145, 346, 246, 235, 166, 112, 351, 436]

def solve(receipts: list):
    result = receipts[2::3]
    return result, len(result)

# Первое задание
@pytest.mark.parametrize("receipts, expected_result, expected_length", [
    ([123, 145, 346, 246, 235, 166, 112, 351, 436], [346, 166, 436], 3),  # обычный случай
    ([1, 2], [], 0),  # список меньше 3 элементов
    ([10, 20, 30], [30], 1),  # ровно 3 элемента
    ([100, 200, 300, 400], [300], 1),  # 4 элемента
    ([], [], 0)  # пустой список
])

def test_solve_with_params(receipts, expected_result, expected_length):
    assert solve(receipts) == (expected_result, expected_length)
#Второе задание

def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
        return result
    else:
        result = 'Доступ ограничен'
        return result

@pytest.mark.parametrize('login, password, expected_result', (
        ('admin', 'password', 'Добро пожаловать'), # обычный случай
        ('admin', 'PASSWORD', 'Доступ ограничен'), # не тот регистр
        ('adminnn', 'pasword', 'Доступ ограничен') # неправильный логин и пароль
))

def test_check_auth(login, password, expected_result):
    assert check_auth(login, password) == expected_result

#третье задание

def vote(votes):
    return max(set(votes), key=votes.count)

@pytest.mark.parametrize("votes, expected_result", (
        ([1,1,1,2,3], 1), #Правильная работа
        ([2,-1,7,2,6,7], 2), #отрицательные числа
        ((1,1,1,2,3), 1), #передали кортеж
        ((2,3,4,5,6), 2) #всех одинаковое количество
))



def test_vote(votes, expected_result):
    assert vote(votes) == expected_result

#тест на пустой список

@pytest.mark.parametrize("votes", [
    [],
])

def test_vote_empty(votes):
    with pytest.raises(ValueError):
        vote(votes)

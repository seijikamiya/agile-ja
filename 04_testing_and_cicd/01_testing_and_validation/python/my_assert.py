names = ["Nick", "Lewis", "Nikos"]

def contains(name, list_of_names):
    if name not in list_of_names:
        return False
    else:
        return True

def get_name(name, list_of_names):
    if name in list_of_names:
        return name
    else:
        return -1

def add_name(name, list_of_names):
    list_of_names.append(name)
    return name

def add_two(num):
    return num + 2

def divide_by_two(num):
    return num / 2

def greeting(name, num):
    message = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    print(message)
    return message

# ----ここにコードを書いてください----*/
# ----難易度: 富士----

# `my_assert` をここに定義し、以降のテストに使用してください。
def my_assert(expr, msg="AssertionError!!"):
    if not expr:
        return msg

# `contains` 用のテスト `test_contains` を作成してください
def test_contains():
    list_of_names = ["Nick", "Lewis", "Nikos"]
    test_pattern = [
        ("Nick", True),
        ("Lewis", True),
        ("Nikos", True),
        ("Mike", False),
    ]
    for test in test_pattern:
        res=my_assert(contains(test[0], list_of_names)==test[1])
        print(res)

test_contains()

# `add_name` 用のテスト `test_add_name` を作成してください
def test_add_name():
    list_of_names = ["Nick", "Lewis", "Nikos"]
    name = "Mike"
    new_list = ["Nick", "Lewis", "Nikos", "Mike"]
    res=my_assert(add_name(name, list_of_names)==new_list, "AssertionError for add_name function!!")
    print(res)

test_add_name()

# `add_two` 用のテスト `test_add_two` を作成してください
def test_add_two():
    test_pattern = [
        (2, 4),
        (0, 2),
        (-5, -3),
    ]
    for test in test_pattern:
        res=my_assert(add_two(test[0])==test[1], "AssertionError for add_two function!!")
        print(res)

test_add_two()


# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください
def test_divide_by_two():
    test_pattern = [
        (2, 1),
        (0, 0),
        (-5, -2.5),
    ]
    for test in test_pattern:
        res=my_assert(divide_by_two(test[0])==test[1], "AssertionError for divide_by_two function!!")
        print(res)

test_divide_by_two()


# `greeting` 用のテスト `test_greeting` を作成してください
def test_greeting():
    name = "Mark"
    num = 3
    message = f"Hello, Mark. It is 3 degrees warmer today than yesterday"
    res=my_assert(greeting(name, num)==message, "AssertionError for greeting function!!")
    print(res)

test_greeting()


# ----難易度: キリマンジャロ----

# `my_assert` 用のテスト `test_my_assert_false` を作成し、式がFalseと評価されたときに指定したオプションの `msg` を適切に返すかどうかをチェックしてください。
def test_my_assert_false():
    res=my_assert(my_assert(True)==None, 'Pass assert test is failed')
    print(res)
    res=my_assert(my_assert(False)!=None, 'Fail assert test is failed')
    print(res)

test_my_assert_false()
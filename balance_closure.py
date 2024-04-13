def perents(coin: int):
    """use when user buy something"""
    coin_balans = coin  # Приймає "бюджет"

    def child(lose: int) -> int:
        nonlocal coin_balans  # виклик no local функції
        coin_balans -= lose  # зміна бюджету на lose
        return coin_balans

    return child


# Створення користувачів
will = perents(100)  # Створення/Виклик функції для вілл
sara = perents(100)  # виклик вже іншої функції для сара

sell = input("Waste\n")

sel_list = [int(i) for i in sell.split(",")]


for i in sel_list:
    if i % 2 == 0:
        print(f"will balance {will(i)}")
    else:
        print(f"sara balance {sara(i)}")

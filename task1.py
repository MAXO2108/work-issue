def summ_positive_numbers(numbers: list[int | float -> int | float
    """Возвращает сумму всех положительных чисел в списке."""
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

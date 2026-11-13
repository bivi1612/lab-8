# Модуль 1
def check_arr(arr):
    # Создание списка для строчных латинских букв
    latin_lower_arr = []
    # Проверка строчных латинских букв
    for char in arr:
        if isinstance(char, str) and 'a' <= char <= 'z':
            latin_lower_arr.append(char)

    # Проверка массива на пустоту
    if len(latin_lower_arr) == 0:
        return False
    
    # Результат проверки  
    return latin_lower_arr == sorted(latin_lower_arr)

# Модуль 2
if __name__ == "__main__":
    arr1 = ['A', 'b', 'C', 'd', 'E']
    arr2 = ['z', 'Y', 'C', 'X', 'W']
    arr3 = ['x', 'y', 'A', 'b']
    arr4 = ['H', 'e', 'L', 'l', 'o']
    arr5 = ['A', 'B', 'c', 'D', 'e', 'F']
    
    all_arrays = [arr1, arr2, arr3, arr4, arr5]
    # Список для номеров отсортированных массивов
    arr_num = []
    # Фиксирование отсортированных массивов
    for num in range(len(all_arrays)):
        is_sorted = check_arr(all_arrays[num])
        if is_sorted:
            arr_num.append(num + 1)
    # Результат проверки массивов
    if arr_num:  
        print("Номера отсортированных массивов:", *arr_num)
    else:
        print("Отсортированных массивов нет")         
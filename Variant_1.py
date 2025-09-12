def calculate_bmi():
    """
    Рассчитывает Индекс Массы Тела (BMI) и выводит категорию.
    Формула: вес (кг) / (рост (м))²
    """
    try:
        weight = float(input("Введите ваш вес в килограммах: "))
        height_cm = float(input("Введите ваш рост в сантиметрах: "))
        
        if height_cm <= 0:
            print("Ошибка! Рост должен быть положительным числом.")
            return
            
        height = height_cm / 100  # Переводим см в метры
        bmi = weight / (height ** 2)
        print(f"\nВаш Индекс Массы Тела (BMI): {bmi:.2f}")

        # Определяем категорию
        if bmi < 16:
            category = "Выраженный дефицит массы тела"
        elif 16 <= bmi < 18.5:
            category = "Недостаточная масса тела"
        elif 18.5 <= bmi < 25:
            category = "Нормальная масса тела"
        elif 25 <= bmi < 30:
            category = "Избыточная масса тела (предожирение)"
        elif 30 <= bmi < 35:
            category = "Ожирение I степени"
        elif 35 <= bmi < 40:
            category = "Ожирение II степени"
        else:
            category = "Ожирение III степени"

        print(f"Категория: {category}")

    except ValueError:
        print("Ошибка! Пожалуйста, вводите только числа.")

# Запуск функции
if __name__ == "__main__":
    calculate_bmi()
def calculate_water_intake():
    """
    Рассчитывает примерную суточную норму воды.
    Стандартная рекомендация: 30-40 мл на 1 кг веса.
    """
    try:
        weight = float(input("Введите ваш вес в килограммах: "))
        
        if weight <= 0:
            print("Ошибка! Вес должен быть положительным числом.")
            return
            
        activity_level = input("Вы ведете активный образ жизни? (да/нет): ").lower().strip()

        # Базовый расчет: 35 мл на кг
        base_water_ml = weight * 35

        # Корректировка на активность
        if activity_level in ['да', 'yes', 'д', 'y']:
            base_water_ml += 400  # Добавляем примерно 0.4 л при активности
            recommendation = "Увеличьте норму из-за высокой физической активности."
        else:
            recommendation = "Норма для умеренного образа жизни."

        water_liters = base_water_ml / 1000

        print(f"\nВаша примерная суточная норма воды: {water_liters:.2f} л.")
        print(f"Рекомендация: {recommendation}")
        print("*Помните: норма индивидуальна и зависит от многих факторов.*")

    except ValueError:
        print("Ошибка! Пожалуйста, вводите только числа.")

# Запуск функции
if __name__ == "__main__":
    calculate_water_intake()
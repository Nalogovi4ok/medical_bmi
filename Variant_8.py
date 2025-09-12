def calculate_heart_rate_zones():
    """
    Рассчитывает максимальную частоту сердечных сокращений (ЧССmax)
    и определяет целевую зону для тренировок.
    """
    try:
        age = int(input("Введите ваш возраст: "))
        resting_hr = int(input("Введите вашу частоту пульса в покое (уд/мин): "))
        
        if age <= 0 or resting_hr <= 0:
            print("Ошибка! Значения должны быть положительными.")
            return

        # Расчет ЧССmax по формуле Хансена
        max_hr = 208 - (0.7 * age)
        # Расчет резерва ЧСС по Карвонену
        hr_reserve = max_hr - resting_hr
        
        if hr_reserve <= 0:
            print("Ошибка в расчетах! Проверьте введенные данные.")
            return

        print(f"\nВаша максимальная ЧСС (прогноз): {max_hr:.0f} уд/мин")
        print(f"Резерв ЧСС: {hr_reserve:.0f} уд/мин")
        print("\n--- Ваши тренировочные зоны ---")

        # Определение и вывод зон (исправлены расчеты)
        zones = {
            "Разминка / Восстановление": (0.5, 0.6),
            "Жиросжигание / Аэробная": (0.6, 0.7),
            "Анаэробная (силовая)": (0.7, 0.8),
            "Максимальная (VO2 Max)": (0.8, 0.9),
            "Экстремальная (опасно!)": (0.9, 1.0)
        }

        for zone_name, (min_intensity, max_intensity) in zones.items():
            min_hr = resting_hr + (hr_reserve * min_intensity)
            max_hr_zone = resting_hr + (hr_reserve * max_intensity)
            print(f"{zone_name}: {min_hr:.0f} - {max_hr_zone:.0f} уд/мин")

    except ValueError:
        print("Ошибка! Пожалуйста, вводите только целые числа.")

# Запуск функции
if __name__ == "__main__":
    calculate_heart_rate_zones()
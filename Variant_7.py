def calculate_pef_percentage():
    """
    Рассчитывает процент от должного пиковой скорости выдоха (PEF%) -
    важный показатель для мониторинга астмы и ХОБЛ.
    """
    try:
        # Ввод фактического и должного значений PEF
        actual_pef = float(input("Введите вашу измеренную пиковую скорость выдоха (PEF, л/мин): "))
        predicted_pef = float(input("Введите ваше должное значение PEF (л/мин): "))
        
        if actual_pef <= 0 or predicted_pef <= 0:
            print("Ошибка! Значения должны быть положительными.")
            return
            
        if predicted_pef == 0:
            print("Ошибка! Должное значение PEF не может быть нулевым.")
            return

        # Расчет процента
        pef_percentage = (actual_pef / predicted_pef) * 100
        print(f"\nПроцент от должного PEF: {pef_percentage:.1f}%")

        # Интерпретация (Зеленая, Желтая, Красная зоны)
        if pef_percentage >= 80:
            zone = "ЗЕЛЕНАЯ ЗОНА: Хороший контроль."
        elif pef_percentage >= 50:
            zone = "ЖЕЛТАЯ ЗОНА: Обострение. Требуется усиление терапии по плану врача."
        else:
            zone = "КРАСНАЯ ЗОНА: Опасность! Немедленно обратитесь к врачу!"

        print(zone)

    except ValueError:
        print("Ошибка! Пожалуйста, вводите только числа.")

# Запуск функции
if __name__ == "__main__":
    calculate_pef_percentage()
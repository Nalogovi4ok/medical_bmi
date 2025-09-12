def calculate_pulse_pressure():
    """
    Рассчитывает пульсовое давление.
    Формула: Систолическое АД - Диастолическое АД
    """
    try:
        systolic = int(input("Введите систолическое (верхнее) АД (мм рт. ст.): "))
        diastolic = int(input("Введите диастолическое (нижнее) АД (мм рт. ст.): "))
        
        if systolic <= 0 or diastolic <= 0:
            print("Ошибка! Значения давления должны быть положительными.")
            return
            
        if systolic < diastolic:
            print("Ошибка! Систолическое давление не может быть меньше диастолического.")
            return

        pulse_pressure = systolic - diastolic
        print(f"\nВаше пульсовое давление: {pulse_pressure} мм рт. ст.")

        # Интерпретация
        if 30 <= pulse_pressure <= 50:
            interpretation = "Нормальное пульсовое давление."
        elif pulse_pressure < 30:
            interpretation = "Низкое пульсовое давление. Рекомендуется консультация врача."
        else:
            interpretation = "Высокое пульсовое давление. Рекомендуется консультация врача."

        print(interpretation)

    except ValueError:
        print("Ошибка! Пожалуйста, вводите только целые числа.")

# Запуск функции
if __name__ == "__main__":
    calculate_pulse_pressure()
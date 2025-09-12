def calculate_robinson_index():
    """
    Рассчитывает Индекс Робинсона (показатель адаптационного потенциала сердца).
    Формула: (ЧСС (уд/мин) * систолическое АД (мм рт. ст.)) / 100
    """
    try:
        heart_rate = int(input("Введите вашу частоту сердечных сокращений (ЧСС, уд/мин): "))
        systolic_bp = int(input("Введите ваше систолическое артериальное давление (мм рт. ст.): "))
        
        if heart_rate <= 0 or systolic_bp <= 0:
            print("Ошибка! Значения должны быть положительными.")
            return

        robinson_index = (heart_rate * systolic_bp) / 100
        print(f"\nВаш Индекс Робинсона: {robinson_index:.2f}")

        # Интерпретация (условная, для взрослого человека)
        if robinson_index < 70:
            interpretation = "Низкий уровень регуляции"
        elif robinson_index < 80:
            interpretation = "Достаточный уровень регуляции"
        elif robinson_index < 89:
            interpretation = "Напряжение механизмов регуляции"
        elif robinson_index < 95:
            interpretation = "Срыв механизмов регуляции"
        else:
            interpretation = "Перенапряжение механизмов регуляции"

        print(f"Оценка: {interpretation}")

    except ValueError:
        print("Ошибка! Пожалуйста, вводите только целые числа.")

# Запуск функции
if __name__ == "__main__":
    calculate_robinson_index()
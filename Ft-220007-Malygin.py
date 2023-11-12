
def get_criteria_weights(num_criteria):
    # Функция для получения матрицы весов критериев от пользователя
    # Принимает количество критериев в качестве аргумента
    criteria_weights = []
    for i in range(num_criteria):
        row = []
        for j in range(num_criteria):
            if i == j:
                row.append(1.0)
            elif i < j:
                while True:
                    try:
                        weight = float(input(f"Введите вес для критерия {i + 1} по отношению к критерию {j + 1}: "))
                        break
                    except ValueError:
                        print("Ошибка ввода! Введите число.")
                row.append(weight)
            else:
                row.append(1.0 / criteria_weights[j][i])
        criteria_weights.append(row)
    return criteria_weights
            

def calculate_weights(criteria_weights):
    # Функция для вычисления весовых коэффициентов на основе матрицы весов
    # Принимает матрицу весов в качестве аргумента
    num_criteria = len(criteria_weights)
    weights = []
    for i in range(num_criteria):
        product = 1
        for j in range(num_criteria):
            product *= criteria_weights[i][j] / sum(criteria_weights[j])
        weights.append(product)
    total_weight = sum(weights)
    weights = [weight / total_weight for weight in weights]
    return weights


def main():
    # Основной блок кода программы
    while True:
        try:
            num_criteria = int(input("Введите количество критериев: "))
            break
        except ValueError:
            print("Ошибка ввода! Введите целое число.")
    criteria_weights = get_criteria_weights(num_criteria)
    weights = calculate_weights(criteria_weights)
    print("Весовые коэффициенты:")
    for i, weight in enumerate(weights):
        print(f"Критерий {i + 1}: {weight:.2f}")


if __name__ == "__main__":
    main()




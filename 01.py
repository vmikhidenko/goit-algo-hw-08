import heapq

def min_connection_cost(cables):
    # Ініціалізуємо купу з довжинами кабелів
    heapq.heapify(cables)
    
    # Змінна для підрахунку загальних витрат
    total_cost = 0
    
    # Поки у купі більше одного кабелю
    while len(cables) > 1:
        # Виймаємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислюємо вартість з'єднання
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання:", min_connection_cost(cables))

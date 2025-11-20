Вариант 20. Генетический алгоритм для задачи коммивояжера 
Задача: реализовать генетический алгоритм для решения задачи коммивояжера.
Пункт 1
Алгоритм Коды
import random

class GeneticTSP:
    def __init__(self, distances, pop_size=100, generations=500, mutation_rate=0.02):
        self.distances = distances
        self.n = len(distances)
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
    
    def create_route(self):
        route = list(range(self.n))
        random.shuffle(route)
        return route
    
    def route_distance(self, route):
        return sum(self.distances[route[i]][route[(i+1)%self.n]] for i in range(self.n))
    
    def crossover(self, parent1, parent2):
        start, end = sorted(random.sample(range(self.n), 2))
        child = [-1] * self.n
        child[start:end] = parent1[start:end]
        
        pos = end
        for city in parent2:
            if city not in child:
                child[pos % self.n] = city
                pos += 1
        return child
    
    def mutate(self, route):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.n), 2)
            route[i], route[j] = route[j], route[i]
        return route
    
    def solve(self):
        population = [self.create_route() for _ in range(self.pop_size)]
        best_route = None
        best_distance = float('inf')
        
        for generation in range(self.generations):
            # Оценка популяции
            fitness = []
            for route in population:
                dist = self.route_distance(route)
                if dist < best_distance:
                    best_distance = dist
                    best_route = route.copy()
                fitness.append(1 / dist)
            
            # Создание нового поколения
            new_population = []
            for _ in range(self.pop_size):
                parent1, parent2 = random.choices(population, weights=fitness, k=2)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            
            population = new_population
            
            if generation % 100 == 0:
                print(f"Поколение {generation}: Лучшая длина = {best_distance:.2f}")
        
        return best_route, best_distance

# Пример использования
if __name__ == "__main__":
    # Матрица расстояний между городами
    dist_matrix = [
        [0, 29, 20, 21, 16],
        [29, 0, 15, 17, 28],
        [20, 15, 0, 28, 18],
        [21, 17, 28, 0, 23],
        [16, 28, 18, 23, 0]
    ]
    
    solver = GeneticTSP(dist_matrix, pop_size=50, generations=300)
    best_route, distance = solver.solve()
    
    print(f"\nЛучший маршрут: {best_route}")
    print(f"Длина маршрута: {distance:.2f}")
# Генетический алгоритм для задачи коммивояжера

## 1. Алгоритм (код)

```python
import random

class GeneticTSP:
    def __init__(self, distances, pop_size=100, generations=500, mutation_rate=0.02):
        self.distances = distances
        self.n = len(distances)
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
    
    def create_route(self):
        route = list(range(self.n))
        random.shuffle(route)
        return route
    
    def route_distance(self, route):
        return sum(self.distances[route[i]][route[(i+1)%self.n]] for i in range(self.n))
    
    def crossover(self, parent1, parent2):
        start, end = sorted(random.sample(range(self.n), 2))
        child = [-1] * self.n
        child[start:end] = parent1[start:end]
        
        pos = end
        for city in parent2:
            if city not in child:
                child[pos % self.n] = city
                pos += 1
        return child
    
    def mutate(self, route):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.n), 2)
            route[i], route[j] = route[j], route[i]
        return route
    
    def solve(self):
        population = [self.create_route() for _ in range(self.pop_size)]
        best_route = None
        best_distance = float('inf')
        
        for generation in range(self.generations):
            # Оценка популяции
            fitness = []
            for route in population:
                dist = self.route_distance(route)
                if dist < best_distance:
                    best_distance = dist
                    best_route = route.copy()
                fitness.append(1 / dist)
            
            # Создание нового поколения
            new_population = []
            for _ in range(self.pop_size):
                parent1, parent2 = random.choices(population, weights=fitness, k=2)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            
            population = new_population
            
            if generation % 100 == 0:
                print(f"Поколение {generation}: Лучшая длина = {best_distance:.2f}")
        
        return best_route, best_distance

# Пример использования
if __name__ == "__main__":
    # Матрица расстояний между городами
    dist_matrix = [
        [0, 29, 20, 21, 16],
        [29, 0, 15, 17, 28],
        [20, 15, 0, 28, 18],
        [21, 17, 28, 0, 23],
        [16, 28, 18, 23, 0]
    ]
    
    solver = GeneticTSP(dist_matrix, pop_size=50, generations=300)
    best_route, distance = solver.solve()
    
    print(f"\nЛучший маршрут: {best_route}")
    print(f"Длина маршрута: {distance:.2f}")
```

Пункт 2 
Объяснение алгоритма
Генетический алгоритм для задачи коммивояжера** работает по принципу естественной эволюции:
1. Инициализация популяции**: Создаём случайные маршруты между городами
2. Оценка приспособленности**: Вычисляем длину каждого маршрута (чем короче - тем лучше)
3. Селекция: Выбираем родителей для размножения с вероятностью, пропорциональной их приспособленности
4. Кроссовер: Создаём потомков, комбинируя маршруты родителей
5. Мутация: Вносим случайные изменения в маршруты для поддержания разнообразия
6. Замена поколения: Формируем новую популяцию из потомков
Особенности реализации:
- Order Crossover (OX) сохраняет порядок следования городов
- Точечная мутация обменивает два случайных города
- Пропорциональная селекция по приспособленности
Пункт3
Временная сложность алгоритма
O(G × P × N²)
где:
- G - количество поколений
- P - размер популяции
- N - количество городов
Пункт4
Объяснение временной сложности
Детальный анализ операций:
- Создание одного маршрута: O(N)
- Вычисление длины маршрута: O(N)
- Кроссовер: O(N) с проверками принадлежности
- Мутация: O(1)
На каждое поколение:
- Оценка P маршрутов: O(P × N)
- Создание P потомков: O(P × N)
- Итого на поколение: O(P × N)
Общая сложность: O(G × P × N)
Однако из-за операций проверки в кроссовере практическая сложность ближе к O(G × P × N²).
Пункт 5
Ответ на контрольный вопрос
5 примеров реальных приложений эвристических алгоритмов:
1. Логистика и доставка - оптимизация маршрутов транспортных компаний (UPS, FedEx)
2. Производственное планирование - составление оптимальных последовательностей операций
3. Телекоммуникации - проектирование сетевых топологий и маршрутизация
4. Биоинформатика - сборка геномов и анализ белковых структур
5. Финансы - оптимизация инвестиционных портфелей и управление рисками

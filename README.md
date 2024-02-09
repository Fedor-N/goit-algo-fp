# Висновки. Завдання #7

Програмно реалізовано алгоритм для моделювання кидання двох ігрових кубиків та їх імовірностей за допомогою методу Монте-Карло.

Код виконується та імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, підраховує, скільки разів кожна можлива сума з’являється у процесі симуляції, і визначає ймовірність кожної можливої суми.

## Порівняння результатів

| Сума | Аналітична імовірність | Монте-Карло імовірність |
|------|-------------------------|-------------------------|
| 2    | 2.78% (1/36)            | 2.81% (0.03)            |
| 3    | 5.56% (2/36)            | 5.54% (0.06)            |
| 4    | 8.33% (3/36)            | 8.34% (0.08)            |
| 5    | 11.11% (4/36)           | 11.12% (0.11)           |
| 6    | 13.89% (5/36)           | 13.85% (0.14)           |
| 7    | 16.67% (6/36)           | 16.68% (0.17)           |
| 8    | 13.89% (5/36)           | 13.88% (0.14)           |
| 9    | 11.11% (4/36)           | 11.10% (0.11)           |
| 10   | 8.33% (3/36)            | 8.35% (0.08)            |
| 11   | 5.56% (2/36)            | 5.53% (0.06)            |
| 12   | 2.78% (1/36)            | 2.79% (0.03)            |

Відхилення в імовірностях менше ніж на 0.03% в більшості випадків, що свідчить про правильність реалізації програми та точність методу Монте-Карло в цьому випадку.

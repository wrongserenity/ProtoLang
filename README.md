# Proto Lang

## Идея
Основная цель - быстрое прототипирование  
Можно вызывать как построчно так и файл целиком  
Смесь python, скриптового языка и c#

## Особенности
1. Можно вызвать команду, которая соберет все запрошенные построчно команды в файл с необходимым именем
2. Возможность удобно задавать сразу несколько переменных
3. Встроенный оператор, позволяющий узнать все текущие поля и функции в памяти
4. Постарался сделать, чтобы код не падал при большинстве ошибок в написании (program must go on)

## Функционал
### Декларирование
   1. Переменных
   2. Функций (return опционален)
### Утверждение (работают с выражениями)
  1. if конструкция (+else if, +else)
  2. while конструкция
  3. вывод
  4. назначение
  5. сохранение в файл
  6. чтение файла
  7. получение информации из памяти
### Выражения
  1. отрицательный унарный оператор
  2. унарный оператор "not"
  3. мультипликация
     1. умножение
     2. деление
     3. модуль
  4. дополнение
     1. сложение
     2. вычитание
  5. отношение
     1. меньше или равно
     2. больше или равно
     3. меньше
     4. больше
  6. сравнение
     1. равенство
     2. неравенство
  7. оператор and
  8. оператор or
  9. термы
### Термы
  1. Выражения в скобках (для установления порядка вычисления)
  2. Целые числа
  3. Числа с плавающей точкой
  4. True / False
  5. Обращение к переменной
  6. Получение значения возрата функции
  7. Строка

## Пример
1. Запустить main.py
2. Обработать файл test_foo.proto:  
```readfile "test_foo";```

Внутри файла test_foo.proto можно найти использование основных операций:
![Image alt](https://github.com/wrongserenity/ProgrammEngineeringLaboratoryWork/blob/main/images/test_foo.jpg)  
Вот что выводит:  
![Image alt](https://github.com/wrongserenity/ProgrammEngineeringLaboratoryWork/blob/main/images/test_foo_read_result.jpg)  

Файл test_foo.proto был сгенерирован с помощью команды *(перед этим ввел команды отдельно по строкам)*:
```
savelines "test_foo";
```

## Служебное
Для запуска требуется java последней версии и указание пути antlr в PATH
Команда для корректной генерации классов:
```antlr4 -Dlanguage=Python3 proto.g4 -visitor -o dist```

## Ресурсы:
1. https://www.antlr.org/download.html
2. https://github.com/antlr/antlr4/blob/master/doc/grammars.md
3. https://faun.pub/introduction-to-antlr-python-af8a3c603d23
4. https://raw.githubusercontent.com/antlr/antlr4/master/doc/getting-started.md
5. https://stackoverflow.com/questions/15610183/if-else-statements-in-antlr-using-listeners
6. https://habr.com/ru/companies/sberdevices/articles/597553/
7. https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form

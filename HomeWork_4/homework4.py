import pandas as pd
import numpy as np

pd.set_option('display.width', 180)
pd.set_option('display.max_columns', None)

print('часть 2 первичный анализ')
data = pd.read_csv('train.csv')
required = ['Age', 'Sex', 'Pclass', 'Fare', 'Embarked', 'Cabin', 'Survived']
for column in required:
    if column not in data.columns:
        raise ValueError('нет столбца ' + column)

n = int(input('сколько первых строк вывести '))
print('перыве строки')
print(data.head(n))
print('последнии 5 строк')
print(data.tail(5))
old_rows, old_columns = data.shape
print('количесвто строк', old_rows)
print('количество столбцов', old_columns)
print('названя столбцов', data.columns.tolist())
print('типы данных')
print(data.dtypes)

numbers = ['Age', 'Fare', 'SibSp', 'Parch']
categories = ['Survived', 'Pclass', 'Sex', 'Embarked', 'Cabin']
identifiers = ['PassengerId', 'Name', 'Ticket']
print('числовые признаки', numbers)
print('категориалные признаки', categories)
print('идентификаторы', identifiers)
print(data[numbers].agg(['mean', 'median', 'min', 'max', 'std']).round(2))
print('пасажиры по классам')
print(data['Pclass'].value_counts().sort_index())
print('сколько портов', data['Embarked'].nunique())
print('Pclass это катигория билета а не число для измерений')

print('\nчасть 3 пропуски')
missing = data.isna().sum()
print('количество пропусков')
print(missing)
print('процент пропускв')
print((missing / old_rows * 100).round(2))
print('больше всего пропусков в столбце', missing.idxmax())

measures = ['mean', 'median', 'min', 'max', 'std', 'count']
before = data['Age'].agg(measures)
print('возраст до заполнения')
print(before)
median_age = data['Age'].median()
data['Age'] = data['Age'].fillna(median_age)
after = data['Age'].agg(measures)
print('возраст после заполненя')
print(after)

age_table = pd.DataFrame({'До обработки': before, 'После обработки': after})
age_table.index = ['Среднее', 'Медиана', 'Минимум', 'Максимум', 'Стандартное отклонение', 'Известные значения']
print(age_table.round(3))

data = data.dropna(subset=['Embarked'])
cabin_missing = data['Cabin'].isna().mean() * 100
print('процент пропусков Cabin', round(cabin_missing, 2))
if cabin_missing > 50:
    data = data.drop(columns=['Cabin'])
    print('столбец Cabin удален')

print('оставшиеся пропуски')
print(data.isna().sum())
print('размер до обработки', old_rows, old_columns)
print('размер после обработк', data.shape)
print('медиана меньше зависит от слишком больших и маленьких значений')
print('изменились среднее стандартое отклонение и число извесных возрастов')
print('медиана минимум и максимум остались прежними')
print('отклонение стало меньше так как добавили значеня около центра')
print('расприделение поменялось так как медиана встречается чаще')

print('\nчасть 4 анализ через NumPy')
ages = data['Age'].to_numpy()
sex = data['Sex'].to_numpy()
survived = data['Survived'].to_numpy()
fares = data['Fare'].to_numpy()
men = sex == 'male'
women = sex == 'female'
alive = survived == 1
dead = survived == 0

all_survival = np.mean(survived) * 100
men_survival = np.mean(survived[men]) * 100
women_survival = np.mean(survived[women]) * 100
print('общий процент выжевших', round(all_survival, 2))
comparison = pd.DataFrame({
    'Мужчины': [men_survival, np.nanmean(ages[men]), np.nanmean(ages[men & alive]), np.nanmean(ages[men & dead])],
    'Женщины': [women_survival, np.nanmean(ages[women]), np.nanmean(ages[women & alive]), np.nanmean(ages[women & dead])]
}, index=['Выжили (%)', 'Средний возраст', 'Возраст выживших', 'Возраст погибших'])
print(comparison.round(2))
print('минимальная стоимость билета', np.nanmin(fares))
print('максималная стоимость билета', np.nanmax(fares))
print('средняя стоимость билета', round(np.nanmean(fares), 2))
print('стандартное отклонение возраста', round(np.nanstd(ages, ddof=1), 2))
print('женщины выживали чаще а мужчины в среднем старше')
print('среди мужчин выжившие моложе погибших а у женщин наоброт')

print('\nчасть 5 фильтрация')
first = data[(data['Sex'] == 'male') & (data['Age'] > 30) & (data['Pclass'] == 1)]
print('1 мужчины старше 30 лет в первом классе', len(first))
print(first.head(10))

second = data[((data['Age'] < 18) | (data['Sex'] == 'female')) & (data['Survived'] == 1)]
print('2 выжившие женщины или пасажиры младше 18 лет', len(second))

third_class = data[data['Pclass'] == 3]
third = third_class[third_class['Fare'] > third_class['Fare'].mean()]
print('3 пассажиры 3 класса с билетом дороже среднего', len(third))
print(third.to_string(index=False))

fourth = data[(data['Age'] >= 20) & (data['Age'] <= 40) & (data['Embarked'] == 'S')]
print('4 пассажиры от 20 до 40 лет из порта S', len(fourth))
print(fourth.to_string(index=False))
print('И (&) когда оба условия верны ИЛИ (|) когда хотя бы одно')

print('\nчасть 6 групировка')
statistics = data.groupby(['Pclass', 'Sex']).agg(
    passengers=('PassengerId', 'size'),
    mean_age=('Age', 'mean'),
    survived_percent=('Survived', 'mean'),
    mean_fare=('Fare', 'mean')
)
statistics['survived_percent'] = statistics['survived_percent'] * 100
statistics = statistics.round(2)
print(statistics)

ports = data.groupby('Embarked').agg(
    passengers=('PassengerId', 'size'),
    survived_percent=('Survived', 'mean')
)
ports['survived_percent'] = ports['survived_percent'] * 100
print('статистика по портам')
print(ports.round(2))

classes = data.groupby('Pclass')['Survived'].mean() * 100
print('процент выживших по классам')
print(classes.round(2))
print('класс с наиболшей долей выживших', classes.idxmax())
print('фильтрация отбирает строки а группировка обьединяет их для подсчета статистки')

print('\nчасть 7 сохранение')
data.to_csv('titanic_processed.csv', index=False)
statistics.to_csv('titanic_statistics.csv')
loaded = pd.read_csv('titanic_processed.csv')
pd.testing.assert_frame_equal(data.reset_index(drop=True), loaded, check_dtype=False)
print('файлы сохранены и повторно загруженны')

print('\nчасть 8 выводы')
print('больше всего пропусков в Cabin и Age')
print('после обработки убрали Cabin и строки без Embarked')
print('средний возраст до и после заполнения', round(before['mean'], 2), round(after['mean'], 2))
print('стандартное отклонение до и после', round(before['std'], 2), round(after['std'], 2))
print('выживаемсть мужчин и женщин', round(men_survival, 2), round(women_survival, 2))
print('наибольшая доля выживших в классе', classes.idxmax())
print('Pandas удобен для пропусков фильтрации и группировки а NumPy для вычеслений')

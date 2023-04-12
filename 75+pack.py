import sqlite3

connection = sqlite3.connect('gameidea.db')


cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cards (
    name TEXT,
    team TEXT,
    rating INTEGER
)
""")

cursor.execute("""
INSERT INTO cards VALUES
('Konstatin Tyukavin', 'Dinamo Moscow', 74),
('Dmitri Skopintsev', 'Dinamo Moscow', 72),
('Daniil Fomin', 'Dinamo Moscow', 76),
('Arsen Zakharyan', 'Dinamo Moscow', 78),
('Vyacheslav Grulev', 'Dinamo Moscow', 73),
('Fedor Smolov', 'Dinamo Moscow', 76),
('Yaroslav Gladyshev', 'Dinamo Moscow', 68),
('Saba Sazonov', 'Dinamo Moscow', 72),
('Denis Makarov', 'Dinamo Moscow', 74),
('Aleksandr Kutitskiy', 'Dinamo Moscow', 69),
('Anton Shunin', 'Dinamo Moscow', 74),
('Douglas Santos', 'Zenit St. Petersburg', 79),
('Malcom', 'Zenit St. Petersburg', 82),
('Andrey Mostovoy', 'Zenit St. Petersburg', 75),
('Ivan Sergeev', 'Zenit St. Petersburg', 75),
('Wendel', 'Zenit St. Petersburg', 80),
('Zelimkhan Bakaev', 'Zenit St. Petersburg', 73),
('Wilmar Barrios', 'Zenit St. Petersburg', 79),
('Daler Kuzyaev', 'Zenit St. Petersburg', 77),
('Mateo Cassierra', 'Zenit St. Petersburg', 73),
('Rodrigão', 'Zenit St. Petersburg', 75),
('Claudinho', 'Zenit St. Petersburg', 80)
""")

cursor.execute("""
SELECT DISTINCT * FROM cards WHERE rating >= 75 ORDER BY RANDOM()LIMIT 9;
""")

rows = cursor.fetchall()
rows_sorted = sorted(rows, key=lambda row: row[2], reverse=True)
print(rows_sorted)

connection.commit()

connection.close()


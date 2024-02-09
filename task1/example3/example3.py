def get_mentors_names_by_course(mentors):
    mentors_names = []
    for m in mentors:
        course_names = [name.split()[0] for name in m]
        mentors_names.append(course_names)
    return mentors_names

def find_common_mentors(mentors_names, courses):
    pairs = []
    results = []
    for id1 in range(len(mentors_names)):
        for id2 in range(id1 + 1, len(mentors_names)):
            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:
                pair = frozenset([courses[id1], courses[id2]])
                if pair not in pairs:
                    pairs.append(pair)
                    all_names_sorted = sorted(intersection_set)
                    results.append((courses[id1], courses[id2], all_names_sorted))
    return results

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

mentors_names = get_mentors_names_by_course(mentors)
common_mentors_results = find_common_mentors(mentors_names, courses)

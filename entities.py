import numpy as np
import dictionary as dct


def generate_entities(count):
        full_name, email = name_and_email(count)  # I believe thats faster way
        return np.dstack([full_name, ip(count), email, state(count),
                          postcode(count), city(count),
                          address(count), phone(count),
                          company(count), department(count), job(count),
                          creditcard(count), eye_color(count), car(count),
                          university(count), currencies(count)])


def ip(count):
        ip_octet = np.random.random_integers(1, 255, count)
        ip_octet = map(str, ip_octet)

        ip = np.core.defchararray.add(ip_octet, '.')
        for i in range(2):
            np.random.shuffle(ip_octet)
            ip = np.core.defchararray.add(ip, ip_octet)
            ip = np.core.defchararray.add(ip, '.')

        np.random.shuffle(ip_octet)
        return np.core.defchararray.add(ip, ip_octet)


def phone(count):
        return np.random.random_integers(1000000000, 9999999999, count)


def postcode(count):
        return np.random.random_integers(10000, 99999, count)


def city(count):
        city_prefix = np.random.choice(dct.city_prefixes, count)
        city_suffix = np.random.choice(dct.city_suffixes, count)
        return np.core.defchararray.add(city_prefix, city_suffix)


def address(count):
        building = np.random.random_integers(1, 10000, count)
        street = np.random.choice(dct.street_suffixes, count)
        return np.core.defchararray.add(street, map(str, building))


def state(count):
        return np.random.choice(dct.states, count)


def company(count):
        company_1 = np.random.choice(dct.catch_phrase_words, count)
        company_2 = np.random.choice(dct.bsWords, count)
        company_3 = np.random.choice(dct.company_suffixes, count)
        company = np.core.defchararray.add(company_1, company_2)
        return np.core.defchararray.add(company, company_3)


def creditcard(count):
        creditcard_prefix = np.random.choice(dct.prefix_maestro, count)
        creditcard_number = np.random.random_integers(100000000000, 999999999990, count)
        return np.core.defchararray.add(creditcard_prefix, map(str, creditcard_number))


def job(count):
        return np.random.choice(dct.jobs, count)


def name_and_email(count):
        name = np.random.choice(dct.first_names, count)
        last_name = np.random.choice(dct.last_names, count)
        full_name = np.core.defchararray.add(name, last_name)
        name_with_spaces = np.core.defchararray.add(name, ' ')

        email_domain = np.random.choice(dct.free_email_domains, count)
        email = np.core.defchararray.add(full_name, '@')

        return np.core.defchararray.add(name_with_spaces, last_name), np.core.defchararray.add(email, email_domain)


def eye_color(count):
        return np.random.choice(dct.all_colors, count)


def currencies(count):
        return np.random.choice(dct.currencies, count)


def car(count):
        car_make = np.random.choice(dct.cars, count)
        car_model = np.random.choice(dct.car_model, count)
        return np.core.defchararray.add(car_make, car_model)


def university(count):
        return np.random.choice(dct.university, count)


def department(count):
        return np.random.choice(dct.department, count)

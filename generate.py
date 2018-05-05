import dictionary as dct
import numpy as np
import entities

import multiprocessing
import sys


def worker():
    current = multiprocessing.current_process()
    np.random.seed(int(current.pid))
    count = 32768
    argv = int(sys.argv[1])
    if argv > 67:
        cycles = argv/67
    else:
        cycles = 1
        count = int(float(320)/8/1024/1024*argv)
    for i in range(cycles):
        postcode = np.random.random_integers(10000, 99999, count)
        phonenumber = np.random.random_integers(1000000000, 9999999999, count)

        ip_first_octet = np.random.random_integers(1, 255, count)
        ip_octet = np.random.random_integers(0, 255, count)
        ip_first_octet = map(str, ip_first_octet)
        ip_octet = map(str, ip_octet)
        ip = np.core.defchararray.add(ip_first_octet, '.')
        ip = np.core.defchararray.add(ip, ip_octet)
        ip_dot = np.core.defchararray.add(ip, '.')
        np.random.shuffle(ip_dot)
        ip = np.core.defchararray.add(ip, ip_dot)
        np.random.shuffle(ip_dot)
        ip = np.core.defchararray.add(ip, ip_dot)
        np.random.shuffle(ip_octet)
        ip = np.core.defchararray.add(ip, ip_octet)

        city_prefix = np.random.choice(dct.city_prefixes, count)
        city_suffix = np.random.choice(dct.city_suffixes, count)
        city = np.core.defchararray.add(city_prefix, city_suffix)

        building = np.random.random_integers(1, 10000, count)
        street = np.random.choice(dct.street_suffixes, count)
        address = np.core.defchararray.add(street, map(str, building))

        state = np.random.choice(dct.states, count)

        company_1 = np.random.choice(dct.catch_phrase_words, count)
        company_2 = np.random.choice(dct.bsWords, count)
        company_3 = np.random.choice(dct.company_suffixes, count)
        company = np.core.defchararray.add(company_1, company_2)
        company = np.core.defchararray.add(company, company_3)

        creditcard_prefix = np.random.choice(dct.prefix_maestro, count)
        creditcard_number = np.random.random_integers(100000000000,
                                                      999999999990, count)
        creditcard = np.core.defchararray.add(creditcard_prefix,
                                              map(str, creditcard_number))

        job = np.random.choice(dct.jobs, count)

        name = np.random.choice(dct.first_names, count)
        last_name = np.random.choice(dct.last_names, count)
        full_name = np.core.defchararray.add(name, last_name)

        full_name_space = np.random.choice(dct.first_names_spaced, count)
        full_name_space = np.core.defchararray.add(full_name_space, last_name)

        email_domain = np.random.choice(dct.free_email_domains, count)
        email = np.core.defchararray.add(full_name, '@')
        email = np.core.defchararray.add(email, email_domain)

        eye_color = np.random.choice(dct.all_colors, count)
        currencies = np.random.choice(dct.currencies, count)

        car_make = np.random.choice(dct.cars, count)
        car_model = np.random.choice(dct.car_model, count)
        car = np.core.defchararray.add(car_make, car_model)

        university = np.random.choice(dct.university, count)

        department = np.random.choice(dct.department, count)

        a = np.dstack([full_name_space, ip, email, state, postcode, city,
                       address, phonenumber, company, department, job,
                       creditcard, eye_color, car, university, currencies])

        b = ''
        i = 0

        for x in a[0]:
            b += '"' + '","'.join(x) + '"\n'
            i += 1
            if i > 8192:
                print b
                i = 0
                b = ''

        print b
    return


if __name__ == '__main__':
    jobs = []
    for i in range(8):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()

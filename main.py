from application.salary import calculate_salary as c_s
from application.db.people import get_employees as g_e
from datetime import datetime

if __name__ == '__main__':
    print(datetime.today())
    g_e()
    c_s()

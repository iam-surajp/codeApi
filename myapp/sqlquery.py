from .models import Company

def search_companies_by_employees_range(min_employees, max_employees):
    companies = Company.objects.filter(employees__range=(min_employees, max_employees))
    return companies
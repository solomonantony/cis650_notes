
import pandas as pd
import numpy as np

data = {
    "emp_id":     list(range(101, 126)),
    "name":       ["Alice", "Bob", "Carla", "David", "Elena", "Frank", "Grace",
                   "Henry", "Irene", "Jack", "Karen", "Leo", "Maria", "Nate",
                   "Olivia", "Paul", "Quinn", "Rosa", "Sam", "Tina", "Uma",
                   "Victor", "Wendy", "Xavier", "Yara"],
    "department": ["Sales", "IT", "HR", "Sales", "IT", "Finance", "Sales",
                   "IT", "HR", "Finance", "Sales", "IT", "Finance", "HR",
                   "Sales", "IT", "Finance", "Sales", "HR", "IT", "Finance",
                   "Sales", "IT", "HR", np.nan],
    "age":        [29, 41, 35, np.nan, 28, 52, 33, 45, np.nan, 38, 27, 31, 49,
                   36, 30, np.nan, 42, 26, 55, 34, 39, 44, 32, np.nan, 37],
    "salary":     [58000, 82000, 61000, 55000, np.nan, 97000, 62000, 91000,
                   59000, np.nan, 54000, 78000, 99000, 60000, 57000, 85000,
                   np.nan, 52000, 64000, 80000, 93000, 66000, 76000, 58000,
                   72000],
    "years_exp":  [4, 15, 9, 3, 5, 25, 8, 20, 11, 12, 2, 7, 22, 10, 6, 18, 14,
                   1, 30, 9, 13, 17, 6, 12, 10],
    "rating":     [4.2, 3.8, 4.5, 3.1, np.nan, 4.8, 3.9, 4.1, np.nan, 4.4, 3.5,
                   4.0, 4.7, 3.6, 4.3, np.nan, 4.6, 3.2, 3.9, 4.2, 4.5, 4.0,
                   3.7, np.nan, 4.1],
}

import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(42)
random.seed(42)

print("Өгөгдөл үүсгэж байна...")

# ── SHEET 1: Ажилтны хувийн мэдээлэл ──
employees = []
for i in range(1, 1_000_001):
    employees.append({
        "employee_id":   i,
        "ovog":          fake.last_name(),
        "ner":           fake.first_name(),
        "email":         fake.email(),
        "utas":          fake.phone_number(),
        "huis":          random.choice(["Эрэгтэй", "Эмэгтэй"]),
        "torolson_ognoo": fake.date_of_birth(minimum_age=22, maximum_age=60).strftime("%Y-%m-%d"),
        "haig":          fake.address().replace("\n", ", "),
        "albан_tushaal": random.choice(["Менежер", "Инженер", "Нягтлан", "Зөвлөх", "Дизайнер", "Программист", "Борлуулагч"]),
        "bag":           random.choice(["IT", "Санхүү", "Маркетинг", "Үйлдвэрлэл", "Хүний нөөц"]),
        "eleссэн_огноо": fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d"),
    })

employees_df = pd.DataFrame(employees)
print(f"✅ Sheet 1 - Хувийн мэдээлэл: {len(employees_df):,} мөр")

# ── SHEET 2: Цалин ба ажлын мэдээлэл ──
salaries = []
for i in range(1, 1_000_001):
    undsen_tsalin = random.randint(800_000, 5_000_000)
    ajillah_tsag  = 168  # сард ёсоор байх цаг
    ajilsan_tsag  = random.randint(140, 200)
    iluu_tsag     = max(0, ajilsan_tsag - ajillah_tsag)
    bonus         = random.choice([0, 0, 0, 100_000, 200_000, 500_000])
    iluu_tsagiin_tuluv = round(iluu_tsag * (undsen_tsalin / ajillah_tsag) * 1.5)
    niit_tsalin   = undsen_tsalin + iluu_tsagiin_tuluv + bonus

    salaries.append({
        "employee_id":       i,
        "undsen_tsalin":     undsen_tsalin,
        "ajillah_tsag":      ajillah_tsag,
        "ajilsan_tsag":      ajilsan_tsag,
        "iluu_tsag":         iluu_tsag,
        "iluu_tsagiin_tuluv": iluu_tsagiin_tuluv,
        "bonus":             bonus,
        "niit_tsalin":       niit_tsalin,
        "tsalin_ognoo":      fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        "tuluv":             random.choice(["Олгосон", "Хүлээгдэж байна", "Хойшлогдсон"]),
    })

salaries_df = pd.DataFrame(salaries)
print(f"✅ Sheet 2 - Цалин мэдээлэл: {len(salaries_df):,} мөр")

# ── XLSX хадгалах (2 sheet) ──
print("Excel файл хадгалж байна...")
with pd.ExcelWriter("data/employees.xlsx", engine="openpyxl") as writer:
    employees_df.to_excel(writer, sheet_name="Huviin_Medeelel", index=False)
    salaries_df.to_excel(writer, sheet_name="Tsalin_Medeelel", index=False)

print("\n🎉 Дууслаа! → data/employees.xlsx")
print("2 sheet employee_id-аар холбогдсон байна.")
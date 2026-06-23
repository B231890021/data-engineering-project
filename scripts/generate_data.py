import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(42)
random.seed(42)

print("Өгөгдөл үүсгэж байна...")

heltes_tushaal = {
    "IT":          ["Программист", "Инженер", "Дизайнер", "Менежер"],
    "Санхүү":      ["Нягтлан", "Зөвлөх", "Менежер"],
    "Маркетинг":   ["Дизайнер", "Зөвлөх", "Борлуулагч", "Менежер"],
    "Үйлдвэрлэл": ["Инженер", "Зөвлөх", "Менежер"],
    "Хүний нөөц": ["Зөвлөх", "Менежер"],
}

tsalin_range = {
    "Менежер":     (3_000_000, 8_000_000),
    "Инженер":     (2_000_000, 6_000_000),
    "Программист": (2_500_000, 7_000_000),
    "Нягтлан":     (1_500_000, 4_000_000),
    "Борлуулагч":  (800_000,   3_000_000),
    "Дизайнер":    (1_000_000, 4_000_000),
    "Зөвлөх":      (2_000_000, 6_000_000),
}

hoishlogdson_shaltgaan = [
    "Банкны алдаа",
    "Баримт бүрдүүлэлт дутуу",
    "Санхүүгийн дутагдал",
    "Баяр сайн өдөр",
    "Системийн доголдол",
]

huleegdej_bga_shaltgaan = [
    "Менежерийн зөвшөөрөл хүлээж байна",
    "Нягтлан шалгаж байна",
    "Банкны гүйлгээ хийгдэж байна",
    "Баримт бүрдүүлэлт хийгдэж байна",
]

bolovsrol_list = ["Бүрэн дунд", "Бакалавр", "Магистр", "Доктор"]

# TABLE 1
print("Table 1 үүсгэж байна...")
employees = []
for i in range(1, 1_000_001):
    heltes = random.choice(list(heltes_tushaal.keys()))
    alban_tushaal = random.choice(heltes_tushaal[heltes])
    elessen = fake.date_between(start_date="-10y", end_date="-1y")
    ajillaj_bgaa = random.random() > 0.1
    garsan_ognoo = None if ajillaj_bgaa else fake.date_between(
        start_date=elessen, end_date="today"
    )
    employees.append({
        "employee_id":   i,
        "ner":           fake.first_name(),
        "ovog":          fake.last_name(),
        "nas":           random.randint(22, 60),
        "huis":          random.choice(["Эрэгтэй", "Эмэгтэй"]),
        "utas":          fake.phone_number(),
        "email":         fake.email(),
        "hayg":          fake.city(),
        "bolovsrol":     random.choice(bolovsrol_list),
        "alban_tushaal": alban_tushaal,
        "heltes":        heltes,
        "elessen_ognoo": elessen.strftime("%Y-%m-%d"),
        "garsan_ognoo":  garsan_ognoo.strftime("%Y-%m-%d") if garsan_ognoo else None,
    })

emp_df = pd.DataFrame(employees)
print(f"✅ Table 1: {len(emp_df):,} мөр")

# TABLE 2
print("Table 2 үүсгэж байна...")
salaries = []
for i in range(1, 1_000_001):
    alban_tushaal = employees[i-1]["alban_tushaal"]
    min_tsalin, max_tsalin = tsalin_range[alban_tushaal]
    undsen_tsalin      = random.randint(min_tsalin, max_tsalin)
    ajillah_ystoi_tsag = 168
    ajilsan_tsag       = random.randint(100, 220)
    unelgee            = random.choice(["A", "B", "C", "D"])
    bonus              = {"A": 500_000, "B": 200_000, "C": 100_000, "D": 0}[unelgee]
    tsalin_sar         = fake.date_between(
        start_date="-2y", end_date="today"
    ).strftime("%Y-%m")
    tuluv              = random.choice([
        "Олгосон", "Олгосон", "Олгосон",
        "Хүлээгдэж байна", "Хойшлогдсон"
    ])
    if tuluv == "Хойшлогдсон":
        shaltgaan = random.choice(hoishlogdson_shaltgaan)
    elif tuluv == "Хүлээгдэж байна":
        shaltgaan = random.choice(huleegdej_bga_shaltgaan)
    else:
        shaltgaan = None

    salaries.append({
        "employee_id":            i,
        "undsen_tsalin":          undsen_tsalin,
        "ajillah_ystoi_tsag":     ajillah_ystoi_tsag,
        "ajilsan_tsag":           ajilsan_tsag,
        "guitsetgeliiin_unelgee": unelgee,
        "bonus":                  bonus,
        "tsalin_sar":             tsalin_sar,
        "tuluv":                  tuluv,
        "shaltgaan":              shaltgaan,
    })

sal_df = pd.DataFrame(salaries)
print(f"✅ Table 2: {len(sal_df):,} мөр")

print("Excel файл хадгалж байна...")
with pd.ExcelWriter("data/employees.xlsx", engine="openpyxl") as writer:
    emp_df.to_excel(writer, sheet_name="Huviin_Medeelel", index=False)
    sal_df.to_excel(writer, sheet_name="Tsalin_Medeelel", index=False)

print("\n🎉 Дууслаа! → data/employees.xlsx")
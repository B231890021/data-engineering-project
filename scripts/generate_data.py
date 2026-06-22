import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(42)
random.seed(42)

print("Өгөгдөл үүсгэж байна...")

# ── TABLE 1: Хувийн мэдээлэл ──
employees = []
for i in range(1, 1_000_001):
    eleссэн = fake.date_between(start_date="-10y", end_date="today")
    employees.append({
        "employee_id":    i,
        "ner":            fake.first_name(),
        "ovog":           fake.last_name(),
        "nas":            random.randint(22, 60),
        "huis":           random.choice(["Эрэгтэй", "Эмэгтэй"]),
        "utas":           fake.phone_number(),
        "email":          fake.email(),
        "hayg":           fake.city(),
        "bolovsrol":      random.choice(["Бүрэн дунд", "Бакалавр", "Магистр", "Доктор"]),
        "alban_tushaal":  random.choice(["Менежер", "Инженер", "Нягтлан", "Программист", "Борлуулагч", "Дизайнер", "Зөвлөх"]),
        "bag":            random.choice(["IT", "Санхүү", "Маркетинг", "Үйлдвэрлэл", "Хүний нөөц"]),
        "elessen_ognoo":  eleссэн.strftime("%Y-%m-%d"),
        "ajliin_jil":     (pd.Timestamp.today() - pd.Timestamp(eleссэн)).days // 365,
        "tuluv":          random.choice(["Идэвхтэй", "Чөлөөтэй", "Гарсан"]),
    })

emp_df = pd.DataFrame(employees)
print(f"✅ Table 1 - Хувийн мэдээлэл: {len(emp_df):,} мөр")

# ── TABLE 2: Ажлын мэдээлэл ──
salaries = []
for i in range(1, 1_000_001):
    undsen_tsalin      = random.randint(800_000, 5_000_000)
    ajillah_ystoi_tsag = 168
    ajilsan_tsag       = random.randint(120, 210)
    iluu_tsag          = max(0, ajilsan_tsag - ajillah_ystoi_tsag)
    dutuu_tsag       = max(0, ajillah_ystoi_tsag - ajilsan_tsag)
    tsagiin_unelgee      = round(undsen_tsalin / ajillah_ystoi_tsag, 0)
    iluu_tsagiin_tuluv = round(iluu_tsag * tsagiin_unelgee * 1.5, 0)
    unelgee            = random.choice(["A", "B", "C", "D"])
    bonus              = {"A": 500_000, "B": 200_000, "C": 100_000, "D": 0}[unelgee]
    niit_tsalin        = undsen_tsalin + iluu_tsagiin_tuluv + bonus
    tatvar             = round(niit_tsalin * 0.10, 0)
    ndsh               = round(niit_tsalin * 0.10, 0)
    gart_avah_tsalin   = niit_tsalin - tatvar - ndsh

    salaries.append({
        "employee_id":          i,
        "undsen_tsalin":        undsen_tsalin,
        "ajillah_ystoi_tsag":   ajillah_ystoi_tsag,
        "ajilsan_tsag":         ajilsan_tsag,
        "iluu_tsag":            iluu_tsag,
        "dutuu_tsag":         dutuu_tsag,
        "tsagiin_unelgee":        tsagiin_unelgee,
        "iluu_tsagiin_tuluv":   iluu_tsagiin_tuluv,
        "guitsetgeliiin_unelgee": unelgee,
        "bonus":                bonus,
        "niit_tsalin":          niit_tsalin,
        "tatvar_10%":           tatvar,
        "ndsh_10%":             ndsh,
        "gart_avah_tsalin":     gart_avah_tsalin,
        "tsalin_ognoo":         fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        "tuluv":                random.choice(["Олгосон", "Хүлээгдэж байна", "Хойшлогдсон"]),
    })

sal_df = pd.DataFrame(salaries)
print(f"✅ Table 2 - Ажлын мэдээлэл: {len(sal_df):,} мөр")

# ── XLSX хадгалах ──
print("Excel файл хадгалж байна...")
with pd.ExcelWriter("data/employees.xlsx", engine="openpyxl") as writer:
    emp_df.to_excel(writer, sheet_name="Huviin_Medeelel", index=False)
    sal_df.to_excel(writer, sheet_name="Ajliin_Medeelel", index=False)

print("\n🎉 Дууслаа! → data/employees.xlsx")
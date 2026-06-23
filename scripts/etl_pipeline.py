import pandas as pd
from sqlalchemy import create_engine
import time

engine = create_engine('postgresql://admin:admin123@localhost:5432/main_db')

print("ETL Pipeline эхэллээ...")
start = time.time()

# ── SHEET 1: Хувийн мэдээлэл ──
print("\n📂 Sheet 1 уншиж байна...")
emp_df = pd.read_excel("data/employees.xlsx", sheet_name="Huviin_Medeelel")
emp_df = emp_df.rename(columns={"haig": "hayg"})
print(f"✅ {len(emp_df):,} мөр уншигдлаа")

print("⬆️  huviin_medeelel хүснэгтэд оруулж байна...")
emp_df.to_sql(
    name="huviin_medeelel",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=10_000,
    method="multi"
)
print(f"✅ huviin_medeelel: {len(emp_df):,} мөр оруулагдлаа")

# ── SHEET 2: Цалингийн мэдээлэл ──
print("\n📂 Sheet 2 уншиж байна...")
sal_df = pd.read_excel("data/employees.xlsx", sheet_name="Tsalin_Medeelel")
print(f"✅ {len(sal_df):,} мөр уншигдлаа")

print("⬆️  tsalin_medeelel хүснэгтэд оруулж байна...")
sal_df.to_sql(
    name="tsalin_medeelel",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=10_000,
    method="multi"
)
print(f"✅ tsalin_medeelel: {len(sal_df):,} мөр оруулагдлаа")

end = time.time()
print(f"\n🎉 ETL дууслаа! Нийт хугацаа: {round(end - start, 1)} секунд")
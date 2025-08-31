import pandas as pd
import numpy as np
import math, re

src = "../apps/web/public/data/cvs-test/test-data-set.csv"
dst = "../apps/web/public/data/cvs-test/reform-data.csv"

wide = pd.read_csv(src)

date_col = "date"
long = wide.melt(id_vars=[date_col],
                 value_vars=[c for c in wide.columns if c != date_col],
                 var_name="participant", value_name="value")

long["date"] = pd.to_datetime(long["date"], errors="coerce", dayfirst=False)

# for later, to convert all values into integers

# def to_int_0_10(x):
#     if pd.isna(x): return np.nan
#     s = str(x).strip().lower().replace(",", ".")
#     try:
#         return int(round(np.clip(float(s), 0, 10)))
#     except:
#         pass
#     for alias in {"π","п","pi","пи"}: s = s.replace(alias,"pi")
#     if re.findall(r"[a-zA-Z]+", s) not in ([], ["pi"]): return np.nan
#     try:
#         v = eval(s.replace("pi", str(math.pi)), {"__builtins__":{}}, {})
#         return int(round(np.clip(float(v), 0, 10)))
#     except:
#         return np.nan

#long["value"] = long["value"].apply(to_int_0_10)

long = long.dropna(subset=["date","value"]).sort_values(["participant","date"]).reset_index(drop=True)

long.to_csv(dst, index=False)
print("saved ->", dst)
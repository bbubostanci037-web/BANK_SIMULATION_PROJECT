# main.py
from data.scenario_1 import INVESTORS, DEBTORS, BANK_DATA
from models.accounts import InvestmentAccount, LoanAccount
from models.banker import Banker

# 1. Banka yöneticisini (merkezi kontrol) başlatalım
my_bank = Banker(
    starting_capital=BANK_DATA["starting_capital"],
    base_loan_rate=BANK_DATA["loan_interest_rate"],
    base_invest_rate=BANK_DATA["investment_interest_rate"]
)

# 2. TÜM YATIRIMCILARI TEK SEFERDE EKLEME (Otomasyon)
for inv_data in INVESTORS:
    account = InvestmentAccount(inv_data, my_bank.base_invest_rate)
    my_bank.add_account(account)

# 3. TÜM BORÇLULARI TEK SEFERDE EKLEME
for debt_data in DEBTORS:
    account = LoanAccount(debt_data, my_bank.base_loan_rate)
    my_bank.add_account(account)

print(f"Sisteme toplam {len(my_bank.accounts)} müşteri yüklendi.")
print(f"--- Simülasyon Başladı ---")
print(f"Başlangıç Sermayesi: {my_bank.total_capital:,.2f} TL\n")

# 4. Zaman Sınırlarını Bulma
if not my_bank.accounts:
    print("Sistemde hiç müşteri yok!")
    exit()

min_month_abs = min(acc.start_month_abs for acc in my_bank.accounts)
max_month_abs = max(acc.end_month_abs for acc in my_bank.accounts)

# 5. Dinamik Zaman Döngüsü (Time-Series Loop)
for current_month_abs in range(min_month_abs, max_month_abs):
    
    # Mutlak ayı Yıl-Ay formatına çevir (Gösterim için)
    year = current_month_abs // 12
    month = current_month_abs % 12
    if month == 0:
        month = 12
        year -= 1
    date_str = f"{year}-{month:02d}"

    report = my_bank.process_monthly_cycle(current_month_abs)
    
    if report == "BANKRUPT":
        print(f"!!! {date_str} TARİHİNDE BANKA İFLAS ETTİ !!!")
        print(f"Banka Kasası: {my_bank.total_capital:,.2f} TL")
        break
    
    # Rapor çıktısı
    if report["active_count"] > 0:
        print(f"Tarih: {date_str} | Aktif Müşteri: {report['active_count']} | Kasa: {my_bank.total_capital:,.2f} TL | Aylık Net Akış: {report['net_flow']:,.2f} TL")

print(f"\n--- Simülasyon Bitti ---")
if my_bank.is_bankrupt:
    print("Durum: BANKRUPT")
else:
    print(f"Final Capital : {my_bank.total_capital:,.2f} TL")

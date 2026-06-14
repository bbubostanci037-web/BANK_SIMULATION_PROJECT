# new_branch.py
from data.scenario_1 import INVESTORS, DEBTORS, BANK_DATA
from models.accounts import InvestmentAccount, LoanAccount
from models.banker import Banker

print("Analiz başlatiliyor...\n")

# 1. Banka yöneticisini (merkezi kontrol) başlatalım
my_bank = Banker(
    starting_capital=BANK_DATA["starting_capital"],
    base_loan_rate=BANK_DATA["loan_interest_rate"],
    base_invest_rate=BANK_DATA["investment_interest_rate"]
)

# 2. Müşterileri ekleme
for inv_data in INVESTORS:
    my_bank.add_account(InvestmentAccount(inv_data, my_bank.base_invest_rate))

for debt_data in DEBTORS:
    my_bank.add_account(LoanAccount(debt_data, my_bank.base_loan_rate))

if not my_bank.accounts:
    print("Sistemde müşteri yok.")
    exit()

# Şubelerin net getirilerini (kâr/zarar) tutacağımız sözlük
branch_profits = {}

min_month_abs = min(acc.start_month_abs for acc in my_bank.accounts)
max_month_abs = max(acc.end_month_abs for acc in my_bank.accounts)

# 3. Simülasyon döngüsü üzerinden şube analizi
for current_month_abs in range(min_month_abs, max_month_abs):
    for acc in my_bank.accounts:
        if acc.is_active_in_month(current_month_abs):
            flow = acc.calculate_monthly_flow()
            branch = acc.branch
            
            # Şube listede yoksa sıfırdan başlat
            if branch not in branch_profits:
                branch_profits[branch] = 0
            
            # Bu ayki nakit akışını şubenin toplamına ekle
            branch_profits[branch] += flow

# 4. Sonuçları Gösterme
print("--- ŞUBE BAZLI KÂRLILIK ANALİZİ ---")
for branch, profit in sorted(branch_profits.items(), key=lambda item: item[1], reverse=True):
    print(f"Şube: {branch:<10} | Toplam Net Getiri: {profit:,.2f} TL")

en_karli_sube = max(branch_profits, key=branch_profits.get)
print(f"\n=> SONUÇ: En yüksek kâri getiren ve yeni şube açmak için en mantikli lokasyon: {en_karli_sube.upper()}")

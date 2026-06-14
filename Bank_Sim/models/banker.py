# models/banker.py

class Banker:
   
   # Bankanın tüm finansal operasyonunu yöneten merkezi sınıf.
    
    def __init__(self, starting_capital, base_loan_rate, base_invest_rate):
        self.total_capital = starting_capital  # Başlangıç sermayesi
        self.base_loan_rate = base_loan_rate    # Bankanın kredi faiz politikası
        self.base_invest_rate = base_invest_rate # Bankanın yatırım faiz politikası
        self.accounts = []                     # Sisteme kayıtlı tüm nesneler (Yatırımcı/Borçlu)
        self.is_bankrupt = False               # İflas durumu kontrolü

    def add_account(self, account):
        """
        Döngü ile gelen tüm nesneleri (InvestmentAccount/LoanAccount) 
        bankanin sistemine kaydeder.
        """
        self.accounts.append(account)

    def process_monthly_cycle(self, current_month_abs):
        
       # Akış diyagramındaki 'Process the cash flow' kutusunun kod karşılığıdır.
       
        if self.total_capital <= 0:
            self.is_bankrupt = True
            return "BANKRUPT"

        monthly_net_flow = 0
        active_accounts_count = 0
        
        # Tüm hesapları tek bir döngüyle gezer (Abstraction)
        for acc in self.accounts:
            # Hesap, simülasyonun o anki ayında aktifse sürece dahil edilir
            if acc.is_active_in_month(current_month_abs):
                active_accounts_count += 1
                # Polimorfizm: acc'nin türüne göre faiz gelir mi gider mi kendi bilir
                monthly_net_flow += acc.calculate_monthly_flow()
        
        # Kasayı güncelle
        self.total_capital += monthly_net_flow
        return {"net_flow": monthly_net_flow, "active_count": active_accounts_count}
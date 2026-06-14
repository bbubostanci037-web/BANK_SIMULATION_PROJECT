# models/accounts.py
from utils.calculator import calculate_custom_investment_rate, calculate_custom_loan_rate

class Account:
    def __init__(self, account_id, owner_name, amount, duration, start_date_str, status):
        self.account_id = account_id
        self.owner_name = owner_name
        self.amount = amount
        self.duration = duration
        self.status = status
        
        # Tarih bilgisini matematiksel olarak kolay işlemek için mutlak aya çeviriyoruz.
        # Örnek: "2026-01-10" -> 2026 * 12 + 1 = 24313
        year, month, _ = map(int, start_date_str.split("-"))
        self.start_month_abs = year * 12 + month
        self.end_month_abs = self.start_month_abs + duration

    def is_active_in_month(self, current_month_abs):
        # İflas etmiş hesaplardan nakit akışını tamamen kesiyoruz.
        if self.status == "defaulted":
            return False
        # Hesap sadece başlangıç ayı ile bitiş ayı arasında işlem görecektir.
        return self.start_month_abs <= current_month_abs < self.end_month_abs

    def calculate_monthly_flow(self):
        raise NotImplementedError("Subclasses must implement calculate_monthly_flow")

class InvestmentAccount(Account):
    #"""Yatırımcılar için hesap sınıfı."""
    def __init__(self, data_dict, base_invest_rate):
        super().__init__(
            account_id=data_dict["id"],
            owner_name=data_dict["name"],
            amount=data_dict["deposit_amount"],
            duration=data_dict["duration_months"],
            start_date_str=data_dict["start_date"],
            status=data_dict["status"]
        )
        self.branch = data_dict["branch"]
        
        self.interest_rate = calculate_custom_investment_rate(
            base_invest_rate, 
            data_dict["credit_score"], 
            data_dict["duration_months"]
        )

    def calculate_monthly_flow(self):
        # Bankanın yatırımcıya ödediği aylık faiz (Gider olduğu için negatif)
        return -(self.amount * self.interest_rate / 12)


class LoanAccount(Account):
    def __init__(self, data_dict, base_loan_rate):
        super().__init__(
            account_id=data_dict["id"],
            owner_name=data_dict["name"],
            amount=data_dict["loan_amount"],
            duration=data_dict["duration_months"],
            start_date_str=data_dict["start_date"],
            status=data_dict["status"]
        )
        self.branch = data_dict["branch"]
        
        self.interest_rate = calculate_custom_loan_rate(base_loan_rate, data_dict["credit_score"], data_dict["duration_months"])

    def calculate_monthly_flow(self):
        # Bankanın borçludan aldığı aylık ödeme (anapara + faiz) (Gelir olduğu için pozitif)
        monthly_payment = (self.amount / self.duration) + (self.amount * self.interest_rate / 12)
        return monthly_payment
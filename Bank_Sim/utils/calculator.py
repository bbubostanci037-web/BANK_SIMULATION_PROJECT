
    
# utils/calculator.py içindeki calculate_custom_loan_rate fonksiyonu:
'''

def calculate_custom_loan_rate(base_rate, credit_score):
    # Kredi notuna göre faiz oranini belirleyen basit bir formül
    if credit_score >= 750:
        return base_rate * 0.8  # İyi kredi notu, daha düşük faiz
    elif credit_score >= 600:
        return base_rate  # Orta kredi notu, standart faiz
    else:
        return base_rate * 1.2  # Düşük kredi notu, daha yüksek faiz
        
'''




def calculate_custom_loan_rate(base_loan_rate, credit_score, duration):
    """
    Borçluya özel kredi faizi hesaplar.
    Kredi skoru düşükse risk artacaği için faiz orani yükselir.
    """
    # Risk Primi: Skor 850'den ne kadar uzaksa faiz o kadar artar
    risk_premium = ((850 - credit_score) / 850) * 0.02  # Max %2 ek faiz
    
    return round(base_loan_rate + risk_premium, 4)

def calculate_custom_investment_rate(base_invest_rate, credit_score, duration):
    
    #Yatırımcıya özel faiz oranını hesaplar.
    #Bu fonksiyon çağrılana kadar Python faizin ne olacağını bilmez.
    
    # Skor Primi: Kredi skoru 850'ye ne kadar yakınsa o kadar ek faiz (Max %1)
    score_bonus = (credit_score / 850) * 0.01 
    
    # Vade Primi: Para 12 aydan uzun kalırsa %0.5 ek teşvik
    duration_bonus = 0.005 if duration > 12 else 0
    
    # Sonuç: Taban faiz + bonuslar
    final_rate = base_invest_rate + score_bonus + duration_bonus
    
    return round(final_rate, 4)
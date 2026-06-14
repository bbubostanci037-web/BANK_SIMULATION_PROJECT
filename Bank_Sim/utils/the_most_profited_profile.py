import sys
import os

# Sistemin ana dizinini path'e ekliyoruz ki data ve utils modüllerini bulabilsin
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.scenario_1 import INVESTORS
from utils.calculator import calculate_custom_investment_rate

toplam_mevduat = 0
toplam_odenecek_faiz = 0
en_yuksek_getiri = 0
en_kazancli_musteri = ""

# Taban faiz oranını %5 (0.05) olarak belirliyoruz.
# İsterseniz bu değeri sonradan değiştirebilirsiniz.
BASE_INVEST_RATE = 0.05 

for m in INVESTORS:
    # 1. Kredi skoruna ve vadeye göre yatırımcıya özel faiz oranını hesaplama
    ozel_faiz_orani = calculate_custom_investment_rate(BASE_INVEST_RATE, m["credit_score"], m["duration_months"])
    
    # 2. Her müşteri için basit faiz hesaplama
    faiz_getirisi = m["deposit_amount"] * ozel_faiz_orani * (m["duration_months"] / 12)
    toplam_para = m["deposit_amount"] + faiz_getirisi
     
    # 3. Banka geneli toplamları biriktirme
    toplam_mevduat += m["deposit_amount"]
    toplam_odenecek_faiz += faiz_getirisi
    
    # 4. En çok kazanan müşteriyi bulma (Analiz)
    if faiz_getirisi > en_yuksek_getiri:
        en_yuksek_getiri = faiz_getirisi
        en_kazancli_musteri = m["name"]

# --- ANALİZ SONUÇLARI ---
print(f"Bankadaki Toplam Mevduat: {toplam_mevduat:,.2f} TL")
print(f"Vade Sonunda Bankanın Ödeyeceği Toplam Faiz: {toplam_odenecek_faiz:,.2f} TL")
print(f"En Yüksek Getiri Sağlayan: {en_kazancli_musteri} ({en_yuksek_getiri:,.2f} TL)")
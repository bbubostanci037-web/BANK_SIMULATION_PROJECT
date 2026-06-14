

BANK_DATA = {
    "starting_capital": 1000000,  
    "loan_interest_rate": 0.12,  
    "investment_interest_rate": 0.05 
}




INVESTORS = [
    {"id": 201, "name": "Caner Akin", "deposit_amount": 500000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 850, "start_date": "2026-01-01", "branch": "İstanbul"},
    {"id": 202, "name": "Sibel Yilmaz", "deposit_amount": 250000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 720, "start_date": "2026-02-15", "branch": "Mersin"},
    {"id": 203, "name": "Mert Erdem", "deposit_amount": 100000, "duration_months": 6, "type": "investor", "status": "active", "credit_score": 680, "start_date": "2026-03-01", "branch": "Gebze"},
    {"id": 204, "name": "Derya Sönmez", "deposit_amount": 750000, "duration_months": 36, "type": "investor", "status": "closed", "credit_score": 810, "start_date": "2026-01-10", "branch": "İstanbul"},
    {"id": 205, "name": "Okan Kurt", "deposit_amount": 150000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 750, "start_date": "2026-04-12", "branch": "Gebze"},
    {"id": 206, "name": "Melis Aydin", "deposit_amount": 300000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 790, "start_date": "2026-02-20", "branch": "Mersin"},
    {"id": 207, "name": "Bora Çetin", "deposit_amount": 450000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 830, "start_date": "2026-05-05", "branch": "İstanbul"},
    {"id": 208, "name": "Gaye Yildiz", "deposit_amount": 80000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 640, "start_date": "2026-03-15", "branch": "İstanbul"},
    {"id": 209, "name": "Umut Doğan", "deposit_amount": 1200000, "duration_months": 48, "type": "investor", "status": "active", "credit_score": 880, "start_date": "2026-01-05", "branch": "Gebze"},
    {"id": 210, "name": "Ebru Şahin", "deposit_amount": 600000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 770, "start_date": "2026-06-01", "branch": "Mersin"},
    {"id": 211, "name": "Turgut Alp", "deposit_amount": 40000, "duration_months": 3, "type": "investor", "status": "closed", "credit_score": 600, "start_date": "2026-07-20", "branch": "Gebze"},
    {"id": 212, "name": "Asli Demir", "deposit_amount": 180000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 740, "start_date": "2026-02-10", "branch": "İstanbul"},
    {"id": 213, "name": "Kerem Işik", "deposit_amount": 900000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 820, "start_date": "2026-01-25", "branch": "Mersin"},
    {"id": 214, "name": "İrem Kaya", "deposit_amount": 220000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 710, "start_date": "2026-08-14", "branch": "Gebze"},
    {"id": 215, "name": "Sinan Yavuz", "deposit_amount": 350000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 785, "start_date": "2026-03-30", "branch": "İstanbul"},
    {"id": 216, "name": "Zuhal Avci", "deposit_amount": 75000, "duration_months": 6, "type": "investor", "status": "closed", "credit_score": 660, "start_date": "2026-09-01", "branch": "Mersin"},
    {"id": 217, "name": "Firat Güneş", "deposit_amount": 550000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 840, "start_date": "2026-04-18", "branch": "Gebze"},
    {"id": 218, "name": "Nihal Tekin", "deposit_amount": 420000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 760, "start_date": "2026-05-22", "branch": "İstanbul"},
    {"id": 219, "name": "Levent Ege", "deposit_amount": 130000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 730, "start_date": "2026-10-05", "branch": "Mersin"},
    {"id": 220, "name": "Pelin Aksoy", "deposit_amount": 680000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 805, "start_date": "2026-01-15", "branch": "İstanbul"},
    {"id": 221, "name": "Onur Bulut", "deposit_amount": 95000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 690, "start_date": "2026-11-12", "branch": "Gebze"},
    {"id": 222, "name": "Selma Koç", "deposit_amount": 1100000, "duration_months": 60, "type": "investor", "status": "active", "credit_score": 890, "start_date": "2026-01-02", "branch": "İstanbul"},
    {"id": 223, "name": "Metin Uzun", "deposit_amount": 200000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 745, "start_date": "2026-12-01", "branch": "Mersin"},
    {"id": 224, "name": "Hande Polat", "deposit_amount": 320000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 775, "start_date": "2026-04-25", "branch": "Gebze"},
    {"id": 225, "name": "Cem Şimşek", "deposit_amount": 850000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 835, "start_date": "2026-02-28", "branch": "İstanbul"}
]



DEBTORS = [
    {"id": 101, "name": "Ahmet Yilmaz", "loan_amount": 45000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 820, "start_date": "2026-01-10", "branch": "İstanbul"},
    {"id": 102, "name": "Ayşe Demir", "loan_amount": 120000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 710, "start_date": "2026-02-05", "branch": "Mersin"},
    {"id": 103, "name": "Mehmet Kaya", "loan_amount": 35000, "duration_months": 6, "type": "debtor", "status": "closed", "credit_score": 650, "start_date": "2025-12-01", "branch": "Gebze"},
    {"id": 104, "name": "Fatma Şahin", "loan_amount": 85000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 780, "start_date": "2026-03-20", "branch": "İstanbul"},
    {"id": 105, "name": "Can Özkan", "loan_amount": 200000, "duration_months": 48, "type": "debtor", "status": "defaulted", "credit_score": 450, "start_date": "2026-01-15", "branch": "Gebze"},
    {"id": 106, "name": "Zeynep Çelik", "loan_amount": 15000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 690, "start_date": "2026-04-01", "branch": "Mersin"},
    {"id": 107, "name": "Murat Aydin", "loan_amount": 60000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 740, "start_date": "2026-05-12", "branch": "İstanbul"},
    {"id": 108, "name": "Elif Yildiz", "loan_amount": 95000, "duration_months": 36, "type": "debtor", "status": "active", "credit_score": 810, "start_date": "2026-02-28", "branch": "Gebze"},
    {"id": 109, "name": "Burak Aksoy", "loan_amount": 40000, "duration_months": 12, "type": "debtor", "status": "closed", "credit_score": 720, "start_date": "2025-11-15", "branch": "Mersin"},
    {"id": 110, "name": "Deniz Arslan", "loan_amount": 250000, "duration_months": 60, "type": "debtor", "status": "active", "credit_score": 850, "start_date": "2026-01-05", "branch": "İstanbul"},
    {"id": 111, "name": "Selin Bulut", "loan_amount": 12000, "duration_months": 6, "type": "debtor", "status": "active", "credit_score": 600, "start_date": "2026-06-10", "branch": "Gebze"},
    {"id": 112, "name": "Hakan Tekin", "loan_amount": 75000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 730, "start_date": "2026-02-20", "branch": "Mersin"},
    {"id": 113, "name": "Asli Güneş", "loan_amount": 30000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 760, "start_date": "2026-07-01", "branch": "İstanbul"},
    {"id": 114, "name": "Emre Koç", "loan_amount": 110000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 700, "start_date": "2026-03-15", "branch": "Gebze"},
    {"id": 115, "name": "Gamze Erdem", "loan_amount": 55000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 680, "start_date": "2026-04-25", "branch": "Mersin"},
    {"id": 116, "name": "Oğuzhan Kiliç", "loan_amount": 180000, "duration_months": 36, "type": "debtor", "status": "defaulted", "credit_score": 420, "start_date": "2026-01-10", "branch": "İstanbul"},
    {"id": 117, "name": "Büşra Doğan", "loan_amount": 22000, "duration_months": 10, "type": "debtor", "status": "active", "credit_score": 750, "start_date": "2026-08-05", "branch": "Gebze"},
    {"id": 118, "name": "Serkan Avci", "loan_amount": 90000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 790, "start_date": "2026-05-18", "branch": "Mersin"},
    {"id": 119, "name": "Merve Kurt", "loan_amount": 65000, "duration_months": 15, "type": "debtor", "status": "active", "credit_score": 715, "start_date": "2026-09-12", "branch": "İstanbul"},
    {"id": 120, "name": "Gökhan Yavuz", "loan_amount": 140000, "duration_months": 36, "type": "debtor", "status": "active", "credit_score": 800, "start_date": "2026-02-14", "branch": "Gebze"},
    {"id": 121, "name": "Derya Uzun", "loan_amount": 28000, "duration_months": 8, "type": "debtor", "status": "closed", "credit_score": 670, "start_date": "2025-10-20", "branch": "Mersin"},
    {"id": 122, "name": "Yasin Polat", "loan_amount": 50000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 740, "start_date": "2026-10-30", "branch": "İstanbul"},
    {"id": 123, "name": "Seda Şimşek", "loan_amount": 70000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 725, "start_date": "2026-04-12", "branch": "Gebze"},
    {"id": 124, "name": "Kaan Çetin", "loan_amount": 125000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 770, "start_date": "2026-06-25", "branch": "Mersin"},
    {"id": 125, "name": "Pinar Altin", "loan_amount": 42000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 735, "start_date": "2026-11-15", "branch": "İstanbul"}
]
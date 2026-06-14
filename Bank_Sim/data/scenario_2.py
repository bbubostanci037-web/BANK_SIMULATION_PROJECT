

BANK_DATA = {
    "starting_capital": 2500000,       
    "loan_interest_rate": 0.15,        
    "investment_interest_rate": 0.07    
}




INVESTORS = [
    {"id": 301, "name": "Alperen Yilmaz", "deposit_amount": 600000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 820, "start_date": "2026-02-10", "branch": "Ankara"},
    {"id": 302, "name": "Burcu Kaya", "deposit_amount": 400000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 740, "start_date": "2026-03-15", "branch": "İzmir"},
    {"id": 303, "name": "Cemil Çetin", "deposit_amount": 150000, "duration_months": 6, "type": "investor", "status": "closed", "credit_score": 690, "start_date": "2026-01-05", "branch": "Bursa"},
    {"id": 304, "name": "Damla Demir", "deposit_amount": 850000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 860, "start_date": "2026-02-20", "branch": "Ankara"},
    {"id": 305, "name": "Eren Güneş", "deposit_amount": 200000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 710, "start_date": "2026-05-01", "branch": "Bursa"},
    {"id": 306, "name": "Figen Arslan", "deposit_amount": 350000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 780, "start_date": "2026-04-12", "branch": "İzmir"},
    {"id": 307, "name": "Gökhan Avci", "deposit_amount": 500000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 800, "start_date": "2026-01-18", "branch": "Ankara"},
    {"id": 308, "name": "Hande Öztürk", "deposit_amount": 95000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 660, "start_date": "2026-06-15", "branch": "Ankara"},
    {"id": 309, "name": "İlker Doğan", "deposit_amount": 1400000, "duration_months": 48, "type": "investor", "status": "active", "credit_score": 890, "start_date": "2026-01-10", "branch": "Bursa"},
    {"id": 310, "name": "Jale Şahin", "deposit_amount": 700000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 790, "start_date": "2026-07-01", "branch": "İzmir"},
    {"id": 311, "name": "Kamil Polat", "deposit_amount": 55000, "duration_months": 3, "type": "investor", "status": "closed", "credit_score": 620, "start_date": "2026-08-25", "branch": "Bursa"},
    {"id": 312, "name": "Lale Uzun", "deposit_amount": 220000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 730, "start_date": "2026-03-05", "branch": "Ankara"},
    {"id": 313, "name": "Murat Kiliç", "deposit_amount": 950000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 840, "start_date": "2026-01-22", "branch": "İzmir"},
    {"id": 314, "name": "Nalan Bulut", "deposit_amount": 280000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 750, "start_date": "2026-09-10", "branch": "Bursa"},
    {"id": 315, "name": "Orhan Tekin", "deposit_amount": 420000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 770, "start_date": "2026-04-05", "branch": "Ankara"},
    {"id": 316, "name": "Pelin Kurt", "deposit_amount": 85000, "duration_months": 6, "type": "investor", "status": "closed", "credit_score": 640, "start_date": "2026-10-01", "branch": "İzmir"},
    {"id": 317, "name": "Rasim Yavuz", "deposit_amount": 650000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 815, "start_date": "2026-05-20", "branch": "Bursa"},
    {"id": 318, "name": "Seda Erdem", "deposit_amount": 480000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 765, "start_date": "2026-06-18", "branch": "Ankara"},
    {"id": 319, "name": "Tarik Aksoy", "deposit_amount": 190000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 720, "start_date": "2026-11-02", "branch": "İzmir"},
    {"id": 320, "name": "Ufuk Aydin", "deposit_amount": 720000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 830, "start_date": "2026-01-28", "branch": "Ankara"},
    {"id": 321, "name": "Vildan Koç", "deposit_amount": 110000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 675, "start_date": "2026-12-05", "branch": "Bursa"},
    {"id": 322, "name": "Yavuz Şimşek", "deposit_amount": 1350000, "duration_months": 60, "type": "investor", "status": "active", "credit_score": 895, "start_date": "2026-01-02", "branch": "Ankara"},
    {"id": 323, "name": "Zuhal Altin", "deposit_amount": 310000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 755, "start_date": "2026-12-15", "branch": "İzmir"},
    {"id": 324, "name": "Bahar Sönmez", "deposit_amount": 390000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 785, "start_date": "2026-05-28", "branch": "Bursa"},
    {"id": 325, "name": "Kenan Akin", "deposit_amount": 920000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 850, "start_date": "2026-03-20", "branch": "Ankara"}
]




DEBTORS = [
    {"id": 401, "name": "Oğuz Yilmaz", "loan_amount": 65000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 810, "start_date": "2026-01-20", "branch": "Ankara"},
    {"id": 402, "name": "Merve Demir", "loan_amount": 145000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 730, "start_date": "2026-02-15", "branch": "İzmir"},
    {"id": 403, "name": "Fatih Kaya", "loan_amount": 50000, "duration_months": 6, "type": "debtor", "status": "closed", "credit_score": 660, "start_date": "2025-12-10", "branch": "Bursa"},
    {"id": 404, "name": "Selin Şahin", "loan_amount": 95000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 760, "start_date": "2026-04-05", "branch": "Ankara"},
    {"id": 405, "name": "Tolga Özkan", "loan_amount": 320000, "duration_months": 48, "type": "debtor", "status": "defaulted", "credit_score": 410, "start_date": "2026-01-18", "branch": "Bursa"},
    {"id": 406, "name": "Ece Çelik", "loan_amount": 25000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 700, "start_date": "2026-04-20", "branch": "İzmir"},
    {"id": 407, "name": "Kadir Aydin", "loan_amount": 80000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 725, "start_date": "2026-05-25", "branch": "Ankara"},
    {"id": 408, "name": "Asli Yildiz", "loan_amount": 115000, "duration_months": 36, "type": "debtor", "status": "active", "credit_score": 795, "start_date": "2026-03-02", "branch": "Bursa"},
    {"id": 409, "name": "Serhat Aksoy", "loan_amount": 55000, "duration_months": 12, "type": "debtor", "status": "closed", "credit_score": 740, "start_date": "2025-11-20", "branch": "İzmir"},
    {"id": 410, "name": "Gaye Arslan", "loan_amount": 300000, "duration_months": 60, "type": "debtor", "status": "active", "credit_score": 840, "start_date": "2026-01-12", "branch": "Ankara"},
    {"id": 411, "name": "Yiğit Bulut", "loan_amount": 20000, "duration_months": 6, "type": "debtor", "status": "active", "credit_score": 610, "start_date": "2026-07-02", "branch": "Bursa"},
    {"id": 412, "name": "Banu Tekin", "loan_amount": 85000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 715, "start_date": "2026-03-01", "branch": "İzmir"},
    {"id": 413, "name": "Doruk Güneş", "loan_amount": 45000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 750, "start_date": "2026-07-15", "branch": "Ankara"},
    {"id": 414, "name": "Melisa Koç", "loan_amount": 130000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 690, "start_date": "2026-03-25", "branch": "Bursa"},
    {"id": 415, "name": "Cihan Erdem", "loan_amount": 70000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 675, "start_date": "2026-05-10", "branch": "İzmir"},
    {"id": 416, "name": "Tuğba Kiliç", "loan_amount": 210000, "duration_months": 36, "type": "debtor", "status": "defaulted", "credit_score": 435, "start_date": "2026-01-25", "branch": "Ankara"},
    {"id": 417, "name": "Efe Doğan", "loan_amount": 35000, "duration_months": 10, "type": "debtor", "status": "active", "credit_score": 735, "start_date": "2026-08-12", "branch": "Bursa"},
    {"id": 418, "name": "İrem Avci", "loan_amount": 105000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 780, "start_date": "2026-06-01", "branch": "İzmir"},
    {"id": 419, "name": "Metin Kurt", "loan_amount": 75000, "duration_months": 15, "type": "debtor", "status": "active", "credit_score": 705, "start_date": "2026-09-20", "branch": "Ankara"},
    {"id": 420, "name": "Nisa Yavuz", "loan_amount": 160000, "duration_months": 36, "type": "debtor", "status": "active", "credit_score": 820, "start_date": "2026-02-22", "branch": "Bursa"},
    {"id": 421, "name": "Onur Uzun", "loan_amount": 38000, "duration_months": 8, "type": "debtor", "status": "closed", "credit_score": 655, "start_date": "2025-10-28", "branch": "İzmir"},
    {"id": 422, "name": "Sibel Polat", "loan_amount": 60000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 755, "start_date": "2026-11-10", "branch": "Ankara"},
    {"id": 423, "name": "Umut Şimşek", "loan_amount": 85000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 745, "start_date": "2026-05-02", "branch": "Bursa"},
    {"id": 424, "name": "Zeynep Çetin", "loan_amount": 150000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 765, "start_date": "2026-07-01", "branch": "İzmir"},
    {"id": 425, "name": "Hakan Altin", "loan_amount": 48000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 720, "start_date": "2026-11-20", "branch": "Ankara"}
]
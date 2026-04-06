#import library ที่จำเป็น
from forex_python.converter import CurrencyRates
from datetime import datetime, timedelta
import statistics

#เรียกใช้ class currency rate
c = CurrencyRates()

#กำหนดตัวแปลและ input ของ user
base_currency_value = int(input("จำนวนเงินที่ต้องการแปลงค่า : "))
base_currency = input("ใส่ค่าเงินหลัก(THB) : ")
target_currency = input("ใส่ค่าเงินปลายทาง : ")
day_back = int(input("ใส่จำนวนวันย้อนหลังที่ต้องการคำนวน : "))
rates_list = []

#แสดงข้อความดำเนินการ
print(f'กำลังคำนวณการแปลงค่าเงิน {base_currency} เพื่อไปเป็น {target_currency} ย้อนหลัง {day_back} วัน')

#loop จำนวนวันลงใน timedelta(เพื่อนับวันย้อนหลัง) แล้วลบกับวันปัจจุบัน
#เพื่อดึงสถิติย้อนหลังตามจำนวนวันที่กรอก
for day in range(day_back):
    date = datetime.now() - timedelta(days=day)
    try:
        rate = c.get_rate(base_currency, target_currency, date)
        rates_list.append(rate)
    except:
        continue


#ดึงค่าเงินปัจจุบัน
current_rate = c.get_rate(base_currency,target_currency)


#print(f'') เพื่อแสดงค่าผลการแปลง ค่าปัจจุบัน ค่าเฉลี่ย ค่า MAX MIN
if rates_list:
    print(f'\n--- เงินมูลค่า {base_currency_value} {base_currency} แปลงเป็นเงิน {target_currency} ย้อนหลัง {day_back} วัน ได้ดังนี้ ---')
    print(f'ผลการแปลงค่าเงินปัจจุบัน = {current_rate * base_currency_value:.4f} {target_currency}')
    print(f'ค่าเงินปัจจุบันคือ {current_rate:.4f}: {target_currency}')
    print(f'ค่าเฉลี่ยย้อนหลัง {day_back} วัน = {statistics.mean(rates_list):.4f} {target_currency}')
    print(f'ค่าสูงสุดย้อนหลัง {day_back} วัน = {max(rates_list):.4f} {target_currency}')
    print(f'ค่าต่ำสุดย้อนหลัง {day_back} วัน = {min(rates_list):.4f} {target_currency}')
else:
    print("ไม่พบข้อมูล")
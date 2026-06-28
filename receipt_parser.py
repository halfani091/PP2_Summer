"""
Practice 5: Python Regular Expressions (RegEx)


Демонстрирует использование:
  re.search()   — поиск первого совпадения
  re.findall()  — поиск всех совпадений
  re.split()    — разбивка строки по паттерну
  re.sub()      — замена по паттерну
  re.match()    — совпадение с начала строки
  Флаги: re.MULTILINE, re.IGNORECASE
"""

import re
import json



def parse_price(raw: str) -> float:
    """Конвертирует строку цены казахстанского формата в float.

    Примеры:
        "1 200,00"  →  1200.0
        "51,00"     →  51.0

    Используем re.sub() для удаления пробелов-разделителей тысяч
    и замены запятой на точку.
    """
    # re.sub() — заменяем все пробелы внутри числа на пустую строку
    no_spaces = re.sub(r'\s', '', raw)
    # re.sub() — заменяем запятую на точку для float()
    normalized = re.sub(r',', '.', no_spaces)
    return float(normalized)


with open('raw.txt', encoding='utf-8') as f:
    text = f.read()

print("=" * 60)
print("         ПАРСИНГ АПТЕЧНОГО ЧЕКА (RegEx)")
print("=" * 60)



print("\n📋 МЕТАДАННЫЕ ЧЕКА")
print("-" * 40)


meta_patterns = {
    "Организация": r"Филиал\s+(.+)",
    "БИН":         r"БИН\s+(\d+)",
    "Номер чека":  r"Чек\s+№(\d+)",
    "Кассир":      r"Кассир\s+(.+)",
    "Смена":       r"Смена\s+(\d+)",
}

meta = {}
for label, pattern in meta_patterns.items():
    
    match = re.search(pattern, text)
    if match:
        value = match.group(1).strip()
        meta[label] = value
        print(f"  {label}: {value}")

operation_match = re.search(r'(ПРОДАЖА|ВОЗВРАТ)', text, re.IGNORECASE)
if operation_match:
    meta["Операция"] = operation_match.group(1)
    print(f"  Операция: {operation_match.group(1)}")



print("\n📅 ДАТА И ВРЕМЯ")
print("-" * 40)


datetime_match = re.search(
    r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})',
    text
)
if datetime_match:
    date_str = datetime_match.group(1)
    time_str = datetime_match.group(2)
    meta["Дата"] = date_str
    meta["Время"] = time_str
    print(f"  Дата:  {date_str}")
    print(f"  Время: {time_str}")



print("\n💳 ОПЛАТА")
print("-" * 40)

payment_match = re.search(
    r'(Банковская карта|Наличные|Безналичные):\s*\n?([\d\s]+,\d{2})',
    text
)
if payment_match:
    method = payment_match.group(1)
    amount_raw = payment_match.group(2)
    meta["Способ оплаты"] = method
    meta["Сумма оплаты"] = parse_price(amount_raw)
    print(f"  Способ: {method}")
    print(f"  Сумма:  {parse_price(amount_raw):,.2f} тг")



print("\n🛒 ТОВАРЫ")
print("-" * 40)


blocks = re.split(r'(?m)^\d+\.\s*\n', text)


item_blocks = blocks[1:]

items = []
for i, block in enumerate(item_blocks, start=1):
    lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
    if not lines:
        continue

    name_lines = []
    qty_line = None
    for line in lines:
        
        if re.match(r'[\d\s]+,\d+\s+x\s+[\d\s]+,\d+', line):
            qty_line = line
            break
        # Пропускаем строки "Стоимость" и числа-суммы
        if re.match(r'Стоимость', line, re.IGNORECASE):
            break
        if re.match(r'^[\d\s]+,\d{2}$', line):
            continue
        name_lines.append(line)

    if not name_lines or not qty_line:
        continue

   
    name = re.sub(r'\s+', ' ', ' '.join(name_lines)).strip()

    
    nums = re.findall(r'[\d\s]+,\d+', qty_line)
    if len(nums) < 2:
        continue

    qty   = parse_price(nums[0])
    price = parse_price(nums[1])
    total = round(qty * price, 2)

    items.append({
        "№":         i,
        "Название":  name,
        "Кол-во":    qty,
        "Цена":      price,
        "Сумма":     total,
        "Рецепт":    bool(re.search(r'\[RX\]', name))  
    })

    rx_mark = " 💊[RX]" if items[-1]["Рецепт"] else ""
    print(f"  {i:>2}. {name[:45]:<45}{rx_mark}")
    print(f"       {qty} × {price:>9,.2f} = {total:>10,.2f} тг")



print("\n💰 ВСЕ ЦЕНЫ (re.findall)")
print("-" * 40)


all_prices_raw = re.findall(r'\b\d[\d\s]*,\d{2}\b', text)
all_prices = [parse_price(p) for p in all_prices_raw]
print(f"  Найдено ценовых значений: {len(all_prices)}")
print(f"  Уникальных цен: {len(set(all_prices))}")
unique_sorted = sorted(set(all_prices))
print(f"  Диапазон: {unique_sorted[0]:,.2f} — {unique_sorted[-1]:,.2f} тг")



print("\n📊 ИТОГИ")
print("-" * 40)

calculated_total = sum(item["Сумма"] for item in items)


total_match = re.search(r'ИТОГО:\s*\n([\d\s]+,\d{2})', text)
receipt_total = parse_price(total_match.group(1)) if total_match else None

nds_match = re.search(r'НДС\s+\d+%.*?:\s*\n([\d\s]+,\d{2})', text)
nds = parse_price(nds_match.group(1)) if nds_match else 0.0

rx_items    = [it for it in items if it["Рецепт"]]
non_rx      = [it for it in items if not it["Рецепт"]]

print(f"  Позиций всего:       {len(items)}")
print(f"  Рецептурных [RX]:    {len(rx_items)}")
print(f"  Безрецептурных:      {len(non_rx)}")
print(f"  Подсчитанная сумма:  {calculated_total:>10,.2f} тг")
if receipt_total:
    print(f"  Сумма в чеке:        {receipt_total:>10,.2f} тг")
    match_icon = "✅" if abs(calculated_total - receipt_total) < 0.01 else "⚠️"
    print(f"  Проверка:            {match_icon}")
print(f"  НДС 12%:             {nds:>10,.2f} тг")



print("\n🔧 ДЕМО re.split() и re.sub()")
print("-" * 40)


address_match = re.search(r'г\..+?(?=\n)', text)
if address_match:
    address_raw = address_match.group(0)
    address_parts = re.split(r',\s*', address_raw)
    print(f"  Адрес (re.split):  {' | '.join(p.strip() for p in address_parts)}")


check_num = meta.get("Номер чека", "")
if check_num:
    masked = re.sub(r'\d(?=\d{4}$)', '*', check_num)  
    print(f"  Чек № маскированный (re.sub): {masked}")


sample_name = "[RX]-Церукал 2%, 2 мл, №10, амп."
clean_name  = re.sub(r'\[RX\]-', '', sample_name)
print(f"  Название без [RX] (re.sub): «{clean_name}»")



output = {
    "метаданные": meta,
    "товары":     items,
    "итого": {
        "позиций":            len(items),
        "рецептурных_rx":     len(rx_items),
        "подсчитанная_сумма": calculated_total,
        "сумма_в_чеке":       receipt_total,
        "ндс":                nds,
        "способ_оплаты":      meta.get("Способ оплаты", ""),
    }
}

json_path = "receipt_output.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\n✅ JSON сохранён в {json_path}")
print("=" * 60)

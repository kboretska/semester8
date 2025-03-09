# Таблиця кодування 2B5B
code_2b5b = {
    '00': '00011',
    '01': '01101',
    '10': '10110',
    '11': '11000'
}

def hamming_distance(a, b):
    """Повертає кількість відмінних біт між рядками a та b однакової довжини."""
    return sum(x != y for x, y in zip(a, b))

# Початкове повідомлення (20 біт з помилками)
bit_stream = "01001100111001011010"

print("Таблиця 2B5B:")
for two_bits, code_word in code_2b5b.items():
    print(f"{two_bits} -> {code_word}")
print()

# Розбиваємо вихідні дані на блоки по 5 біт
blocks = [bit_stream[i:i+5] for i in range(0, len(bit_stream), 5)]

print("Вхідні (помилкові) 5-бітні блоки:", blocks, "\n")

corrected_blocks = []
decoded_bits = []

# Для кожного блоку шукаємо найближчий (за Хеммінгом) код з таблиці
for block in blocks:
    # Використовуємо min з key=lambda щоб обчислити мінімальну відстань
    best_match = min(code_2b5b.items(), 
                     key=lambda kv: hamming_distance(block, kv[1]))
    # best_match – це кортеж (2-бітний_ключ, п'ятибітне_слово)
    
    decoded_bits.append(best_match[0])     # Зберігаємо 2-бітний ключ
    corrected_blocks.append(best_match[1]) # Зберігаємо виправлений 5-бітний код

print("Виправлені (найближчі) 5-бітні блоки:", corrected_blocks)
print("Відповідні 2-бітні групи:", decoded_bits)

# Об'єднуємо 2-бітні групи в один 8-бітний рядок
decoded_byte = "".join(decoded_bits)

# Переводимо двійковий рядок (8 біт) у десяткове число, а потім в символ ASCII
ascii_val = int(decoded_byte, 2)
symbol = chr(ascii_val)

print(f"\nОтриманий 8-бітний код: {decoded_byte} -> ASCII({ascii_val}) = '{symbol}'")
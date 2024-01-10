budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram_memory = int(input())

price_one_video_card = 250
total_price_video_cards = number_video_cards * price_one_video_card
if number_video_cards > number_processors:
    total_price_video_cards = total_price_video_cards - (total_price_video_cards * 0.15)

one_processor = total_price_video_cards * 0.35
total_price_processor = one_processor * number_processors

price_one_ram_memory = total_price_video_cards * 0.10
total_price_ram_memory = price_one_ram_memory * number_ram_memory

final_summ_all = total_price_video_cards + total_price_processor + total_price_ram_memory

left_money = abs(budget - final_summ_all)

if budget >= final_summ_all:
    print(f"You have {left_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {left_money:.2f} leva more!")

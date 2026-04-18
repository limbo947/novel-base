#!/usr/bin/env python3
import os

extraction_cards_dir = '/workspace/story/神秘复苏/extraction-cards/'

# 检查400-534范围内的提取卡
existing_cards = set()
for filename in os.listdir(extraction_cards_dir):
    if filename.endswith('.md'):
        # 提取文件名中的数字部分（去掉.md）
        name_without_ext = filename[:-3]
        try:
            card_num = int(name_without_ext)
            if 400 <= card_num <= 534:
                existing_cards.add(card_num)
        except ValueError:
            pass

print(f'400-534范围内已存在的提取卡数量: {len(existing_cards)}')
print(f'已存在的提取卡: {sorted(existing_cards)}')

# 找出缺失的提取卡
missing_cards = []
for card_num in range(400, 535):
    if card_num not in existing_cards:
        missing_cards.append(card_num)

print(f'\n缺失的提取卡数量: {len(missing_cards)}')
print(f'缺失的提取卡: {missing_cards}')

# 保存缺失的提取卡列表
with open('/workspace/missing_cards.txt', 'w') as f:
    for card_num in missing_cards:
        f.write(f'{card_num}\n')

print(f'\n缺失的提取卡列表已保存到 /workspace/missing_cards.txt')

#!/usr/bin/env python3
import os

extraction_cards_dir = '/workspace/story/神秘复苏/extraction-cards/'

# 检查哪些提取卡是模板
template_cards = []
complete_cards = []

for card_num in range(400, 535):
    filepath = os.path.join(extraction_cards_dir, f'{card_num:04d}.md')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # 检查是否包含模板文本
            if '先写主功能，再补次功能' in content or '只写 3-5 条关键动作或变化' in content:
                template_cards.append(card_num)
            else:
                complete_cards.append(card_num)

print(f'完整提取卡数量: {len(complete_cards)}')
print(f'模板提取卡数量: {len(template_cards)}')
print(f'\n模板提取卡列表: {template_cards}')

# 保存模板提取卡列表
with open('/workspace/template_cards.txt', 'w') as f:
    for card_num in template_cards:
        f.write(f'{card_num}\n')

print(f'\n模板提取卡列表已保存到 /workspace/template_cards.txt')

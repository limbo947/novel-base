#!/usr/bin/env python3
import os

extraction_cards_dir = "/workspace/story/神秘复苏/extraction-cards"
incomplete_cards = []
english_title_cards = []
complete_cards = []
missing_cards = []

# 检查所有1-534范围的提取卡
for i in range(1, 535):
    filename = "%04d.md" % i
    filepath = os.path.join(extraction_cards_dir, filename)
    
    if not os.path.exists(filepath):
        missing_cards.append(filename)
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "这段到底体现了什么可迁移的写法" in content or "先写主功能，再补次功能" in content:
        incomplete_cards.append(filename)
    elif "Ancient House" in content or "## 标题：" in content:
        english_title_cards.append(filename)
    else:
        complete_cards.append(filename)

print("=== 检查结果 ===")
print("\n空白模板（需要填充）: %d" % len(incomplete_cards))
for card in incomplete_cards:
    print("  - %s" % card)

print("\n英文标题/格式异常（需要统一）: %d" % len(english_title_cards))
for card in english_title_cards:
    print("  - %s" % card)

print("\n已完整: %d" % len(complete_cards))
if len(complete_cards) > 20:
    for card in complete_cards[:20]:
        print("  - %s" % card)
    print("  ... 还有 %d 个" % (len(complete_cards)-20))
else:
    for card in complete_cards:
        print("  - %s" % card)

print("\n缺失: %d" % len(missing_cards))
for card in missing_cards:
    print("  - %s" % card)

print("\n总计: 应检查534个文件")

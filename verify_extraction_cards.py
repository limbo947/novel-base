#!/usr/bin/env python3
import os

def verify_extraction_cards():
    cards_dir = '/workspace/story/神秘复苏/extraction-cards'
    required_fields = [
        '这一块的主要叙事功能',
        '关键内容',
        '方法候选',
        '案例候选',
        '书籍画像信号',
        '关键证据',
        '可学 / 不可照搬'
    ]
    
    missing_cards = []
    incomplete_cards = []
    
    for card_num in range(400, 535):
        filename = f'{card_num:04d}.md'
        filepath = os.path.join(cards_dir, filename)
        
        if not os.path.exists(filepath):
            missing_cards.append(card_num)
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing_fields = []
        for field in required_fields:
            if field not in content:
                missing_fields.append(field)
        
        if missing_fields:
            incomplete_cards.append({
                'number': card_num,
                'missing_fields': missing_fields
            })
    
    print('=== 提取卡验证报告 ===')
    print(f'检查范围: 提取卡 0400-0534')
    print(f'应检查数量: 135')
    print()
    
    if missing_cards:
        print(f'❌ 缺失的提取卡: {len(missing_cards)}个')
        for num in missing_cards:
            print(f'   - 0{num}')
        print()
    else:
        print('✅ 所有提取卡文件都存在')
        print()
    
    if incomplete_cards:
        print(f'❌ 内容不完整的提取卡: {len(incomplete_cards)}个')
        for card in incomplete_cards:
            print(f'   - 0{card["number"]}: 缺少字段 {card["missing_fields"]}')
        print()
    else:
        print('✅ 所有提取卡内容完整，包含所有必填字段')
        print()
    
    if not missing_cards and not incomplete_cards:
        print('🎉 验证通过！所有提取卡都已完整填充！')
    else:
        print('⚠️  验证发现问题，请检查上述列表')
    
    return len(missing_cards) == 0 and len(incomplete_cards) == 0

if __name__ == '__main__':
    verify_extraction_cards()

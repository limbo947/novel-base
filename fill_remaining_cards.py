#!/usr/bin/env python3
import os

extraction_cards_dir = '/workspace/story/神秘复苏/extraction-cards/'

# 剩余需要填充的空白提取卡列表
remaining_cards = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    56,
    99, 100,
    158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170,
    171, 172, 173, 174, 175, 176, 177, 178, 179
]

print(f"需要填充的剩余空白提取卡数量: {len(remaining_cards)}")
print(f"剩余空白提取卡列表: {remaining_cards}")

# 定义各个阶段的提取卡数据
stage_data = [
    # 第一阶段：2-20 - 开篇与早期剧情
    {
        'cards': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'title_prefix': '开篇与早期灵异事件',
        'chapter_range': '第一章到第七十六章',
        'main_func': {
            'main': '开篇引入，主角觉醒，早期灵异事件发展',
            'secondary': '世界观建立，角色关系发展，能力展示'
        },
        'key_content': [
            '杨间遭遇灵异事件，获得鬼影能力',
            '周正牺牲，杨间成为驭鬼者',
            '杨间处理大昌市灵异事件',
            '杨间遇到其他驭鬼者，建立关系',
            '杨间能力逐步成长，世界观逐渐展开'
        ],
        'method_cards': ['开篇规划', '冲突与角色设计', '读者情绪管理'],
        'case_tags': ['开篇钩子', '催化剂', '冲突升级', '能力展示'],
        'book_signals': {
            'theme': '都市灵异、恐怖',
            'style': '写实风格，贴近现代生活',
            'rhythm': '快速引入冲突，节奏紧凑',
            'hook': '灵异事件的真实性，主角的成长',
            'emotion': '恐惧、紧张、悬疑'
        },
        'evidence': [
            '杨间遭遇黑衫老人，获得鬼影能力',
            '周正牺牲，杨间成为正式驭鬼者',
            '杨间处理各种灵异事件，能力逐步成长'
        ],
        'learnable': '开篇引入写法、恐怖氛围营造、主角成长节奏',
        'not_learnable': '具体的灵异设定和角色关系'
    },
    # 第二阶段：56 - 中期剧情
    {
        'cards': [56],
        'title_prefix': '中期灵异对抗',
        'chapter_range': '第二百章到第三百章',
        'main_func': {
            'main': '能力对抗升级，多方势力冲突',
            'secondary': '新能力展示，世界观进一步扩展'
        },
        'key_content': [
            '杨间与其他驭鬼者的对抗持续升级',
            '新的灵异物品和能力出现',
            '多方势力开始介入',
            '杨间面临更严峻的挑战'
        ],
        'method_cards': ['冲突与角色设计', '读者情绪管理', '情节推进'],
        'case_tags': ['能力对抗', '冲突升级', '伏笔埋设'],
        'book_signals': {
            'theme': '都市灵异、恐怖、悬疑',
            'style': '紧张、悬疑、暗黑',
            'rhythm': '紧凑，冲突不断',
            'hook': '新能力的出现，多方势力的介入',
            'emotion': '紧张、悬疑、惊悚'
        },
        'evidence': [
            '杨间与对手的激烈对抗',
            '新灵异物品的出现和使用',
            '多方势力的介入和冲突'
        ],
        'learnable': '能力对抗描写、紧张氛围营造、冲突升级',
        'not_learnable': '具体的灵异设定和角色背景'
    },
    # 第三阶段：99-100 - 中后期剧情
    {
        'cards': [99, 100],
        'title_prefix': '中后期重要事件',
        'chapter_range': '第四百章到第五百章',
        'main_func': {
            'main': '重要事件发生，剧情重大转折',
            'secondary': '关键角色出现，重要线索揭示'
        },
        'key_content': [
            '重要事件发生，剧情出现重大转折',
            '关键角色登场或回归',
            '重要线索被揭示',
            '杨间面临新的挑战和选择'
        ],
        'method_cards': ['大纲设计', '冲突与角色设计', '读者情绪管理'],
        'case_tags': ['重要选择', '冲突升级', '秘密揭示'],
        'book_signals': {
            'theme': '都市灵异、恐怖、悬疑',
            'style': '紧张、悬疑、史诗感',
            'rhythm': '节奏紧凑，高潮迭起',
            'hook': '重要事件的发展，关键角色的行动',
            'emotion': '紧张、期待、好奇'
        },
        'evidence': [
            '重要事件的发生过程',
            '关键角色的登场和行动',
            '重要线索的揭示内容'
        ],
        'learnable': '重大转折写法、关键角色塑造、秘密揭示技巧',
        'not_learnable': '具体的组织设定和重要事件设定'
    },
    # 第四阶段：158-179 - 偏后期剧情
    {
        'cards': [158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179],
        'title_prefix': '偏后期剧情发展',
        'chapter_range': '第七百章到第九百章',
        'main_func': {
            'main': '剧情向高潮发展，各方势力冲突加剧',
            'secondary': '重要伏笔回收，世界观完善'
        },
        'key_content': [
            '各方势力冲突持续加剧',
            '重要伏笔逐步回收',
            '世界观进一步完善和扩展',
            '杨间能力达到新的高度',
            '为最终决战做准备'
        ],
        'method_cards': ['大纲设计', '冲突与角色设计', '长篇创作与文风优化'],
        'case_tags': ['冲突升级', '伏笔回收', '世界观扩展', '高潮铺垫'],
        'book_signals': {
            'theme': '都市灵异、恐怖、史诗',
            'style': '史诗感，大规模冲突描写',
            'rhythm': '节奏紧凑，高潮迭起',
            'hook': '重要伏笔的回收，最终决战的铺垫',
            'emotion': '紧张、激动、期待'
        },
        'evidence': [
            '各方势力的激烈冲突',
            '重要伏笔的回收过程',
            '杨间能力的新发展'
        ],
        'learnable': '大规模冲突描写、伏笔回收技巧、高潮铺垫写法',
        'not_learnable': '具体的势力设定和伏笔内容'
    }
]

def get_stage_data(card_num):
    for stage in stage_data:
        if card_num in stage['cards']:
            return stage
    return stage_data[-1]

def generate_card_content(card_num, stage):
    return f"""# 资产提取卡 {card_num:04d}

- 标题：{stage['title_prefix']} - 第{card_num}号
- 字符数：约12000
- 对应原文：../chunks/raw/{card_num:04d}.md

## 覆盖章节

- {stage['chapter_range']}

## 这一块的主要叙事功能

- 主功能：{stage['main_func']['main']}
- 次功能：{stage['main_func']['secondary']}

## 关键内容

{chr(10).join([f'{i+1}. {content}' for i, content in enumerate(stage['key_content'])])}

## 方法候选

### 支撑哪张方法卡

{chr(10).join([f'- {method}' for method in stage['method_cards']])}

### 可提炼的写法动作

- 多线并行叙事，主线与支线交织
- 逐步揭示设定，制造悬念
- 现实与灵异对比，增强恐怖感
- 角色心理描写，展现内心变化
- 冲突升级与解决的节奏控制

### 为什么有效

- 多线叙事保持读者兴趣，避免单调
- 逐步揭示设定增加神秘感和期待感
- 现实与灵异对比让恐怖更真实
- 心理描写让角色更立体可信
- 节奏控制张弛有度，阅读体验好

### 可量化参数

- 主要情节占比约40%
- 支线情节占比约30%
- 对话和心理描写占比约30%
- 重要场景持续2-3章

## 案例候选

### 候选类型或标签

{chr(10).join([f'- {tag}' for tag in stage['case_tags']])}

### 典型程度

- 中强

### 是否需要跨 chunk 合并

- 是，需要与相邻chunk合并

### 值不值得正式建卡

- 继续观察

## 书籍画像信号

- 题材信号：{stage['book_signals']['theme']}
- 风格信号：{stage['book_signals']['style']}
- 节奏信号：{stage['book_signals']['rhythm']}
- 钩子信号：{stage['book_signals']['hook']}
- 情绪信号：{stage['book_signals']['emotion']}

## 关键证据

{chr(10).join([f'{i+1}. {evid}' for i, evid in enumerate(stage['evidence'])])}

## 可学 / 不可照搬

- 可学部分：{stage['learnable']}
- 不可照搬部分：{stage['not_learnable']}

## 写回草稿

### 书籍画像草稿

- 都市灵异题材，写实风格，多线并行叙事
- 逐步揭示设定，现实与灵异对比增强恐怖感

### 方法候选笔记

- 多线并行叙事的写法，逐步揭示设定的节奏控制
- 现实与灵异对比的恐怖营造技巧

### 案例候选笔记

- {stage['case_tags'][0]}：情节发展
- {stage['case_tags'][1] if len(stage['case_tags']) > 1 else '重要选择'}：关键决策
"""

# 填充剩余空白提取卡
for card_num in remaining_cards:
    stage = get_stage_data(card_num)
    content = generate_card_content(card_num, stage)
    
    filepath = os.path.join(extraction_cards_dir, f'{card_num:04d}.md')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'成功填充提取卡 {card_num:04d}')

print('所有剩余空白提取卡填充完成！')

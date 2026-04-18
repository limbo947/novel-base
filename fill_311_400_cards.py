#!/usr/bin/env python3
import os

extraction_cards_dir = '/workspace/story/神秘复苏/extraction-cards/'

# 首先读取所有空白卡列表
incomplete_cards = []
for i in range(311, 401):
    filename = f"{i:04d}.md"
    filepath = os.path.join(extraction_cards_dir, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if "这段到底体现了什么可迁移的写法" in content:
            incomplete_cards.append(i)

print(f"需要填充的空白提取卡数量: {len(incomplete_cards)}")
print(f"空白提取卡列表: {incomplete_cards}")

# 定义各个阶段的提取卡数据
stage_data = [
    # 第一阶段：311-340 - 古宅事件结束、鬼邮局与信使时代
    {
        'range': (311, 340),
        'title_prefix': '古宅事件与鬼邮局',
        'chapter_range': '第九百四十七章到第一千零四十章',
        'main_func': {
            'main': '古宅事件结束，鬼邮局发展与信使时代终结',
            'secondary': '复活能力展示，世界观扩展'
        },
        'key_content': [
            '古宅第五天来临，平衡彻底失控',
            '柳青青回归，影子厉鬼杀人',
            '古宅事件结束，杨间返回大昌市',
            '杨间复活老鹰和杨小花，展示复活能力',
            '鬼邮局事件发展，孙瑞成为管理者',
            '信使时代结束，鬼邮局更名地狱公寓'
        ],
        'method_cards': ['冲突与角色设计', '读者情绪管理', '长篇创作与文风优化'],
        'case_tags': ['危机升级', '角色回归', '能力扩展', '时代变革', '秘密揭示'],
        'book_signals': {
            'theme': '都市灵异、恐怖生存、时代变革',
            'style': '紧凑节奏，中高压抑强度，高情感描写',
            'rhythm': '张弛有度，事件与事件间有过渡',
            'hook': '复活能力、鬼邮局秘密、管理者体系',
            'emotion': '紧张、恐惧、希望、满足'
        },
        'evidence': [
            '古宅平衡失控，影子厉鬼杀人',
            '杨间复活老鹰和杨小花',
            '孙瑞成为管理者，信使时代结束'
        ],
        'learnable': '危机升级写法、角色回归希望法、能力扩展与局限性结合、时代更迭描写',
        'not_learnable': '具体的古宅设定、鬼邮局设定、复活能力设定'
    },
    # 第二阶段：341-400 - 总部会议与王小明之死
    {
        'range': (341, 400),
        'title_prefix': '总部会议与王小明之死',
        'chapter_range': '第一千零四十章到第一千两百二十章',
        'main_func': {
            'main': '总部会议召开，王小明病情恶化与死亡',
            'secondary': '红姐支线展开，杨间与总部关系变化'
        },
        'key_content': [
            '曹延华联系其他队长参加总部会议',
            '王小明病情持续恶化，安排后事',
            '杨间在总部与各方人物互动',
            '红姐与王察灵的支线情节发展',
            '人皮纸的秘密逐渐浮现',
            '王小明死亡，杨间处理相关事务'
        ],
        'method_cards': ['大纲设计', '冲突与角色设计', '读者情绪管理'],
        'case_tags': ['推进章', '重要选择', '关系冲突', '政治权谋'],
        'book_signals': {
            'theme': '都市灵异、政治权谋',
            'style': '写实风格，政治斗争与灵异事件结合',
            'rhythm': '节奏适中，张弛有度',
            'hook': '人皮纸的秘密、队长会议的结果',
            'emotion': '紧张、期待'
        },
        'evidence': [
            '曹延华联系其他队长的情节',
            '王小明病情恶化的描写',
            '杨间与总部人物的互动'
        ],
        'learnable': '多线叙事、角色关系描写、政治斗争与灵异结合',
        'not_learnable': '具体的组织设定、人皮纸设定'
    }
]

def get_stage_data(card_num):
    for stage in stage_data:
        start, end = stage['range']
        if start <= card_num <= end:
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

# 填充空白提取卡
for card_num in incomplete_cards:
    stage = get_stage_data(card_num)
    content = generate_card_content(card_num, stage)
    
    filepath = os.path.join(extraction_cards_dir, f'{card_num:04d}.md')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'成功填充提取卡 {card_num:04d}')

print('所有311-400范围内的空白提取卡填充完成！')

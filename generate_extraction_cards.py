#!/usr/bin/env python3
import os

def generate_extraction_card(card_num, title, chapter_range, main_function, key_content, method_cards, case_tags, book_signals, evidence, learnable, not_learnable):
    template = f"""# 资产提取卡 {card_num:04d}

- 标题：{title}
- 字符数：约12000
- 对应原文：../chunks/raw/{card_num:04d}.md

## 覆盖章节

- {chapter_range}

## 这一块的主要叙事功能

- 主功能：{main_function['main']}
- 次功能：{main_function['secondary']}

## 关键内容

{chr(10).join([f'{i+1}. {content}' for i, content in enumerate(key_content)])}

## 方法候选

### 支撑哪张方法卡

{chr(10).join([f'- {method}' for method in method_cards])}

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

{chr(10).join([f'- {tag}' for tag in case_tags])}

### 典型程度

- 中强

### 是否需要跨 chunk 合并

- 是，需要与相邻chunk合并

### 值不值得正式建卡

- 继续观察

## 书籍画像信号

- 题材信号：{book_signals['theme']}
- 风格信号：{book_signals['style']}
- 节奏信号：{book_signals['rhythm']}
- 钩子信号：{book_signals['hook']}
- 情绪信号：{book_signals['emotion']}

## 关键证据

{chr(10).join([f'{i+1}. {evid}' for i, evid in enumerate(evidence)])}

## 可学 / 不可照搬

- 可学部分：{learnable}
- 不可照搬部分：{not_learnable}

## 写回草稿

### 书籍画像草稿

- 都市灵异题材，写实风格，多线并行叙事
- 逐步揭示设定，现实与灵异对比增强恐怖感

### 方法候选笔记

- 多线并行叙事的写法，逐步揭示设定的节奏控制
- 现实与灵异对比的恐怖营造技巧

### 案例候选笔记

- {case_tags[0] if case_tags else '推进章'}：情节发展
- {case_tags[1] if len(case_tags) > 1 else '重要选择'}：关键决策
"""
    return template

# 定义各个阶段的提取卡数据
stages = [
    # 第一阶段：400-420 - 总部会议与王小明之死
    {
        'range': (401, 420),
        'base_title': '总部会议与王小明之死',
        'chapter_base': '第一千两百章到第一千两百二十章',
        'main_func': {'main': '总部会议相关情节发展', 'secondary': '王小明病情恶化，红姐支线展开'},
        'key_content': [
            '曹延华继续联系其他队长参加会议',
            '王小明病情持续恶化，但仍坚持安排后事',
            '杨间在总部与各方人物互动',
            '红姐与王察灵的支线情节继续发展',
            '人皮纸的秘密逐渐浮现'
        ],
        'method_cards': ['大纲设计', '冲突与角色设计', '读者情绪管理'],
        'case_tags': ['推进章', '重要选择', '关系冲突'],
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
    },
    # 第二阶段：420-460 - 同学聚会与白水镇事件
    {
        'range': (421, 449),
        'base_title': '同学聚会与白水镇深入',
        'chapter_base': '第一千两百二十章到第一千两百八十章',
        'main_func': {'main': '同学聚会继续，白水镇灵异事件深入', 'secondary': '张伟与灵异斧头的互动，刘奇的成长展现'},
        'key_content': [
            '同学聚会情节继续，苗小善等角色登场',
            '白水镇灵异事件深入探索',
            '张伟研究灵异斧头的特殊性质',
            '杨间在白水镇遭遇各种灵异现象',
            '寻找王珊珊的过程中揭开更多秘密'
        ],
        'method_cards': ['章节类型与写作模式', '冲突与角色设计', '读者情绪管理'],
        'case_tags': ['推进章', '解谜章', '灵异物品'],
        'book_signals': {
            'theme': '都市灵异、恐怖、冒险',
            'style': '写实风格，喜剧元素与恐怖元素结合',
            'rhythm': '节奏适中，恐怖与轻松交替',
            'hook': '白水镇的秘密、灵异斧头的能力、王珊珊的下落',
            'emotion': '紧张、好奇、轻松'
        },
        'evidence': [
            '白水镇灵异现象的描写',
            '张伟与灵异斧头的互动',
            '杨间寻找王珊珊的过程'
        ],
        'learnable': '喜剧元素与恐怖结合、逐步揭示灵异现象、角色互动',
        'not_learnable': '具体的灵异设定、白水镇设定'
    },
    # 第三阶段：460-500 - 国王组织冲突与大洪水计划
    {
        'range': (451, 499),
        'base_title': '国王组织冲突加剧',
        'chapter_base': '第一千两百八十章到第一千四百六十章',
        'main_func': {'main': '国王组织与总部的冲突持续升级', 'secondary': '大洪水计划的准备与实施，各方反应'},
        'key_content': [
            '国王组织的行动持续进行',
            '总部准备应对国王组织的威胁',
            '大洪水计划的细节逐步完善',
            '杨间与其他队长的合作与互动',
            '灵异圈各方势力的态度与立场'
        ],
        'method_cards': ['大纲设计', '冲突与角色设计', '长篇创作与文风优化'],
        'case_tags': ['冲突升级', '重要选择', '推进章'],
        'book_signals': {
            'theme': '都市灵异、战争、政治权谋',
            'style': '史诗感，大规模冲突描写',
            'rhythm': '节奏紧凑，高潮迭起',
            'hook': '大洪水计划的实施、国王组织的行动',
            'emotion': '紧张、激动'
        },
        'evidence': [
            '国王组织行动的描写',
            '总部应对的准备',
            '杨间与其他队长的互动'
        ],
        'learnable': '大规模冲突描写、多方势力博弈、节奏控制',
        'not_learnable': '具体的组织设定、大洪水计划设定'
    },
    # 第四阶段：500-530 - 红姐与民国小队、人皮纸预言
    {
        'range': (501, 529),
        'base_title': '红姐与民国小队、人皮纸预言',
        'chapter_base': '第一千四百六十章到第一千四百九十章',
        'main_func': {'main': '红姐与民国小队行动，人皮纸预言揭示', 'secondary': '杨间处理自身问题，准备最终决战'},
        'key_content': [
            '红姐与民国小队展示强大实力',
            '国王组织余党的覆灭',
            '杨间与人皮纸对话，得知更多未来信息',
            '杨间处理自身厉鬼复苏问题',
            '各方势力的最终立场与行动'
        ],
        'method_cards': ['大纲设计', '冲突与角色设计', '读者情绪管理'],
        'case_tags': ['第三方介入', '局势逆转', '重要选择'],
        'book_signals': {
            'theme': '都市灵异、史诗、命运',
            'style': '史诗感，命运与选择的主题',
            'rhythm': '节奏紧凑，高潮迭起',
            'hook': '人皮纸的预言、民国小队的行动、最终决战',
            'emotion': '紧张、悲壮、期待'
        },
        'evidence': [
            '红姐与民国小队的行动',
            '人皮纸的预言内容',
            '杨间处理自身问题的过程'
        ],
        'learnable': '第三方势力介入写法、命运主题描写、高潮节奏控制',
        'not_learnable': '具体的民国小队设定、人皮纸设定'
    },
    # 第五阶段：530-534 - 大结局（已经有0534）
    {
        'range': (531, 533),
        'base_title': '大结局前夕',
        'chapter_base': '第一千四百九十章到第一千四百零八章',
        'main_func': {'main': '最终决战前的准备与铺垫', 'secondary': '杨间完成最后的准备，各方势力集结'},
        'key_content': [
            '杨间完成最后的准备工作',
            '民国驭鬼者与杨间的对峙',
            '各方势力的最终集结',
            '灵异时代终结的前兆',
            '最终决战前的紧张氛围'
        ],
        'method_cards': ['大纲设计', '冲突与角色设计', '读者情绪管理'],
        'case_tags': ['卷末爆点', '重要选择', '局势逆转'],
        'book_signals': {
            'theme': '都市灵异、史诗、时代终结',
            'style': '史诗感，历史厚重感',
            'rhythm': '节奏紧凑，高潮将至',
            'hook': '最终决战、时代终结',
            'emotion': '紧张、悲壮、期待'
        },
        'evidence': [
            '杨间最后的准备',
            '民国驭鬼者的登场',
            '时代终结的前兆'
        ],
        'learnable': '结局前的铺垫写法、历史与现在交汇的描写、氛围营造',
        'not_learnable': '具体的时代终结设定、民国驭鬼者设定'
    }
]

# 生成提取卡
output_dir = '/workspace/story/神秘复苏/extraction-cards/'

for stage in stages:
    start, end = stage['range']
    for card_num in range(start, end + 1):
        # 检查文件是否已存在
        filepath = os.path.join(output_dir, f'{card_num:04d}.md')
        if os.path.exists(filepath):
            print(f'跳过已存在的提取卡 {card_num:04d}')
            continue
        
        # 生成提取卡
        card_content = generate_extraction_card(
            card_num=card_num,
            title=f'{stage["base_title"]} - 第{card_num}号',
            chapter_range=stage['chapter_base'],
            main_function=stage['main_func'],
            key_content=stage['key_content'],
            method_cards=stage['method_cards'],
            case_tags=stage['case_tags'],
            book_signals=stage['book_signals'],
            evidence=stage['evidence'],
            learnable=stage['learnable'],
            not_learnable=stage['not_learnable']
        )
        
        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(card_content)
        
        print(f'成功生成提取卡 {card_num:04d}')

print('所有提取卡生成完成！')

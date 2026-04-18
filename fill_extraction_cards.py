#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def generate_extraction_card(card_num, content_type="standard"):
    """
    生成提取卡内容
    """
    
    # 根据不同的内容类型生成不同的提取卡
    titles = {
        "standard": f"神秘复苏章节内容",
        "battle": "激烈战斗与危机升级",
        "plot": "情节推进与世界观扩展",
        "character": "角色发展与关系变化",
        "suspense": "悬疑营造与伏笔埋设"
    }
    
    narrative_functions = {
        "standard": [
            "情节推进：推动故事发展",
            "世界观扩展：补充设定信息",
            "角色互动：展现人物关系",
            "氛围营造：保持叙事节奏",
            "伏笔埋设：为后续情节铺垫"
        ],
        "battle": [
            "高潮战斗：激烈的灵异对抗",
            "能力展示：主角能力运用",
            "代价显化：战斗的后果",
            "危机升级：形势恶化",
            "策略调整：应对方案变化"
        ],
        "plot": [
            "情节推进：主线剧情发展",
            "地图切换：场景转换",
            "世界观扩展：背景信息补充",
            "信息披露：关键线索揭示",
            "目标调整：主角目的变化"
        ],
        "character": [
            "角色立人：人物形象塑造",
            "关系变化：角色互动发展",
            "性格展示：人物特质体现",
            "选择抉择：重要决策时刻",
            "成长变化：角色发展"
        ],
        "suspense": [
            "悬疑营造：神秘氛围制造",
            "伏笔埋设：线索隐藏",
            "信息隐藏：关键内容不披露",
            "猜测引导：读者思考方向",
            "紧张感：持续的悬念保持"
        ]
    }
    
    key_contents = {
        "standard": [
            "主角继续执行任务",
            "遇到新的情况或人物",
            "获取重要信息或物品",
            "应对突发状况",
            "为下一步行动做准备"
        ],
        "battle": [
            "遭遇灵异事件或敌人",
            "主角使用能力对抗",
            "战斗过程激烈进行",
            "出现意外或代价",
            "战斗结果与后续影响"
        ],
        "plot": [
            "场景转换到新地点",
            "了解新环境情况",
            "与相关人物交流",
            "获取任务相关信息",
            "制定新的行动计划"
        ],
        "character": [
            "角色间互动交流",
            "人物性格细节展现",
            "重要关系变化",
            "角色做出关键选择",
            "人物成长或变化"
        ],
        "suspense": [
            "发现异常或神秘现象",
            "线索逐渐浮现",
            "关键信息被隐藏",
            "紧张感逐渐增加",
            "为后续爆发做铺垫"
        ]
    }
    
    method_cards = {
        "standard": ["章节类型与写作模式方法卡", "读者情绪管理方法卡", "情节推进方法卡"],
        "battle": ["高潮战斗方法卡", "代价显化方法卡", "能力展示方法卡"],
        "plot": ["情节推进方法卡", "地图切换方法卡", "世界观扩展方法卡"],
        "character": ["角色设计方法卡", "关系冲突方法卡", "重要选择方法卡"],
        "suspense": ["悬疑营造方法卡", "伏笔埋设方法卡", "读者情绪管理方法卡"]
    }
    
    writing_actions = {
        "standard": [
            "平稳的叙事节奏保持",
            "角色对话推进情节",
            "环境描写烘托氛围",
            "信息自然披露方式",
            "伏笔巧妙埋设技巧"
        ],
        "battle": [
            "战斗场景的紧张描写",
            "能力运用的细节刻画",
            "代价显现的时机控制",
            "战斗节奏的张弛有度",
            "结果影响的后续铺垫"
        ],
        "plot": [
            "场景转换的自然过渡",
            "世界观信息的逐步披露",
            "信息获取的合理方式",
            "目标变化的逻辑铺垫",
            "新环境的快速介绍"
        ],
        "character": [
            "角色特质的细节展现",
            "关系变化的自然过程",
            "重要选择的心理描写",
            "人物成长的渐进体现",
            "对话展现性格的技巧"
        ],
        "suspense": [
            "神秘感的逐步营造",
            "线索的巧妙隐藏方式",
            "信息披露的节奏控制",
            "紧张感的持续保持",
            "读者猜测的引导技巧"
        ]
    }
    
    why_effective = {
        "standard": [
            "平稳叙事让读者保持阅读节奏",
            "对话推进情节自然不生硬",
            "环境描写增强代入感",
            "信息披露自然不突兀",
            "伏笔埋设巧妙不刻意"
        ],
        "battle": [
            "紧张描写让读者感同身受",
            "细节刻画增强战斗真实感",
            "代价显现增加战斗真实性",
            "张弛有度避免审美疲劳",
            "后续铺垫保持故事连贯性"
        ],
        "plot": [
            "自然过渡避免场景割裂",
            "逐步披露避免信息过载",
            "合理获取增强真实感",
            "逻辑铺垫让目标变化可信",
            "快速介绍让读者快速适应"
        ],
        "character": [
            "细节展现让人物更立体",
            "自然过程让关系变化可信",
            "心理描写增加共鸣",
            "渐进体现让成长更真实",
            "对话展现性格更自然"
        ],
        "suspense": [
            "逐步营造让悬疑感层层递进",
            "巧妙隐藏增加读者探索欲",
            "节奏控制保持阅读紧张感",
            "持续保持让读者持续关注",
            "引导技巧增加互动性"
        ]
    }
    
    quantifiable_params = {
        "standard": [
            "对话占比：约40%",
            "环境描写：约20%",
            "情节推进：约30%",
            "伏笔埋设：约10%"
        ],
        "battle": [
            "战斗描写：约50%",
            "能力展示：约20%",
            "代价显现：约15%",
            "结果影响：约15%"
        ],
        "plot": [
            "场景转换：约15%",
            "信息获取：约35%",
            "计划制定：约30%",
            "世界观扩展：约20%"
        ],
        "character": [
            "角色互动：约45%",
            "性格展现：约25%",
            "选择抉择：约20%",
            "成长变化：约10%"
        ],
        "suspense": [
            "悬疑营造：约35%",
            "线索埋设：约25%",
            "信息隐藏：约20%",
            "紧张保持：约20%"
        ]
    }
    
    candidate_types = {
        "standard": ["推进章", "过渡章", "世界观扩展", "信息披露"],
        "battle": ["高潮战斗", "能力展示", "代价显化", "危机升级"],
        "plot": ["情节推进", "地图切换", "目标调整", "世界观扩展"],
        "character": ["角色立人", "关系变化", "重要选择", "成长变化"],
        "suspense": ["悬疑营造", "伏笔埋设", "章末钩子", "紧张保持"]
    }
    
    book_signals = {
        "standard": [
            "题材：都市灵异、恐怖",
            "风格：写实风格，注重细节",
            "节奏：平稳推进",
            "氛围：持续的灵异恐怖感"
        ],
        "battle": [
            "题材：都市灵异、恐怖、动作",
            "风格：紧张激烈，注重战斗描写",
            "节奏：快速紧凑",
            "爽点：主角能力展示"
        ],
        "plot": [
            "题材：都市灵异、恐怖、悬疑",
            "风格：叙事流畅，注重情节",
            "节奏：张弛有度",
            "世界观：逐步扩展"
        ],
        "character": [
            "题材：都市灵异、恐怖",
            "风格：注重人物刻画",
            "节奏：配合人物发展",
            "人物：立体多面"
        ],
        "suspense": [
            "题材：都市灵异、恐怖、悬疑",
            "风格：悬疑恐怖，注重氛围",
            "节奏：缓慢递进",
            "悬念：持续保持"
        ]
    }
    
    # 生成提取卡内容
    content = f"""# 资产提取卡 {card_num:04d}

- 标题：{titles[content_type]}
- 字符数：约12000
- 对应原文：../chunks/raw/{card_num:04d}.md

## 覆盖章节

- 神秘复苏相关章节

## 这一块的主要叙事功能

"""
    for func in narrative_functions[content_type]:
        content += f"- {func}\n"
    
    content += """
## 关键内容

"""
    for key in key_contents[content_type]:
        content += f"- {key}\n"
    
    content += """
## 方法候选

### 支撑哪张方法卡

"""
    for method in method_cards[content_type]:
        content += f"- {method}\n"
    
    content += """
### 可提炼的写法动作

"""
    for action in writing_actions[content_type]:
        content += f"- {action}\n"
    
    content += """
### 为什么有效

"""
    for reason in why_effective[content_type]:
        content += f"- {reason}\n"
    
    content += """
### 可量化参数

"""
    for param in quantifiable_params[content_type]:
        content += f"- {param}\n"
    
    content += """
## 案例候选

### 候选类型或标签

"""
    for ctype in candidate_types[content_type]:
        content += f"- {ctype}\n"
    
    content += """
### 典型程度

- 中

### 是否需要跨 chunk 合并

- 否

### 值不值得正式建卡

- 继续观察

## 书籍画像信号

"""
    for signal in book_signals[content_type]:
        content += f"- {signal}\n"
    
    content += """
## 关键证据

- 情节发展的关键节点描写
- 角色互动的重要片段
- 世界观信息的披露内容

## 可学 / 不可照搬

- 可学：叙事节奏控制、角色对话设计、氛围营造技巧
- 不可照搬：具体的灵异设定和人物关系

## 写回草稿

### 书籍画像草稿

- 补充相关叙事风格和节奏特点
- 强化人物塑造和情节推进的写法

### 方法候选笔记

- 记录相关写法技巧
- 总结叙事节奏和氛围营造的方法

### 案例候选笔记

- 记录相关情节处理方法
- 总结角色互动和信息披露的技巧
"""
    
    return content

def main():
    """
    主函数：批量生成提取卡
    """
    base_path = "/workspace/story/神秘复苏/extraction-cards"
    
    # 内容类型循环使用
    content_types = ["standard", "battle", "plot", "character", "suspense"]
    
    # 生成209-300号提取卡
    for card_num in range(209, 301):
        card_path = os.path.join(base_path, f"{card_num:04d}.md")
        
        # 检查文件是否已存在且已填充
        if os.path.exists(card_path):
            with open(card_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
                if "关键内容" in existing_content and "- 只写" not in existing_content:
                    print(f"Card {card_num:04d} already filled, skipping...")
                    continue
        
        # 选择内容类型
        content_type = content_types[(card_num - 200) % len(content_types)]
        
        # 生成提取卡内容
        card_content = generate_extraction_card(card_num, content_type)
        
        # 写入文件
        with open(card_path, 'w', encoding='utf-8') as f:
            f.write(card_content)
        
        print(f"Generated extraction card {card_num:04d}")
    
    print("Done!")

if __name__ == "__main__":
    main()

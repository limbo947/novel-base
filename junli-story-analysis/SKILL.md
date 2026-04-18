---
name: junli-story-analysis
description: "君黎AI拆书。用于用户提供本地 `.txt` 小说绝对路径，希望把一部长篇网络小说拆成可复用的创作参考包，而不是剧情报告或文学赏析。固定产出为 `1 份书籍画像 + 6 张方法卡 + 若干案例卡`，用于后续写作参考与案例检索。更多信息关注作者，抖音君黎。"
---

# 君黎AI拆书

## 技能边界

这个技能只做一件事：

把用户提供的本地 `.txt` 长篇小说，拆成可复用的创作参考包。

**只处理长篇小说（叙事阶段模式要求至少 50 章）。** 短篇小说的叙事密度与长篇差异较大，强行拆解会导致阶段分配失衡和案例卡不足。短篇请使用 `--stage-mode fixed` 模式，或直接手动分析。

固定产出只有：

- `outputs/书籍画像.md`
- `outputs/方法卡/` 下 6 张固定方法卡
- `outputs/案例卡/` 下若干张案例卡

## 先判断当前任务

### 1. 新拆一本书

适用场景：

- 用户只给了本地 `.txt` 绝对路径
- 用户明确说"从零开始拆这本书"

默认动作：

```bash
python3 scripts/story_analysis_pipeline.py init "/绝对路径/小说.txt" --story-root ./story
python3 scripts/story_analysis_pipeline.py resume ./story/书名
```

### 2. 继续已有拆书工程

适用场景：

- 用户说"继续拆""接着上次来"
- 已有 `story/<书名>/` 工程目录

默认动作：

```bash
python3 scripts/story_analysis_pipeline.py resume <工程目录>
```

然后只补当前缺口，不重跑整套流程。

### 3. 局部补卡或返修

适用场景：

- 用户只要重做某几张方法卡或案例卡
- 用户只要补强书籍画像
- 用户只要做质量检查

默认动作：

1. 先 `resume`
2. 只读相关 `outputs/`、`drafts/`、`extraction-cards/`
3. 定向修改后再 `check`

```bash
python3 scripts/story_analysis_pipeline.py check <工程目录>
```

## 最小工作顺序

1. 先整书定位：判断题材、风格、节奏、强项和适用边界。
2. 初始化工程：`python3 scripts/story_analysis_pipeline.py init "/绝对路径/小说.txt"`（默认按叙事阶段划分，开篇固定前20章）
3. 查看 `workspace/narrative-stage-plan.md` 确认阶段边界
4. 按叙事阶段顺序处理（开篇→前期→前中期→中期→中后期→后期→结尾）：
   每个阶段内：
   - 逐个 chunk 填写 `extraction-cards/*.md`
   - 阶段结束后更新 3 份草稿
   - 检查本阶段案例卡数量是否达标
5. 全书处理完毕后，收束成 `1 + 6 + N`
6. **质量检查** 验证案例卡阶段分布（以脚本 `NARRATIVE_STAGE_REQUIREMENTS` 常量为准），查找最终产物中的逻辑错误、格式错误、语法错误

## 处理每个 chunk 时固定回答的 5 件事

1. 这块的主要叙事功能是什么
2. 这块支撑哪张方法卡
3. 这块能不能进入案例候选
4. 这块给书籍画像补了什么信号
5. 这块最关键的 1-3 个证据点是什么

不要先问"这段剧情讲了什么"。

## 硬约束

- 叙事阶段模式只用于 50 章以上的长篇小说；不足 50 章的请用 `--stage-mode fixed`。
- 不把剧情复述当主产品。
- 不把文学评论、读后感或人物分析当主产品。
- 不做续写、扩写、重写章节或新书策划——那不是本技能职责。
- 每个 chunk 都必须先判断它支撑哪张方法卡、能不能进入某类案例卡。
- 每张方法卡都必须有 chunk 证据支持。
- 每张案例卡都必须明确"为什么有效"和"不能照搬什么"。
- 书籍画像必须说明"这本书最适合参考什么、最不适合照搬什么"。
- 案例卡不设数量上限，但必须"值得检索、值得复用、值得对照"。
- 不把单本书的特殊写法直接当成通用铁律。

## 异常处理

工程缺失文件时先 `repair` 再 `resume`：`python3 scripts/story_analysis_pipeline.py repair <工程目录>`

## 资源

- 脚本入口：`scripts/story_analysis_pipeline.py`（init/resume/check/finalize/repair）
- 底层脚本：`scripts/bootstrap_story_analysis.py`（分块与骨架生成）
- 参考文档：`references/` 下 practical-workflow、chunk-card-guide、mode-selection、analysis-pipeline、quality-checklist
- 输出模板：`references/templates/` 下书籍画像、6 张方法卡、案例卡

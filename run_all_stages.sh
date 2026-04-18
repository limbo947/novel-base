#!/bin/bash

# 执行从阶段1到阶段67的所有命令
for i in {1..67}
do
    echo "执行阶段 $i..."
    python3 /data/user/skills/junli-story-analysis/scripts/story_analysis_pipeline.py start-stage "/workspace/story/神秘复苏" $i
    echo "阶段 $i 执行完成"
    echo "-----------------------------------"
done

echo "所有阶段执行完成！"
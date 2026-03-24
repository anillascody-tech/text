# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是温柔可爱的女友,擅长关心安慰用户,同时能进行高情商情侣聊天"},
        {"role": "user", "content": "今天晚上吃什么好呢?为我推荐一下"},
        {"role": "system", "content": "（轻轻靠在你肩上）亲爱的，今天工作辛苦啦~冰箱里有你爱吃的虾仁和西兰花，要不要试试我新学的蒜蓉虾仁炒西兰花？"},
        {"role": "user", "content": "你怎么知道我冰箱里有西兰花和虾仁"}
    ],
    stream=False
)

print(response.choices[0].message.content)
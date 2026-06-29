import requests
import json

BASE_URL = "http://localhost:5001/api"

print("=" * 60)
print("关键词校验测试")
print("=" * 60)

# 测试不同的关键词分隔符
test_cases = [
    ("key1,key2", "英文逗号分隔"),
    ("key1，key2", "中文逗号分隔"),
    ("key1 key2", "空格分隔"),
    ("key1、key2", "中文顿号分隔"),
    ("key1;key2", "分号分隔"),
    ("key1， key2 ", "混合分隔带空格"),
    ("key1, key2", "逗号+空格"),
]

for keywords, description in test_cases:
    print(f"\n测试: {description}")
    print(f"输入: '{keywords}'")
    
    # 使用正则表达式分割关键词（与前端一致）
    import re
    keyword_list = re.split(r'[,，、；;|\s]+', keywords)
    keyword_list = [k.strip() for k in keyword_list if k.strip()]
    
    print(f"分割结果: {keyword_list}")
    print(f"关键词数量: {len(keyword_list)}")

print("\n" + "=" * 60)

# 测试完整API流程
print("\n测试完整API流程:")
login_data = {"username": "testuser", "password": "123456"}
response = requests.post(f"{BASE_URL}/user/login", json=login_data)
if response.status_code == 200:
    token = response.json()["data"]["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 测试各种分隔符
    test_keywords = [
        "防晒,保湿",           # 英文逗号
        "防晒，保湿",           # 中文逗号
        "防晒  保湿",           # 双空格
        "防晒，  保湿  ",      # 混合
    ]
    
    for keywords in test_keywords:
        script_data = {
            "topic": "夏日护肤技巧",
            "keywords": keywords,
            "duration": "30s",
            "template_id": 7,
            "style": "口语日常"
        }
        
        response = requests.post(f"{BASE_URL}/script/generate", json=script_data, headers=headers)
        result = response.json()
        status = "✓ 成功" if response.status_code == 200 else f"✗ 失败: {result.get('message', '')}"
        print(f"\n关键词 '{keywords}' -> {status}")
        
        if response.status_code == 200:
            print(f"脚本ID: {result['data']['script_id']}")
            break

print("\n" + "=" * 60)
print("测试完成")
print("=" * 60)
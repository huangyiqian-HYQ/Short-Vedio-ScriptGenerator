import requests
import json

BASE_URL = "http://localhost:5001/api"

print("=" * 60)
print("短视频脚本生成器 API 测试")
print("=" * 60)

# 测试登录
print("\n1. 测试登录接口:")
login_data = {"username": "testuser", "password": "123456"}
response = requests.post(f"{BASE_URL}/user/login", json=login_data)
print(f"状态码: {response.status_code}")
result = response.json()
print(f"响应: {json.dumps(result, ensure_ascii=False, indent=2)}")

if response.status_code == 200:
    token = result["data"]["access_token"]
    print(f"\n获取的Token: {token[:50]}...")
    
    # 测试脚本生成
    print("\n2. 测试脚本生成接口:")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    script_data = {
        "topic": "夏日护肤技巧",
        "keywords": "防晒,保湿",
        "duration": "30s",
        "template_id": 7,
        "style": "口语日常"
    }
    
    print(f"请求数据: {json.dumps(script_data, ensure_ascii=False)}")
    response = requests.post(f"{BASE_URL}/script/generate", json=script_data, headers=headers)
    print(f"状态码: {response.status_code}")
    result = response.json()
    print(f"响应: {json.dumps(result, ensure_ascii=False, indent=2)}")
    
    if response.status_code == 200:
        print("\n3. 脚本内容预览:")
        script_content = result["data"]["script_content"]
        print(script_content[:500] + "..." if len(script_content) > 500 else script_content)
        
        # 测试历史记录
        print("\n4. 测试历史记录接口:")
        response = requests.get(f"{BASE_URL}/script/list", headers=headers)
        print(f"状态码: {response.status_code}")
        result = response.json()
        print(f"响应: {json.dumps(result, ensure_ascii=False, indent=2)}")

print("\n" + "=" * 60)
print("测试完成")
print("=" * 60)
import json

def json_to_query_string(json_obj):
    # 确保json_obj是一个字典类型
    if not isinstance(json_obj, dict):
        raise ValueError("Input must be a dictionary")

    # 使用列表推导式构建键值对列表，然后用"&"连接
    query_string = '&'.join(f"{key}={value}" for key, value in json_obj.items())
    
    return query_string

# 示例JSON对象
json_data = {
    "client_plat": "android",
    "channel_app_id": "10151",
    "role_vip_level": "1",
    "sign": "cc1585e00b04f59a01fed5eacfd4cbcc",
    "role_level": "1",
    "channel_code": "jinshan",
    "type": "create-order",
    "product_quantity": "1",
    "uid": "jinshan__fd0dbbc4d55422d9345530__EXP_.",
    "zone_id": "1",
    "role_id": "123456",
    "sdk_version": "3.2.2_debug",
    "release_version": "200000",
    "app_id": "2126",
    "ad_channel_id": "jinshan",
    "currency_name": "CNY",
    "device_id": "f4e30da9-b9d1-4639-b5c9-9efe1f851253",
    "goods_id": "003",
    "phone_brand": "Redmi",
    "phone_android_id": "ad921d60486366258809553a3db49a4a",
    "product_unit_price": "1.0",
    "server_id": "1",
    "product_name": "test",
    "notify_cp_url": "https://a2.xgsdk.dev.seayoo.com/mock/recharge/notify",
    "phone_model": "23113RKC6C,14",
    "access_token": "165101ec44b0b078",
    "role_name": "Tester",
    "app_channel": "10011",
    "pay_description": "购买60钻石畅玩游戏",
    "request_timestamp": "1722584460191",
    "custom_info": "{\"loc\":\"cn\"}",
    "total_amount": "1.0",
    "app_channel_name": "jinshan",
    "cp_order_id": "sdk_807e63fe5995414cb8367da28a5e6f44",
    "package_name": "com.ppcr.kgame",
    "paid_amount": "1.0",
    "build_number": "20240726064826",
    "cp_uid": "jinshan__fd0dbbc4d55422d9345530__EXP_.",
    "channel_sequence": "10011",
    "plan_id": "200000"
}

# 转换为查询字符串
query_string = json_to_query_string(json_data)
print(query_string)
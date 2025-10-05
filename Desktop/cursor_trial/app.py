from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

# 塔罗牌数据（完整78张）
# 用于前端纯色块+文字展示，不再包含 image 字段
TAROT_CARDS = [
    # 大阿尔克那（22张）
    {"name": "愚者", "meaning": "新的开始、冒险精神、纯真", "color": "#8B4513"},
    {"name": "魔术师", "meaning": "意志力、创造力、技能", "color": "#4169E1"},
    {"name": "女祭司", "meaning": "直觉、潜意识、神秘", "color": "#9370DB"},
    {"name": "皇后", "meaning": "母性、丰饶、创造力", "color": "#FF69B4"},
    {"name": "皇帝", "meaning": "权威、秩序、领导力", "color": "#DC143C"},
    {"name": "教皇", "meaning": "传统、精神指导、学习", "color": "#FFD700"},
    {"name": "恋人", "meaning": "爱情、选择、和谐", "color": "#FF1493"},
    {"name": "战车", "meaning": "意志力、胜利、控制", "color": "#2E8B57"},
    {"name": "力量", "meaning": "内在力量、勇气、耐心", "color": "#FF6347"},
    {"name": "隐者", "meaning": "内省、寻求真理、孤独", "color": "#708090"},
    {"name": "命运之轮", "meaning": "命运、变化、循环", "color": "#FF8C00"},
    {"name": "正义", "meaning": "平衡、公正、真理", "color": "#32CD32"},
    {"name": "倒吊人", "meaning": "牺牲、等待、新视角", "color": "#8A2BE2"},
    {"name": "死神", "meaning": "结束、转变、重生", "color": "#000000"},
    {"name": "节制", "meaning": "平衡、调和、耐心", "color": "#20B2AA"},
    {"name": "恶魔", "meaning": "束缚、诱惑、物质主义", "color": "#800080"},
    {"name": "塔", "meaning": "突然变化、启示、解放", "color": "#FF4500"},
    {"name": "星星", "meaning": "希望、灵感、指引", "color": "#87CEEB"},
    {"name": "月亮", "meaning": "幻觉、恐惧、潜意识", "color": "#C0C0C0"},
    {"name": "太阳", "meaning": "成功、活力、快乐", "color": "#FFD700"},
    {"name": "审判", "meaning": "重生、觉醒、宽恕", "color": "#FFA500"},
    {"name": "世界", "meaning": "完成、成功、旅行", "color": "#00CED1"},
    # 权杖（Wands）14张
    {"name": "权杖王牌", "meaning": "灵感、创造力、潜力", "color": "#FF7F50"},
    {"name": "权杖二", "meaning": "计划、未来、选择", "color": "#FF7F50"},
    {"name": "权杖三", "meaning": "远景、拓展、机会", "color": "#FF7F50"},
    {"name": "权杖四", "meaning": "庆祝、家庭、稳定", "color": "#FF7F50"},
    {"name": "权杖五", "meaning": "竞争、冲突、挑战", "color": "#FF7F50"},
    {"name": "权杖六", "meaning": "胜利、认可、进步", "color": "#FF7F50"},
    {"name": "权杖七", "meaning": "防御、坚持、斗争", "color": "#FF7F50"},
    {"name": "权杖八", "meaning": "快速、行动、消息", "color": "#FF7F50"},
    {"name": "权杖九", "meaning": "坚韧、考验、防备", "color": "#FF7F50"},
    {"name": "权杖十", "meaning": "负担、压力、责任", "color": "#FF7F50"},
    {"name": "权杖侍者", "meaning": "探索、热情、消息", "color": "#FF7F50"},
    {"name": "权杖骑士", "meaning": "冒险、冲动、能量", "color": "#FF7F50"},
    {"name": "权杖皇后", "meaning": "自信、独立、魅力", "color": "#FF7F50"},
    {"name": "权杖国王", "meaning": "领导、远见、激励", "color": "#FF7F50"},
    # 圣杯（Cups）14张
    {"name": "圣杯王牌", "meaning": "情感、爱、潜力", "color": "#1E90FF"},
    {"name": "圣杯二", "meaning": "伙伴、结合、和谐", "color": "#1E90FF"},
    {"name": "圣杯三", "meaning": "友谊、庆祝、社交", "color": "#1E90FF"},
    {"name": "圣杯四", "meaning": "冷漠、沉思、厌倦", "color": "#1E90FF"},
    {"name": "圣杯五", "meaning": "失望、遗憾、悲伤", "color": "#1E90FF"},
    {"name": "圣杯六", "meaning": "回忆、童年、怀旧", "color": "#1E90FF"},
    {"name": "圣杯七", "meaning": "幻想、选择、诱惑", "color": "#1E90FF"},
    {"name": "圣杯八", "meaning": "放弃、追寻、转变", "color": "#1E90FF"},
    {"name": "圣杯九", "meaning": "满足、愿望实现、幸福", "color": "#1E90FF"},
    {"name": "圣杯十", "meaning": "家庭、和谐、圆满", "color": "#1E90FF"},
    {"name": "圣杯侍者", "meaning": "消息、创造力、情感", "color": "#1E90FF"},
    {"name": "圣杯骑士", "meaning": "浪漫、追求、理想", "color": "#1E90FF"},
    {"name": "圣杯皇后", "meaning": "关怀、直觉、温柔", "color": "#1E90FF"},
    {"name": "圣杯国王", "meaning": "情感成熟、智慧、平衡", "color": "#1E90FF"},
    # 宝剑（Swords）14张
    {"name": "宝剑王牌", "meaning": "新思想、真理、决断", "color": "#4682B4"},
    {"name": "宝剑二", "meaning": "犹豫、选择、平衡", "color": "#4682B4"},
    {"name": "宝剑三", "meaning": "心碎、痛苦、分离", "color": "#4682B4"},
    {"name": "宝剑四", "meaning": "休息、恢复、静思", "color": "#4682B4"},
    {"name": "宝剑五", "meaning": "冲突、失败、自私", "color": "#4682B4"},
    {"name": "宝剑六", "meaning": "过渡、旅行、疗愈", "color": "#4682B4"},
    {"name": "宝剑七", "meaning": "欺骗、策略、逃避", "color": "#4682B4"},
    {"name": "宝剑八", "meaning": "束缚、限制、无助", "color": "#4682B4"},
    {"name": "宝剑九", "meaning": "焦虑、担忧、噩梦", "color": "#4682B4"},
    {"name": "宝剑十", "meaning": "结束、背叛、失败", "color": "#4682B4"},
    {"name": "宝剑侍者", "meaning": "好奇、警觉、消息", "color": "#4682B4"},
    {"name": "宝剑骑士", "meaning": "果断、冲动、行动", "color": "#4682B4"},
    {"name": "宝剑皇后", "meaning": "理性、独立、诚实", "color": "#4682B4"},
    {"name": "宝剑国王", "meaning": "权威、智慧、公正", "color": "#4682B4"},
    # 钱币（Pentacles/Coins）14张
    {"name": "钱币王牌", "meaning": "财富、机会、潜力", "color": "#DAA520"},
    {"name": "钱币二", "meaning": "平衡、适应、灵活", "color": "#DAA520"},
    {"name": "钱币三", "meaning": "合作、技能、成就", "color": "#DAA520"},
    {"name": "钱币四", "meaning": "保守、控制、稳定", "color": "#DAA520"},
    {"name": "钱币五", "meaning": "贫困、困难、支持", "color": "#DAA520"},
    {"name": "钱币六", "meaning": "慷慨、分享、平衡", "color": "#DAA520"},
    {"name": "钱币七", "meaning": "耐心、评估、等待", "color": "#DAA520"},
    {"name": "钱币八", "meaning": "勤奋、学习、成长", "color": "#DAA520"},
    {"name": "钱币九", "meaning": "独立、成就、享受", "color": "#DAA520"},
    {"name": "钱币十", "meaning": "财富、家庭、传承", "color": "#DAA520"},
    {"name": "钱币侍者", "meaning": "机会、学习、成长", "color": "#DAA520"},
    {"name": "钱币骑士", "meaning": "责任、勤奋、实际", "color": "#DAA520"},
    {"name": "钱币皇后", "meaning": "关怀、实际、富足", "color": "#DAA520"},
    {"name": "钱币国王", "meaning": "安全、成功、慷慨", "color": "#DAA520"}
]

def drawRandomCards():
    """随机抽取三张塔罗牌"""
    selected_cards = random.sample(TAROT_CARDS, 3)
    for card in selected_cards:
        # 随机决定正位或逆位
        card['position'] = '正位' if random.choice([True, False]) else '逆位'
    return selected_cards

import openai
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def generateReading(question, cards):
    """调用OpenAI GPT-4o生成塔罗牌解读"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return "错误：未配置OpenAI API密钥，请联系管理员。"
    
    client = openai.OpenAI(api_key=api_key)

    # 构建牌面描述
    card_descriptions = []
    for i, card in enumerate(cards, 1):
        card_descriptions.append(
            f"第{i}张牌：{card['name']}（{card['position']}），含义：{card['meaning']}"
        )
    cards_text = "\n".join(card_descriptions)

    prompt = (
        f"用户的问题是：{question}\n"
        f"抽到的三张塔罗牌如下：\n"
        f"{cards_text}\n"
        "请你作为一名专业的塔罗牌解读师，结合用户的问题和三张牌的牌意、正逆位，给出详细、具体、有启发性的中文解读，内容不少于150字。"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "你是一位专业的中文塔罗牌解读师。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        reading = response.choices[0].message.content.strip()
        return reading
    except openai.AuthenticationError:
        return "错误：OpenAI API密钥无效，请联系管理员。"
    except openai.RateLimitError:
        return "错误：API调用频率过高，请稍后重试。"
    except openai.APIConnectionError:
        return "错误：网络连接失败，请检查网络后重试。"
    except Exception as e:
        return f"调用AI解读时出现错误：{str(e)}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw-cards', methods=['POST'])
def drawCards():
    """抽取塔罗牌"""
    try:
        cards = drawRandomCards()
        return jsonify({
            'success': True,
            'cards': cards
        })
    except Exception as e:
        return jsonify({'error': f'抽牌过程中出现错误：{str(e)}'}), 500

@app.route('/divination', methods=['POST'])
def divination():
    """生成解读"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        cards = data.get('cards', [])
        
        if not question:
            return jsonify({'error': '请输入您的问题'}), 400
        
        if not cards:
            return jsonify({'error': '请先抽取塔罗牌'}), 400
        
        # 生成解读
        reading = generateReading(question, cards)
        
        return jsonify({
            'success': True,
            'reading': reading
        })
    
    except Exception as e:
        return jsonify({'error': f'解读过程中出现错误：{str(e)}'}), 500

if __name__ == '__main__':
    # 生产环境配置
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

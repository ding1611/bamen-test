# -*- coding: utf-8 -*-
"""
八门识人完整版报告生成器 - 2026年度版
根据用户测试结果，生成个性化报告
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# 注册中文字体
try:
    pdfmetrics.registerFont(TTFont('SimHei', 'C:/Windows/Fonts/simhei.ttf'))
    pdfmetrics.registerFont(TTFont('SimSun', 'C:/Windows/Fonts/simsun.ttc'))
    CHINESE_FONT = 'SimHei'
    CONTENT_FONT = 'SimSun'
except:
    CHINESE_FONT = 'Helvetica'
    CONTENT_FONT = 'Helvetica'

# 颜色方案
PRIMARY_COLOR = HexColor('#2D5F8A')  # 深蓝
ACCENT_COLOR = HexColor('#E8A838')   # 金色
DARK_COLOR = HexColor('#1A1A1A')     # 深灰
LIGHT_BG = HexColor('#F5F7FA')        # 浅灰背景
SUCCESS_COLOR = HexColor('#2E7D32')   # 绿色

def create_styles():
    """创建样式"""
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        name='MainTitle',
        fontName=CHINESE_FONT,
        fontSize=28,
        leading=34,
        alignment=TA_CENTER,
        textColor=PRIMARY_COLOR,
        spaceAfter=20
    ))
    
    styles.add(ParagraphStyle(
        name='SubTitle',
        fontName=CHINESE_FONT,
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        textColor=DARK_COLOR,
        spaceAfter=30
    ))
    
    styles.add(ParagraphStyle(
        name='SectionTitle',
        fontName=CHINESE_FONT,
        fontSize=18,
        leading=24,
        alignment=TA_LEFT,
        textColor=PRIMARY_COLOR,
        spaceBefore=20,
        spaceAfter=12
    ))
    
    styles.add(ParagraphStyle(
        name='SubSection',
        fontName=CHINESE_FONT,
        fontSize=14,
        leading=20,
        alignment=TA_LEFT,
        textColor=ACCENT_COLOR,
        spaceBefore=15,
        spaceAfter=8
    ))
    
    styles.add(ParagraphStyle(
        name='BulletText',
        fontName=CONTENT_FONT,
        fontSize=11,
        leading=16,
        alignment=TA_LEFT,
        textColor=DARK_COLOR,
        leftIndent=20,
        spaceAfter=4
    ))
    
    styles.add(ParagraphStyle(
        name='QuoteText',
        fontName=CONTENT_FONT,
        fontSize=12,
        leading=18,
        alignment=TA_CENTER,
        textColor=PRIMARY_COLOR,
        spaceBefore=15,
        spaceAfter=15,
        leftIndent=30,
        rightIndent=30
    ))
    
    styles.add(ParagraphStyle(
        name='HighlightText',
        fontName=CHINESE_FONT,
        fontSize=12,
        leading=16,
        alignment=TA_LEFT,
        textColor=SUCCESS_COLOR,
        spaceBefore=8,
        spaceAfter=8
    ))
    
    return styles

# ==================== 八门数据定义 ====================

MEN_DATA = {
    "休门": {
        "name": "休门",
        "subtitle": "情商调和型",
        "color": "#4A90D9",
        "personality": "你是天生的『和事佬』，情商极高，善于平衡各种关系。你的温和与包容让你在人际圈中备受欢迎，无论是家庭、朋友还是职场，你都能游刃有余地处理各种微妙的人情世故。",
        "strengths": [
            "情商极高，善于化解矛盾",
            "人缘极好，身边贵人不断",
            "懂得平衡工作与生活",
            "适应能力强，随遇而安",
            "善于倾听，给人安全感"
        ],
        "weaknesses": [
            "有时过于迁就他人，失去自我",
            "面对冲突容易选择逃避",
            "决策偏慢，优柔寡断",
            "不善于主动争取机会"
        ],
        "career": {
            "suitable": ["人力资源、行政管理、咨询顾问、外交公关、教育培训"],
            "不适合": ["需要强硬手段的销售、与竞争对手直接对抗的岗位"],
            "tips": [
                "发挥情商优势，在需要协调的岗位更容易成功",
                "学会适度拒绝，不要让所有人都满意",
                "可以尝试做团队润滑剂的角色",
                "2026年适合拓展人脉，参加行业交流活动"
            ]
        },
        "love": {
            "ideal_partner": ["生门", "景门"],
            "avoid": ["伤门", "死门"],
            "traits": [
                "在感情中你是温柔的守护者",
                "懂得体贴照顾，但有时过于迁就",
                "适合找个能给你安全感的伴侣"
            ],
            "tips": [
                "2026年感情运势上升，下半年可能有重要情感进展",
                "学会表达自己的真实需求，不要一味忍让",
                "单身者可以多参加社交活动，但不必刻意追求"
            ]
        },
        "health": {
            "weak_points": ["泌尿系统", "肾脏", "腰部"],
            "tips": [
                "注意保持规律作息，不要熬夜太多",
                "适合瑜伽、太极等舒缓运动",
                "多喝水，保持体内水分平衡",
                "定期检查泌尿系统"
            ]
        },
        "action_plan": {
            "morning": ["起床后喝一杯温水", "对着镜子微笑3秒，给自己积极暗示", "制定今日人际目标"],
            "work": ["处理人际问题保持平和", "主动与同事交流，建立关系网", "遇到冲突先冷静再处理"],
            "evening": ["回顾今天人际得失", "给重要的人发个问候", "睡前冥想5分钟"]
        },
        "compatibility": {
            "with_生门": "生门带你开拓财运，两人合作商业项目很有潜力",
            "with_伤门": "伤门冲动激进，可能与你的温和产生摩擦，需要多沟通",
            "with_杜门": "你们都是内敛型，相处默契，但可能缺乏激情",
            "with_景门": "景门活泼开朗，能给你带来活力，但要注意被对方带跑节奏",
            "with_死门": "死门固执执着，容易与你的灵活性冲突，需要相互理解",
            "with_惊门": "惊门善变灵活，你们相处轻松，但要注意承诺兑现",
            "with_开门": "开门领导力强，能带动你走出舒适区，但要注意主次"
        }
    },
    "生门": {
        "name": "生门",
        "subtitle": "财富创造型",
        "color": "#4CAF50",
        "personality": "你是天生的『财神体质』，对财富有敏锐的嗅觉，善于发现商机。你的创造力和执行力让你在财富道路上总能快人一步。追求财务自由是你人生的重要目标。",
        "strengths": [
            "财运极佳，财商出众",
            "善于发现商机，把握机会",
            "执行力强，说干就干",
            "商业嗅觉敏锐",
            "有创业精神和风险意识"
        ],
        "weaknesses": [
            "有时过于追求利益，忽略人际关系",
            "风险偏好较高，可能冒进",
            "工作狂模式，容易忽略健康",
            "对合作伙伴要求苛刻"
        ],
        "career": {
            "suitable": ["创业", "投资理财", "企业管理", "商业贸易", "房地产"],
            "不适合": ["按部就班的行政岗位", "不需要决策的基层工作"],
            "tips": [
                "2026年是财运爆发年，特别适合创业或拓展业务",
                "可以关注政策导向的行业机会",
                "找靠谱的合伙人，分工合作",
                "注意分散投资，不要把所有鸡蛋放一个篮子"
            ]
        },
        "love": {
            "ideal_partner": ["休门", "杜门"],
            "avoid": ["惊门"],
            "traits": [
                "在感情中你务实但有时忽略浪漫",
                "愿意为爱人提供优渥的物质生活",
                "但需要学会平衡事业与家庭"
            ],
            "tips": [
                "2026年感情稳定，适合结婚或订婚",
                "多花时间陪伴伴侣，不要只有工作",
                "单身者可以通过商业活动认识优质对象"
            ]
        },
        "health": {
            "weak_points": ["肝脏", "消化系统", "头部"],
            "tips": [
                "注意肝脏保养，少熬夜少喝酒",
                "保持规律饮食，不要暴饮暴食",
                "适当运动，缓解压力",
                "定期体检，特别关注肝功能"
            ]
        },
        "action_plan": {
            "morning": ["查看财经新闻和市场动态", "制定今日财务目标", "给潜在客户发早安问候"],
            "work": ["专注核心业务，提高效率", "积极拓展新客户和渠道", "处理财务决策要果断"],
            "evening": ["复盘今日财务收获", "研究新的投资机会", "保持适度休息，不要过度消耗"]
        },
        "compatibility": {
            "with_休门": "休门温和包容，是你理想的家庭后盾，让你安心闯事业",
            "with_伤门": "你们都敢闯敢干，合作创业很有火花，但要注意分工",
            "with_杜门": "杜门稳重内敛，能弥补你的冲动，是很好的合伙人",
            "with_景门": "景门能说会道，帮你做营销推广很合适，但要管好预算",
            "with_死门": "死门执着专注，适合一起做长期项目，但沟通要耐心",
            "with_惊门": "惊门善变，可能与你的务实风格冲突，合作需谨慎",
            "with_开门": "开门格局大、资源多，强强联合可以做大事业"
        }
    },
    "伤门": {
        "name": "伤门",
        "subtitle": "突破进取型",
        "color": "#F44336",
        "personality": "你是天生的『破局者』，敢于挑战规则，善于发现问题和漏洞。你的勇气和执行力让你在别人退缩时能够勇往直前。",
        "strengths": [
            "敢于挑战，不惧权威",
            "洞察力强，善于发现问题",
            "执行力强，敢于行动",
            "抗压能力出众",
            "适合开疆拓土"
        ],
        "weaknesses": [
            "有时过于激进，容易树敌",
            "说话直接，容易伤人",
            "冲动决策，风险意识不足",
            "不善于维护关系"
        ],
        "career": {
            "suitable": ["销售", "市场开拓", "项目管理", "执法部门", "竞技行业"],
            "不适合": ["需要圆滑处事的客服岗位", "强调服从的工作"],
            "tips": [
                "发挥突破能力，适合开疆拓土",
                "学会控制情绪，说话留余地",
                "2026年适合主动出击，争取晋升或转型",
                "找准方向再行动，不要盲目冲刺"
            ]
        },
        "love": {
            "ideal_partner": ["生门", "景门"],
            "avoid": ["休门"],
            "traits": [
                "在感情中你是热烈的追求者",
                "敢爱敢恨，但有时过于强势",
                "需要学会尊重对方的节奏"
            ],
            "tips": [
                "2026年感情有突破，主动表白有机会",
                "学会温柔表达，不要只有命令",
                "单身者可以大胆追求，但要注意方式"
            ]
        },
        "health": {
            "weak_points": ["肝脏", "手脚", "筋骨"],
            "tips": [
                "注意运动损伤，热身要充分",
                "控制脾气，怒伤肝",
                "多进行力量训练",
                "保持充足睡眠，恢复体力"
            ]
        },
        "action_plan": {
            "morning": ["进行高强度运动释放能量", "制定今日挑战目标", "给自己打气，保持斗志"],
            "work": ["主动承担困难任务", "敢于表达不同意见", "处理问题要果断但要理性"],
            "evening": ["复盘今日得失", "学习提升专业能力", "做一些放松练习"]
        },
        "compatibility": {
            "with_休门": "休门温和包容，能平衡你的冲动，是很好的伴侣",
            "with_生门": "你们都敢闯敢干，可以一起创业或合作项目",
            "with_杜门": "杜门沉稳，帮你想清楚再行动，减少冲动损失",
            "with_景门": "景门能说会道，帮你做公共关系，互补性强",
            "with_死门": "你们都很执着，合作很有冲劲，但容易起冲突",
            "with_惊门": "惊门比你还善变，容易让你抓狂，需多沟通",
            "with_开门": "开门有格局，能带你看到更大的世界"
        }
    },
    "杜门": {
        "name": "杜门",
        "subtitle": "内敛深藏型",
        "color": "#6A5ACD",
        "personality": "你是深藏不露的『扫地僧』，表面低调，内心世界丰富。你的洞察力和思考力超越常人，善于谋略和规划。",
        "strengths": [
            "深谋远虑，考虑周全",
            "善于隐藏实力，关键时刻出手",
            "专注力极强",
            "学习能力强",
            "守口如瓶，值得信任"
        ],
        "weaknesses": [
            "过于内敛，不善于表现自己",
            "社交能力相对较弱",
            "有时想太多，行动力不足",
            "给人距离感"
        ],
        "career": {
            "suitable": ["技术研发", "策略分析", "财务审计", "情报分析", "幕后策划"],
            "不适合": ["需要频繁公开演讲的销售", "强调表现的市场岗位"],
            "tips": [
                "适合做幕后军师，不要强求出风头",
                "2026年适合深耕专业领域",
                "学会适度展示自己，让别人发现你的能力",
                "找对平台，不用靠嘴皮子也能成功"
            ]
        },
        "love": {
            "ideal_partner": ["生门", "开门"],
            "avoid": ["景门"],
            "traits": [
                "在感情中你是专一的守护者",
                "不善表达，但用行动证明爱",
                "需要找能读懂你内心的人"
            ],
            "tips": [
                "2026年感情需要主动一点",
                "学会表达爱意，不要只有默默付出",
                "单身者可以通过专业圈子认识志同道合的人"
            ]
        },
        "health": {
            "weak_points": ["呼吸系统", "肺部", "皮肤"],
            "tips": [
                "多进行户外活动，呼吸新鲜空气",
                "注意室内空气质量",
                "保持适度社交，避免过度孤独",
                "皮肤敏感者要注意防护"
            ]
        },
        "action_plan": {
            "morning": ["静坐或冥想清空思绪", "学习新知识提升自己", "制定今日计划"],
            "work": ["专注深度工作，减少干扰", "做好幕后工作，等待机会", "适时展示成果"],
            "evening": ["独处充电，阅读学习", "保持规律作息", "整理今日收获"]
        },
        "compatibility": {
            "with_休门": "休门理解你的内敛，相处轻松不累",
            "with_生门": "生门有魄力，能带动你行动，合作创业不错",
            "with_伤门": "伤门太冲动，可能理解不了你的深思熟虑",
            "with_景门": "景门太爱表现，可能让你觉得浮躁",
            "with_死门": "你们都是内敛型，相处默契，互相尊重",
            "with_惊门": "惊门太善变，让你没有安全感",
            "with_开门": "开门格局大，能带你看到更大世界，值得跟随"
        }
    },
    "景门": {
        "name": "景门",
        "subtitle": "展示表达型",
        "color": "#FF9800",
        "personality": "你是天生的『舞台明星』，魅力四射，善于表达。你的亲和力和表现力让你在任何场合都能成为焦点。人脉广泛是你们最大的优势。",
        "strengths": [
            "魅力出众，善于吸引注意",
            "表达能力极强",
            "人脉广泛，社交达人",
            "善于包装和营销",
            "适应各种场合"
        ],
        "weaknesses": [
            "有时过于追求表面",
            "做事容易三分钟热度",
            "承诺过多，兑现不足",
            "深度不够，容易浮夸"
        ],
        "career": {
            "suitable": ["销售", "公关", "市场营销", "自媒体", "讲师"],
            "不适合": ["需要沉下心做技术研发的岗位", "强调严谨的财务"],
            "tips": [
                "发挥表达优势，在需要曝光的岗位更容易成功",
                "学会深耕，不要只有广度没有深度",
                "2026年适合打造个人IP",
                "承诺要谨慎，兑现要靠谱"
            ]
        },
        "love": {
            "ideal_partner": ["伤门", "死门"],
            "avoid": ["杜门"],
            "traits": [
                "在感情中你是浪漫的制造者",
                "会哄人，但有时过于花哨",
                "需要找能给你安全感的伴侣"
            ],
            "tips": [
                "2026年感情有戏剧性变化",
                "学会真诚表达，不要只有套路",
                "单身者要主动出击，多参加社交活动"
            ]
        },
        "health": {
            "weak_points": ["眼睛", "心脏", "血液循环"],
            "tips": [
                "注意用眼卫生，少看电子屏幕",
                "保护心脏，避免过度兴奋",
                "保持规律作息",
                "适当安静活动，平衡能量"
            ]
        },
        "action_plan": {
            "morning": ["精心打扮出门", "制定今日社交计划", "练习演讲或表达技巧"],
            "work": ["发挥表达优势做业绩", "积极拓展人脉关系", "保持热情但要务实"],
            "evening": ["复盘今日社交得失", "学习提升表达能力", "保持适度休息"]
        },
        "compatibility": {
            "with_休门": "休门温和包容，欣赏你的魅力，相处和谐",
            "with_生门": "生门务实有魄力，你们互补，能一起做大事",
            "with_伤门": "你们都很直接，相处热烈但可能有摩擦",
            "with_杜门": "杜门太内敛，可能觉得你的表现太张扬",
            "with_死门": "死门执着专注，能互补你的浮躁，但沟通要耐心",
            "with_惊门": "你们都很会表现，在一起很热闹，要避免攀比",
            "with_开门": "开门格局大，能带你做更大的平台"
        }
    },
    "死门": {
        "name": "死门",
        "subtitle": "执着坚持型",
        "color": "#455A64",
        "personality": "你是『匠人精神』的代表，一旦认定目标就会坚持到底，不达目的不罢休。你的专注和执着让你在专业领域往往能成为顶尖专家。",
        "strengths": [
            "目标坚定，不轻易放弃",
            "专注力极强，能深度钻研",
            "抗压能力强",
            "原则性强，有底线",
            "做事有始有终"
        ],
        "weaknesses": [
            "有时过于固执，不知变通",
            "不善于接受批评",
            "给人压迫感",
            "缺乏灵活性"
        ],
        "career": {
            "suitable": ["科研", "技术专家", "律师", "医生", "传统手工艺", "竞技体育"],
            "不适合": ["需要经常变换方向的岗位", "强调变通的销售"],
            "tips": [
                "适合深耕专业领域，成为专家",
                "学会变通，不要一条道走到黑",
                "2026年适合专注做一件大事",
                "多听不同意见，但要坚守核心"
            ]
        },
        "love": {
            "ideal_partner": ["景门", "惊门"],
            "avoid": ["休门"],
            "traits": [
                "在感情中你是专一的伴侣",
                "一旦认定就是一辈子",
                "但表达方式可能过于强硬"
            ],
            "tips": [
                "2026年感情需要主动表达",
                "学会温柔，不要只有命令",
                "单身者可以从小事开始表达关心"
            ]
        },
        "health": {
            "weak_points": ["消化系统", "脾胃", "肌肉"],
            "tips": [
                "注意消化系统保养",
                "保持适度运动，不要久坐",
                "学会放松，不要给自己太大压力",
                "定期体检"
            ]
        },
        "action_plan": {
            "morning": ["规划今日核心任务", "提醒自己专注目标", "保持积极心态"],
            "work": ["专注深度工作", "坚持原则但要灵活", "与团队保持沟通"],
            "evening": ["复盘今日目标完成度", "学习专业知识", "适度放松休息"]
        },
        "compatibility": {
            "with_休门": "休门温和包容，能平衡你的固执，是很好的伴侣",
            "with_生门": "生门有魄力，能带动你行动，合作创业不错",
            "with_伤门": "你们都很执着，合作很有冲劲，但容易起冲突",
            "with_杜门": "杜门理解你的专注，相处和谐，互相尊重",
            "with_景门": "景门能说会道，帮你做公共关系，互补性强",
            "with_惊门": "惊门太善变，可能让你觉得没有原则",
            "with_开门": "开门格局大，能带你看到更大的世界"
        }
    },
    "惊门": {
        "name": "惊门",
        "subtitle": "变通灵活型",
        "color": "#00BCD4",
        "personality": "你是『百变达人』，善于随机应变，适应能力极强。你的思维敏捷，总能在困境中找到出路。创意和点子是你们最大的武器。",
        "strengths": [
            "思维敏捷，应变能力强",
            "善于发现机会",
            "表达能力很强",
            "创意无限",
            "多才多艺"
        ],
        "weaknesses": [
            "有时过于善变，缺乏定性",
            "承诺过多难以兑现",
            "做事容易半途而废",
            "给人不可靠的感觉"
        ],
        "career": {
            "suitable": ["创意行业", "咨询顾问", "媒体传播", "应急处理", "金融创新"],
            "不适合": ["需要稳定长期投入的岗位", "强调经验的传统行业"],
            "tips": [
                "发挥创意优势，在需要创新的岗位更容易成功",
                "学会专注深耕，不要只有点子没有行动",
                "2026年适合做跟风口相关的事",
                "承诺要谨慎，兑现要靠谱"
            ]
        },
        "love": {
            "ideal_partner": ["死门", "开门"],
            "avoid": ["生门"],
            "traits": [
                "在感情中你是有趣的伴侣",
                "总能给对方带来惊喜",
                "但需要学会给对方安全感"
            ],
            "tips": [
                "2026年感情需要稳定一点",
                "学会承诺并兑现",
                "单身者要主动但要靠谱"
            ]
        },
        "health": {
            "weak_points": ["神经系统", "心脏", "口腔"],
            "tips": [
                "注意神经系统保养",
                "保持规律作息，不要熬夜",
                "适当安静活动，平衡能量",
                "注意口腔健康"
            ]
        },
        "action_plan": {
            "morning": ["列出今日创意想法", "选择最重要的事情专注做", "给自己定个小目标"],
            "work": ["发挥创意优势", "保持灵活性但要有计划", "跟进落实重要事项"],
            "evening": ["记录今日创意灵感", "回顾目标完成情况", "为明天做准备"]
        },
        "compatibility": {
            "with_休门": "休门温和包容，欣赏你的创意，相处轻松",
            "with_生门": "生门务实，能帮你把创意落地，但风格差异大",
            "with_伤门": "你们都很直接，相处热烈但可能有摩擦",
            "with_杜门": "杜门太内敛，可能觉得你的表现太张扬",
            "with_景门": "你们都很会表现，在一起很热闹，要避免攀比",
            "with_死门": "死门太执着，可能觉得你没有原则，需要相互理解",
            "with_开门": "开门格局大，能带你做更大的平台"
        }
    },
    "开门": {
        "name": "开门",
        "subtitle": "开拓领袖型",
        "color": "#9C27B0",
        "personality": "你是天生的『领袖』，格局宏大，善于整合资源。你的领导力和号召力让你天然就是人群中的焦点。开创一番事业是你的人生使命。",
        "strengths": [
            "格局宏大，有远见",
            "领导力强，善于带队",
            "资源整合能力强",
            "执行力强",
            "敢于承担责任"
        ],
        "weaknesses": [
            "有时过于强势，不够民主",
            "喜欢掌控，不善于放权",
            "决策快但可能考虑不周",
            "给人距离感"
        ],
        "career": {
            "suitable": ["企业高管", "创业当老板", "政府领导", "项目负责人"],
            "不适合": ["需要服从执行的基层岗位", "自由职业者"],
            "tips": [
                "适合做领导者，不要强做执行者",
                "学会放权，不要事事亲力亲为",
                "2026年适合开疆拓土",
                "多听团队意见，但要果断决策"
            ]
        },
        "love": {
            "ideal_partner": ["杜门", "惊门"],
            "avoid": ["伤门"],
            "traits": [
                "在感情中你是强势的领导者",
                "愿意为对方提供资源",
                "但需要学会尊重对方的选择"
            ],
            "tips": [
                "2026年感情要学会放下控制",
                "多关心对方感受，不要只有命令",
                "单身者可以通过事业平台认识优秀的人"
            ]
        },
        "health": {
            "weak_points": ["头部", "大脑", "心脏"],
            "tips": [
                "注意头部健康，不要用脑过度",
                "保持充足睡眠",
                "适当运动，放松身心",
                "定期体检，关注心脑健康"
            ]
        },
        "action_plan": {
            "morning": ["思考战略方向", "制定今日团队目标", "激励自己保持状态"],
            "work": ["发挥领导优势", "整合资源推动项目", "关注团队状态"],
            "evening": ["复盘团队成果", "思考战略规划", "保持学习提升"]
        },
        "compatibility": {
            "with_休门": "休门温和包容，是你理想的后盾，让你安心闯事业",
            "with_生门": "你们都是强者，合作可以做大事业，但要处理好主次",
            "with_伤门": "伤门敢闯敢干，是得力干将，但要注意方式",
            "with_杜门": "杜门深谋远虑，是很好的军师，能帮你想清楚",
            "with_景门": "景门能说会道，帮你做公共关系很合适",
            "with_死门": "死门执着专注，适合做核心团队成员",
            "with_惊门": "惊门创意无限，但要安排好位置发挥优势"
        }
    }
}

def create_report(men_type, output_path):
    """生成完整版报告"""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=(21*cm, 29.7*cm),
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    styles = create_styles()
    story = []
    data = MEN_DATA.get(men_type, MEN_DATA["休门"])
    
    # ==================== 封面 ====================
    story.append(Spacer(1, 3*cm))
    
    # 主标题
    story.append(Paragraph("八门识人", styles['MainTitle']))
    story.append(Paragraph("完整版能量分析报告", styles['SubTitle']))
    
    story.append(Spacer(1, 1*cm))
    
    # 用户信息
    story.append(Paragraph("2026年度 · 专属定制版", styles['BodyText']))
    
    story.append(Spacer(1, 2*cm))
    
    # 能量类型
    story.append(Paragraph(f"【{data['name']}】", styles['SectionTitle']))
    story.append(Paragraph(data['subtitle'], styles['SubSection']))
    
    story.append(Spacer(1, 2*cm))
    
    # 底部信息
    story.append(Paragraph("— 预见丁老师 · 易学智慧解读 —", styles['QuoteText']))
    
    story.append(PageBreak())
    
    # ==================== 目录 ====================
    story.append(Paragraph("目 录", styles['MainTitle']))
    story.append(Spacer(1, 0.5*cm))
    
    toc_items = [
        "一、核心能量属性解读",
        "二、性格深度画像",
        "三、事业能量分析",
        "四、情感能量解读",
        "五、身体健康指南",
        "六、2026年度能量趋势",
        "七、每日行动清单",
        "八、八种能量相处指南",
        "九、深度咨询通道"
    ]
    
    for item in toc_items:
        story.append(Paragraph(item, styles['BodyText']))
        story.append(Spacer(1, 0.3*cm))
    
    story.append(PageBreak())
    
    # ==================== 一、核心能量属性 ====================
    story.append(Paragraph("一、核心能量属性解读", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph(f"【{data['name']}】{data['subtitle']}", styles['SubSection']))
    story.append(Spacer(1, 0.2*cm))
    
    story.append(Paragraph(data['personality'], styles['BodyText']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("◆ 能量优势", styles['SubSection']))
    for s in data['strengths']:
        story.append(Paragraph(f"• {s}", styles['BulletText']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("◆ 需要注意的特质", styles['SubSection']))
    for w in data['weaknesses']:
        story.append(Paragraph(f"• {w}", styles['BulletText']))
    
    story.append(PageBreak())
    
    # ==================== 二、性格深度画像 ====================
    story.append(Paragraph("二、性格深度画像", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("你的人生剧本", styles['SubSection']))
    story.append(Paragraph(
        f"你是带着【{data['name']}】能量来到这个世界的。这种能量决定了你的思维方式、行为模式和人际风格。",
        styles['BodyText']
    ))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("性格特点总结", styles['SubSection']))
    
    # 根据不同门调整描述
    if data['name'] in ['休门', '杜门', '死门']:
        traits = [
            f"你天生具有{data['name']}的特质，这让你在人群中独具特色",
            "你处理问题的方式偏向于深思熟虑、稳扎稳打",
            "在人际交往中，你更倾向于深度交流、质量优先",
            "面对压力时，你的反应是理性分析、寻求最优解",
            "你的价值观更注重长期价值和实际成果"
        ]
    else:
        traits = [
            f"你天生具有{data['name']}的特质，这让你在人群中独具特色",
            "你处理问题的方式偏向于灵活应变、随机应变",
            "在人际交往中，你更倾向于广泛社交、人脉为王",
            "面对压力时，你的反应是直觉判断、快速响应",
            "你的价值观更注重当下体验和机会把握"
        ]
    
    for t in traits:
        story.append(Paragraph(f"• {t}", styles['BulletText']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("◆ 性格真相", styles['SubSection']))
    story.append(Paragraph(
        "很多人觉得你外向，但只有你自己知道，你内心其实渴望的是深度连接。",
        styles['QuoteText']
    ))
    
    story.append(PageBreak())
    
    # ==================== 三、事业能量分析 ====================
    story.append(Paragraph("三、事业能量分析", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("你的核心事业特质", styles['SubSection']))
    story.append(Paragraph(
        f"你是{data['name']}主导的事业能量，这种特质让你在职场中有着独特的优势。",
        styles['BodyText']
    ))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 最适合的事业方向", styles['SubSection']))
    for c in data['career']['suitable']:
        story.append(Paragraph(f"✓ {c}", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 不太适合的方向", styles['SubSection']))
    for c in data['career']['不适合']:
        story.append(Paragraph(f"✗ {c}", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 2026年事业建议", styles['SubSection']))
    for i, tip in enumerate(data['career']['tips'], 1):
        story.append(Paragraph(f"{i}. {tip}", styles['BulletText']))
    
    story.append(PageBreak())
    
    # ==================== 四、情感能量解读 ====================
    story.append(Paragraph("四、情感能量解读", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("你的情感特质", styles['SubSection']))
    for t in data['love']['traits']:
        story.append(Paragraph(f"• {t}", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 理想伴侣类型", styles['SubSection']))
    partners_text = "、".join(data['love']['ideal_partner'])
    story.append(Paragraph(f"你最来电的能量类型是：{partners_text}", styles['BodyText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 需要注意的关系", styles['SubSection']))
    avoid_text = "、".join(data['love']['avoid'])
    story.append(Paragraph(f"相处需要磨合的类型是：{avoid_text}", styles['BodyText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 2026年感情建议", styles['SubSection']))
    for tip in data['love']['tips']:
        story.append(Paragraph(f"• {tip}", styles['BulletText']))
    
    story.append(PageBreak())
    
    # ==================== 五、身体健康指南 ====================
    story.append(Paragraph("五、身体健康指南", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("你的身体特质", styles['SubSection']))
    story.append(Paragraph(
        f"{data['name']}能量的人，身体容易在{'、'.join(data['health']['weak_points'])}方面有反应，需要特别注意。",
        styles['BodyText']
    ))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 健康保养建议", styles['SubSection']))
    for tip in data['health']['tips']:
        story.append(Paragraph(f"• {tip}", styles['BulletText']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("身体预警信号", styles['HighlightText']))
    story.append(Paragraph(
        "如果你经常出现以下症状，说明你的能量可能失衡了，需要及时调整：",
        styles['BodyText']
    ))
    story.append(Paragraph("• 长期疲劳、精力不足", styles['BulletText']))
    story.append(Paragraph("• 情绪波动大、难以控制", styles['BulletText']))
    story.append(Paragraph("• 睡眠质量差、失眠多梦", styles['BulletText']))
    
    story.append(PageBreak())
    
    # ==================== 六、2026年度能量趋势 ====================
    story.append(Paragraph("六、2026年度能量趋势", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("你今年的能量周期", styles['SubSection']))
    story.append(Paragraph(
        "2026年是关键的一年，你的能量会有明显的起伏。把握好能量高峰期，规避低谷期，能让你事半功倍。",
        styles['BodyText']
    ))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 上半年（1-6月）", styles['SubSection']))
    story.append(Paragraph("能量逐步回升，适合开始新计划、拓展新关系。这个时期适合主动出击，但要注意节奏。", styles['BodyText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 下半年（7-12月）", styles['SubSection']))
    story.append(Paragraph("能量达到高峰，适合收获成果、做出关键决策。这个时期适合冲刺，但也要注意身体。", styles['BodyText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 今年最关键的月份", styles['SubSection']))
    
    if data['name'] in ['生门', '开门']:
        story.append(Paragraph("3-4月：财运爆发期，适合谈合作、签合同", styles['BulletText']))
        story.append(Paragraph("9-10月：事业高峰，适合做重大决策", styles['BulletText']))
        story.append(Paragraph("6-7月：注意调整节奏，避免过度消耗", styles['BulletText']))
    elif data['name'] in ['休门', '杜门']:
        story.append(Paragraph("5-6月：贵人运旺盛，适合拓展人脉", styles['BulletText']))
        story.append(Paragraph("11-12月：适合沉淀积累，为明年做准备", styles['BulletText']))
        story.append(Paragraph("2-3月：低调行事，不宜冒险", styles['BulletText']))
    else:
        story.append(Paragraph("4-5月：能量上升期，适合开始新项目", styles['BulletText']))
        story.append(Paragraph("8-9月：人际关系活跃期", styles['BulletText']))
        story.append(Paragraph("1-2月：休养生息，不要强求", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 今年要抓住的3个机会", styles['SubSection']))
    story.append(Paragraph("1. 主动拓展高质量人脉圈", styles['BulletText']))
    story.append(Paragraph("2. 尝试新的事业方向或副业", styles['BulletText']))
    story.append(Paragraph("3. 提升专业技能或考取证书", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("◆ 今年要避开的3个坑", styles['SubSection']))
    story.append(Paragraph("1. 避免冲动决策，特别是1-2月", styles['BulletText']))
    story.append(Paragraph("2. 避免过度承诺，量力而行", styles['BulletText']))
    story.append(Paragraph("3. 避免忽略健康透支体力", styles['BulletText']))
    
    story.append(PageBreak())
    
    # ==================== 七、每日行动清单 ====================
    story.append(Paragraph("七、每日行动清单", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("早晨习惯", styles['SubSection']))
    for item in data['action_plan']['morning']:
        story.append(Paragraph(f"• {item}", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("工作时间", styles['SubSection']))
    for item in data['action_plan']['work']:
        story.append(Paragraph(f"• {item}", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("晚间习惯", styles['SubSection']))
    for item in data['action_plan']['evening']:
        story.append(Paragraph(f"• {item}", styles['BulletText']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("本月能量重点", styles['SubSection']))
    story.append(Paragraph("2026年4月：适合整理思路、制定计划，不宜做重大决定。", styles['BodyText']))
    story.append(Paragraph("2026年5月：能量上升期，适合主动出击、拓展业务。", styles['BodyText']))
    
    story.append(PageBreak())
    
    # ==================== 八、八种能量相处指南 ====================
    story.append(Paragraph("八、八种能量相处指南", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph(
        "了解不同能量类型的相处方式，能帮助你更好地处理各种人际关系。",
        styles['BodyText']
    ))
    
    story.append(Spacer(1, 0.3*cm))
    
    # 休门相处指南
    story.append(Paragraph("◆ 休门（情商调和型）相处指南", styles['SubSection']))
    story.append(Paragraph("• 特点：温和包容，善于平衡关系", styles['BulletText']))
    story.append(Paragraph("• 相处之道：给他足够的尊重和安全感", styles['BulletText']))
    story.append(Paragraph("• 沟通建议：直接表达需求，不要让他猜测", styles['BulletText']))
    story.append(Paragraph("• 避免：过于强硬或给他太大压力", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    
    # 生门相处指南
    story.append(Paragraph("◆ 生门（财富创造型）相处指南", styles['SubSection']))
    story.append(Paragraph("• 特点：务实进取，追求实际成果", styles['BulletText']))
    story.append(Paragraph("• 相处之道：用实力说话，给他展示价值的机会", styles['BulletText']))
    story.append(Paragraph("• 沟通建议：简洁高效，不要绕弯子", styles['BulletText']))
    story.append(Paragraph("• 避免：空谈理想不谈利益", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    
    # 伤门相处指南
    story.append(Paragraph("◆ 伤门（突破进取型）相处指南", styles['SubSection']))
    story.append(Paragraph("• 特点：直接大胆，敢于挑战", styles['BulletText']))
    story.append(Paragraph("• 相处之道：尊重他的勇气，给他挑战的空间", styles['BulletText']))
    story.append(Paragraph("• 沟通建议：有话直说，不要拐弯抹角", styles['BulletText']))
    story.append(Paragraph("• 避免：打击他的积极性或过于保守", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    
    # 杜门相处指南
    story.append(Paragraph("◆ 杜门（内敛深藏型）相处指南", styles['SubSection']))
    story.append(Paragraph("• 特点：深思熟虑，低调内敛", styles['BulletText']))
    story.append(Paragraph("• 相处之道：给他独立空间，不要强迫社交", styles['BulletText']))
    story.append(Paragraph("• 沟通建议：真诚直接，不要表面一套背后一套", styles['BulletText']))
    story.append(Paragraph("• 避免：过于喧嚣或强行拉入社交场合", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    
    # 景门相处指南
    story.append(Paragraph("◆ 景门（展示表达型）相处指南", styles['SubSection']))
    story.append(Paragraph("• 特点：魅力四射，善于表达", styles['BulletText']))
    story.append(Paragraph("• 相处之道：欣赏他的魅力，给他展示的舞台", styles['BulletText']))
    story.append(Paragraph("• 沟通建议：热情回应，不要冷场", styles['BulletText']))
    story.append(Paragraph("• 避免：过于挑剔或当众批评他", styles['BulletText']))
    
    story.append(PageBreak())
    
    # 继续相处指南
    story.append(Paragraph("八种能量相处指南（续）", styles['SectionTitle']))
    story.append(Spacer(1, 0.3*cm))
    
    # 死门相处指南
    story.append(Paragraph("◆ 死门（执着坚持型）相处指南", styles['SubSection']))
    story.append(Paragraph("• 特点：专注执着，不轻言放弃", styles['BulletText']))
    story.append(Paragraph("• 相处之道：尊重他的原则，给他时间考虑", styles['BulletText']))
    story.append(Paragraph("• 沟通建议：要有耐心，不要急于求成", styles['BulletText']))
    story.append(Paragraph("• 避免：强行改变他的想法或逼他做决定", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    
    # 惊门相处指南
    story.append(Paragraph("◆ 惊门（变通灵活型）相处指南", styles['SubSection']))
    story.append(Paragraph("• 特点：思维敏捷，善于应变", styles['BulletText']))
    story.append(Paragraph("• 相处之道：欣赏他的创意，给他灵活空间", styles['BulletText']))
    story.append(Paragraph("• 沟通建议：新鲜有趣，不要太死板", styles['BulletText']))
    story.append(Paragraph("• 避免：过度约束或要求他一成不变", styles['BulletText']))
    
    story.append(Spacer(1, 0.3*cm))
    
    # 开门相处指南
    story.append(Paragraph("◆ 开门（开拓领袖型）相处指南", styles['SubSection']))
    story.append(Paragraph("• 特点：格局宏大，善于领导", styles['BulletText']))
    story.append(Paragraph("• 相处之道：尊重他的格局，给他发挥空间", styles['BulletText']))
    story.append(Paragraph("• 沟通建议：有高度，不要只谈细节", styles['BulletText']))
    story.append(Paragraph("• 避免：与他竞争领导地位或过于唠叨", styles['BulletText']))
    
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("与你相处的特别建议", styles['SubSection']))
    
    # 根据用户类型给出特别建议
    advice_map = {
        "休门": "你是温和的协调者，与各类型相处时要记得表达自己的真实想法，不要一味迁就。",
        "生门": "你是务实的创造者，与各类型相处时要记得关注人际关系，不要只有利益。",
        "伤门": "你是勇敢的突破者，与各类型相处时要学会控制情绪，不要过于直接伤人。",
        "杜门": "你是深沉的思考者，与各类型相处时要学会适度展示自己，不要只做幕后英雄。",
        "景门": "你是魅力的传播者，与各类型相处时要学会深度交流，不要只有表面功夫。",
        "死门": "你是坚定的践行者，与各类型相处时要学会变通，不要过于固执不知变通。",
        "惊门": "你是灵活的创意者，与各类型相处时要学会专注深耕，不要只有点子没有行动。",
        "开门": "你是伟大的领导者，与各类型相处时要学会倾听团队意见，不要过于独断专行。"
    }
    story.append(Paragraph(advice_map.get(data['name'], ""), styles['BodyText']))
    
    story.append(PageBreak())
    
    # ==================== 九、深度咨询通道 ====================
    story.append(Paragraph("九、深度咨询通道", styles['SectionTitle']))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("专属咨询邀请", styles['SubSection']))
    story.append(Paragraph(
        "看完这份报告，你可能还有一些具体的问题想要深入了解：",
        styles['BodyText']
    ))
    
    story.append(Spacer(1, 0.3*cm))
    
    questions = [
        "我和他/她的关系到底合不合？未来发展如何？",
        "我现在的事业方向适合我吗？要不要转型？",
        "今年财运如何？有没有能把握的机会？",
        "我想买房/创业/投资，时机对吗？",
        "我的孩子是什么能量类型？如何培养？",
        "我和某个人的关系问题出在哪里？"
    ]
    
    for q in questions:
        story.append(Paragraph(f"• {q}", styles['BulletText']))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("丁老师【一对一深度咨询】可以帮你：", styles['SubSection']))
    benefits = [
        "针对你的具体困惑，深度解读分析",
        "制定专属的个人发展方案",
        "全年能量追踪陪伴，随时答疑",
        "重要决策前的专业建议"
    ]
    for b in benefits:
        story.append(Paragraph(f"✓ {b}", styles['BulletText']))
    
    story.append(Spacer(1, 0.5*cm))
    
    # 咨询价格
    story.append(Paragraph("咨询费用", styles['SubSection']))
    story.append(Paragraph("限时优惠：299元/次（原价599元）", styles['HighlightText']))
    story.append(Paragraph("包含：60分钟一对一深度咨询 + 书面建议 + 30天跟进", styles['BodyText']))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("如何预约深度咨询", styles['SubSection']))
    steps = [
        "1. 关注【预见丁老师】公众号",
        "2. 回复'深度咨询'",
        "3. 助理会联系您确认时间",
        "4. 完成咨询，获得专属方案"
    ]
    for s in steps:
        story.append(Paragraph(s, styles['BulletText']))
    
    story.append(Spacer(1, 1*cm))
    
    # 底部信息
    story.append(Paragraph("— 感谢阅读，祝你在2026年能量满满！—", styles['QuoteText']))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("预见丁老师 · 易学智慧解读", styles['BodyText']))
    
    # 生成PDF
    doc.build(story)
    print(f"报告已生成：{output_path}")

# 生成8种门的报告
if __name__ == "__main__":
    base_path = "E:/虾文档/"
    
    # 生成所有8种门的报告
    for men_type in MEN_DATA.keys():
        output_file = f"{base_path}八门识人_完整版报告_{men_type}_2026.pdf"
        create_report(men_type, output_file)
    
    print("\n全部8种门的报告已生成完毕！")

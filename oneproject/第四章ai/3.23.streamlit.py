from pathlib import Path

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR / "reasources"
AGENT_IMAGE = RESOURCES_DIR / "agent.png"
LOGO_IMAGE = RESOURCES_DIR / "img.png"


st.set_page_config(
    page_title="AI Agent 全景介绍",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://docs.streamlit.io/",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": "# AI Agent 全景介绍页面\n聚焦概念、能力、场景与选型。",
    },
)


st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(31, 119, 180, 0.12), transparent 28%),
            radial-gradient(circle at top right, rgba(255, 127, 80, 0.12), transparent 24%),
            linear-gradient(180deg, #f6f8fb 0%, #eef3f8 100%);
    }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    .hero-card, .info-card, .timeline-card, .case-card {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid rgba(15, 23, 42, 0.08);
        border-radius: 22px;
        padding: 1.2rem 1.4rem;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
        backdrop-filter: blur(8px);
    }
    .hero-title {
        font-size: 2.7rem;
        font-weight: 800;
        line-height: 1.08;
        color: #0f172a;
        margin-bottom: 0.8rem;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #334155;
        margin-bottom: 1rem;
    }
    .tag-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-top: 0.8rem;
    }
    .tag {
        background: linear-gradient(135deg, #0f766e, #1d4ed8);
        color: white;
        border-radius: 999px;
        padding: 0.4rem 0.9rem;
        font-size: 0.88rem;
        font-weight: 600;
    }
    .section-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: #0f172a;
        margin: 1.2rem 0 0.7rem 0;
    }
    .metric-label {
        color: #475569;
        font-size: 0.95rem;
    }
    .metric-value {
        color: #0f172a;
        font-size: 1.7rem;
        font-weight: 800;
    }
    .small-note {
        color: #64748b;
        font-size: 0.92rem;
        line-height: 1.7;
    }
    .timeline-step {
        border-left: 4px solid #0f766e;
        padding-left: 0.9rem;
        margin-bottom: 1rem;
    }
    .timeline-step h4 {
        margin: 0;
        color: #0f172a;
        font-size: 1.02rem;
    }
    .timeline-step p {
        margin: 0.35rem 0 0 0;
        color: #475569;
        line-height: 1.7;
    }
    .highlight {
        background: linear-gradient(120deg, rgba(255, 237, 213, 0.9), rgba(254, 215, 170, 0.75));
        border-radius: 14px;
        padding: 0.9rem 1rem;
        color: #7c2d12;
        font-weight: 600;
    }
    div[data-testid="stDataFrame"] {
        border-radius: 18px;
        overflow: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if LOGO_IMAGE.exists():
    st.logo(str(LOGO_IMAGE))


models_df = pd.DataFrame(
    [
        {
            "模型": "GPT-4o",
            "开发方": "OpenAI",
            "定位": "通用多模态",
            "优势": "对话、代码、图像理解较均衡",
            "适合场景": "智能助手、办公协作、原型开发",
        },
        {
            "模型": "Claude 3.5",
            "开发方": "Anthropic",
            "定位": "推理与写作",
            "优势": "长文处理、分析表达稳定",
            "适合场景": "文档总结、方案撰写、复杂问答",
        },
        {
            "模型": "Gemini 1.5",
            "开发方": "Google",
            "定位": "超长上下文",
            "优势": "长文本、多模态输入处理能力强",
            "适合场景": "长视频摘要、知识库问答",
        },
        {
            "模型": "DeepSeek V3",
            "开发方": "DeepSeek",
            "定位": "中文与代码",
            "优势": "中文表现突出，工程使用门槛低",
            "适合场景": "中文助手、教育、代码生成",
        },
        {
            "模型": "Llama 3",
            "开发方": "Meta",
            "定位": "开源生态",
            "优势": "可私有化部署，便于二次微调",
            "适合场景": "本地部署、行业定制 Agent",
        },
    ]
)


capability_cards = [
    ("规划拆解", "把抽象目标转换为步骤、优先级和执行路径。"),
    ("记忆管理", "结合短期上下文和外部知识库，持续记住事实与偏好。"),
    ("工具调用", "通过 API、数据库、搜索、代码执行完成闭环任务。"),
    ("结果反思", "在执行过程中检查结果、修复错误并继续推进。"),
]

use_cases = [
    ("学习助教", "按知识点生成讲解、练习题和个性化复习计划。"),
    ("办公协同", "自动整理会议纪要、输出行动项并追踪进度。"),
    ("数据分析", "读取表格、生成洞察、给出下一步决策建议。"),
    ("客户服务", "结合知识库与工单系统，完成分流、答复和升级。"),
]


with st.sidebar:
    st.markdown("## 导航")
    st.caption("这个页面聚焦 AI Agent 的核心概念、能力、场景和模型选型。")
    focus = st.selectbox(
        "你当前最关注什么？",
        ["整体理解", "学习入门", "业务应用", "模型选型"],
    )
    maturity = st.slider("你认为自己对 Agent 的熟悉程度", 0, 10, 4)
    preferred_model = st.selectbox(
        "你更想体验哪类模型？",
        ["中文与代码", "推理分析", "多模态交互", "本地部署"],
    )
    st.markdown(
        """
        <div class="highlight">
        提示：如果一个系统只能回答问题，它更像聊天模型；如果它能理解目标、调用工具并交付结果，才更接近 Agent。
        </div>
        """,
        unsafe_allow_html=True,
    )


left_col, right_col = st.columns([1.25, 0.95], gap="large")

with left_col:
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-title">AI Agent 不只是会聊天，而是会完成任务</div>
            <div class="hero-subtitle">
                如果把大语言模型看作“大脑”，那么 Agent 就是在大脑之外加上了“手、眼和工作流”。
                它能够理解目标、做计划、调用工具、检查结果，并在多轮执行中持续推进任务。
            </div>
            <div class="tag-row">
                <span class="tag">目标驱动</span>
                <span class="tag">工具调用</span>
                <span class="tag">多步执行</span>
                <span class="tag">结果交付</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    if AGENT_IMAGE.exists():
        st.image(str(AGENT_IMAGE), use_container_width=True)
    else:
        st.info("未找到配图：reasources/agent.png")


metric_cols = st.columns(4)
metrics = [
    ("核心区别", "能执行", "不只输出文字，而是推动任务完成"),
    ("关键环节", "4 步", "理解目标、规划、调用工具、校验结果"),
    ("典型形态", "多代理", "角色分工协作提高复杂任务表现"),
    ("落地重点", "闭环", "从回答问题升级为交付结果"),
]
for column, (label, value, note) in zip(metric_cols, metrics):
    with column:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="small-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown('<div class="section-title">核心能力</div>', unsafe_allow_html=True)
cap_cols = st.columns(4)
for column, (title, description) in zip(cap_cols, capability_cards):
    with column:
        st.markdown(
            f"""
            <div class="info-card">
                <h4>{title}</h4>
                <div class="small-note">{description}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


process_col, scenario_col = st.columns([1.1, 0.9], gap="large")

with process_col:
    st.markdown('<div class="section-title">Agent 如何工作</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="timeline-card">
            <div class="timeline-step">
                <h4>1. 理解目标</h4>
                <p>把用户的自然语言需求转换成清晰的目标、约束和验收标准。</p>
            </div>
            <div class="timeline-step">
                <h4>2. 规划路径</h4>
                <p>拆分子任务，决定先查什么、再做什么、何时校验结果。</p>
            </div>
            <div class="timeline-step">
                <h4>3. 调用工具</h4>
                <p>连接搜索、数据库、代码执行、办公软件或业务系统完成动作。</p>
            </div>
            <div class="timeline-step">
                <h4>4. 反思与交付</h4>
                <p>判断结果是否达标，不达标则修正，再输出最终结论或产物。</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with scenario_col:
    st.markdown('<div class="section-title">典型应用场景</div>', unsafe_allow_html=True)
    for title, description in use_cases:
        st.markdown(
            f"""
            <div class="case-card">
                <h4>{title}</h4>
                <div class="small-note">{description}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown('<div class="section-title">主流模型观察</div>', unsafe_allow_html=True)
st.dataframe(models_df, use_container_width=True, hide_index=True)


st.markdown('<div class="section-title">交互体验</div>', unsafe_allow_html=True)
input_col, output_col = st.columns([0.95, 1.05], gap="large")

with input_col:
    task_goal = st.text_area(
        "输入一个你希望 Agent 帮你完成的任务",
        placeholder="例如：帮我整理一份关于新能源汽车行业的调研提纲，并给出汇报结构。",
        height=130,
    )
    role = st.radio("你当前的身份更接近", ["学生", "开发者", "产品经理", "运营"], horizontal=True)

with output_col:
    role_map = {
        "学生": "优先关注学习辅导、资料整理和知识点拆解。",
        "开发者": "优先关注代码生成、调试辅助、自动化脚本和文档协作。",
        "产品经理": "优先关注需求分析、竞品研究、PRD 草案和会议纪要。",
        "运营": "优先关注内容生成、活动策划、数据复盘和用户沟通。",
    }
    st.markdown(
        f"""
        <div class="info-card">
            <h4>你的场景建议</h4>
            <div class="small-note">
                关注方向：{focus}<br>
                熟悉程度：{maturity}/10<br>
                偏好模型类型：{preferred_model}<br><br>
                {role_map[role]}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if task_goal.strip():
        st.success(
            "这个任务适合 Agent 处理，因为它同时涉及目标理解、内容生成和可能的多步执行。"
        )
        st.write("建议执行链路：明确目标 -> 搜集资料 -> 输出结构 -> 自检优化。")
    else:
        st.info("输入一个任务后，这里会给出更贴近实际使用的 Agent 判断。")


st.markdown('<div class="section-title">一句话总结</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="hero-card">
        <div class="hero-subtitle">
            AI Agent 的价值不在于“回答得像人”，而在于“像一个数字员工一样推进任务并交付结果”。
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

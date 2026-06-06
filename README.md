# 🎨 AI Design System

AI设计系统工具，支持组件库设计、主题系统、设计规范。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 设计系统设计
- 🧩 组件代码生成
- 🎨 主题配置生成
- 📖 Storybook Stories
- 🎯 图标系统设计
- 🏷️ 设计令牌生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_design_system import create_tools

tools = create_tools()

# 设计系统
ds = tools.design_design_system("MyBrand", "modern")

# 组件生成
component = tools.generate_component("Button", "react")

# 主题配置
theme = tools.generate_theme_config("MyBrand", "light")

# Storybook Stories
stories = tools.generate_storybook_stories("Button", ["primary", "secondary"])

# 图标系统
icons = tools.design_icon_system("outline", ["导航", "操作", "状态"])

# 设计令牌
tokens = tools.generate_design_tokens(ds)
```

## 📁 项目结构

```
ai-design-system/
├── tools.py       # 设计系统工具核心
└── README.md
```

## 📄 许可证

MIT License

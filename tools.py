"""
AI Design System - AI设计系统工具
支持组件库设计、主题系统、设计规范
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDesignSystemTools:
    """
    AI设计系统工具
    支持：组件库、主题、规范
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_design_system(self, brand: str, style: str) -> Dict:
        """设计设计系统"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{brand}设计{style}风格的设计系统：

请返回JSON格式：
{{
    "colors": {{"primary": "#xxx", "secondary": "#xxx", "accent": "#xxx"}},
    "typography": {{"font_family": "字体", "sizes": {{}}}},
    "spacing": {{}},
    "components": ["组件列表"],
    "principles": ["设计原则"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"design_system": content}

    def generate_component(self, component_name: str, framework: str = "react") -> str:
        """生成组件代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{framework} {component_name}组件：

要求：
1. TypeScript
2. 可访问性
3. 主题支持
4. 文档字符串"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_theme_config(self, brand: str, mode: str = "light") -> str:
        """生成主题配置"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{brand}生成{mode}主题配置：

要求：
1. CSS变量
2. 颜色系统
3. 排版系统
4. 间距系统"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def generate_storybook_stories(self, component: str, variants: List[str]) -> str:
        """生成Storybook Stories"""
        if not self.client:
            return "LLM客户端未配置"

        variants_text = ", ".join(variants)

        prompt = f"""请为{component}生成Storybook Stories：

变体：{variants_text}

要求：
1. 所有变体
2. 控制参数
3. 文档"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_icon_system(self, style: str, categories: List[str]) -> Dict:
        """设计图标系统"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        categories_text = ", ".join(categories)

        prompt = f"""请设计{style}风格的图标系统：

类别：{categories_text}

请返回JSON格式：
{{
    "style_guide": "风格指南",
    "categories": [
        {{"name": "类别", "icons": ["图标名"]}}
    ],
    "sizes": ["尺寸"],
    "formats": ["格式"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"icons": content}

    def generate_design_tokens(self, design_system: Dict) -> str:
        """生成设计令牌"""
        if not self.client:
            return "LLM客户端未配置"

        system_text = json.dumps(design_system, ensure_ascii=False)

        prompt = f"""请根据设计系统生成设计令牌：

{system_text}

要求：
1. JSON格式
2. CSS变量
3. 命名规范"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIDesignSystemTools:
    """创建设计系统工具"""
    return AIDesignSystemTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Design System Tools")
    print()

    # 测试
    ds = tools.design_design_system("MyBrand", "modern")
    print(json.dumps(ds, ensure_ascii=False, indent=2))

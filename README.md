# Personal Agent Skills

个人 Cursor Agent Skills 集合，用于在不同项目中复用前端开发与设计相关的工作流。

## 标准 Skill 目录结构

每个 skill 遵循统一布局：

```
my-skill/
├── SKILL.md              # 核心操作手册（必须）
├── scripts/              # 可选：自动化脚本
│   ├── validate.py       # 校验脚本
│   └── scaffold.sh       # 脚手架/部署脚本
├── references/           # 可选：参考文档（按需阅读）
│   ├── examples.md
│   └── guide.md
└── assets/               # 可选：模板与资源（复制到项目中使用）
    └── config-template.json
```

- `SKILL.md`：精简的操作指南，控制在 500 行以内
- `references/`：详细文档，按需阅读（渐进式披露）
- `scripts/`：可执行的校验/自动化脚本
- `assets/`：复制到项目中使用的模板文件

## 本仓库结构

```
skills/
├── README.md
├── frontend-component-design/
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── validate.py
│   │   └── scaffold.sh
│   ├── references/
│   │   ├── examples.md
│   │   ├── patterns-guide.md
│   │   └── accessibility-guide.md
│   └── assets/component-props-template.ts
└── responsive-ui-design/
    ├── SKILL.md
    ├── scripts/
    │   ├── validate.py
    │   └── scaffold.sh
    ├── references/
    │   ├── design-tokens-guide.md
    │   ├── layout-patterns.md
    │   └── breakpoints-guide.md
    └── assets/
        ├── design-tokens-template.json
        └── tailwind-theme-template.js
```

## 安装到 Cursor

将需要的 skill 目录复制到个人 skills 目录：

```bash
# macOS / Linux
cp -r frontend-component-design ~/.cursor/skills/
cp -r responsive-ui-design ~/.cursor/skills/

# Windows (PowerShell)
Copy-Item -Recurse frontend-component-design $env:USERPROFILE\.cursor\skills\
Copy-Item -Recurse responsive-ui-design $env:USERPROFILE\.cursor\skills\
```

或在 Cursor 设置中配置 skills 路径指向本仓库。

## Skills 一览

| Skill | 用途 |
|-------|------|
| [frontend-component-design](./frontend-component-design/) | 设计可复用 UI 组件：Props API、组合模式、无障碍、状态拆分 |
| [responsive-ui-design](./responsive-ui-design/) | 响应式布局、设计令牌、排版间距、Tailwind/CSS 实现规范 |

## 新增 Skill 规范

1. 目录名：小写 + 连字符，如 `my-new-skill`
2. 必须包含 `SKILL.md`（含 `name` 与 `description` frontmatter）
3. 详细内容放入 `references/`，模板放入 `assets/`，校验脚本放入 `scripts/`
4. `description` 用第三人称，写明 **做什么** 和 **何时触发**
5. 不要写入 `~/.cursor/skills-cursor/`（Cursor 内置 skills 目录）

## Commit 规范

本仓库采用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<type>(<scope>): <subject>

<body>
```

常用 type：`feat`（新 skill）、`docs`（文档）、`fix`（修正 skill 内容）、`refactor`（结构调整）

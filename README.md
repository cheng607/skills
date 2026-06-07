# Personal Agent Skills

个人 Cursor Agent Skills 集合，用于在不同项目中复用前端开发与设计相关的工作流。

## 目录结构

```
skills/
├── README.md
├── frontend-component-design/   # 组件设计与实现
│   ├── SKILL.md
│   └── examples.md
└── responsive-ui-design/        # 响应式 UI 与布局
    ├── SKILL.md
    └── reference.md
```

每个 skill 是一个独立目录，核心文件为 `SKILL.md`（含 YAML frontmatter）。

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
2. `SKILL.md` 必须包含 `name` 与 `description` frontmatter
3. `description` 用第三人称，写明 **做什么** 和 **何时触发**
4. 主文件控制在 500 行以内；详细内容放到 `reference.md` / `examples.md`
5. 不要写入 `~/.cursor/skills-cursor/`（Cursor 内置 skills 目录）

## Commit 规范

本仓库采用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<type>(<scope>): <subject>

<body>
```

常用 type：`feat`（新 skill）、`docs`（文档）、`fix`（修正 skill 内容）、`refactor`（结构调整）

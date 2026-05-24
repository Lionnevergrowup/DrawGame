# CLAUDE.md

给以后接手这个项目的 Claude Code 会话看的说明。

## 项目概述

给小朋友(主要 5 岁左右)的画图涂色单页 Web App。50 张卡通线稿 + 30 个贴纸,
浏览器全本地运行,GitHub Pages 托管。所有运行时代码都在一个 `index.html` 里。

线上:https://lionnevergrowup.github.io/DrawGame/

> 早期叫 "Bluey 画图填色",后来全部换成无版权场景。仓库里已经 0 处 Bluey 字样。

## 重要:这个项目用构建脚本

`index.html` 是生成产物 —— 由仓库根目录的 `build.py` 生成。**请改 build.py,然后跑
一次脚本**,不要直接编辑 index.html(任何手改下一次重新构建都会被覆盖)。

构建步骤:

```bash
cd /home/user/DrawGame && python3 build.py
```

build.py 里包含:
- `TEMPLATES` 列表 — 50 个图样,每条 `(key, name, category, svg)`
- `STAMPS` 列表 — 30 个贴纸,每条 `(key, name, viewBox, svg, category)`
- `CATEGORIES` / `STAMP_CATEGORIES` — 分类元数据
- `PATTERNS` — 8 种填色纹路(纯色 / 圆点 / 条纹 / 网格 / 锯齿 / 心 / 星 / 鱼鳞 / 波浪)
- `PALETTE` — 20 色十六进制
- `HTML_HEAD_CSS` / `HTML_BODY` / `JS` — 三个大字符串模板,write_html() 拼起来写出文件

如果要改主样式 / 主 JS,改对应的三大字符串。如果要加图样或贴纸,直接 add() / stamp()。

## 开发分支规则

直接在 `main` 上开发并推送。不要再创建 `claude/...` 功能分支(Pages 环境保护规则
只允许从 main 部署)。推 main 后,`.github/workflows/pages.yml` 自动重新发布,1 分钟生效。

## 关键文件

- `build.py` — 构建脚本(源),里面有数据 + HTML/CSS/JS 三大字符串模板
- `index.html` — 构建产物(浏览器加载这个),~200KB
- `.github/workflows/pages.yml` — GitHub Pages 自动部署
- `README.md` — 用户文档

## 运行时主要模块速查(在生成的 index.html 里都是一段一段标好的)

| 模块 | 干什么 |
|---|---|
| `PAGES` / `STAMPS` / `CATEGORIES` / `PATTERNS` / `PALETTE` | 数据(由 build.py 注入) |
| `state` + `localStorage` 持久化 | 当前工具/颜色/纹路/笔粗细/页面/视图/计时器/各页填色快照(`_pageStates`)/自定义图 |
| `loadPersisted()` / `savePersisted()` | LS key 是 `cga_state_v1`,debounce 350ms,保存当前页面的填色+笔迹+贴纸 |
| `capturePageState()` / `applyPageState()` | 按填色元素索引序号存还原。canvas 用 PNG dataURL 存 |
| `loadPage(key)` | 切图,自动 snapshot 离开的页、复原进入的页 |
| `bindFillable()` | 给 SVG 里 `.fillable` 元素绑点击填色,支持纯色 + url(#pat-xxx) 纹路填充 |
| Pattern defs | `#patternDefsContent` 内置 SVG `<defs>`,8 个 pattern 用当前 accent 色染色 |
| 画笔 canvas | `startStroke/continueStroke/endStroke`,DPR-aware,只在 brush/eraser 工具下接收 pointer |
| Pan/Zoom | 两指捏合 + Ctrl+滚轮,变换在 `.stage-inner` 上,zoom 1-5x |
| Stamp 工具 | `placeStamp(key,x,y,color)` 在 SVG 内插 `<g class="stamp-instance" transform="...">` |
| Picture/Stamp modals | 分类 tab + 缩略图网格,选完关 modal |
| 自定义图上传 | `addCustomPage(dataUrl,label)` → 进 `state.customPages` → 进 LS。删除走缩略图右上 × |
| 倒计时 | `state.timer` { durationSec, startTs, elapsedBefore, paused, fired },chip 上点击开设置 modal,到时弹 `timerExpiredModal` |
| 全屏 | `document.documentElement.requestFullscreen()`,iPad Safari 不支持(提示用"加到主屏幕") |
| 保存 PNG | `saveBtn`,把 SVG 序列化 + canvas 叠加到离屏 canvas → toBlob |

## SVG 模板约定(viewBox 固定 400×300)

- 可填色形状:加 `class="fillable" fill="#ffffff"`
- 固定颜色细节(瞳孔/嘴线):不加 `.fillable`,直接写死 fill
- 外层 `<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">` 统一描边
- **不要做覆盖大半画布的单个 `.fillable` 矩形**。用户专门要求"倒颜料区域不要太大,
  一点一大片就没意思了"。背景留白即可,顶多分多块小区域
- 每张图目标 ≥ 15 个小 `.fillable` 区域,带子结构(熊猫脸有眼眶/眼白/瞳孔分开,
  老虎身上的条纹一条一条独立)

## 贴纸约定(stamp 用)

- viewBox 固定 50×50
- 主体颜色用 `__C__` 占位,运行时被替换为当前选中颜色
- 描边/眼睛之类用 `#1a1a1a` 固定色
- 整体包在 `<g stroke="#1a1a1a" stroke-width="2" stroke-linejoin/cap="round">` 里
- 别太复杂,缩到 50px 还要能看出来

## 约束

- **保持单文件**:`index.html` 是唯一运行产物。不能引外部 JS/CSS。
- **触屏第一**:所有手势用 Pointer Events,`touch-action` 配好,确保 iPad 不会因长按
  弹复制菜单、不会双指缩放页面。
- **不要塞商标卡通形象**(Bluey/米老鼠/小猪佩奇之类),用户需要时通过"上传图片"放进来。
- **localStorage 配额**:画太多页面 + canvas PNG 会爆 5–10MB,代码里已对
  QuotaExceededError 做了提示。如果数据量再涨,考虑只存填色不存 canvas PNG。
- **保存 PNG 的 CORS**:外网 URL 当 `<image>` 用会污染 canvas。URL 载入流程用 `fetch`
  转 dataURL 规避,新增类似功能时保持这条路径。
- **5 岁可用**:所有触摸目标 ≥ 56px,按钮文字够大,主要动作不要藏在二级菜单。

## 本地预览

```bash
python3 -m http.server 8000   # 然后 http://localhost:8000
```

无构建产物(浏览器直接打开生成好的 index.html)。改了 build.py 后重跑一次即可。

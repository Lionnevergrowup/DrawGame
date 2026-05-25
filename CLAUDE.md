# CLAUDE.md

给以后接手这个项目的 Claude Code 会话看的说明。

## 项目概述

给小朋友(主要 5 岁左右)的画图涂色单页 Web App。100 张卡通线稿 + 30 个贴纸,
8 种纹路 + 35 色调色板,自动保存到 localStorage,支持双指缩放 / 全屏 / 倒计时
(单人 + 多人轮流)。**运行时是单个 `index.html`** — 双击即开,部署到 GitHub
Pages 后通过 URL 访问。

线上:https://lionnevergrowup.github.io/DrawGame/

> 早期叫 "Bluey 画图填色",后来全部换成无版权场景。仓库里已经 0 处 Bluey 字样。

## 重要:用构建脚本,源码是模块化的

`index.html` **是生成产物**,不要手改。生成它的源码拆成三个文件:

| 文件 | 干什么 |
|---|---|
| `build.py` | 主脚本。配置(PALETTE / CATEGORIES / PATTERNS)+ HTML/CSS/JS 三大字符串模板 + `write_html()` 拼起来 |
| `templates.py` | 100 张图样的数据(每条 `add(key, name, category, svg)`) |
| `stamps.py` | 30 个贴纸的数据(每条 `stamp(key, name, vb, svg, category)`) |
| `index.html` | 构建产物(浏览器加载这个),~320KB |

构建步骤:

```bash
cd /home/user/DrawGame && python3 build.py
```

如果要改主样式 / 主 JS:改 `build.py` 里的 `HTML_HEAD_CSS` / `HTML_BODY` / `JS`
三大字符串。如果要加图样:在 `templates.py` 里调一次 `add(...)`。要加贴纸:
在 `stamps.py` 里调 `stamp(...)`。改完跑一次 `python3 build.py` 重新生成 index.html。

## 开发分支规则

直接在 `main` 上开发并推送。不要再创建 `claude/...` 功能分支(Pages 环境保护规则
只允许从 main 部署)。推 main 后,`.github/workflows/pages.yml` 自动重新发布,
1 分钟生效。

## 关键文件

- `build.py` — 构建脚本(主),配置 + HTML/CSS/JS 模板 + 拼装逻辑
- `templates.py` — 100 个图样的 SVG 数据
- `stamps.py` — 30 个贴纸的 SVG 数据
- `index.html` — 构建产物(浏览器加载这个)
- `.github/workflows/pages.yml` — GitHub Pages 自动部署
- `README.md` — 给最终用户看的中文说明

## 运行时模块速查(在生成的 index.html 里都是一段一段标好的)

| 模块 | 干什么 |
|---|---|
| `PAGES` / `STAMPS` / `CATEGORIES` / `STAMP_CATEGORIES` / `PATTERNS` / `PALETTE` | 数据(由 build.py 注入) |
| `state` + `localStorage` 持久化 | 当前工具/颜色/纹路/笔粗细/贴纸大小/页面/视图/计时器/各页填色快照(`_pageStates`)/自定义图 |
| `loadPersisted()` / `savePersisted()` | LS key 是 `cga_state_v1`,debounce 350ms |
| `capturePageState()` / `applyPageState()` | 按填色元素索引序号存还原。纹路填色保存为 `{p: patternKey, c: color}`,canvas 用 PNG dataURL |
| `loadPage(key)` | 切图,自动 snapshot 离开的页、复原进入的页 |
| `bindFillable()` | 给 SVG 里 `.fillable` 元素绑点击:**fill 工具**填当前色/纹,**eraser 工具**还原成白(支持纹路) |
| `svgStampClick()` | 点 SVG 时:stamp 工具放贴纸;eraser 工具删贴纸 |
| `patternInstanceFor(key, color)` | **每个 (纹路, 颜色) 组合生成独立 `<pattern>` 实例并缓存**,所以换颜色不会影响之前画的 |
| `patternDefsContent` | 全局 `<defs>`,放所有 pattern 实例 |
| 画笔 canvas | `startStroke/continueStroke/endStroke`,DPR-aware,只在 brush/eraser 工具下接收 pointer |
| Pan/Zoom | 两指捏合 + Ctrl+滚轮,变换在 `.stage-inner` 上,zoom 1–5x |
| Stamp 工具 | `placeStamp(key,x,y,color,addHistory,patternKey,size)` 在 SVG 内插 `<g class="stamp-instance" transform="...">`,**支持纹路填充和可调大小** |
| 色板 / 纹路 popup | 主屏只有"颜色"和"纹路"两个 popup 按钮,点开才出选项,不平铺 |
| Picture/Stamp modals | 分类 tab + 缩略图网格。**选 stamp 工具自动开贴纸窗** |
| 自定义图上传 | `addCustomPage(dataUrl,label)` → 进 `state.customPages` → 进 LS。删除走缩略图右上 × |
| **Google 搜图** | `doGoogleSearch()`,使用 Google Custom Search JSON API。用户在 ⚙️ 设置面板填 key + cx,存 localStorage |
| 倒计时 | **支持单人 + 多人轮流**(玩家数 + 每人时长 + 总轮数;最后一轮结束后弹"都画完啦",可"再玩一局")。`state.timer` { mode, durationSec, startTs, elapsedBefore, paused, fired, playerCount, currentPlayer, totalRounds, currentRound, done } |
| 全屏 | `document.documentElement.requestFullscreen()`,iPad Safari 不支持(提示用"加到主屏幕") |
| 保存 PNG | `saveBtn`,把 SVG + pattern defs 序列化 + canvas 叠加到离屏 canvas → toBlob |

## SVG 模板约定(viewBox 固定 400×300)

- 可填色形状:加 `class="fillable" fill="#ffffff"`
- 固定颜色细节(瞳孔/嘴线):不加 `.fillable`,直接写死 fill
- 外层 `<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">` 统一描边
- **不要做覆盖大半画布的单个 `.fillable` 矩形**。用户专门要求"倒颜料区域不要太大,
  一点一大片就没意思了"。背景留白即可
- 每张图目标 ≥ 15 个小 `.fillable` 区域,带子结构(熊猫脸有眼眶/眼白/瞳孔分开,
  老虎身上的条纹一条一条独立)

## 贴纸约定(stamp 用)

- viewBox 固定 50×50
- 主体颜色用 `__C__` 占位,运行时被替换为当前选中颜色(支持纹路 url)
- 描边/眼睛之类用 `#1a1a1a` 固定色
- 整体包在 `<g stroke="#1a1a1a" stroke-width="2" stroke-linejoin/cap="round">` 里
- 别太复杂,缩到 50px 还要能看出来

## 约束

- **运行时保持单文件**:`index.html` 是唯一运行产物。不能引外部 JS/CSS。源码模块化
  是 build 时的事(`templates.py` / `stamps.py`)。
- **触屏第一**:所有手势用 Pointer Events,`touch-action` 配好,确保 iPad 不会因长按
  弹复制菜单、不会双指缩放页面。
- **不要塞商标卡通形象**(Bluey/米老鼠/小猪佩奇之类),用户需要时通过"上传图片"或
  Google 搜图功能放进来。
- **localStorage 配额**:画太多页面 + canvas PNG 会爆 5–10MB,代码里已对
  QuotaExceededError 做了提示。如果数据量再涨,考虑只存填色不存 canvas PNG。
- **保存 PNG 的 CORS**:外网 URL 当 `<image>` 用会污染 canvas。URL 载入流程用 `fetch`
  转 dataURL 规避,新增类似功能时保持这条路径。
- **5 岁可用**:所有触摸目标 ≥ 56px(手机 ≥ 44px),按钮文字够大,选项太多用 popup
  收起来不要平铺。
- **纹路实例化**:**不要回退到全局共享 pattern**。每次填色要走 `patternInstanceFor()`
  生成独立实例,否则换颜色会污染之前画的。

## 本地预览

```bash
python3 -m http.server 8000   # 然后 http://localhost:8000
```

或者直接在浏览器打开 `index.html`。改了 build.py / templates.py / stamps.py 后
重跑 `python3 build.py` 重新生成 index.html。

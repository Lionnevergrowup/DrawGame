# CLAUDE.md

给以后接手这个项目的 Claude Code 会话看的说明。

## 项目概述

一个给小朋友的 Bluey 风格画图填色网页应用,**所有代码都在一个 `index.html` 里**(内联 CSS + JS + SVG),无构建步骤、无依赖、无服务器。直接双击就能开,部署到 GitHub Pages 后通过 URL 访问。

线上地址:https://lionnevergrowup.github.io/DrawGame/

## 开发分支规则

**直接在 `main` 上开发并推送。** 不要再创建 `claude/...` 形式的功能分支(GitHub Pages 环境保护规则只允许从 main 部署,在功能分支上开发会卡在部署一步)。

每次推送 `main` 后,`.github/workflows/pages.yml` 会自动把站点重新发布,大约 1 分钟生效。

## 关键文件

- `index.html` — 整个应用,**所有改动几乎都发生在这里**
- `.github/workflows/pages.yml` — GitHub Pages 自动部署,通常不需要改
- `README.md` — 给最终用户看的中文说明

## index.html 结构速查

| 区域 | 在哪 |
|---|---|
| 样式 | `<style>` 单块,顶部有 CSS 变量(主色 `--bluey-blue`) |
| 着色图样数据 | JS 里的 `const PAGES = { ... }`,每条 `{ name, svg }`。新增图只要往里加一个 key 即可 |
| 调色板颜色 | `const PALETTE = [...]`,15 色十六进制数组 |
| 工具切换(填色/画笔/橡皮) | `toolbar.addEventListener('click', ...)` |
| 点击填色逻辑 | `bindFillable()`,绑在 SVG 里 `class="fillable"` 的元素上 |
| 画笔/橡皮(Canvas) | `startDraw/moveDraw/endDraw`,用 Pointer + Touch 事件 |
| 撤销 | 单个 `state.history` 栈,两种条目:`{kind:'fill', el, prevColor}` 和 `{kind:'stroke', imageData}` |
| 保存 PNG | `saveBtn` 处理器,把 SVG 序列化成 data URL 后画到离屏 canvas,再叠加画笔 canvas |
| 自定义图(上传/URL/Google) | `addCustomPage(dataUrl, label)`、`fileInput`、`urlLoadBtn`、`googleBtn` |
| 帮助弹窗 | `#helpModal`,首次打开自动弹(`localStorage` 标记 `bluey_help_seen`) |

## SVG 着色图样的约定

每条 `PAGES` 条目的 `svg` 是一段内联 `<g>...</g>`(viewBox 固定 `0 0 400 300`):

- 想被点击填色的形状加 `class="fillable" fill="#ffffff"`(用白色作底,这样调色板的颜色才能正常覆盖)
- 不想被填的部分(瞳孔、嘴线等)就不加 `class="fillable"`,直接写死颜色
- 描边统一在外层 `<g>` 上设 `stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"`

加新图模板:
```js
mykey: {
  name: '展示名',
  svg: `
    <g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
      <rect class="fillable" fill="#ffffff" x="0" y="0" width="400" height="300"/>
      <!-- 各个区块 -->
    </g>`
}
```

## 约束 / 注意事项

- **保持单文件**:不要引入打包工具、外部 JS/CSS、npm 包。所有逻辑都进 `index.html`。
- **触屏第一**:任何新交互都要 Pointer Events + `touch-action: none`(canvas)/`manipulation`(body),iPad 上验证。
- **不要往 SVG 里塞官方 Bluey 美术资源**:Bluey 是 Ludo Studio 商标,只做"卡通蓝色狗狗"风格简笔画。用户想用真实着色页时,通过自定义图功能上传。
- **保存 PNG 的 CORS 风险**:`<image>` 引用外网 URL 会污染 canvas 导致 `toBlob` 抛错。URL 载入流程已经先用 `fetch` 转 data URL,新增类似功能时务必保持这条路径。
- **不要破坏 viewBox `0 0 400 300`**:很多坐标硬编码在里面,改 viewBox 等于要重排所有图样。

## 本地预览

```bash
# 任意一种都行
open index.html                       # macOS
python3 -m http.server 8000           # 然后 http://localhost:8000
```

无构建、无测试套件,改完直接浏览器刷新看效果即可。

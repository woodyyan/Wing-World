# 岚翎世界百科（Wing-World）

介绍岚翎世界的纯静态多页百科网站。内容来自已有完整设定集，以世界内部视角组织，不将资料不足的细目补写为事实。

## 网站内容

- 66个完整词条、83个HTML页面。
- 8个主题栏目、8个观察维度、8个应用场景、222个标签。
- 16幅SVG系统图解，包括城市双网节点图与四层剖面。
- 分类导航、全文搜索、组合筛选、词条目录和关联链接。
- 桌面与移动排版；移动端支持展开原尺寸图解。

网站不需要后端、数据库、环境变量或第三方运行依赖。图解嵌入页面，搜索在浏览器中完成。

## 目录结构

```text
Wing-World/
├── index.html              # 首页
├── all.html                # 全部词条及组合筛选
├── search.html             # 全文搜索
├── category-*.html         # 分类目录
├── e-*.html                # 百科词条
├── atlas.html              # 图解总览
├── tags.html               # 标签索引
├── dimensions.html         # 观察维度
├── scenarios.html          # 应用场景
├── sources.html            # 资料依据与统一术语
├── gaps.html               # 待补资料
├── style.css               # 共享样式
├── site.js                 # 共享浏览交互
├── scripts/                # 校验、构建及本地预览
├── package.json
├── static-assets.json      # 部署资源白名单
├── vercel.json
└── dist/                   # 构建输出，Git忽略
```

`.workbuddy/`与`outputs/`保留在本地，不纳入Git或部署包。根目录HTML是当前维护的源码；修改这里，不要直接修改`dist/`或旧交付副本。

## 本地运行

要求Node.js 22或更高版本。没有依赖，无需先执行`npm install`。

```bash
npm run dev
```

打开`http://127.0.0.1:3000`。该预览只绑定本机地址。

```bash
# 校验HTML、站内链接、搜索索引、脚本和部署配置
npm run check

# 校验后将83个HTML与共享CSS/JS复制至dist
npm run build

# 浏览构建后的站点
npm run preview
```

可用`PORT=4173 npm run dev`调整端口。也可解压完整静态交付包后直接打开`index.html`，但使用本地HTTP预览更适合检查部署行为。

构建仅复制`static-assets.json`明确列出的HTML及`style.css`、`site.js`。未知HTML、符号链接或未知构建目录内容会使构建中止，且不会清空该目录。说明文档、Git目录、本地资料、ZIP、环境文件或脚本不会进入`dist`。

`.vercelignore`另行排除本地资料、环境文件与密钥，避免它们进入CLI源码上传包。部署产物范围与源码上传范围是两项独立检查。新增页面、图片或字体时，需要同时更新资源白名单和校验器。

## Vercel部署配置

仓库内的`vercel.json`已配置为静态站点：

| 配置 | 值 |
| --- | --- |
| Framework Preset | Other（`framework: null`） |
| Root Directory | 仓库根目录 |
| Install Command | 空字符串，跳过安装 |
| Build Command | `npm run build` |
| Output Directory | `dist` |
| Node.js | 22.x或更高 |
| HTML地址 | 保留`.html`后缀 |

使用文件路径路由，无单页应用回退或全站重写。已有分类、搜索查询参数和词条链接保持原样。仅`dist`内容会被作为网站公开提供。

后续需要实际部署时，可在Vercel导入代码仓库，或在项目根目录运行Vercel CLI。**本次交付仅准备配置并在本地提交代码，未推送远程、未创建云端部署。**

## Git管理

默认分支为`main`。网站源码、部署配置、校验脚本及本说明纳入版本管理；构建结果、原交付素材与本地工作记录被忽略。

```bash
git status
git log --oneline -5
npm run check
git add <本次修改的文件>
git commit -m "描述本次修改"
```

不要将密钥、`.env`、验证缓存或原始资料强制加入仓库。未经明确授权，不执行远程推送。

## 内容维护

- 保持岚翎内部视角、客观说明文风与术语一致。
- 未确定参数、地点、机构或事件标注“待补充”。
- 假设情境不作为历史事件；原始约略年代保留限定。
- 修改词条时同步相关目录、关联链接，以及`all.html`和`search.html`中的全文索引。
- 新增空间、结构或流程内容时提供相关图解与图注，并测试移动端展开阅读。

Vercel配置依据：[静态站点构建说明](https://vercel.com/docs/builds/configure-a-build)、[vercel.json配置参考](https://vercel.com/docs/project-configuration/vercel-json)。

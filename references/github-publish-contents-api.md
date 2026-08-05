# GitHub 发布：受限 fine-grained PAT + Contents API 直推（无 git / 无 gh）

场景：沙箱没装 `gh`、不想在发布目录跑 `git init`，或系统环境对 git 交互不便。用 **GitHub REST Contents API** 直接把文件推到空仓库，纯 Python stdlib（urllib），无需任何额外依赖。

> ⛔ 前置：该 PAT（fine-grained access token）必须被授权**访问目标仓库**，且至少 `Contents: Read and write`。细粒度 token 默认只授给它被勾选的仓库；新建的仓库默认**不在**范围内（会 403）。

## 0. 权限探测（先做，再推）

```python
import base64, json, urllib.request
pat = base64.b64decode("<BASE64_PAT>").decode()  # 或从环境变量读
def req(method, path, data=None):
    body = json.dumps(data).encode() if data is not None else None
    r = urllib.request.Request(f"https://api.github.com{path}", method=method, data=body,
        headers={"Authorization":f"token {pat}","Accept":"application/vnd.github+json",
                 "Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(r, timeout=15) as resp: return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e: return e.code, e.read().decode()[:300]

s,_ = req("GET","/user");                     # 账号核对
s,_ = req("GET","/repos/Dellazj/amz-x");      # 200=有访问权, 403/404=受限PAT无权限
# 写权限探测：上传再删除临时文件
import base64 as b64
s,b = req("PUT","/repos/Dellazj/amz-x/contents/_perm_test.txt",
          {"message":"perm test","content":b64.b64encode(b"x").decode()})
print("write PUT:", s)                        # 201 = 有写权限
if s==201:
    sha = json.loads(b).get("content",{}).get("sha")
    req("DELETE","/repos/Dellazj/amz-x/contents/_perm_test.txt",{"message":"cleanup","sha":sha})
```

关键判定：
- `GET /user` 返回的 `login` 必须是你预期的账号。
- `GET /repos/...` 返回 **200** 且 `permissions.push:true`（或 `admin:true`）→ 可写。**403/404** → 让用户在 GitHub 上把该 token 的 Repository access 加上目标仓库，或重新生成 token。
- 拿不到写权限就直接给它建私有仓库或换 token，**不要硬推**。

## 1. 逐个上传文件（空仓库场景）

```python
def put_file(owner, repo, repo_path, local_path, message):
    with open(local_path,'rb') as f: b64 = base64.b64encode(f.read()).decode()
    s,b = req("PUT", f"/repos/{owner}/{repo}/contents/{repo_path}",
              {"message":message,"content":b64})
    print(f"PUT {repo_path}: HTTP {s}")   # 201 = 成功
```
要点：
- 文件内容用 **base64（UTF-8 bytes）** 编码，不是明文。
- 空仓库上传没有冲突；若已有文件，PUT 会因缺 `sha` 报 409 → 需先 `GET /contents/{path}` 拿 `sha` 再带上（覆盖更新）。
- 目录路径直接写在 repo_path 里（如 `references/pure-css-trend-curves.md`），API 会自动建目录。

## 2. 验证推送结果

```python
s, tree = req("GET","/repos/{owner}/{repo}/git/trees/main?recursive=1")
# 打印每个 node 的 type 和 path，确认文件齐全、无漏传
```
再 `GET /repos/{owner}/{repo}` 拿 `html_url` 返回用户。

## 3. 发布物离线组装（推荐做法）

不要直接从工作目录 git push 整个目录（会把 state.db/logs/旧报告等带进去）。正确流程：
1. 建**干净暂存目录**：`rm -rf /tmp/gh_repo && mkdir -p /tmp/gh_repo/references`
2. 只 `cp` 要发布的文件进去。
3. 在暂存目录做**敏感扫描**：`grep -rInE "apikey|token|secret|@gmail|/opt/|cf_env|mcp_client|first-run" .`——确认剩余命中都是通用警示/示例文本，而非真实凭据或内部路径。
4. 对要发布的 SKILL.md/脚本做脱敏（内部绝对路径 → 相对/占位符；删掉指向被排除 reference 的悬空链接；品类专用脚本如含产品数据需参数化或干脆只发 SKILL+通用组件）。
5. 用 Contents API 从暂存目录逐个上传（或 git push）。

（详见主 SKILL 的「公开分享 / GitHub 发布前脱敏清单」配套使用。）

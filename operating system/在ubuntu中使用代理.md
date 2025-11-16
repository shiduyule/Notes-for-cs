
✅ 第一部分：让 WSL Ubuntu 走 Clash 代理
1️⃣ 打开 WSL Ubuntu
```bash
nano ~/.bashrc
```

2️⃣ 在文件末尾追加如下内容

⚠️ 已经根据你提供的信息 自动替换成 172.23.176.1:7890，直接复制即可。

```bash
# ---- WSL 全局 HTTP/HTTPS 代理 ----
export HTTP_PROXY="http://172.23.176.1:7890"
export HTTPS_PROXY="$HTTP_PROXY"
export ALL_PROXY="$HTTP_PROXY"
export NO_PROXY="localhost,127.0.0.1,::1"
```


# 使用更全面的基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# 安装系统依赖（以Debian/Ubuntu为例）
RUN apt-get update 
RUN apt-get install -y \
    build-essential \
    libpq-dev \
    libmysqlclient-dev \
    # 根据需要添加其他依赖

    # 复制requirements.txt到容器中
    COPY requirements.txt /app/

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制其余的项目文件到容器中（确保.dockerignore文件配置得当，以避免复制不必要的文件）
COPY . /app

# 容器启动时执行的命令
CMD ["python", "your_app.py"]

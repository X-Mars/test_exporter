### 项目介绍
1. prometheus exporter 开发示例代码
2. 可以基于该功能扩展其他功能
### 食用方法
1. 安装组件
```shell
pip install flask 
```
2. 启动服务
```shell
python -m flask run --host=192.168.68.244
```
3. prometheus.yml 添加以下配置
```yml
  - job_name: "test_exporter"
    static_configs:
      - targets: ["192.168.68.244:5000"]
```
4. 访问 prometheus web 检索
5. 
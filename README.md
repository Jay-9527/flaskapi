# 环境配置项目法
通过设置好环境变量，以某种方法导入到项目中，为项目进行初始化做准备。

用法： os.getenv(key, default = None) 

参数:
key:表示环境变量名称的字符串
默认值(可选)：表示 key 不存在时默认值的字符串。如果省略，则默认设置为“无”。
返回类型：此方法返回一个字符串，该字符串表示环境变量键的值。如果 key 不存在，则返回默认参数的值。


> DB_URL = os.getenv("DB_URL", os.path.join(os.environ.get("DB_URL")))

os.getenv 和 os.path.join的使用。
在使用getenv时，不用结合path，因为path是从文件系统中获取值，所得来的结果不是键值对的形式。

marshmallow

marshmallow是一个用来将复杂的orm对象与python原生数据类型之间相互转换的库，简而言之，就是实现
object -> dict， objects -> list， string -> dict和 string -> list。

# 项目的配置流程
1. 把配置文件创建，并编写好配置文件【项目环境配置文件】
2. 创建application配置文件，里头存放创建APP的内容【项目启动文件】
3. 创建application管理文件名为：manager，里头存放项目初始化的方法和蓝图映射方法。【项目管理文件】
4. 创建软件包，存放模块（业务）。在里头编写__init__文件，统一管理模块。
5. 创建环境变量脚本。为项目提供环境变量。


error已经告诉你了 list对象不能用函数形式调用，就是不能callable。
简单来说就是list变量和list函数重名了。
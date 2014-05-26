# The Client Of DO In PC

## 账户篇

### 注册

```python
from account import *

account = Account()
response = account.regist(user_name=.., email=.., phone_number=.., password=..)

print response.text
```

### 登录

```python
from account import *

account = Account()
response = account.log_in(log_in_tag='email', tag_info=..., password=...)

print response.text
```

### 查看自己的信息

```python
from account import *

account = Account()
account.log_in(log_in_tag='email', tag_info=..., password=...)
response = account.look_my_profile()

print response.text
```


## 项目篇

### 创建项目

```python
from account import *
from item import *

account = Account()
account.log_in(log_in_tag='email', tag_info=..., password=...)

item_handler = Item(account)
mission_info = create_mission_info()  # 这一步生成预设的项目信息，可以参考自设

response = item_handler.post_item(mission_info)

print response.text
```

### 得到新项目列表

```python
from account import *
from item import *

account = Account()
account.log_in(log_in_tag='email', tag_info=..., password=...)

item_handler = Item(account)

response = item_handler.get_new_items(ids=[])   # 可以填入本地已有的项目id(创建项目时会反馈)以过滤掉比ids内id旧的信息

print response.text
```

## 得到项目详细信息

```python
from account import *
from item import *

account = Account()
account.log_in(log_in_tag='email', tag_info=..., password=...)

item_handler = Item(account)

response = item_handler.(mission_id)

print response.text
```

### 接受项目

```python
from account import *
from item import *

account = Account()
account.log_in(log_in_tag='email', tag_info=..., password=...)

item_handler = Item(account)

response = item_handler.recieve_item(mission_id)             # 项目id，可通过多种方法得到

print response.text
```

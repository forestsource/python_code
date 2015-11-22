
* 文字列内の任意文字の個数カウント

``` python
string , number = map(str, raw_input().split(","))
string = map(str,inout)
string = ''.join(string)
print string.count()
```

* 進捗管理
* import sys
all_task,clear_task,symbol = map(str, raw_input().split(","))
all_task = int(all_task)
clear_task = int(clear_task)
if all_task < clear_task:
    print "invalid"
else:
    percent = (clear_task / float(all_task) * 100)
    for i in range(int(percent)):
        sys.stdout.write(symbol)
    sys.stdout.write("\n")

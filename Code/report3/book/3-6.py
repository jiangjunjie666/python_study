# 列表的添加操作
names = ["alice", "bob", "cindy"]
# 前面插入
names.insert(0, "david")
# 中间插入
names.insert(2, "john")
# 后面插入
names.append("david")

for i in names:
    print(i)

#  列表的删除操作
# 使用pop删除到只剩二个
for i in range(4):
    names.pop()
print(names)

# 使用del删除全部
del names[:]
print(names)

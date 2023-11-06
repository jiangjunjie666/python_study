# [Currying versus partial application](https://2ality.com/2011/09/currying-vs-part-eval.html)是将一个函数转换为具有更小arity(参数更少)的另一个函数的两种方法。虽然它们经常被混淆，但它们的工作方式是不同的。目标是学会区分它们。

# Currying

# 是一种将接受多个参数的函数转换为以每个参数都只接受一个参数的一系列函数链的技术。

# Currying接受一个函数：

# ```python
# f：X × Y → R
# ```

# 并将其转换为一个函数：

# ```python
# f'：X → (Y → R)
# ```

# 我们不再使用两个参数调用f，而是使用第一个参数调用f'。结果是一个函数，然后我们使用第二个参数调用该函数来产生结果。因此，如果非curried f被调用为：

# ```python
# f(3, 5)
# ```

# 那么curried f'被调用为：

# ```python
# f'(3)(5)
# ```

# 示例
# 给定以下函数：

# ```python
# def add(x, y, z):
#   return x + y + z
# ```

# 我们可以以普通方式调用：

# ```python
# add(1, 2, 3) # => 6
# ```

# 但我们可以创建一个curried版本的add(a, b, c)函数：

# ```python
# curriedAdd = lambda a: (lambda b: (lambda c: add(a,b,c)))
# curriedAdd(1)(2)(3) # => 6
# ```

# Partial application
# 是将一定数量的参数固定到函数中，从而产生另一个更小arity(参数更少)的函数的过程。

# 部分应用接受一个函数：

# ```python
# f：X × Y → R
# ```

# 和一个固定值x作为第一个参数，以产生一个新的函数

# ```python
# f'：Y → R
# ```

# f'与f执行的操作相同，但只需要填写第二个参数，这就是其arity比f的arity少一个的原因。可以说第一个参数绑定到x。

# 示例:

# ```python
# partialAdd = lambda a: (lambda *args: add(a,*args))
# partialAdd(1)(2, 3) # => 6
# ```

# 你的任务是实现一个名为curryPartial()的通用函数，可以进行currying或部分应用。

# 例如：

# ```python
# curriedAdd = curryPartial(add)
# curriedAdd(1)(2)(3) # => 6

# partialAdd = curryPartial(add, 1)
# partialAdd(2, 3) # => 6
# ```

# 我们希望函数保持灵活性。

# 所有下面这些例子都应该产生相同的结果：

# ```python
# curryPartial(add)(1)(2)(3) # =>6
# curryPartial(add, 1)(2)(3) # =>6
# curryPartial(add, 1)(2, 3) # =>6
# curryPartial(add, 1, 2)(3) # =>6
# curryPartial(add, 1, 2, 3) # =>6
# curryPartial(add)(1, 2, 3) # =>6
# curryPartial(add)(1, 2)(3) # =>6
# curryPartial(add)()(1, 2, 3) # =>6
# curryPartial(add)()(1)()()(2)(3) # =>6

# curryPartial(add)()(1)()()(2)(3, 4, 5, 6) # =>6
# curryPartial(add, 1)(2, 3, 4, 5) # =>6

# curryPartial(curryPartial(curryPartial(add, 1), 2), 3) # =>6
# curryPartial(curryPartial(add, 1, 2), 3) # =>6
# curryPartial(curryPartial(add, 1), 2, 3) # =>6
# curryPartial(curryPartial(add, 1), 2)(3) # =>6
# curryPartial(curryPartial(add, 1)(2), 3) # =>6
# curryPartial(curryPartial(curryPartial(add, 1)), 2, 3) # =>6
# ```

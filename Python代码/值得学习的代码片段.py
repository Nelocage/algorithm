def use_logging(func):
    loging.warn("%s is running" % func.__name__)  #函数还有这个属性！
    func()

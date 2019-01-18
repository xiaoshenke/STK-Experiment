#!/usr/bin/python
# coding=utf-8

# 日内策略的支持

# 1, strategy.base_strategy设计api set_use_inn_api,便于子类迅速开始日内模式
# 2, strategy.composition支持参数 use_inn_api,用来在初始化df的时候使用inn_util.get_inn_mixed_df

# 3, 具体的features的计算函数支持日内模式,比如features.xt.brk_util.find_brk_df_days_inn -> 因为日内模式的判断也会略有不同
# 4, strategy子类在use_inn_api为true的时候,在get_composite_stra函数中调用相应的inn feature函数,如 strategy.single.brkxt func = find_brk_df_days if not self.use_inn_api else find_brk_df_days_inn -> 且注意对应的comp的设置

# 5, 在inn文件下的文件中开启use_inn_api选项,如inn_strategy.brkxt_inn.apply_brkxt brk = BrkxtStrategy().set_use_inn_api(True);df = brk.apply([ser['code']],start,self.day,on_pp=False)

# 因此由上面的过程知,若新的算子要支持日内模式,需要以下三个步骤
# 1 feature的支持
# 2 strategy子类在构建compostion的时候使用inn的api
# 3 inn策略开启strategy子类的inn模式


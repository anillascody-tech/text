#类型注解
#变量名: 数据容器类型[类型]
#name: int =
#names: list[str | int] =
#  | 类似于and
#phones: set[str] =
#options: dict[str,int] =
#goods: tuple[str,int,int] =
#未添加注解时,python会进行类型推断
#添加了注解只起提示效果,并不会影响实际运行
#有默认值就不用注解
def calc(scores: list[int] = (0,1) ) -> float:
    return sum(scores)/len(scores)

def calc_data(scores: list[int]) -> tuple[int,float]:
    return max(scores),sum(scores)/len(scores)
al  =calc([1,2,6])


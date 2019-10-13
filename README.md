# draw
数据可视化--Python 3/前端 画图工具：Matplotlib，canvajs，pyecharts                  


之前我一直是用Matplotlib画图，写了挺多博客：                  

*   [Python：matplotlib绘图时指定图像大小，放大图像](https://blog.csdn.net/zhangpeterx/article/details/90734660)                    
*   [matplotlib绘制平滑的曲线](https://blog.csdn.net/zhangpeterx/article/details/83684239)                           
*   [Matplotlib使用日期作为横坐标](https://blog.csdn.net/zhangpeterx/article/details/83628558)                            
*   [matplotlib 设置坐标轴单位](https://blog.csdn.net/zhangpeterx/article/details/96887459)                               

Matplotlib画图示例如下：                  

```python
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y = [5, 20, 36, 10, 75, 90]
plt.title("商家A")
plt.bar(x, y)
plt.show()

```
结果如图所示：                                    
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190822201255258.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5ncGV0ZXJ4,size_16,color_FFFFFF,t_70)                  

怎么说呢，用Matplotlib画图很朴实。                  
*******
现在前端发展太快了，感觉这种图太朴素了，不够炫酷。                  

我现在经常使用canvajs画图，官网：[Beautiful HTML5 JavaScript Charts](https://canvasjs.com/)                  

代码如下：
```js
        function draw() {
            var chart = new CanvasJS.Chart("chartContainer", {
                theme: "light2",
                title: {
                    text: "商家A"
                },
                data: [{
                    type: "bar",
                    dataPoints: [ //array
                        {label: "衬衫", y: 5},
                        {label: "羊毛衫", y: 20},
                        {label: "雪纺衫", y: 36},
                        {label: "裤子", y: 10},
                        {label: "高跟鞋", y: 75},
                        {label: "袜子", y: 90},
                    ]
                }]
            });
            chart.render();
        }
```

效果如图所示：                  

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190822201314954.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5ncGV0ZXJ4,size_16,color_FFFFFF,t_70)                  
从效果来看，明显炫酷多了。
*********                  
最近发现了另外一个工具：`pyecharts`                  

这个工具是把`echarts`用Python进行操作，代码如下：                  
```python
from pyecharts.charts import Bar
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()
```
效果图如下：                  
![在这里插入图片描述](https://img-blog.csdnimg.cn/201908222023335.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5ncGV0ZXJ4,size_16,color_FFFFFF,t_70)                  

感觉echarts没有canvajs好看。                  
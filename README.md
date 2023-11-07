![logo](img/logo.svg)

> “你的字体圆吗？”
>
> “满圆的。”
>
> “到底是圆还是不圆？”
>
> “满圆。”

![sample](img/sample.svg)

```tex
\noindent jalan~-i siden~de mini xanggiyan alin bi,\\
alin~-i hanqi sahaliyan ula eyer tugi~-i adali.\\
alin muke~de musei mafari banjihabi,\\
mukvn~-i enen amba kesi~be alimbi

``arxan burge~de fulehe akvqi, tere uthai gargan banjirakv. ere uthai gaxan~be kidure akaqun inu, ere uthai gaxan~be kidure gvnin inu.''

\noindent jalan~-i siden de mini xanggiyan alin bi,\\
alin~-i hanqi sahaliyan ula eyer tugi~-i adali.\\
muse ainu mafari gaxan~be waliyambi,\\
enenggi mafari gaxan~be hargaxambi.

``kituhan~de berge akvqi, tere uthai uqulerakv. ere uthai gaxan be kidule akaqun inu, ere uthai gaxan~be kidure gvnin inu.''
```

满圆体（ᠮᠠᠨ  ᠶᡠᠸᠠᠨ ᡨ᠋ᡳ; Modern manJu Round, MJR）是一款开源满文美术字体。致力于从以下三个方向来优化满文字体设计：

- 尽量不借助辅助字符来正确显示字母变体；
- 利用尽量少的字体特性方便拓展制作；
- 在保持可读性的前提下尽力简化笔形。

## 特性



从字体层面，去除了满文抄本、刻本中古朴的笔锋，合并了一些不影响识读的元素，用尽量少元素来表达纷繁复杂的满文字符。字体目前支持满文、锡伯文常用字符和标点符号。



## 下载

下载请见ttf下的最新版本，其中带有test后缀的是还未发布的版本

更新日志：

0.1/0.2

- 字形绘制

0.3

- -i的支持
- 新增对单、双、四qik，冒号、引号的支持

0.4beta

- 调整字号和行距
- 词首、词中形字符增加尖角，避免白缝
- 对于kgh的阴性词形和k'v g'v h'v的支持（需要对U+180B即FVS1的适配）
  - k'v g'v h'v采用U+180C
- g'.init显示错误
- l.fina显示错误
- 诸如᠊ᠸᠠᠶ᠊形式下字符碰撞的问题
  - 当f/w和y之间只有一个字符时，采用更长的y
- x有些跟k‘混淆，需要把左边一撇适当分离

0.5 

- 解决曲线的方向不统一，转化为形状时会出现空档的问题（软件直接压平，若要调整再从从0.4beta粘）
- 完全重做字符逻辑
- r调整，-ri词尾形过于拥挤、hergen的r-g过于拥挤
- 拉长j，避免词中跟前文打架严重
- 解决Tu du 独立型显示错误
- 解决ᠪᡠ词中不显示点

0.6

- LaTeX适配（LaTeX似乎会将init、isol、fina等特性自动优先解决，导致后面进行calt时需要匹配更多字符）
- 添加180B以强制转换g-h-k及t-d自形，依惯例使用180B强制转换
- dv正确显示

## 已知问题（打勾表示test后缀版本中已解决）

- [ ] 无标点符号和ASCII支持
- [ ] 补全latex映射文件
- [x] 圆头字母后接ml的右侧协调
- [ ] 词中形x的一撇感觉偏细（从字符数据来看是一样的，应该是显示效果的问题）
- [ ] 所有转角统一为圆角，涉及ᠪᠣ等复杂情况，搁置




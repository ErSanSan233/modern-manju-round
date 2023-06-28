# Modern manJu Round：一款现代风格的满文字体

![sample](/Users/yongze/Documents/GitHub/modern-manju-round/img/sample.png)

下载请见ttf下的最新版本，其中带有test后缀的是还未发布的版本

目前版本：0.3

- -i的支持
- 新增对单、双、四qik，冒号、引号的支持

0.4beta

- 调整字号和行距
- 词首、词中形字符增加尖角，避免白缝

已知问题（打勾表示test后缀版本中已解决）

- [ ] 无标点符号和ASCII支持
- [x] 对于kgh的阴性词形和k'v g'v h'v的支持（需要对U+180B即FVS1的适配）
  - [x] k'v g'v h'v采用U+180C
- [x] g'.init显示错误
- [x] l.fina显示错误
- [x] 诸如᠊ᠸᠠᠶ᠊形式下字符碰撞的问题
  - [x] 当f/w和y之间只有一个字符时，采用更长的y
- [x] x有些跟k‘混淆，需要把左边一撇适当分离
- [ ] ~~字母间接缝宜引入尖角，涉及全部重绘，搁置~~
- [ ] ~~所有转角统一为圆角，涉及ᠪᠣ等复杂情况，搁置~~

### 使用示例

```
``manju gisun serengge, manju halangga niyalmai fulehe da yaya we bahanarakvqi ojorakvngge kai, adarame seqi, muse jabxan de wesihun jalan -i ayan suwayan manju ofi, aika manjurame bahanarakv, niyalma be aqaha dari, fonjiha \nolinebreak de, angga gahvxara yasa xarinjara oqi, ereqi giqukengge biu ereq=====i fanqaquk==========angge ge=====li bi===============o::''

tangsu: batu si ainambi ni.

batu: bi jing bithe hvlame bi. taqibusi muse be xu bithe be labdu hvlabumbi, uttu ofi, bi jing <<ilan gurun -i bithe>> be hvlamebi.

tangsu: mini tere dabteli <<hari poter>> be si sabuhau.

neh'v, dvmbi, hv, h'v. h h' h''. t'' d'' t d 
```


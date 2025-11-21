# Rime Settings

基于[薄荷](https://github.com/Mintimate/oh-my-rime)的配置覆写，导入部分[雾凇](https://github.com/iDvel/rime-ice)的预设，结合起来使用。

本人主用小鹤双拼，同时维护全拼和全拼带小鹤混输的方案，但这两个方案不实际使用。其余方案因为不使用不做修改。

使用本自定义方案默认搭配最新的薄荷配置，如果遇到问题请先确认自己的输入法和方案是否最新。如果仍有问题再进行反馈。

配置过程和解析请看：[Website](https://blog.emptylight.cn/post/rime-input-method-configuration-z1snn)(addr:cn) 或 [GitHub Page](https://emptylight370.github.io/post/rime-input-method-configuration-z1snn)(addr:global but in chinese)

Mirrors: [GitHub](https://github.com/emptylight370/rime-settings)(addr:global) or [Gitee](https://gitee.com/emptylight370/rime-settings)(addr:cn)

## 词典

自行导入了明日方舟、崩坏三、崩坏星穹铁道的词库。这些可以直接下载使用，自测没问题。并且我会不定期补充一些词条，同时也欢迎 Pull Request 补充词库词条。

自己添加了一些自定义短语，并且用中英文分离的方式导入了一些自定义的纯英文短语。

导入的词典未去重。自行添加的词典与万象词典重叠部分会吞掉注音，开着注音打字会更明显。

## 快捷键

使用了雾凇的 <kbd>v</kbd> 和 <kbd>V</kbd> 快捷键来替代薄荷的 <kbd>/</kbd> 快捷键。

使用了雾凇的部分快捷键，使用 <kbd>-=</kbd> 定字，使用 <kbd>[]</kbd> 翻页，使用 <kbd>,.</kbd> 翻页。

在原有基础上添加 <kbd>'</kbd> 分字。

因个人习惯，使用 <kbd>CTRL</kbd> 来切换输入中英文输入，<kbd>SHIFT</kbd> 禁用。

**注意**：Weasel 在 0.16.3beta 里面尝试添加了 <kbd>CTRL</kbd>+<kbd>SPACE</kbd> 支持，不确定效果如何。应该是随着 0.16.4 发布的，现在可通过 preRelease 试用。

## 语言模型

根据[设置语言模型 | oh-my-rime 输入法](https://www.mintimate.cc/zh/guide/languageModel.html)导入万象拼音语言模型，由（目前 release 不可见的）旧版本模型转移至长期支持版本模型。具体变更详见提交历史。

现在使用的长期支持版本语言模型更新时间为：2025/11/10 08:49（GMT+8）。

# 导入

## 概括

词库可以直接导入，注意导入方法。

自定义配置自行与本地配置合并，不建议直接套用。可参考语法自行配置。

## 说明

可以将 custom 的文件按需复制到自己的文件中，不要直接替换，也不要直接整个复制。里面的配置是特化的，大体上只适合我自己使用。

导入词库时自定义词库不要直接导入，自己将里面的内容删干净了再写自己的词条。

新加的游戏词库可以直接导入，这部分没有问题。可以正常使用。至于整理，大部分是从搜狗词库导入的，但是新增内容是我自己整理的。怎么大家都不喜欢更新词库呢，一个个的都几年没更新词库了。

# 脚本

## 排序脚本

### Python 脚本

目前添加了一个用于排序拼音词库的脚本，要求词库必须是 YAML 格式的词库，其中注释会在排序后统一添加到最开始的地方。

这个脚本有两个版本，一个是会生成新的文件（new），另一个是替换原本的文件（replace）。值得注意的是，如果词条中间没有使用 `\t` 分隔会直接被丢弃。这个不在设计中，但是原因不明。

在元数据结束前所有内容会认为是元数据的一部分，会保持原样。即在`...`前的所有内容。

才发现脚本对中英文词库基本上算是通用的，那么应该不存在兼容性问题，用英文扩展词库试了好像不存在什么问题。（话说是不是只有薄荷有英文扩展词库啊）

本地使用 Python 3.13，未特别安装依赖库。感谢通义。目前的扩展词库使用此方式排序，如崩坏系列、明日方舟、脑叶系列等词库。

# Quicker 动作

目前也写了一个 Quicker 动作，可以对选中的行进行排序，并且将排序结果写回编辑器中。脚本地址为[rime 词库排序 - by Emptylight - 动作信息 - Quicker](https://getquicker.net/Sharedaction?code=17042fb9-5292-4bdf-0172-08dd6c0ac9c8)，目前测试中，可以正常对 VSCode 中打开的词库进行排序。

目前的扩展词库使用此方式排序，如中文自定义补充词库、英文自定义补充词库等。可以在一个分区范围内排序，如两行注释之间。

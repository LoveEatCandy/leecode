/*
#!/usr/bin/env gorun
@author :yinzhengjie
Blog:http://www.cnblogs.com/yinzhengjie/tag/GO%E8%AF%AD%E8%A8%80%E7%9A%84%E8%BF%9B%E9%98%B6%E4%B9%8B%E8%B7%AF/
EMAIL:y1053419035@qq.com
*/


package main

import (
    "bufio"
    "os"
    "fmt"
)

var   (
    String string
    Number int
    Input string
)

func main()  {
    f := bufio.NewReader(os.Stdin) //读取输入的内容
    for {
        fmt.Print("请输入一些字符串>")
        Input,_ = f.ReadString('\n') //定义一行输入的内容分隔符。
        if len(Input) == 1 {
            continue //如果用户输入的是一个空行就让用户继续输入。
        }
        fmt.Printf("您输入的是:%s",Input)
        fmt.Sscan(Input,&String,&Number) //将Input
        if String == "stop" {
            break
        }
        fmt.Printf("您输入的第一个参数是：·\033[31;1m%v\033[0m·,输入的第二个参数是··\033[31;1m%v\033[0m·.\n",String,Number)
    }
}


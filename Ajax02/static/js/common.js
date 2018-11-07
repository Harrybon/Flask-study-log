/**
 * Created by tarena on 18-11-6.
 */

function getxhr(){
    if (window.XMLHttpRequest){
        //支持 XMLHttpRequest
        return new XMLHttpRequest();
    }else{
        // 不支持XMLHttpRequest,使用 ActiveXObject 创建异步对象
        return new ActiveXObject("Microsoft.XMLHTTP");
    }
}


function btnAjax() {
            //1.创建.获取xhr
            var xhr  =getxhr();
            //2.创建请求
            xhr.open('get','/02-server',true);
            //3.设置回调函数
            xhr.onreadystatechange = function(){
                //判断xhr.readystate是否为４，并且xhr.status是否为200
                if (xhr.readyState == 4 && xhr.status == 200){
                    var resText = xhr.responseText;
                    //处理业务
                    document.getElementById('show').innerHTML = resText;
                }

            }
            //4.发送请求
            xhr.send(null)
        }


function btnAjax2() {
            //1.创建.获取xhr
            var xhr  =getxhr();
            //2.创建请求
            var uname = document.getElementById('uname').value;
            xhr.open('get','/02-server02?uname='+uname,true);
            //3.设置回调函数
            xhr.onreadystatechange = function(){
                //判断xhr.readystate是否为４，并且xhr.status是否为200
                if (xhr.readyState == 4 && xhr.status == 200){
                    var resText = xhr.responseText;
                    //处理业务
                    document.getElementById('show').innerHTML = resText;
                }

            }
            //4.发送请求
            xhr.send(null)
        }


function btnAjax3() {
            //1.创建.获取xhr
            var xhr  =getxhr();
            //2.创建请求
            xhr.open('post','/04-server',true);
            //POST方式需要自己设置http的请求头
            xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
            //3.设置回调函数
            xhr.onreadystatechange = function(){
                //判断xhr.readystate是否为４，并且xhr.status是否为200
                if (xhr.readyState == 4 && xhr.status == 200){
                    var resText = xhr.responseText;
                    //处理业务
                    document.getElementById('show').innerHTML = resText;
                }

            }
            //4.发送请求
            xhr.send('uname=qqq&uage=20')
        }














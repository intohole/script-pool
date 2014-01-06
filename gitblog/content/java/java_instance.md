Title: java单例模式  
Slug: java
Date: 2013-12-29 11:53:55
Tags: java 设计模式  
Category: java  
Author: 泽  
Lang: zh  
Summary: java 设计模式  


单例模式
================================
单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。  
*节省资源
*唯一性  

:::java  
       
       //
       public class JavaInstance {
              private static JavaInstance = null; //设置单例模式句柄为null

              private JavaInstance()
              {
                   //私有化初始函数
              }

              public static getInstance()
              {
                    if(instance == null) //第一次判断是否为空
                    {  
                        synchronized(JavaInstance.class)//锁住类 多线程同步问题
                        {
                              if(instance == null)
                              {
                                   instance = new JavaInstance(); //调用私有构造函数初始化
                              }
                        }
                    }
                    return instance;//返回单例句柄
              }



              public void work()
              {
                  //do something
              }
       }



:::java
       
       //枚举类型 可以避免多线程同步问题 ，防止反序列化重新创建新的对象
       public enum JavaInstance(){
            INSTANCE;

            private JavaInstance(){
            //初始化
            }
       }

:::java  
       

       //最简单的方式
       public class JavaInstance(){
            private static JavaInstance instance = new JavaInstance();
            private JavaInstance()
            {
               //初始化 
            }

            public static getInstance()
            {
                return instance;
            }
       }
       